def isYearLeap(year):
    if (year % 4 != 0):
        return False
    elif (year % 100 != 0):
        return True
    elif (year % 400 != 0):
        return False
    else:
        return True

def daysInMonth(year, month):
    leapYear = isYearLeap(year)
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (leapYear and (month == 2)):
        return 29
    for i in range (len(days)):
        if month == (i+1):
            return days[i]
    

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")