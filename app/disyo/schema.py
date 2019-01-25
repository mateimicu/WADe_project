from graphene import ObjectType, Node, Schema
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType
from disyo.models import DSApplication


class DSAppNode(DjangoObjectType):
    class Meta:
        model = DSApplication
        interfaces = Node,



class Query(ObjectType):
    dsApp = Node.Field(DSAppNode)
    allDSApps = DjangoConnectionField(DSAppNode)


schema = Schema(query=Query)