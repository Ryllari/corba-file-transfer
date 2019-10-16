import CosNaming, Server, Client
import os
import sys

from omniORB import CORBA, PortableServer


def read_in_chunks(file_object, chunk_size=65536):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def connect_to_server(server_name):
    orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
    try:
        obj = orb.resolve_initial_references("NameService")
        rootContext = obj._narrow(CosNaming.NamingContext)

        name = [CosNaming.NameComponent(server_name, "context"),
                CosNaming.NameComponent(server_name, "Object")]
        
        obj = rootContext.resolve(name)
        obj = obj._narrow(Server.CentralServer)
        
        if obj is None:
            print("Voce tem certeza deste servidor?")
            sys.exit(1)

        print("Conectado a {} com sucesso".format(server_name))        
        return obj
        
    except CosNaming.NamingContext.NotFound, ex:
        print("Servidor nao encontrado")
        sys.exit(1)

def connect_to_client(server_name):
    orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
    try:
        obj = orb.resolve_initial_references("NameService")
        rootContext = obj._narrow(CosNaming.NamingContext)

        name = [CosNaming.NameComponent(server_name, "context"),
                CosNaming.NameComponent(server_name, "Object")]
        
        obj = rootContext.resolve(name)
        obj = obj._narrow(Client.ClientServer)
        
        if obj is None:
            print("Voce tem certeza deste cliente?")
            sys.exit(1)

        print("Conectado a {} com sucesso".format(server_name))        
        return obj
        
    except CosNaming.NamingContext.NotFound, ex:
        print("Cliente nao encontrado")

