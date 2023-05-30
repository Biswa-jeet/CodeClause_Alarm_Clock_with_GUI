import tkinter as tk
from tkinter import messagebox
import datetime
import pygame

class AlarmClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Alarm Clock")
        self.master.geometry("300x200")
        self.master.configure(bg="#fcad03")

        pygame.mixer.init()

        self.alarm_time = datetime.time()

        self.label = tk.Label(self.master, text="Set Alarm", font=("Helvetica", 14), bg="#f2f2f2")
        self.label.pack(pady=10)

        self.time_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.time_entry.pack(pady=10)

        self.set_button = tk.Button(self.master, text="Set",bg="#4e3eab",highlightbackground='#51cfb1',
                                     font=("Helvetica", 12), command=self.setalarm)
        self.set_button.pack(pady=10)

        self.stop_button = tk.Button(self.master, text="Stop",bg="#fc3503",border=12, font=("Helvetica", 12),
                                      command=self.stopalarm, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

    def setalarm(self):
        try:
            alarm_time_str = self.time_entry.get()
            self.alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M").time()

            current_time = datetime.datetime.now().time()
            current_datetime = datetime.datetime.combine(datetime.date.today(), current_time)
            alarm_datetime = datetime.datetime.combine(datetime.date.today(), self.alarm_time)

            if current_datetime > alarm_datetime:
                alarm_datetime += datetime.timedelta(days=1)

            time_diff = (alarm_datetime - current_datetime).total_seconds()
            self.master.after(int(time_diff * 1000), self.startalarm)

            self.set_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.time_entry.config(state=tk.DISABLED)

        except ValueError:
            messagebox.showerror("Error", "Use HH:MM format.")

    def stopalarm(self):
        self.set_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.time_entry.config(state=tk.NORMAL)
        pygame.mixer.music.stop()

    def startalarm(self):
        messagebox.showinfo("Alarm", "Wake up!")


        pygame.mixer.music.load("alarm.wav")
        pygame.mixer.music.play(loops=-1) 

    def exit(self):
        pygame.mixer.music.stop()
        self.master.destroy()

root = tk.Tk()
alarm_clock = AlarmClock(root)
root.protocol("WM_DELETE_WINDOW", alarm_clock.exit)
root.mainloop()
