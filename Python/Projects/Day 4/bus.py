print("Welcome to Yeshwantpur Station\n\n")
print("Enter the source\n")
print("\t 1) Rajajinagar\t 2) Hebbal\t 3) Vijay Nagar\t 4) Yeshwantpur\n")
source=int(input("\n"))
print("Choose your destination\n")
print("\t 1)Nagenhalli\t 2)Avalahalli\t 3)Rajankunte\t 4)CRPF camp\n")
destination=int(input("\n"))

def sou(source):
    if(source==1):
        return 'Rajajinagar'
    elif(source==2):
        return 'Hebbal'
    elif(source==3):
        return 'Vijay Nagar'
    elif(source==4):
        return 'Yeshwantpur'
    else:
        return 'Invalid source choosen'

def des(destination):
    if(destination==1):
        return 'Nagenhalli'
    elif(destination==2):
        return 'Avalahalli'
    elif (destination == 3):
        return 'Rajankunte'
    elif (destination == 4):
        return 'CRPF CAMP'
    else:
        return "Inavalid destination choosen"

if(source==1 and destination==1):
    distance = 20.6
    fair = distance * 4
elif(source==1 and destination==2):
    distance=8.1
    fair=distance*4
elif(source==1 and destination==3):
    distance=31.3
    fair = distance * 4
elif(source==1 and destination==4):
    distance=14.1
    fair = distance * 4

if (source==2 and destination == 1):
    distance = 15.7
    fair = distance * 4
elif (source==2 and destination == 2):
    distance = 15
    fair = distance * 4
elif (source==2 and destination == 3):
    distance = 22.4
    fair = distance * 4
elif (source==2 and destination == 4):
    distance = 10.1
    fair = distance * 4


if (source==3 and destination == 1):
    distance = 25
    fair = distance * 4
elif (source==3 and destination == 2):
    distance = 26
    fair = distance * 4
elif (source==3 and destination == 3):
    distance = 32
    fair = distance * 4
elif (source==3 and destination == 4):
    distance = 24
    fair = distance * 4

if (source==4 and destination == 1):
    distance = 19
    fair = distance * 4
elif (source==4 and destination == 2):
    distance = 15
    fair = distance * 4
elif (source==4 and destination == 3):
    distance = 30
    fair = distance * 4
elif (source==4 and destination == 4):
    distance = 18
    fair = distance * 4


a=sou(source)
b=des(destination)
print("Source :\t",a)
print("Destination :\t",b)
print("Fair :\t",fair)
print("Distance :\t",distance)


