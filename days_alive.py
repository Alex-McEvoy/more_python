# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet! 
# Just brainstorm ways you might approach it!

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    ##Leap years are not divisible by 4, not divisible by 100, and
    #ARE divisible by 400...(According to the Gregorian Calendar)
    
    if year % 400 == 0:
    	return True
    if year % 100 == 0:
    	return False
    if year % 4 == 0:
    	return True
    else:
    	return False

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
	
	born = calculate_days(y1, m1, d1)
	today = calculate_days(y2, m2, d2)

	return today - born


def calculate_days(y, m, d):
	days = 0
	for year in range(y + 1):
		if isLeapYear(year):
			days += 366
		else:
			days += 365
	if isLeapYear(y):
		daysOfMonths[1] = 29
	for month in daysOfMonths[:m - 1]:
		days += month
	days += d

	return days

print daysBetweenDates(2000, 6, 29, 2000, 6, 31)
print isLeapYear(2000)