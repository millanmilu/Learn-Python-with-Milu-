class Clock():

    def __init__(self,hours = 0,minutes = 0,seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def set_clock(self,hours,minutes,seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        if type(hours) == int and 0 <= hours and hours < 24:
            self.hours = hours
        else:
            raise TypeError("Hours have to be integer between 0 to 23!")
        if type(minutes) == int and 0<= minutes  and minutes< 60:
            self.minutes = minutes
        else:
            raise TypeError("Minutes have to be integer btw 0 to 59!")
        if type(seconds) == int and 0<= seconds and seconds < 60:
            self.seconds = seconds
        else:
            raise TypeError("Seconds have to be integer btw 0 to 59!")

    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self.hours,
                                                self.minutes,
                                                self.seconds)


    def tick(self):
        if self.seconds == 59:
            self.seconds = 0
            if self.minutes == 59:
                self.minutes =0
                if self.hours == 24:
                    self.hours = 0
                else:
                    self.hours +=1
            else:
                self.minutes += 1
        else:
            self.seconds += 1

if __name__ =="__main__":
    x = Clock(23,59,59)
    print(x)
    x.tick()
    print(x)
    y = str(x)
    print(type(y))