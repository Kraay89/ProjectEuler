from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(1901, 1, 1)
end_date = date(2000, 12, 31)
sundays = 0
for single_date in daterange(start_date, end_date):
    print single_date.weekday()
    if single_date.day == 1:
        if single_date.weekday() == 6:
            print "passed"
            sundays+=1

print sundays