import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from . import User as UserModel
from . import db


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node,)


# 共用參數
class UserAttribute:
    username = graphene.String(required=True)
    role_id = graphene.Int(required=True)
    password_hash = graphene.String(required=True)


# 新增使用者的參數
class CreateUserInput(graphene.InputObjectType, UserAttribute):
    """Arguments to create a User."""

    pass


# 更新使用者的參數
class SingleUserInput(graphene.InputObjectType, UserAttribute):
    """Arguments to update a User."""

    uid = graphene.ID(required=True)


# 新增使用者
class CreateUserMutation(graphene.Mutation):
    # 回傳的資料
    user = graphene.Field(lambda: User)

    # 參數
    class Arguments:
        user_data = CreateUserInput(required=True)

    # 主要邏輯, info 為固定
    def mutate(self, info, user_data):
        user = UserModel(
            username=user_data.username,
            role_id=user_data.role_id,
            password_hash=user_data.password_hash,
        )

        db.session.add(user)
        db.session.commit()

        return CreateUserMutation(user=user)


# 更新使用者
class UpdateUserMutation(graphene.Mutation):
    user = graphene.Field(lambda: User)

    class Arguments:
        user_data = SingleUserInput(required=True)

    def mutate(self, info, user_data):
        temp = UserModel.query.filter_by(id=user_data.uid).first()
        if temp:
            temp.username = user_data.username
            temp.role_id = user_data.role_id
            temp.password_hash = user_data.password_hash

        db.session.commit()
        user = UserModel.query.filter_by(id=user_data.id).first()
        return UpdateUserMutation(user=user)


# 刪除使用者
class DelUserMutation(graphene.Mutation):
    user = graphene.Field(lambda: User)
    msg = graphene.String()

    class Arguments:
        uid = graphene.ID(required=True)

    def mutate(self, info, uid):
        UserModel.query.filter_by(id=uid).delete()
        db.session.commit()
        return DelUserMutation(msg="delete success")
