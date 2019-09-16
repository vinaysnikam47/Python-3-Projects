from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import messagebox


def new_window():
    root_2 = Tk()
    TextEditor(root_2)
    root_2.mainloop()


class TextEditor:

    current_file_name = ''

    # Open File
    def open_file(self):
        opened_data = filedialog.askopenfile(title='Select File',
                                             filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
        if opened_data is not None:
            self.text.delete(1.0, END)
            for line in opened_data:
                self.text.insert(END, line)
            self.current_file_name = opened_data.name
            opened_data.close()
        else:
            return

    # Save File as
    def save_as_file(self):
        data_to_be_saved = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if data_to_be_saved is None:
            return
        else:
            self.current_file_name = data_to_be_saved.name
            data_to_be_saved.write(self.text.get(1.0, END))
            data_to_be_saved.close()
            messagebox.showinfo(title='Success', message='File saved successfully.')

    # Save file
    def save_file(self):
        if self.current_file_name == '':
            self.save_as_file()
        else:
            file_to_be_saved = open(self.current_file_name, mode='w+')
            file_to_be_saved.write(self.text.get(1.0, END))
            file_to_be_saved.close()

    # Copy Text
    def copy_text(self):
        self.text.clipboard_clear()
        self.text.clipboard_append(self.text.selection_get())

    # Cut Text
    def cut_text(self):
        self.copy_text()
        self.text.delete('sel.first', 'sel.last')

    # Paste Text
    def paste_text(self):
        self.text.insert(INSERT, self.text.clipboard_get())

    # Color Text editor
    def color_me(self):
        clr = colorchooser.askcolor(title='Select color')
        self.text.configure(bg=clr[1])

    # Constructor of class
    def __init__(self, master):
        self.master = master
        self.master.geometry('300x250')
        self.master.title('Sticky')

        # Scroll bar
        self.scroll = Scrollbar(master)
        self.scroll.pack(side=RIGHT, fill=Y)

        # Text Area
        self.text = Text(master, undo=TRUE, font=('calibry', 10), bg='light green', yscrollcommand=self.scroll.set)
        self.text.pack(fill=BOTH, expand=TRUE)
        self.scroll.config(command=self.text.yview)

        # Menu Bar
        self.main_menu = Menu(master)
        self.master.config(menu=self.main_menu)

        # File Menu
        self.file_menu = Menu(self.main_menu, tearoff=FALSE)
        self.main_menu.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label='New', command=new_window)
        self.file_menu.add_command(label='Open', command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Save', command=self.save_file)
        self.file_menu.add_command(label='Save as', command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=master.quit)

        # Edit menu
        self.edit_menu = Menu(self.main_menu, tearoff=FALSE)
        self.main_menu.add_cascade(label='Edit', menu=self.edit_menu)
        self.edit_menu.add_command(label='Undo', command=self.text.edit_undo)
        self.edit_menu.add_command(label='Redo', command=self.text.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label='Copy', command=self.copy_text)
        self.edit_menu.add_command(label='Cut', command=self.cut_text)
        self.edit_menu.add_command(label='Paste', command=self.paste_text)

        # Color menu
        self.main_menu.add_command(label='Color', command=self.color_me)

        # Shortcut key bind
        self.master.bind('<Control-n>', lambda event: new_window())
        self.master.bind('<Control-o>', lambda event: self.open_file())
        self.master.bind('<Control-s>', lambda event: self.save_file())
        self.master.bind('<Control-Shift-S>', lambda event: self.save_as_file())


if __name__ == '__main__':
    root = Tk()
    text_editor = TextEditor(root)
    root.mainloop()
