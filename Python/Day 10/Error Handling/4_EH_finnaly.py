a = 10
b = 0
try:
    div = a / b
    print("Division is : ", div)
except Exception as e:
    print("Exception :", e)

else:
    print("In else block")

finally:
    print("I am in finally block")

print("End")
