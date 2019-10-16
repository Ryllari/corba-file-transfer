# Python stubs generated by omniidl from server.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


#
# Start of module "Server"
#
__name__ = "Server"
_0_Server = omniORB.openModule("Server", r"server.idl")
_0_Server__POA = omniORB.openModule("Server__POA", r"server.idl")


# typedef ... FileList
class FileList:
    _NP_RepositoryId = "IDL:Server/FileList:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Server.FileList = FileList
_0_Server._d_FileList  = (omniORB.tcInternal.tv_sequence, (omniORB.tcInternal.tv_string,0), 0)
_0_Server._ad_FileList = (omniORB.tcInternal.tv_alias, FileList._NP_RepositoryId, "FileList", (omniORB.tcInternal.tv_sequence, (omniORB.tcInternal.tv_string,0), 0))
_0_Server._tc_FileList = omniORB.tcInternal.createTypeCode(_0_Server._ad_FileList)
omniORB.registerType(FileList._NP_RepositoryId, _0_Server._ad_FileList, _0_Server._tc_FileList)
del FileList

# struct ClientName
_0_Server.ClientName = omniORB.newEmptyClass()
class ClientName (omniORB.StructBase):
    _NP_RepositoryId = "IDL:Server/ClientName:1.0"

    def __init__(self, client_name, files):
        self.client_name = client_name
        self.files = files

_0_Server.ClientName = ClientName
_0_Server._d_ClientName  = (omniORB.tcInternal.tv_struct, ClientName, ClientName._NP_RepositoryId, "ClientName", "client_name", (omniORB.tcInternal.tv_string,0), "files", omniORB.typeMapping["IDL:Server/FileList:1.0"])
_0_Server._tc_ClientName = omniORB.tcInternal.createTypeCode(_0_Server._d_ClientName)
omniORB.registerType(ClientName._NP_RepositoryId, _0_Server._d_ClientName, _0_Server._tc_ClientName)
del ClientName

# typedef ... ClientArray
class ClientArray:
    _NP_RepositoryId = "IDL:Server/ClientArray:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Server.ClientArray = ClientArray
_0_Server._d_ClientArray  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:Server/ClientName:1.0"], 0)
_0_Server._ad_ClientArray = (omniORB.tcInternal.tv_alias, ClientArray._NP_RepositoryId, "ClientArray", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:Server/ClientName:1.0"], 0))
_0_Server._tc_ClientArray = omniORB.tcInternal.createTypeCode(_0_Server._ad_ClientArray)
omniORB.registerType(ClientArray._NP_RepositoryId, _0_Server._ad_ClientArray, _0_Server._tc_ClientArray)
del ClientArray

# interface CentralServer
_0_Server._d_CentralServer = (omniORB.tcInternal.tv_objref, "IDL:Server/CentralServer:1.0", "CentralServer")
omniORB.typeMapping["IDL:Server/CentralServer:1.0"] = _0_Server._d_CentralServer
_0_Server.CentralServer = omniORB.newEmptyClass()
class CentralServer :
    _NP_RepositoryId = _0_Server._d_CentralServer[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_Server.CentralServer = CentralServer
_0_Server._tc_CentralServer = omniORB.tcInternal.createTypeCode(_0_Server._d_CentralServer)
omniORB.registerType(CentralServer._NP_RepositoryId, _0_Server._d_CentralServer, _0_Server._tc_CentralServer)

# CentralServer operations and attributes
CentralServer._d__get_client_files = ((),(omniORB.typeMapping["IDL:Server/ClientArray:1.0"],),None)
CentralServer._d__set_client_files = ((omniORB.typeMapping["IDL:Server/ClientArray:1.0"],),(),None)
CentralServer._d_search = (((omniORB.tcInternal.tv_string,0), ), (omniORB.typeMapping["IDL:Server/ClientArray:1.0"], ), None)
CentralServer._d_connect = (((omniORB.tcInternal.tv_string,0), omniORB.typeMapping["IDL:Server/FileList:1.0"]), ((omniORB.tcInternal.tv_string,0), ), None)
CentralServer._d_update_files = (((omniORB.tcInternal.tv_string,0), omniORB.typeMapping["IDL:Server/FileList:1.0"]), ((omniORB.tcInternal.tv_string,0), ), None)
CentralServer._d_disconnect = (((omniORB.tcInternal.tv_string,0), ), (), None)

# CentralServer object reference
class _objref_CentralServer (CORBA.Object):
    _NP_RepositoryId = CentralServer._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def _get_client_files(self, *args):
        return self._obj.invoke("_get_client_files", _0_Server.CentralServer._d__get_client_files, args)

    def _set_client_files(self, *args):
        return self._obj.invoke("_set_client_files", _0_Server.CentralServer._d__set_client_files, args)

    client_files = property(_get_client_files, _set_client_files)


    def search(self, *args):
        return self._obj.invoke("search", _0_Server.CentralServer._d_search, args)

    def connect(self, *args):
        return self._obj.invoke("connect", _0_Server.CentralServer._d_connect, args)

    def update_files(self, *args):
        return self._obj.invoke("update_files", _0_Server.CentralServer._d_update_files, args)

    def disconnect(self, *args):
        return self._obj.invoke("disconnect", _0_Server.CentralServer._d_disconnect, args)

omniORB.registerObjref(CentralServer._NP_RepositoryId, _objref_CentralServer)
_0_Server._objref_CentralServer = _objref_CentralServer
del CentralServer, _objref_CentralServer

# CentralServer skeleton
__name__ = "Server__POA"
class CentralServer (PortableServer.Servant):
    _NP_RepositoryId = _0_Server.CentralServer._NP_RepositoryId


    _omni_op_d = {"_get_client_files": _0_Server.CentralServer._d__get_client_files, "_set_client_files": _0_Server.CentralServer._d__set_client_files, "search": _0_Server.CentralServer._d_search, "connect": _0_Server.CentralServer._d_connect, "update_files": _0_Server.CentralServer._d_update_files, "disconnect": _0_Server.CentralServer._d_disconnect}

CentralServer._omni_skeleton = CentralServer
_0_Server__POA.CentralServer = CentralServer
omniORB.registerSkeleton(CentralServer._NP_RepositoryId, CentralServer)
del CentralServer
__name__ = "Server"

#
# End of module "Server"
#
__name__ = "server_idl"

_exported_modules = ( "Server", )

# The end.
