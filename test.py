import tkinter
import tkinter.ttk

window=tkinter.Tk()
window.title("TEST")
window.geometry("640x600+100+100")
window.resizable(True, True)

treeview=tkinter.ttk.Treeview(window, columns=["one", "two"], displaycolumns=["two", "one"])
treeview.pack(side='left',fill='both',expand=True)

vsb = tkinter.ttk.Scrollbar(window, orient="vertical", command=treeview.yview)
vsb.pack(side='right', fill='y')

treeview.configure(yscrollcommand=vsb.set)

treeview.column("#0", anchor='center')
treeview.heading("#0", text="num", anchor='center')

treeview.column("one", anchor="center")
treeview.heading("one", text="문자", anchor="center")

treeview.column("#2", anchor="w")
treeview.heading("two", text="ASCII", anchor="center")

treelist=[("A", 65), ("B", 66), ("C", 67), ("D", 68), ("E", 69)]


for i in range(len(treelist)):
    treeview.insert('', 'end', text=str(i)+"번  ", values=treelist[i])
for i in range(len(treelist)):
    treeview.insert('', 'end', text=str(i)+"번", values=treelist[i])
for i in range(len(treelist)):
    treeview.insert('', 'end', text=str(i)+"번", values=treelist[i])
for i in range(len(treelist)):
    treeview.insert('', 'end', text=str(i)+"번", values=treelist[i])
for i in range(len(treelist)):
    treeview.insert('', 'end', text=str(i)+"번", values=treelist[i])
for i in range(len(treelist)):
    treeview.insert('', 'end', text=str(i)+"번", values=treelist[i])
for i in range(len(treelist)):
    treeview.insert('', 'end', text=str(i)+"번", values=treelist[i])
for i in range(len(treelist)):
    treeview.insert('', 'end', text=str(i)+"번", values=treelist[i])
for i in range(len(treelist)):
    treeview.insert('', 'end', text=str(i)+"번", values=treelist[i])
for i in range(len(treelist)):
    treeview.insert('', 'end', text=str(i)+"번", values=treelist[i])

window.mainloop()