import tkinter as tk
from tkinter import messagebox as mb
import calendar
from datetime import datetime

date_now = datetime.now()
month_now = datetime.now().month

root = tk.Tk()
root.resizable(False, False)
WIDTH = 600
HEIGHT = 900
root.geometry(f'{int(WIDTH / 2)}x{int(HEIGHT / 3)}')
root.title('CRM')

date = {'Mon':{'10:20':['Степан Прудников'],
               '12:20':['Аскар Бессолицин'],
               '13:00':['Овчинников Мирон'],
               '15:00':['Весенёв Артемий', 'Пономарёв Денис']}}
try:
    file = open('my_work.txt', 'r', encoding='utf_8')
except:
    print('No File in Directory')
else:
    pass

main_frame = tk.Frame(root, width=WIDTH, height=HEIGHT - 100)
main_frame.pack(expand=True, fill='both')
additional_frame = tk.Frame(root, width=WIDTH, height=HEIGHT - (HEIGHT - 100), bg='yellow')
additional_frame.pack(expand=True, fill='both')
additional_frame.rowconfigure(0, weight=1)
additional_frame.columnconfigure(0, weight=1)

frame_last_month = tk.Frame(main_frame, width=WIDTH, height=HEIGHT / 3)
frame_last_month.pack(expand=True, fill='both')
frame_now_month = tk.Frame(main_frame, width=WIDTH, height=HEIGHT / 3)
frame_now_month.pack(expand=True, fill='both')
frame_new_month = tk.Frame(main_frame, width=WIDTH, height=HEIGHT / 3)
frame_new_month.pack(expand=True, fill='both')
for x in range(0, 7):
    frame_last_month.rowconfigure(x, weight=1)
    frame_now_month.rowconfigure(x, weight=1)
    frame_new_month.rowconfigure(x, weight=1)
    frame_last_month.columnconfigure(x, weight=1)
    frame_now_month.columnconfigure(x, weight=1)
    frame_new_month.columnconfigure(x, weight=1)

def value():
    # answer = mb.askyesno(title="Вопрос",
    #                      message="Перенести данные?")
    # if answer:
    #     # s = entry.get()
    #     entry.delete(0, END)
    #     # label['text'] = s
    pass


def new_value_for_dict_date(weekday):
    new_root = tk.Toplevel()
    new_root.resizable(False, False)
    new_root.title('value')
    entry = tk.Entry()
    entry.pack(pady=10)
    tk.Button(new_root, text='Внести событие', command=value).pack()
    # label_entry = tk.Label()
    # label_entry.pack()
    print(weekday)
    new_root.grab_set()


def button_exit():
    exit()


def button_work(bookyear, bookmonth, bookday, weekday):
    #pass
    print(bookyear, bookmonth, bookday, weekday)
    new_root = tk.Toplevel()
    new_root.resizable(False, False)
    new_root.title('time')
    new_label = tk.Label(new_root, text=f'{weekday} ({bookday}.{bookmonth})')
    new_label.grid(row=0, column=0)
    start_new_button = tk.Button(new_root, text='Создать событие', command=lambda weekday=weekday: new_value_for_dict_date(weekday))
    start_new_button.grid(sticky=tk.NSEW)
    for time in date[weekday]:
        button_time = tk.Button(new_root, text=f'{time} - {date[weekday][time]}', borderwidth=0)
        button_time.grid(sticky=tk.NSEW)
    new_root.grab_set()




