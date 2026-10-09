milliseconds = 10000123

seconds =milliseconds // 10000
milli_seconds_left = milliseconds

hours = seconds // 3600
seconds_left = seconds % 3600

minutes = seconds_left // 60
seconds_left = seconds_left % 60



print()
print("Hours: \t\t" = str(seconds_left))