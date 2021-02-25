try:
    #user_int = int(input("Please enter an integer. "))
    a = 1/0   # 0 devision error
    import I_dont_exist   #import error
except ValueError:
    print("You did not enter a value that can be cast as an integer.")
except ZeroDivisionError:
    print("Please don't divide by zero")
except Exception:
    print("General exception")
finally:
    pass

n = 2
if n < 5:
    raise Exception

print("End of program.")
