import tkinter as tk

root = tk.Tk()
root.geometry('900x900')
frame_last_month = tk.Frame(root, width=900, height=300, bg='red')
frame_last_month.place(x=0, y=0)
frame_now_month = tk.Frame(root, width=900, height=300, bg='yellow')
frame_now_month.place(x=0, y=300)
frame_new_month = tk.Frame(root, width=900, height=300, bg='green')
frame_new_month.place(x=0, y=600)
root.mainloop()