def create_button(year, month, frame):
    day_in_week = now_calendar(year, month)
    label_last_month = tk.Label(frame, text=f'{dict_month[month]}  ({month}.{year})', font=('Arial', 10, 'bold'),
                                bg='lightgreen')
    # label_last_month.place(x=for_x_coords, y=for_y_coords)
    label_last_month.grid(row=0, column=0, columnspan=7, sticky=tk.NSEW)
    for_column = 0
    for_row = 1
    for day_in_dick in day_in_week:
        # for_y_coords += 20
        label_day_in_week = tk.Label(frame, text=day_in_dick, width=5, font=('Arial', 9, 'bold'), bg='purple',
                                     fg='white')
        # label_day_in_week.place(x=for_x_coords, y=for_y_coords, width=63, height=20)
        label_day_in_week.grid(row=for_row, column=for_column, sticky=tk.NSEW)

        for day in day_in_week[day_in_dick]:
            day = str(day).split('-')
            for_row += 1
            # for_y_coords += 25
            if int(day[1]) != month:
                label_day_in_label_last_month = tk.Label(frame, text='')
                # label_day_in_label_last_month.place(x=for_x_coords + 10, y=for_y_coords)
                label_day_in_label_last_month.grid(row=for_row, column=for_column, sticky=tk.NSEW)
                continue
            button_day_in_last_month = tk.Button(frame, text=day[2], height=2, borderwidth=0, font=('Arial', 10),
                                                 command=lambda bookyear=year, bookmonth=month, bookday=day[2], weekday=day_in_dick: button_work(bookyear,
                                                                                                             bookmonth,
                                                                                                             bookday, weekday))
            # button_day_in_last_month.place(x=for_x_coords+10, y=for_y_coords)
            button_day_in_last_month.grid(row=for_row, column=for_column, sticky=tk.NSEW)

        pass_label = tk.Label(frame, text='\n', width=5, height=1, bg='lightblue')
        pass_label.grid(row=for_row + 1, column=for_column, columnspan=7, sticky=tk.NSEW)
        for_column += 1
        for_row = 1
    exit_button = tk.Button(additional_frame, text='Завершить работу', font=('Arial', 17, 'bold'), command=button_exit)
    exit_button.grid(row=0, column=5, columnspan=2, sticky=tk.NSEW)


def time():
    string = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    date_label.config(text=string)
    date_label.after(1000, time)


def start_work():
    start_button.destroy()
    root.geometry(f'{WIDTH}x{HEIGHT}')
    if month_now == 1:
        create_button(datetime.now().year - 1, 12, frame_last_month)
        create_button(datetime.now().year, month_now, frame_now_month)
        create_button(datetime.now().year, month_now + 1, frame_new_month)
    elif month_now == 12:
        create_button(datetime.now().year, month_now - 1, frame_last_month)
        create_button(datetime.now().year, month_now, frame_now_month)
        create_button(datetime.now().year + 1, 1, frame_new_month)
    else:
        create_button(datetime.now().year, month_now - 1, frame_last_month)
        create_button(datetime.now().year, month_now, frame_now_month)
        create_button(datetime.now().year, month_now + 1, frame_new_month)


dict_month = {1: 'Jan', 2: 'Feb',
              3: 'Mar', 4: 'Apr',
              5: 'May', 6: 'Jun',
              7: 'Jul', 8: 'Aug',
              9: 'Sep', 10: 'Oct',
              11: 'Nov', 12: 'Dec'}


def now_calendar(year, month):
    a = calendar.Calendar().monthdatescalendar(year, month)
    dict_month_day_in_week = {'Mon': [i[0] for i in a],
                              'Tue': [i[1] for i in a],
                              'Wed': [i[2] for i in a],
                              'Thu': [i[3] for i in a],
                              'Fri': [i[4] for i in a],
                              'Sat': [i[5] for i in a],
                              'Sun': [i[6] for i in a]}
    return dict_month_day_in_week


start_button = tk.Button(root, text='Начать работу', font=('Arial', 20, 'bold'), command=start_work)
start_button.place(x=int((WIDTH / 2) / 2 - 125), y=int((HEIGHT / 3) / 3), width=250, height=50)

date_label = tk.Label(root, text=f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}', font=('Arial', 10))
date_label.place(x=0, y=0, width=135, height=20)

time()
root.mainloop()
