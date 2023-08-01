import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from . import User as UserModel, db


class UserAttribute:
    username = graphene.String(required=True)
    role_id = graphene.Int(required=True)
    password_hash = graphene.String(required=True)


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class CreateUserInput(graphene.InputObjectType, UserAttribute):
    """Arguments to create a User."""
    pass


class SingleUserInput(graphene.InputObjectType, UserAttribute):
    """Arguments to update a User."""
    id = graphene.ID(required=True)


class CreateUserMutation(graphene.Mutation):
    # 回傳的資料
    user = graphene.Field(lambda: User)

    # 參數
    class Arguments:
        user_data = CreateUserInput(required=True)

    def mutate(self, info, user_data):
        user = UserModel(
            username=user_data.username,
            role_id=user_data.role_id,
            password_hash=user_data.password_hash
        )

        db.session.add(user)
        db.session.commit()

        return CreateUserMutation(user=user)


class UpdateUserMutation(graphene.Mutation):
    user = graphene.Field(lambda: User)

    class Arguments:
        user_data = SingleUserInput(required=True)

    def mutate(self, info, user_data):
        temp = UserModel.query.filter_by(id=user_data.id).first()
        if temp:
            temp.username = user_data.username
            temp.role_id = user_data.role_id
            temp.password_hash = user_data.password_hash

        db.session.commit()
        user = UserModel.query.filter_by(id=user_data.id).first()
        return UpdateUserMutation(user=user)


class DelUserMutation(graphene.Mutation):
    user = graphene.Field(lambda: User)
    msg = graphene.String()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        UserModel.query.filter_by(id=id).delete()
        db.session.commit()
        return DelUserMutation(msg="delete success")
