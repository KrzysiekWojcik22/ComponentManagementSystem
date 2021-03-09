import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()


    def create_widgets(self):

        self.AddComp = tk.Button(root, text="Add new Eq", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=10, y=10)

        self.AddComp = tk.Button(root, text="Show list", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=10, y=60)

        self.AddComp = tk.Button(root, text="Find", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=10, y=110)

        self.AddComp = tk.Button(root, text="Delete Eq", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=10, y=170)

        self.AddComp = tk.Button(root, text="Categories", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=350, y=10)

        self.AddComp = tk.Button(root, text="<", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=400, y=70)

        self.AddComp = tk.Button(root, text=">", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=400, y=120)

        self.AddComp = tk.Button(root, text="Quit", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=950, y=670)


        self.e = tk.Entry(root, width=50)
        self.e.place(height=40, width=80, x=250, y=570)





    def say_hi(self):
        print("hi there, everyone!")

    def show_list(self):
        print("show list")



root = tk.Tk()
app = Application(master=root)

app.master.title("Component Management System ")
root.geometry("1045x720")
app.mainloop()