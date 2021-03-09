import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()


    def create_widgets(self):

        self.AddComp = tk.Button(root, text="Add new Eq", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=15, y=15)

        self.AddComp = tk.Button(root, text="Show list", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=15, y=65)

        self.AddComp = tk.Button(root, text="Find", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=15, y=115)

        self.AddComp = tk.Button(root, text="Delete Eq", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=15, y=165)

        self.AddComp = tk.Button(root, text="<", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=700, y=430)

        self.AddComp = tk.Button(root, text=">", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=880, y=430)

        self.AddComp = tk.Button(root, text="INFO", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=790, y=430)

        self.AddComp = tk.Button(root, text="Quit", command=self.master.destroy)
        self.AddComp.place(height=40, width=80, x=950, y=665)

        self.Zastepcze = tk.Button(root, text="Tutaj Obrazek", command=self.say_hi)
        self.Zastepcze.place(height=400, width=400, x=630, y=15)


        self.Kategoria = tk.Entry(root, width=50)
        self.Kategoria.place(height=25, width=100, x=240, y=50)

        self.Typ = tk.Entry(root, width=50)
        self.Typ.place(height=25, width=100, x=200, y=570)

        self.Ilosc = tk.Entry(root, width=50)
        self.Ilosc.place(height=25, width=100, x=200, y=570)

        self.Informacje=tk.Label(root, text="Information:")
        self.Informacje.place(height=40, width=80, x=350, y=10)

        self.Informacje = tk.Label(root, text="Fast Find:", )
        self.Informacje.place(height=40, width=80, x=120, y=10)

        self.Informacje = tk.Label(root, text="Category:", )
        self.Informacje.place(height=40, width=80, x=120, y=40)

        self.Informacje = tk.Label(root, text="Type:", )
        self.Informacje.place(height=40, width=80, x=120, y=70)

        self.Informacje = tk.Label(root, text="Quantity:", )
        self.Informacje.place(height=40, width=80, x=120, y=100)

        self.Informacje = tk.Label(root, text="Where:", )
        self.Informacje.place(height=40, width=80, x=120, y=100)



    def say_hi(self):
        print("hi there, everyone!")

    def show_list(self):
        print("show list")



root = tk.Tk()
app = Application(master=root)

app.master.title("Component Management System ")
root.geometry("1045x720")
app.mainloop()