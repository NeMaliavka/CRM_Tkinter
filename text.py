# from tkinter import *
# from tkinter.scrolledtext import ScrolledText
#
# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x150")
#
# st = ScrolledText(root, width=50, height=10)
# st.pack(fill=BOTH, side=LEFT, expand=True)
#
# root.mainloop()
'''
from tkinter import *

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

char_editor = Text(height=5, wrap="char")
char_editor.pack(anchor=N, fill=X)

word_editor = Text(height=5, wrap="word")
word_editor.pack(anchor=S, fill=X)

root.mainloop()
'''

from tkinter import *
from tkinter import messagebox as mb


def check():
    answer = mb.askyesno(title="Вопрос",
                         message="Перенести данные?")
    if answer:
        s = entry.get()
        entry.delete(0, END)
        label['text'] = s


root = Tk()
entry = Entry()
entry.pack(pady=10)
Button(text='Передать', command=check).pack()
label = Label(height=3)
label.pack()

root.mainloop()
