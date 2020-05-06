'''  
Given two persons calendar, and meeting duration time, list the available meeting slots, each persons have
their day start time and end time. 
''' 

class Calendar:
    def __init__(self, startTime, endTime, schedule):
        self.startTime = startTime
        self.endTime = endTime
        self.schedule = schedule
        self.preprocessCalendar()
    
    def preprocessCalendar(self):
        self.startTime = self.minute(self.startTime)
        self.endTime = self.minute(self.endTime)
        self.schedule = [ [self.minute(window[0]), self.minute(window[1])] for window in self.schedule]
    
    def minute(self,timeString):
        if type(timeString) is str:
            hour, minute = map(int,timeString.split(":"))
            return hour*60+minute
        return timeString
    
    def timeString(self,minute):
        if type(minute) is int:
            hour = minute//60
            minute = minute%60
            return "{0:02d}:{1:02d}".format(hour,minute)
        return minute

    def insertSchedule(self, window):
        startTime = max(self.startTime,window[0])
        endTime = min(self.endTime,window[1])
        if startTime < endTime:
            self.schedule.append([startTime,endTime])

    def mergeCalendar(self,otherCalendar):
        startTime = max(self.startTime, otherCalendar.startTime)
        endTime = min(self.endTime, otherCalendar.endTime)
        schedule = []
        outputCalendar = Calendar(startTime,endTime,schedule)
        n1 = len(self.schedule)
        n2 = len(otherCalendar.schedule)
        i = j =0
        while(i < n1 and j < n2):
            firstPersonWindowStart , firstPersonWindowEnd = self.schedule[i]
            secondPersonWindowStart, secondPersonWindowEnd = otherCalendar.schedule[j]
            # window is inside another
            if firstPersonWindowStart <= secondPersonWindowStart and secondPersonWindowEnd <= firstPersonWindowEnd:
                outputCalendar.insertSchedule([firstPersonWindowStart,firstPersonWindowEnd])
            elif secondPersonWindowStart <= firstPersonWindowStart and firstPersonWindowEnd <= secondPersonWindowEnd:
                outputCalendar.insertSchedule([secondPersonWindowStart,secondPersonWindowEnd])
            # windows start and end overlap partially
            elif firstPersonWindowEnd <= secondPersonWindowEnd and secondPersonWindowStart <= firstPersonWindowEnd:
                outputCalendar.insertSchedule([firstPersonWindowStart,secondPersonWindowEnd])
            elif secondPersonWindowEnd <= firstPersonWindowEnd and firstPersonWindowStart <= secondPersonWindowEnd:
                outputCalendar.insertSchedule([secondPersonWindowStart,firstPersonWindowEnd])
            # no overlap in window
            elif firstPersonWindowEnd < secondPersonWindowStart:
                outputCalendar.insertSchedule(self.schedule[i])
                outputCalendar.insertSchedule(otherCalendar.schedule[j])
            elif secondPersonWindowEnd < firstPersonWindowStart:
                outputCalendar.insertSchedule(otherCalendar.schedule[j])
                outputCalendar.insertSchedule(self.schedule[i])
            i += 1
            j += 1

        while(i < n1):
            outputCalendar.insertSchedule(self.schedule[i])
            i += 1
        
        while(j < n2):
            outputCalendar.insertSchedule(otherCalendar.schedule[j])    
            j += 1

        return outputCalendar

    def freeSlot(self,duration):
        slots = []
        n = len(self.schedule)
        if (self.schedule[0][0] - self.startTime) >= duration:
            slots.append([self.startTime,self.schedule[0][0]])
        for i in range(n-1):
            startTime = self.schedule[i][1]
            endTime = self.schedule[i+1][0]
            window = endTime - startTime
            if window >= duration:
                slots.append([startTime,endTime])
        if (self.endTime - self.schedule[n-1][1]) >= duration:
            slots.append([self.schedule[n-1][1],self.endTime])
        # print(slots)
        return [[self.timeString(window[0]),self.timeString(window[1])] for window in slots]

if __name__ == "__main__":
    person1 = Calendar("9:00","17:00",[["10:00","11:00"],["12:00","12:30"],["13:00","13:30"],["13:40","13:50"],["14:20","14:30"],["15:20","15:30"]])
    person2 = Calendar("9:00","14:00",[["10:30","11:30"],["11:45","12:15"],["13:10","13:20"],["13:30","14:00"],["14:40","14:50"],["15:00","15:10"]])
    # print(person1.startTime,person1.endTime,person1.schedule)
    # print(person2.startTime,person2.endTime,person2.schedule)
    t = person1.mergeCalendar(person2)
    # print(t.schedule)
    duration = 20
    print("Free slot of duration {} in both person calendar is {}".format(duration,t.freeSlot(duration)))
