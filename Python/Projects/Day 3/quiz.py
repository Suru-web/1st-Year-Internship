print("Are u ready for a quiz?")
print("Okay, here it comes!\n\n")
i=0

print("Q1) What is the capital of alaska?")
print("\t 1) Melbourne\n"
      "\t 2) Anchorage\n"
      "\t 3) Juneau\n")
option=int(input())
co=3
if(option==co):
    print("That's right!")
    i=1
else:
    print("Wrong answer, Try again!")


print("Q2) Can you store the value ""cat"" in a variable of type int?")
print("\t 1) yes\n"
      "\t 2) no\n")
op1=int(input())
co1=2
if(op1==co1):
    print("That's right!")
    i=i+1
else:
    print("Sorry, ""cat"" is a string. int can only store numbers.")


print("Q3) What is the result of 9+6/3?\n\n")
print("\t 1) 5\n"
      "\t 2) 11\n"
      "\t 3)15/3\n")
co2=2
op2=int(input())
if(op2==co2):
    print("That's right!\n")
    i=i+1
else:
    print("Wrong answer, Try again!\n\n")


print("Overall, you got",i,"out of 3 correct.")
print("Thanks for playing")

