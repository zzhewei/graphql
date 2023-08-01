import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from . import User as UserModel, Role as RoleModel
from .schema_user import User, CreateUserMutation, UpdateUserMutation, DelUserMutation
from .schema_role import Role


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    users = graphene.List(lambda: User, id=graphene.Int())
    roles = graphene.List(lambda: Role, id=graphene.Int())

    def resolve_users(self, info, id=None):
        query = User.get_query(info)

        if id:
            query = query.filter(UserModel.id == id)
        return query.all()

    def resolve_roles(self, info, id=None):
        query = Role.get_query(info)

        if id:
            query = query.filter(RoleModel.id == id)
        return query.all()

    all_users = SQLAlchemyConnectionField(User)
    all_roles = SQLAlchemyConnectionField(Role)


class Mutation(graphene.ObjectType):
    CreateUser = CreateUserMutation.Field()
    UpdateUser = UpdateUserMutation.Field()
    DelUser = DelUserMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
