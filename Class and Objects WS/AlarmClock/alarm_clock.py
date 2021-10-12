


class AlarmClock:
    def __init__(self, current_time, set_alarm_time):
        self.current_time = current_time
        self.on_or_off = False
        self.set_alarm_time = set_alarm_time

    def set_time(self):
        time = input('What is the current time? Include PM or AM, do not include timezone.')
        self.current_time = time
        print(f'The current time is {self.current_time}')
    
    def toggle_alarm(self, on_or_off):
        status = on_or_off.lower()
        if status == 'on':
            self.on_or_off = True
            print(f'Alarm is now on!')
        elif status == 'off':
            self.on_or_off = False
            print(f'Alarm is now off!')
        else:
            print(f'Your input was not read properly. ')

    def set_alarm(self):
        alarm_time = input(f'Please input the time you wish to wake up! Include PM or AM, do not include timezone. ')
        self.set_alarm_time = alarm_time
        print(f'Your new alarm time is {alarm_time}')

    def check_alarm(self):
        if self.current_time == self.set_alarm_time:
            print(f'Bepp \nBeep \nBeep \nTime to get up! \nBeep \nBeep \nBeep')