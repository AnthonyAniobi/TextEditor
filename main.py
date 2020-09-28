from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *
from TextEditor import file_menu
from TextEditor import edit_menu
from TextEditor import format_menu
from TextEditor import help_menu

class TextEditor(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Text Editor- Untitled")
        self.geometry("300x250+100+10")
        self.minsize(width=500, height=600)

        text = ScrolledText(self, state='normal', height=400, width=400,
                            wrap='word', pady=2, padx=3, undo=True)
        text.pack(fill=Y, expand=1)
        text.focus_set()

        menu_bar = Menu(self)

        file_menu.main(self, text, menu_bar)
        edit_menu.main(self, text, menu_bar)
        format_menu.main(self,text, menu_bar)
        help_menu.main(self, text, menu_bar)

# if __name__ == "__main__":
#     app = TextEditor()
#     app.mainloop()