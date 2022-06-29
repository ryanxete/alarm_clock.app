# Alarm Clock Lab
# As a developer, I want to use Python’s proper snake_case for variable names.
# As a developer, I want to create a AlarmClock class.
# As a developer, I want the AlarmClock class to have class instance variables to keep track of the AlarmClock’s current time, whether the alarm is on or off, and the time the alarm is set to. (You can use arbitrary strings to represent the time, it does not need to accurately tell the current time or change over time).
# As a developer, I want the AlarmClock class to have a method to set (or change) the current time and print to the console the current time.
# As a developer, I want the AlarmClock class to have a method to toggle the alarm on or off.
# As a developer, I want the AlarmClock class to have a method to set the current alarm time and print to the console the current alarm time.
# As a developer, I want to import the AlarmClock class into main.py so I can instantiate it as a new AlarmClock object and call methods on it.
# 1. Print the clock’s time to the terminal
# 2. Call the alarm clock’s change current time method to change the current time
# 3. Toggle the alarm clock’s on off switch

import random

class AlarmClock:
    def __init__(self):
        self.current_time = random.randint(0, 24)
        self.alarm_is_on = True
        self.set_clock = random.randint(0, 24)

    def display_time(self):
        print(f"time is {self.current_time}o'clock")

    def alarm_switch(self):
        if self.alarm_is_on == True:
            self.alarm_is_on = False
        else:
             alarm_is_on == True

    def set_alarm(self):
        alarm_time

clock = AlarmClock()

