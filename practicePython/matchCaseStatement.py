x = int(input("Enter the value of x :"))

match x:    #  this match statement is like the c language
     
    case 0 :
        print("x is zero")
    case 4 :
        print("case is 4 ")
        
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=80:
        print(x,"is not 80")
    case _ :
        print(x)
        