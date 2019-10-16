import CosNaming
import os
import sys
import threading
from client_server import ClientServer
from omniORB import CORBA, PortableServer
from os.path import isfile, join
from utils import connect_to_server, connect_to_client


def run_orb():
    global orb
    orb.run()

def get_file(file_name):
    global eo
    global server
    global server_file
    eo.start_download(file_name)
    file_data = server_file.send_file(file_name)
    with open(join(eo.path_file,file_name), 'wb') as f:
        f.write(file_data)
        f.close()
    server.update_files(name_server, eo.get_file_list())
    eo.finish_to_download(file_name)

# Initialize the ORB and find the root POA
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

# Create an instance of CentralServer and an CentralServer object reference
ei = ClientServer()
eo = ei._this()

# Obtain a reference to the root naming context
obj = orb.resolve_initial_references("NameService")
rootContext = obj._narrow(CosNaming.NamingContext)

if rootContext is None:
    print("Failed to narrow the root naming context")
    sys.exit(1)

print("BEM-VINDO AO GERENCIAMENTO DE ARQUIVOS")
name_server = raw_input("\nDigite um nome para identificacao:")


# Bind context to the root context
try:
    name = [CosNaming.NameComponent(name_server, "context")]
    context = rootContext.bind_new_context(name)
    print "Ola, {}!".format(name_server)

except CosNaming.NamingContext.AlreadyBound, ex:
    obj = rootContext.resolve(name)
    context = obj._narrow(CosNaming.NamingContext)
    
    if context is None:
        print "Algo deu errado na conexao"
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

t1 = threading.Thread(target=run_orb)
t1.daemon = True
t1.start()

without_path = True
while without_path:
    try:
        dir_file = raw_input("\nDigite o caminho do diretorio completo:")
        if os.path.exists(os.path.dirname(dir_file)):
            eo.set_path_file(dir_file)
            server = connect_to_server('Server')
            server.connect(name_server, eo.get_file_list())
            without_path = False
        else:
            print ("Diretorio nao encontrado!")
    except:
        print ("Diretorio nao encontrado!")

running = True
while running:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n#########################################################")
    print("#############   GERENCIAMENTO DE ARQUIVOS   #############")
    print("#########################################################")
    print("\n# DIGITE O NUMERO REFERENTE AO QUE DESEJA NO MENU")
    print("1 - Buscar arquivo")
    print("2 - Fazer download")
    print("3 - Verificar downloads")
    print("4 - Alterar diretorio")
    print("0 - Sair")
    option = raw_input("\nDigite uma opcao: ")

    if option == '0':
        print("Tchau")
        server.disconnect(name_server)
        running = False
        sys.exit(1)
    
    elif option == '1':
        keyword = raw_input("Digite o termo a ser buscado: ")
        response = server.search(keyword)
        for client in response:
            print("\nCliente {}".format(client.client_name))
            for name_file in client.files:
                print(name_file)

    elif option == '2':
        client_name = raw_input("Digite o nome do cliente que possui o arquivo: ")
        server_file = connect_to_client(client_name)
        file_name = raw_input("Digite o nome do arquivo para download: ")
        if file_name in server_file.get_file_list():
            t2 = threading.Thread(target=get_file, args=(file_name,))
            t2.daemon = True
            t2.start()
            print("Download em processo. Verifique andamento no item 3 do menu!")
        else: 
            print("Arquivo nao encontrado")

    elif option == '3':
        print("\n Downloads finalizados")
        for file_name in eo.finish_download:
            print(file_name)
        print("\n Downloads em andamento...")
        for file_name in eo.working_download:
            print(file_name)

    elif option == '4':
        dir_file = raw_input("\nDigite o caminho do diretorio completo:")
        if os.path.exists(os.path.dirname(dir_file)):
            eo.set_path_file(dir_file)
            server.update_files(name_server, eo.get_file_list())
        else:
            print ("Nao foi possivel alterar o diretorio: Diretorio informado nao encontrado!")
    
    else:
        print("Opcao invalida!")
    
    raw_input("\nPressione qualquer tecla para voltar ao menu principal...")
