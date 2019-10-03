# schema.py

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import DataCenter as DataCenterModel
from models import Router as RouterModel
from models import Switch as SwitchModel
from models import Computer as ComputerModel
from models import Process as ProcessModel


class DataCenter(SQLAlchemyObjectType):
    class Meta:
        model = DataCenterModel
        interfaces = (relay.Node, )


class DataCenterConnection(relay.Connection):
    class Meta:
        node = DataCenter


class Router(SQLAlchemyObjectType):
    class Meta:
        model = RouterModel
        interfaces = (relay.Node, )


class RouterConnection(relay.Connection):
    class Meta:
        node = Router


class Switch(SQLAlchemyObjectType):
    class Meta:
        model = SwitchModel
        interfaces = (relay.Node, )


class SwitchConnection(relay.Connection):
    class Meta:
        node = Switch


class Computer(SQLAlchemyObjectType):
    class Meta:
        model = ComputerModel
        interfaces = (relay.Node, )


class ComputerConnection(relay.Connection):
    class Meta:
        node = Computer


class Process(SQLAlchemyObjectType):
    class Meta:
        model = ProcessModel
        interfaces = (relay.Node, )


class ProcessConnection(relay.Connection):
    class Meta:
        node = Process


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_datacenters = SQLAlchemyConnectionField(DataCenter, sort=DataCenter.sort_argument())
    all_routers = SQLAlchemyConnectionField(Router, sort=None)
    all_switches = SQLAlchemyConnectionField(Switch, sort=None)
    all_computers = SQLAlchemyConnectionField(Computer, sort=None)
    all_processes = SQLAlchemyConnectionField(Process, sort=None)


schema = graphene.Schema(query=Query, types=[DataCenter, Router, Switch, Computer, Process])