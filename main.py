print("***Grade Generator***")
test = input("Type in the name of a test: ")
maxScore = int(input("Type in the maximum score you could receive: "))
receivedPoints = int(input("How many points you received? "))
userPercentage = round(receivedPoints * 100 / maxScore, 2)
if userPercentage >= 90 and userPercentage <= 100:
    print("Your grade is \033[95mA+\033[0m \U0001F60E with ", userPercentage,
          "%.")
elif userPercentage >= 80 and userPercentage < 90:
    print("Your grade is \033[94mA-\033[0m \U0001F601 with ", userPercentage,
          "%.")
elif userPercentage >= 70 and userPercentage < 80:
    print("Your grade is \033[96mB\033[0m \U0001F609 with ", userPercentage,
          "%.")
elif userPercentage >= 60 and userPercentage < 70:
    print("Your grade is \033[92mC\033[0m \U0001F615 with ", userPercentage,
          "%.")
elif userPercentage >= 50 and userPercentage < 60:
    print("Your grade is \033[93mD\033[0m \U0001F62C with ", userPercentage,
          "%.")
elif userPercentage >= 0 and userPercentage < 50:
    print("Your grade is \033[91mU\033[0m \U00002639 with ", userPercentage,
          "%.")
else:
    print("Something wrong, try again! \U0001f914")
