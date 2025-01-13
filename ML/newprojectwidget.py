#!/usr/bin/python3
import tkinter as tk


class NewprojectWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(NewprojectWidget, self).__init__(master, **kw)
        self.configure(background="#000080", height=400, width=600)


if __name__ == "__main__":
    root = tk.Tk()
    widget = NewprojectWidget(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
