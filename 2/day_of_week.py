__author__ = 'Sergei.Ivanov'

def weekDay(year, month, day):
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    week   = ['Sunday',
              'Monday',
              'Tuesday',
              'Wednesday',
              'Thursday',
              'Friday',
              'Saturday']
    afterFeb = 1
    if month > 2: afterFeb = 0
    aux = year - 1700 - afterFeb
    # dayOfWeek for 1700/1/1 = 5, Friday
    dayOfWeek  = 5
    # partial sum of days betweem current date and 1700/1/1
    dayOfWeek += (aux + afterFeb) * 365
    # leap year correction
    dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400
    # sum monthly and day offsets
    dayOfWeek += offset[month - 1] + (day - 1)
    dayOfWeek %= 7
    return week[dayOfWeek]

# import datetime
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
week   = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

with open("input.txt") as f, open("output.txt", "w+") as g:
    for line in f:
        d = line.split()
        day = int(d[0])
        month = months.index(d[1]) + 1
        year = int(d[2])
        week_day = weekDay(year, month, day)
        # week_day = week[datetime.date(year, month, day).weekday() + 1]
        print year, month, day, week_day
        g.write(week_day + '\n')

console = []