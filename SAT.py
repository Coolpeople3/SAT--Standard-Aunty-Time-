# This is a code for predicting aunty time, also works for uncles

# Define and ask for input in the variables at play
EventImportance = int(input("What is the importance or urgency of the event? (enter # between 1-5) "))
TraditionalClothing = input("Are you wearing traditional clothing? (yes/no) ").strip().lower()
UserEstimatedTime = float(input("What is the estimated time? (enter in numbers, 24-hour format, use decimals instead of minutes)  "))
PrepTime = float(input("Will it take extra time to prepare? If so, how much (in Hrs)? If not, put 0  "))
LocationDistance = float(input("Are we going far away to meet? If so, how far (in Hrs.) If not, put 0  "))

# Deal with EventImportance
if EventImportance == 1:
    UserEstimatedTime += 1.25
elif EventImportance == 2:
    UserEstimatedTime += 0.75
elif EventImportance == 3:
    UserEstimatedTime += 0.25
elif EventImportance == 4:
    UserEstimatedTime += 0
elif EventImportance == 5:
    UserEstimatedTime -= 0.15

# Deal with TraditionalClothing
if TraditionalClothing == 'yes':
    UserEstimatedTime += 1.5

# Deal with PrepTime and LocationDistance
UserEstimatedTime += PrepTime + LocationDistance

# Convert to hours and minutes
Hours = int(UserEstimatedTime)
Minutes = round((UserEstimatedTime - Hours) * 60)

if Minutes >= 60:
    Hours += 1
    Minutes -= 60

print("Your time estimate is at:", Hours, ':', Minutes)
