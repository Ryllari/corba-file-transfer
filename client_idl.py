# Python stubs generated by omniidl from client.idl
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
# Start of module "Client"
#
__name__ = "Client"
_0_Client = omniORB.openModule("Client", r"client.idl")
_0_Client__POA = omniORB.openModule("Client__POA", r"client.idl")


# typedef ... OctetSequence
class OctetSequence:
    _NP_RepositoryId = "IDL:Client/OctetSequence:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Client.OctetSequence = OctetSequence
_0_Client._d_OctetSequence  = (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_octet, 0)
_0_Client._ad_OctetSequence = (omniORB.tcInternal.tv_alias, OctetSequence._NP_RepositoryId, "OctetSequence", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_octet, 0))
_0_Client._tc_OctetSequence = omniORB.tcInternal.createTypeCode(_0_Client._ad_OctetSequence)
omniORB.registerType(OctetSequence._NP_RepositoryId, _0_Client._ad_OctetSequence, _0_Client._tc_OctetSequence)
del OctetSequence

# typedef ... PathList
class PathList:
    _NP_RepositoryId = "IDL:Client/PathList:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Client.PathList = PathList
_0_Client._d_PathList  = (omniORB.tcInternal.tv_sequence, (omniORB.tcInternal.tv_string,0), 0)
_0_Client._ad_PathList = (omniORB.tcInternal.tv_alias, PathList._NP_RepositoryId, "PathList", (omniORB.tcInternal.tv_sequence, (omniORB.tcInternal.tv_string,0), 0))
_0_Client._tc_PathList = omniORB.tcInternal.createTypeCode(_0_Client._ad_PathList)
omniORB.registerType(PathList._NP_RepositoryId, _0_Client._ad_PathList, _0_Client._tc_PathList)
del PathList

# interface ClientServer
_0_Client._d_ClientServer = (omniORB.tcInternal.tv_objref, "IDL:Client/ClientServer:1.0", "ClientServer")
omniORB.typeMapping["IDL:Client/ClientServer:1.0"] = _0_Client._d_ClientServer
_0_Client.ClientServer = omniORB.newEmptyClass()
class ClientServer :
    _NP_RepositoryId = _0_Client._d_ClientServer[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_Client.ClientServer = ClientServer
_0_Client._tc_ClientServer = omniORB.tcInternal.createTypeCode(_0_Client._d_ClientServer)
omniORB.registerType(ClientServer._NP_RepositoryId, _0_Client._d_ClientServer, _0_Client._tc_ClientServer)

# ClientServer operations and attributes
ClientServer._d__get_path_file = ((),((omniORB.tcInternal.tv_string,0),),None)
ClientServer._d__set_path_file = (((omniORB.tcInternal.tv_string,0),),(),None)
ClientServer._d__get_finish_download = ((),(omniORB.typeMapping["IDL:Client/PathList:1.0"],),None)
ClientServer._d__set_finish_download = ((omniORB.typeMapping["IDL:Client/PathList:1.0"],),(),None)
ClientServer._d__get_working_download = ((),(omniORB.typeMapping["IDL:Client/PathList:1.0"],),None)
ClientServer._d__set_working_download = ((omniORB.typeMapping["IDL:Client/PathList:1.0"],),(),None)
ClientServer._d_send_file = (((omniORB.tcInternal.tv_string,0), ), ((omniORB.tcInternal.tv_string,0), ), None)
ClientServer._d_set_path_file = (((omniORB.tcInternal.tv_string,0), ), ((omniORB.tcInternal.tv_string,0), ), None)
ClientServer._d_get_file_list = ((), (omniORB.typeMapping["IDL:Client/PathList:1.0"], ), None)
ClientServer._d_start_download = (((omniORB.tcInternal.tv_string,0), ), (), None)
ClientServer._d_finish_to_download = (((omniORB.tcInternal.tv_string,0), ), (), None)

# ClientServer object reference
class _objref_ClientServer (CORBA.Object):
    _NP_RepositoryId = ClientServer._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def _get_path_file(self, *args):
        return self._obj.invoke("_get_path_file", _0_Client.ClientServer._d__get_path_file, args)

    def _set_path_file(self, *args):
        return self._obj.invoke("_set_path_file", _0_Client.ClientServer._d__set_path_file, args)

    path_file = property(_get_path_file, _set_path_file)


    def _get_finish_download(self, *args):
        return self._obj.invoke("_get_finish_download", _0_Client.ClientServer._d__get_finish_download, args)

    def _set_finish_download(self, *args):
        return self._obj.invoke("_set_finish_download", _0_Client.ClientServer._d__set_finish_download, args)

    finish_download = property(_get_finish_download, _set_finish_download)


    def _get_working_download(self, *args):
        return self._obj.invoke("_get_working_download", _0_Client.ClientServer._d__get_working_download, args)

    def _set_working_download(self, *args):
        return self._obj.invoke("_set_working_download", _0_Client.ClientServer._d__set_working_download, args)

    working_download = property(_get_working_download, _set_working_download)


    def send_file(self, *args):
        return self._obj.invoke("send_file", _0_Client.ClientServer._d_send_file, args)

    def set_path_file(self, *args):
        return self._obj.invoke("set_path_file", _0_Client.ClientServer._d_set_path_file, args)

    def get_file_list(self, *args):
        return self._obj.invoke("get_file_list", _0_Client.ClientServer._d_get_file_list, args)

    def start_download(self, *args):
        return self._obj.invoke("start_download", _0_Client.ClientServer._d_start_download, args)

    def finish_to_download(self, *args):
        return self._obj.invoke("finish_to_download", _0_Client.ClientServer._d_finish_to_download, args)

omniORB.registerObjref(ClientServer._NP_RepositoryId, _objref_ClientServer)
_0_Client._objref_ClientServer = _objref_ClientServer
del ClientServer, _objref_ClientServer

# ClientServer skeleton
__name__ = "Client__POA"
class ClientServer (PortableServer.Servant):
    _NP_RepositoryId = _0_Client.ClientServer._NP_RepositoryId


    _omni_op_d = {"_get_path_file": _0_Client.ClientServer._d__get_path_file, "_set_path_file": _0_Client.ClientServer._d__set_path_file, "_get_finish_download": _0_Client.ClientServer._d__get_finish_download, "_set_finish_download": _0_Client.ClientServer._d__set_finish_download, "_get_working_download": _0_Client.ClientServer._d__get_working_download, "_set_working_download": _0_Client.ClientServer._d__set_working_download, "send_file": _0_Client.ClientServer._d_send_file, "set_path_file": _0_Client.ClientServer._d_set_path_file, "get_file_list": _0_Client.ClientServer._d_get_file_list, "start_download": _0_Client.ClientServer._d_start_download, "finish_to_download": _0_Client.ClientServer._d_finish_to_download}

ClientServer._omni_skeleton = ClientServer
_0_Client__POA.ClientServer = ClientServer
omniORB.registerSkeleton(ClientServer._NP_RepositoryId, ClientServer)
del ClientServer
__name__ = "Client"

#
# End of module "Client"
#
__name__ = "client_idl"

_exported_modules = ( "Client", )

# The end.
