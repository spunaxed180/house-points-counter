new_points=[]
current_points=[]
while True:
        try:
            new_points.append(float(input("Enter the number of points that Asgard got this week")))
        except ValueError:
            print("I am sorry that is an incorrect value, please try again")
            continue
        print(new_points)
        Verification=str(input("Are you sure that the point/points entered are correct? yes/no"))
        if(Verification=="yes"):
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
        Verification=str(input("Are you sure that the point/points entered are correct? yes/no"))
        if(Verification=="yes"):
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
        Verification=str(input("Are you sure that the point/points entered are correct? yes/no"))
        if(Verification=="yes"):
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
        Verification=str(input("Are you sure that the point/points entered are correct? yes/no"))
        if(Verification=="yes"):
            break
        else:
            del new_points[3]
            continue        
#The below print statements are not correct, they need to be added with the current points array to get the points of the team
#These print statements only print the new points
print("The total points of Asgard is",new_points[0],"points")
print("\n")
print("The total points of Valhalla is",new_points[1],"points")
print("\n")
print("The total points of Wakanda is",new_points[2],"points")
print("\n")
print("The total points of Xandar is",new_points[3],"points")
print("\n")
