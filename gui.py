import Tkinter

class simpleapp_tk(Tkinter.Tk):
  def __init__(self,parent):
    Tkinter.Tk.__init__(self,parent)
    self.parent = parent
    self.initialize()

  def initialize(self):
    self.grid()

    self.entryVar = Tkinter.StringVar()
    self.entry = Tkinter.Entry(self,textvariable=self.entryVar)
    self.entry.grid(column=0,row=0,sticky='EW')
    self.entry.bind("<Return>",self.OnPressEnter)
    self.entryVar.set(u"Enter Text Here.")

    button = Tkinter.Button(self,text=u"Click Me!",command=self.OnButtonClick)
    button.grid(column=1,row=0)

    self.labelVar = Tkinter.StringVar()
    label = Tkinter.Label(self, textvariable=self.labelVar,anchor="w", fg="white",bg="blue")
    label.grid(column=0,row=1,columnspan=2,sticky='EW')
    self.labelVar.set(u"Hello!")

    self.resizable(False,False)
    self.update()
    self.geometry(self.geometry())
    self.entry.focus_set()
    self.entry.selection_range(0,Tkinter.END)

  def OnButtonClick(self):
    self.labelVar.set(self.entryVar.get()+"You clicked!")
    self.entry.focus_set()
    self.entry.selection_range(0,Tkinter.END)
  def OnPressEnter(self,event):
    self.labelVar.set(self.entryVar.get()+"you pressed enter!")
    self.entry.focus_set()
    self.entry.selection_range(0,Tkinter.END)
    
if __name__ == "__main__":
  app = simpleapp_tk(None)
  app.title('my application')
  app.mainloop()
