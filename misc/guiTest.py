from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

class GUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        EasyFrame.setSize(self, 300, 200)
        EasyFrame.setTitle(self, "GUI")
        EasyFrame.setResizable(self, True)
        
        ImageLabel  = self.addLabel(text="", row=0, column=0, sticky="NSEW")
        TextLabel   = self.addLabel(text="GUI TEST", row=1, column=0)
        
    self.image = PhotoImage(file="mm.gif")
    imageLabel["image"] = self.image
        
def main(): 
    GUI().mainloop()
    
if __name__ == "__main__":
    main()