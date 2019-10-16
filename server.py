import CosNaming, Server, Server__POA
import os
import sys

from omniORB import CORBA, PortableServer


name_server = 'Server'

class ClientName:
    def __init__(self, client_name, files):
        self.client_name = client_name 
        self.files = files


class CentralServer(Server__POA.CentralServer):
    client_files = []

    def connect(self, client_name, files):
        for client in self.client_files:
            if client.client_name == client_name:
                self.client_files.remove(client)
        self.client_files.append(ClientName(client_name, files))
        return client_name

    def update_files(self, client_name, files):
        for client in self.client_files:
            if client.client_name == client_name:
                self.client_files.remove(client)
        self.client_files.append(ClientName(client_name, files))
        return client_name

    def search(self, keyword):
        response = []
        for client in self.client_files:
            results = [x for x in client.files if keyword in x]
            if results:
                response.append(ClientName(client.client_name, results))
        return response

    def get_client_files(self):
        return self.client_files

# Initialize the ORB service and find the root POA
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

# Create an instance of CentralServer and an CentralServer object reference
ei = CentralServer()
eo = ei._this()

# Obtain a reference to the root naming context
obj = orb.resolve_initial_references("NameService")
rootContext = obj._narrow(CosNaming.NamingContext)

if rootContext is None:
    print("Failed to narrow the root naming context")
    sys.exit(1)

# Bind context to the root context
try:
    name = [CosNaming.NameComponent(name_server, "context")]
    context = rootContext.bind_new_context(name)
    print "New context bounded: {}".format(name_server)

except CosNaming.NamingContext.AlreadyBound, ex:
    obj = rootContext.resolve(name)
    context = obj._narrow(CosNaming.NamingContext)
    
    if context is None:
        print "context exists but is not a NamingContext"
        sys.exit(1)
    
# Bind the object to the context
try:
    name = [CosNaming.NameComponent(name_server, "Object")]
    context.bind(name, eo)

except CosNaming.NamingContext.AlreadyBound:
    context.rebind(name, eo)

# Activate the POA
poaManager = poa._get_the_POAManager()
poaManager.activate()

# Block for ever (or until the ORB is shut down)
orb.run()
