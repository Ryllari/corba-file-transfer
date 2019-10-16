import CosNaming, Client, Client__POA
import os
import sys
import threading
from os import listdir
from os.path import isfile, join
from omniORB import CORBA, PortableServer
from utils import connect_to_client, read_in_chunks


class ClientServer(Client__POA.ClientServer):
    path_file = ''
    finish_download = []
    working_download = []

    def send_file(self, file_name):
        data = ''
        with open(join(self.path_file,file_name), 'rb') as f:
            print("entrou")
            for readed in read_in_chunks(f):
                data += readed
        return data

    def get_file_list(self):
        return [f for f in listdir(self.path_file) if isfile(join(self.path_file, f))]

    def set_path_file(self, path):
        self.path_file = path
        return self.path_file

    def finish_to_download(self, file_name):
        for f_name in self.working_download:
            if f_name == file_name:
                self.working_download.remove(f_name)
        self.finish_download.append(file_name)

    def start_download(self, file_name):
        self.working_download.append(file_name)
