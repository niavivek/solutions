# HW01_ch02_ex02
# NOTE: You do not run this script.
# #
# Practice using the Python interpreter as a calculator.
# Paste answer and calculations below

# 1. The volume of a sphere with radius r is 4/3 π r3. W
# What is the volume of a sphere with radius 5? 523.5987755982989
# >>> (4/3)*3.14*(5**3) # 523.3333333333334
# >>> import math
# >>> (4/3)*math.pi*(5**3)

# 2. Suppose the cover price of a book is $24.95, but bookstores get a
# 40% discount. Shipping costs $3 for the first copy and 75 cents for
# each additional copy. What is the total wholesale cost for 60 copies?
# total wholesale cost: 945.45
# >>> ((24.95 * 0.6) * 60) + 3 + (0.75 * 59)

# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace
# (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy
# pace again, what time do I get home for breakfast?
# time: 7:30:06
# >>> secs = 2*(60*8 + 15) + 3*(60*7 + 12) # 2286
# >>> secs/60 # 38.1
