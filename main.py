import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def Add(self):
        top = tk.Toplevel()
        top.title('Add new equipment')
        top.geometry("300x500")




        self.AddComponent = tk.Button(top, text="Add EQ",command=self.fAddComponent)
        self.AddComponent.place(height=40,width=80, x =15, y=445 , )

        self.ClearComponent = tk.Button(top, text="Clear", command=self.fClearComponent)
        self.ClearComponent.place(height=40, width=80, x=110, y=445, )

        self.QuitComponent = tk.Button(top, text="Quit", command=self.fQuitComponent)
        self.QuitComponent.place(height=40, width=80, x=205, y=445, )

        self.lName = tk.Label(top, text="Name:", )
        self.lName.place(height=40, width=80, x=10, y=10)

        self.lCategory = tk.Label(top, text="Category:", )
        self.lCategory.place(height=40, width=80, x=10, y=60)

        self.lGroup = tk.Label(top, text="Group:", )
        self.lGroup.place(height=40, width=80, x=10, y=110)

        self.lAssembly = tk.Label(top, text="Assembly:", )
        self.lAssembly.place(height=40, width=80, x=10, y=160)

        self.lCase = tk.Label(top, text="Case:", )
        self.lCase.place(height=40, width=80, x=10, y=210)

        self.lSize = tk.Label(top, text="Size:", )
        self.lSize.place(height=40, width=80, x=10, y=260)

        self.lStorage = tk.Label(top, text="Storage:", )
        self.lStorage.place(height=40, width=80, x=10, y=310)

        self.lQuantity = tk.Label(top, text="Quantity:", )
        self.lQuantity.place(height=40, width=80, x=10, y=360)

        SizeComponents = ["0201","0402", "0603","0805","1008","1206","1210"]
        Categories = ["Semiconductor",]
        SposobMontazu = ["THT", "SMD"]
        #CasesTHT = ["DIP", "SDIP" , "TO" ]
        CasesSMD = ["SOJ", "SOIC", "PLCC", "QFP", "BGA"]
        grupa = ["1"]


        self.Name = tk.Entry(top, width=50)
        self.Name.place(height=20, width=180, x=100, y=20)

        self.KategoriaZW = ttk.Combobox(top, values = Categories)
        self.KategoriaZW.place(height=20, width=180, x=100, y=70)

        self.Grupaz = ttk.Combobox(top, values = grupa)
        self.Grupaz.place(height=20, width=180, x=100, y=120)

        self.Montazz = ttk.Combobox(top, values = SposobMontazu)
        self.Montazz.place(height=20, width=180, x=100, y=170)

        self.Obudowaz = ttk.Combobox(top, values = CasesSMD)
        self.Obudowaz.place(height=20, width=180, x=100, y=220)

        self.rozmiarz = ttk.Combobox(top, values = SizeComponents)
        self.rozmiarz.place(height=20, width=180, x=100, y=270)

        self.rozmiarz = ttk.Combobox(top, values=CasesSMD)
        self.rozmiarz.place(height=20, width=180, x=100, y=320)



        self.iloscz = tk.Entry(top, width=50)
        self.iloscz.place(height=20, width=180, x=100, y=370)




    def show(self):
        top = tk.Toplevel()
        top.title('Show a equipment')

    def find(self):
        top = tk.Toplevel()
        top.title('Find equipment')

    def delete(self):
        top = tk.Toplevel()
        top.title('Delete equipment')



    def create_widgets(self):

        self.AddComp = tk.Button(root, text="Add new Eq", command=self.Add)
        self.AddComp.place(height=40, width=80, x=15, y=15)

        self.ShowComp = tk.Button(root, text="Show list", command=self.show)
        self.ShowComp.place(height=40, width=80, x=15, y=65)

        self.FindComp = tk.Button(root, text="Find", command=self.find)
        self.FindComp.place(height=40, width=80, x=15, y=115)

        self.DeleteComp = tk.Button(root, text="Delete Eq", command=self.delete)
        self.DeleteComp.place(height=40, width=80, x=15, y=165)

        self.AddComp = tk.Button(root, text="<", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=700, y=430)

        self.AddComp = tk.Button(root, text=">", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=880, y=430)

        self.AddComp = tk.Button(root, text="INFO", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=790, y=430)

        self.AddComp = tk.Button(root, text="Quit", command=self.master.destroy)
        self.AddComp.place(height=40, width=80, x=950, y=665)

        self.AddComp = tk.Button(root, text="+", command=self.master.destroy)
        self.AddComp.place(height=40, width=40, x=265, y=240)

        self.AddComp = tk.Button(root, text="-", command=self.master.destroy)
        self.AddComp.place(height=40, width=40, x=214, y=240)

        self.Zastepcze = tk.Button(root, text="Tutaj Obrazek", command=self.say_hi)
        self.Zastepcze.place(height=400, width=400, x=630, y=15)

        self.AddComp = tk.Button(root, text="Export1", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=15, y=500)

        self.AddComp = tk.Button(root, text="Export2", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=110, y=500)

        self.AddComp = tk.Button(root, text="Export3", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=205, y=500)



        self.Kategoria = tk.Entry(root, width=50)
        self.Kategoria.place(height=25, width=100, x=210, y=50)

        self.Typ = tk.Entry(root, width=50)
        self.Typ.place(height=25, width=100, x=210, y=100)

        self.Ilosc = tk.Entry(root, width=50)
        self.Ilosc.place(height=25, width=100, x=210, y=150)

        self.Where = tk.Entry(root, width=50)
        self.Where.place(height=25, width=100, x=210, y=200)

        self.Informacje = tk.Label(root, text="Information:")
        self.Informacje.place(height=40, width=80, x=350, y=10)

        self.Informacje = tk.Label(root, text="Fast Find:", )
        self.Informacje.place(height=40, width=80, x=120, y=10)

        self.Informacje = tk.Label(root, text="Category:", )
        self.Informacje.place(height=40, width=80, x=120, y=40)

        self.Informacje = tk.Label(root, text="Type:", )
        self.Informacje.place(height=40, width=80, x=120, y=90)

        self.Informacje = tk.Label(root, text="Where:", )
        self.Informacje.place(height=40, width=80, x=120, y=140)

        self.Informacje = tk.Label(root, text="Quantity:", )
        self.Informacje.place(height=40, width=80, x=120, y=190)


        self.Informacje = tk.Label(root, text="text" )
        self.Informacje.place(height=40, width=80, x=500, y=190)

    def say_hi(self):
        print("hi there, everyone!")

    def show_list(self):
        print("show list")

    def fAddComponent(self):
        print("AddComponent")
        messagebox.showinfo("Information", "Components was added")
        messagebox.showerror("Error", "Please complete all tables")

    def fClearComponent(self):
        print("ClearComponent")

    def fQuitComponent(self):
        print("Quit")


root = tk.Tk()
app = Application(master=root)

app.master.title("Component Management System ")
root.geometry("1045x720")

app.mainloop()