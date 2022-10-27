a, b, m = 10, 10, 2
n = [1, 2, 3, 4, 5]
try:
    div = a / b
    print("Division is ", div)
    print("list content : ", n[2])
    m = m + "python"                 #type error
    print("M is ", m)

except ZeroDivisionError as e:
    print("Error is 0-div", e)
except TypeError as e:
    print("Type error ", e)
except Exception as e:
    print(e)
