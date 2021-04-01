# house-points-counter- A program to ease the calculations of the house points
 
import os
import datetime
from collections import defaultdict
import smtplib
from email.mime.text import MIMEText
from collections import deque

houses = ["Asgard", "Valhalla", "Wakanda", "Xandar"]

file = open("house points data.txt", "a")
file.write("")
file.close()
size = os.stat('house points data.txt').st_size
if size == 0:
    print("this is your first time running the program")
    for i in range(len(houses)):
        points = float(input(f"please enter the current points of {houses[i]}: "))
        confirmation = input("are you sure you inputted the correct points? yes/no ")
        if confirmation != "yes":
            while True:
                points = float(input(f"please enter the current points of {houses[i]}: "))
                confirmation = input("are you sure you inputted the correct points? yes/no ")
                if confirmation == "yes":
                    break
        file = open("house points data.txt", "a")
        file.write(f"{houses[i]}:")
        file.write(f"\n{points}")
        file.write("\n")
        file.close()

now = datetime.datetime.now()
Date = now.strftime("%Y-%m-%d %H:%M:%S")
overall = []
pointindex = []
new_points = []  #
current_points = []

print(" ")
while True:
    try:
        new_points.append(float(input("Enter the number of points that Asgard got this week")))
    except ValueError:
        print("I am sorry that is an incorrect value, please try again")
        continue
    print(new_points)
    Verification = str(input("Are you sure that the point/points entered are correct? yes/no"))
    if (Verification == "yes"):
        break
    else:
        del new_points[0]
        continue
    print(new_points)
while True:
    try:
        new_points.append(float(input("Enter the number of points that Valhalla got this week")))
    except ValueError:
        print("I am sorry that is an incorrect value, please try again")
        continue
    Verification = str(input("Are you sure that the point/points entered are correct? yes/no"))
    if (Verification == "yes"):
        break
    else:
        del new_points[1]
        continue
while True:
    try:
        new_points.append(float(input("Enter the number of points that Wakanda got this week")))
    except ValueError:
        print("I am sorry that is an incorrect value, please try again")
        continue
    Verification = str(input("Are you sure that the point/points entered are correct? yes/no"))
    if (Verification == "yes"):
        break
    else:
        del new_points[2]
        continue
while True:
    try:
        new_points.append(float(input("Enter the number of points that Xandar got this week")))
    except ValueError:
        print("I am sorry that is an incorrect value, please try again")
        continue
    Verification = str(input("Are you sure that the point/points entered are correct? yes/no"))
    if (Verification == "yes"):
        break
    else:
        del new_points[3]
        continue

file = open("house points data.txt", "r")
for line in file:
    m = line.strip()
    current_points.append(m)

for i in range(len(houses)):
    xindex = current_points.index(f"{houses[i]}:") + 1
    pointindex.append(xindex)

for x in range(4):
    npoint = float(current_points[int(pointindex[x])]) + float(new_points[x])
    overall.append(npoint)
    print(" ")
    print(f"this week {houses[x]} total points is {npoint}")

d = defaultdict(deque)
for i, x in enumerate(sorted(current_points, reverse=True)):
    d[x].append(i)

result = [d[x].popleft() for x in current_points]

print(f"The rank of Asgard: {result[0]}")
print(f"The rank of Valhalla: {result[1]}")
print(f"The rank of Wakanda: {result[2]}")
print(f"The rank of Xandar: {result[3]}")

file = open("house points data.txt", "w")

for i in range(4):
    file.write(f"{houses[i]}:")
    file.write(f"\n{overall[i]}")
    file.write("\n")

file.write("\n\n\n")
file.write(f"last updated on {Date}")
file.close()

# email part of the file
# contacts = ["secondary.1.students@sis-semarang.org", "secondary.2.students@sis-semarang.org","secondary.3.students@sis-semarang.org", "secondary.4.students@sis-semarang.org", "jc1.students@sis-semarang.org", "jc2.students@sis-semarang.org"]
mailserver = smtplib.SMTP('smtp.gmail.com', 587)
mailserver.starttls()
mailserver.login("kartik.nayak@sis-semarang.org", "karnayak")
x = input("Hello everyone, here is the new update on our House Games points.")
for i in range(len(contacts)):
    mailserver.sendmail("kartik.nayak@sis-semarang.org", x)
mailserver.sendmail("kartik.nayak@sis-semarang.org", "tan.michael@sis-semarang.org", x)
