try:
    num = int(input("Enter a positive number\t\t"))
    if num <= 0:
        raise Exception("This is not a positive number")        #raise can be used to raise an exceptoin manually
    else:
        print("Positive number entered")

except Exception as e:
    print("Exception :", e)

print("End")
