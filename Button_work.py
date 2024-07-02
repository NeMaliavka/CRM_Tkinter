import calendar
from datetime import datetime
import tkinter as tk

dict_clients = {}
root = tk.Tk()
WIDTH = 600
HEIGHT = 900
root.geometry(f'{WIDTH}x{HEIGHT}')
frame_last_month = tk.Frame(root, width=WIDTH, height=HEIGHT / 3, bg='red')
frame_last_month.pack(expand=True, fill='both')
frame_now_month = tk.Frame(root, width=WIDTH, height=HEIGHT / 3, bg='yellow')
#frame_now_month.place(x=0, y=HEIGHT / 3)
frame_now_month.pack(expand=True, fill='both')
frame_new_month = tk.Frame(root, width=WIDTH, height=HEIGHT / 3, bg='green')
#frame_new_month.place(x=0, y=HEIGHT - (HEIGHT / 3))
frame_new_month.pack(expand=True, fill='both')

for x in range(0, 7):
    frame_last_month.rowconfigure(x, weight=1)
    frame_now_month.rowconfigure(x, weight=1)
    frame_new_month.rowconfigure(x, weight=1)
    frame_last_month.columnconfigure(x, weight=1)
    frame_now_month.columnconfigure(x, weight=1)
    frame_new_month.columnconfigure(x, weight=1)

month_now = datetime.now().month
#month_now = int(input())
dict_month = {1: 'Jun', 2: 'Feb',
              3: 'Mar', 4: 'Apr',
              5: 'May', 6: 'Jun',
              7: 'Jul', 8: 'Aug',
              9: 'Sep', 10: 'Oct',
              11: 'Nov', 12: 'Dec'}

for_y_coords = 5
for_x_coords = 5

def button_work():
    pass




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

#for_y_coords += 20
def create_button(year, month, frame):
    day_in_week = now_calendar(year, month)
    label_last_month = tk.Label(frame, text=f'{dict_month[month]}\n{year}', font=('Arial', 10, 'bold'))
    # label_last_month.place(x=for_x_coords, y=for_y_coords)
    label_last_month.grid(row=0, column=0, sticky=tk.NSEW)
    for_column = 0
    for_row = 1
    for day_in_dick in day_in_week:
        # for_y_coords += 20
        label_day_in_week = tk.Label(frame, text=day_in_dick, width=5, font=('Arial', 9, 'bold'))
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
            button_day_in_last_month = tk.Button(frame, text=day[2], height=2, command=button_work)
            # button_day_in_last_month.place(x=for_x_coords+10, y=for_y_coords)
            button_day_in_last_month.grid(row=for_row, column=for_column,sticky=tk.NSEW)
        for_column += 1
        for_row = 1
if month_now == 1:
    create_button(datetime.now().year-1, 12, frame_last_month)
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

    # for_x_coords += 65
    # for_y_coords = 25
    # i = str(i[0])
    # i = i.split('-')
    # if int(i[1]) != month_now - 1:
    #     continue
    # label_day_in_label_last_month = tk.Label(root, text=f'{i[2]}')
    # label_day_in_label_last_month.place(x=10, y=monday_y)
    # monday_y += 20

# label_now_month = tk.Label(root, text=f'{dict_month[month_now]}')
# label_now_month.place(x=10, y=30)
#
# label_new_month = tk.Label(root, text=f'{dict_month[month_now+1]}')
# label_new_month.place(x=10, y=50)

root.mainloop()
