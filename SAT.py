# This is a code for predicting aunty time, also works for uncles

#define and ask for input in the variables at play
EventImportance = int(input("What is the importance or urgency of the event? (enter # between 1-5) "))
TraditionalClothing = (input("Are you wearing traditional clothing?  "))
UserEstimatedTime = int(input("What is the estimated time? (enter in numbers, 24 hour format, use decimals instead of minutes)  "))
PrepTime = int(input("Will it take extra time to prepare? If so, how much (in Hrs)? If not, put 0  "))
LocationDistance = int(input("Are we going far away to meet? If so, how far (in Hrs.) If not, put 0  "))

#deal with EventImportance
if EventImportance == 1:
    UserEstimatedTime += 1.25
elif EventImportance == 2:
    UserEstimatedTime += 0.75
elif EventImportance == 3:
    UserEstimatedTime += 0.25
elif EventImportance == 4:
    UserEstimatedTime +=0
elif EventImportance == 5:
    UserEstimatedTime -= 0.15

#deal with TraditionalClothing
if TraditionalClothing == 'yes':
    UserEstimatedTime +=1.5

#deal with PrepTime
UserEstimatedTime +=PrepTime

#Deal with LocationDistance
UserEstimatedTime += LocationDistance

#trying to deal with time
Hours = int(UserEstimatedTime)
Minutes = round((UserEstimatedTime - Hours) * 100)

if Minutes >= 60:
    Hours +=1
    Minutes -=60

print("Your time estimate is at:", Hours,':',Minutes)
