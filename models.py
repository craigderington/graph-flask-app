# models.py

from db import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean, func
from sqlalchemy.orm import backref, relationship


class DataCenter(Base):
    __tablename__ = "datacenters"
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    street_address = Column(String(255), nullable=False)
    city = Column(String(64), nullable=False)
    state = Column(String(2), nullable=False)
    postal_code = Column(String(10), nullable=False)
    access_network = Column(String(255), nullable=True)
    aggregate_router = Column(String(255), nullable=True)
    aggregate_switch = Column(String(255), nullable=True)
    fabric = Column(String(255), nullable=True)
    primary_dns = Column(String(255), nullable=True)
    secondary_dns = Column(String(255), nullable=True)
    load_balancer = Column(String(255), nullable=True)
    ats = Column(Boolean, default=True)

    def __repr__(self):
        if self.id and self.name:
            return "{} {}".format(
                self.id,
                self.name
            )


class Router(Base):
    __tablename__ = "routers"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=True)
    protocol = Column(String(255), nullable=True)
    state = Column(String(255), nullable=True)
    metric = Column(String(255), nullable=True)
    mtu = Column(Integer, default=1500)
    latency = Column(Integer, default=100)
    domain = Column(String(255), nullable=True)
    datacenter_id = Column(Integer, ForeignKey("datacenters.id"))
    datacenter = relationship(DataCenter, backref=backref("datacenters", uselist=True, cascade="delete,all"))

    def __repr__(self):
        if self.id and self.name:
            return "{} {}".format(
                self.id,
                self.name
            )


class Switch(Base):
    __tablename__ = "switches"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    asset_tag = Column(String(255), nullable=False)
    device_description = Column(String(255), nullable=False)
    device_type = Column(String(255), nullable=False)
    device_model = Column(String(255), nullable=False)
    primary_mac_addr = Column(String(255), nullable=False)
    secondar_mac_addr = Column(String(255), nullable=False)
    ports = Column(String(255), nullable=False)
    ip_eth0 = Column(String(15), nullable=False)
    ip_eth1 = Column(String(15), nullable=False)
    ip_eth2 = Column(String(15), nullable=False)
    ip_eth3 = Column(String(15), nullable=False)
    ip_eth4 = Column(String(15), nullable=False)
    router_id = Column(Integer, ForeignKey("routers.id"))
    router = relationship(Router, backref=backref("routers", uselist=True, cascade="delete,all"))

    def __repr__(self):
        if self.id and self.name:
            return "{} {}".format(
                self.id,
                self.name
            )


class Computer(Base):
    __tablename__ = "computers"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    asset_tag = Column(String(255), nullable=False)
    manufacturer = Column(String(255), nullable=False)
    serial_number = Column(String(255), nullable=False)
    model = Column(String(255), nullable=False)
    os_domain = Column(String(255), nullable=False)
    operating_system = Column(String(255), nullable=False)
    os_version = Column(String(255), nullable=False)
    os_service_pack = Column(String(255), nullable=False)
    dns_domain = Column(String(255), nullable=False)
    description = Column(String(1024), nullable=False)
    cpu_type = Column(String(255), nullable=False)
    cpu_count = Column(Integer)
    cpu_speed = Column(String(255), nullable=False)
    installed_ram = Column(Integer)
    memory_type = Column(String(255), nullable=False)
    switch_id = Column(Integer, ForeignKey("switches.id"))
    switch = relationship(Switch, backref=backref("switches", uselist=True, cascade="delete,all"))

    def __repr__(self):
        if self.id and self.name:
            return "{} {}".format(
                self.id,
                self.name
            )  


class Process(Base):
    __tablename__ = "processes"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    process_id = Column(Integer)
    percent_cpu = Column(Integer)
    percent_memory = Column(Integer)
    started = Column(DateTime, default=func.now())
    run_time = Column(DateTime)
    command = Column(String(255), nullable=False)
    computer_id = Column(Integer, ForeignKey("computers.id"))
    computer = relationship(Computer, backref=backref("computers", uselist=True, cascade="delete,all"))

    def __repr__(self):
        if self.id and self.name:
            return "{} {}".format(
                self.id,
                self.name
            )
