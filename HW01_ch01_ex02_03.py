# HW01_ch01_ex04
# Start the Python interpreter and use it as a calculator.
# Python's syntax for math operations is almost the same as
# standard mathematical notation. For example, the symbols
# +, - and / denote addition, subtraction and division, as you would expect.
# The symbol for multiplication is *.

# If you run a 10 kilometer race in 42 minutes 42 seconds, what is your
# average pace (time per mile in minutes and seconds)? What is your average
# speed in miles per hour?

# Insert Answers
# Average Pace (minutes & seconds per mile): 6:52.482
# Average Speed in MPH: 8.727653570337614

# Insert calculations below (paste from the interpreter):

# >>> miles = 10/1.61 # 6.211180124223602
# >>> secs_ran = (42*60)+42 # 2562
# >>> avg_pace = (secs_ran/miles)/60 # 6.874700000000001
# >>> avg_pace_secs_r = 60*.8747 # 52.482
# >>> avg_pace_minutes = (secs_ran/miles)//60 # 6; math.floor()
# >>> avg_pace_secs_r2 = (secs_ran/miles)%60 # 52.48200000000003

# >>> secs_in_hour = 60*60
# >>> speed = (miles*secs_in_hour)/secs_ran # 8.727653570337614
