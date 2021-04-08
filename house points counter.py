import os
import datetime
from collections import defaultdict
import smtplib
from email.mime.text import MIMEText
from collections import deque
from email.mime.multipart import MIMEMultipart
import sys
import time

houses = ["Asgard", "Valhalla", "Wakanda", "Xandar"]
inputtedpoints = []

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
                    inputtedpoints.append(points)
                    break
        else:
            inputtedpoints.append(points)

    for i in range(len(houses)):
        file = open("house points data.txt", "a")
        file.write(f"{houses[i]}:")
        file.write(f"\n{inputtedpoints[i]}")
        file.write("\n")
        file.close()
else:
    reset = str(input(" press r to reset points, press enter to continue "))
    if reset == "r" or reset == "R":
        while True:
            confirm = str(input("type reset to reset points"))
            if confirm == "reset":
                os.remove("house points data.txt")
                print("re-run the program to input new points")
                time.sleep(5)
                sys.exit()
                break
            else:
                print("points reset cancelled, rerun the program to reset")
                break
    else:
        pass

now = datetime.datetime.now()
Date = now.strftime("%Y-%m-%d %H:%M:%S")
overall = []
pointindex = []
new_points = []
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
for i, x in enumerate(sorted(overall, reverse=True), start=1):
    d[x].append(i)

result = [d[x].popleft() for x in overall]

rank = (
    f"\n The rank of Asgard: {result[0]} \n The rank of Valhalla: {result[1]} \n The rank of Wakanda: {result[2]} \n The rank of Xandar: {result[3]}")

print(rank)

file = open("house points data.txt", "w")

for i in range(4):
    file.write(f"{houses[i]}:")
    file.write(f"\n{overall[i]}")
    file.write("\n")

file.write("\n")
file.write(f"last updated on {Date}")
file.close()

# reading data
file = open("house points data.txt", "r")
data = file.read()
file.close()

# email part of the file
contacts = ["secondary.1.students@sis-semarang.org", "secondary.2.students@sis-semarang.org","secondary.3.students@sis-semarang.org", "secondary.4.students@sis-semarang.org", "jc1.students@sis-semarang.org", "jc2.students@sis-semarang.org", "secondary.teacher@sis-semarang.org"]


sender = "ka@###8828.nz"
mailserver = smtplib.SMTP('smtp.gmail.com', 587)
mailserver.starttls()
mailserver.login(sender, "ask owner")

msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = ",".join(contacts)
msg["Subject"] = "House Points info"

msg.attach(MIMEText(data, 'plain'))
msg.attach(MIMEText(rank, 'plain'))

qna = str(input(" any message/announcement to share? yes/no"))
if qna == "yes":
    note = str(input(" enter your message (short message only): "))
    note = f"\n\n{note}"
    msg.attach(MIMEText(note, 'plain'))
else:
    pass

mailserver.sendmail(sender, contacts, msg.as_string())
print(" \n data sent!")
