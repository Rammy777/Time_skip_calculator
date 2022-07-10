from tkinter import *
import time_add


base = Tk()
base.title("Time_Skip_Calculator_Rammy777")
base.geometry('350x350')
i_text = Label(base, text="Give Start hours and minutes (day is optional)")
i_text.grid(column=0, row=0)
i_text = Label(base, text="**********************************************")
i_text.grid(column=0, row=1)
i_text = Label(base, text="Hours [1 - 12]")
i_text.grid(column=0, row=2)
i_text = Label(base, text="Minutes [0 - 59]")
i_text.grid(column=0, row=3)
i_text = Label(base, text="AM/PM")
i_text.grid(column=0, row=4)
i_text = Label(base, text="Day (Optional)")
i_text.grid(column=0, row=5)
i_text = Label(base, text="**********************************************")
i_text.grid(column=0, row=6)
i_text = Label(base, text="Hours to add [Any Integer Value]")
i_text.grid(column=0, row=7)
i_text = Label(base, text="Minutes to add [0 - 59]")
i_text.grid(column=0, row=8)

hour = Entry(base, width=10)
hour.grid(column=1, row=2)
minute = Entry(base, width=10)
minute.grid(column=1, row=3)
ap = Entry(base, width=10)
ap.grid(column=1, row=4)
day = Entry(base, width=10)
day.grid(column=1, row=5)
hour_add = Entry(base, width=10)
hour_add.grid(column=1, row=7)
minute_add = Entry(base, width=10)
minute_add.grid(column=1, row=8)
i_text = Label(base, text="**********************************************")
i_text.grid(column=0, row=9)


def click():
    out_text = Label(base)
    out_text.grid(column=0, row=10)
    try:
        if int(hour.get()) in range(1,13) and int(minute.get()) in range(0, 59) and int(minute_add.get()) in range(0, 59):
            out = time_add.add_time(str(hour.get())+":"+str(minute.get())+" "+str(ap.get()).upper(), str(hour_add.get())+":" +
                                    str(minute_add.get()), str(day.get()).lower().capitalize())
            output.delete(0, "end")
            output.insert(0, out)
            out_text.configure(text="Okay")
            out_text.update()
        else:
            out_text.configure(text="Give input in right format")
            out_text.update()
    except:
        out_text.configure(text="Give input in right format")
        out_text.update()
    out_text.after(5000, lambda: out_text.destroy())


btn = Button(base, text="Click to post",
             fg="black", command=click)
i_text = Label(base, text="**********************************************")
i_text.grid(column=0, row=11)
btn.grid(column=0, row=12)
output = Entry(base, width=40)
output.grid(column=0, row=13)


base.mainloop()
