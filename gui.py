from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog


class Application2(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.fontePadrao = ("Arial", "10")
        self.container1 = Frame(master)
        self.container1["pady"] = 20
        self.container1.pack()

        self.l_title = Label(self.container1, text="Compartilhamento de arquivos")
        self.l_title["font"] = ("Arial", "10", "bold")
        self.l_title.pack()

    ###########
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2.pack()

        self.l_name = Label(self.container2,text="Nome da conexao: ", font=self.fontePadrao)
        self.l_name.pack(side=LEFT)
  
        self.f_name = Entry(self.container2)
        self.f_name["width"] = 30
        self.f_name["font"] = self.fontePadrao
        self.f_name.pack(side=LEFT)

    ###########
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3.pack()

        self.l_filepath = Label(self.container3, text="Pasta compartilhada: ", font=self.fontePadrao)
        self.l_filepath.pack(side=LEFT)

        self.l_path = Label(self.container3, text="", font=self.fontePadrao)
        self.l_path.pack(side=LEFT)
        
        self.b_path = Button(self.container3)
        self.b_path["text"] = "Selecionar pasta"
        self.b_path["font"] = self.fontePadrao
        self.b_path["width"] = 12
        self.b_path["command"] = self.set_l_path
        self.b_path.pack()
  ####
        self.container4 = Frame(master)
        self.container4["pady"] = 20
        self.container4.pack()
  
        self.b_connect = Button(self.container4)
        self.b_connect["text"] = "Conectar"
        self.b_connect["font"] = self.fontePadrao
        self.b_connect["width"] = 12
        self.b_connect["command"] = 'self.verificaSenha'
        self.b_connect.pack()
    
    def set_l_path(self):
        path_name = tkFileDialog.askdirectory(title = "Select path",)
        self.l_path['text'] = path_name

root = Tk()
# root.geometry("500x500") #You want the size of the app to be 500x500
# root.resizable(0, 0)
app = Application2(master=root)
app.mainloop()
root.destroy()