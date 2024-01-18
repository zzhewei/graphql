import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField

from . import Role as RoleModel
from . import User as UserModel
from .schema_role import Role
from .schema_user import CreateUserMutation, DelUserMutation, UpdateUserMutation, User


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    # field = type 也可是 Obj type
    users = graphene.List(lambda: User, uid=graphene.Int())
    roles = graphene.List(lambda: Role, id=graphene.Int())
    hello = graphene.String()

    # resolver需要加上固定前缀resolve_，會去映射上述的字段
    def resolve_users(self, info, uid=None):
        query = User.get_query(info)

        if uid:
            query = query.filter(UserModel.id == uid)
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


class Subscription(graphene.ObjectType):
    message_received = graphene.String()


schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)
