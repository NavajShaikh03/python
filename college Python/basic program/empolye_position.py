name = input("Enter empolyee name:")
exp = int(input("Enter your experience in year :"))

if(exp >= 0 and exp<=1):
    {
        print(f"{name} you are fresher")
    }
elif(exp > 1 and exp <= 2):
    {
        print("{name} you are senior")
    }
elif(exp > 2 and exp <= 3):
    {
        print("{name} you are cheaf lead")
    }
else:
    {
        print("pleas enter valid experience between (1-3)")
    }    
