import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from . import Role as RoleModel
from . import db


class RoleAttribute:
    name = graphene.String(required=True)
    default = graphene.Int(required=True)
    permissions = graphene.Int(required=True)


class Role(SQLAlchemyObjectType):
    class Meta:
        model = RoleModel
        interfaces = (relay.Node,)
