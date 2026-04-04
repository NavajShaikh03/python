#Esersies

import time     #   this is modules of times 
timestamp = time.strftime('%H:%M:%S')    # print the your time 
print(timestamp)

hour = int( time.strftime('%H'))
print(hour)
if (hour >= 0 and hour < 12):
    print("Good morning")
elif(hour > 12 and hour < 17):
    print("Good Afternoon Sir")
elif(hour >=17 and hour > 0):
    print("Good Night Sir! ")