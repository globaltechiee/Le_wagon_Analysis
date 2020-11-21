#shop is opened from 9am - 12pm, 1pm to 6pm
# time hour
# if hour is between 9 and 11 or bteween 1 and 5
# 	=> display shop is open

hour = 10

if hour >= 9 and hour <= 11 or hour >= 13 and hour < 17:
	print("Shop is open")
else:
	print("Shop is closed")