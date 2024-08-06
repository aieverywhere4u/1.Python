class multiplefunction:
    def subfields():
        print("sub fields in AI are: ")
        print("machine learning")
        print("neural networks")
        print("vision")
        print("robotics")
        print("speech processing")
    
    def oddeven():
        a=int(input("enter the number"))
        if(a%2==0):
            print("the number is even")
            message=("the number is even")
        else:
            print("the number is odd")
            message=("the number is odd")
        return message
    
    def eligible():
        gender=input("enter the gender:")
        age=int(input("enter the age:"))
        if(gender=="male" and age>20):
            print("you are eligible for marriage")
            message="you are eligible for marriage"
        elif(gender=="female" and age>17):
            print("you are eligible for marriage")
            message="you are eligible for marriage"
        else:
            print("you are ineligible for marriage")
            message="you are ineligible for marriage"
        return message
    
    def percentage():
        a=int(input("sub 1:"))
        b=int(input("sub 2:"))
        c=int(input("sub 3:"))
        d=int(input("sub 4:"))
        e=int(input("sub 5:"))
        add=a+b+c+d+e
        percent=(100*add)/500
        print("total",add)
        message=add
        print("percent",percent,end="%")
        message01=percent
        return message,message01
    
    def triangle():
        h=int(input("Height="))
        b=int(input("Breadth="))
        h1=int(input("Height 01="))
        h2=int(input("Height 02="))
        b1=int(input("Breadth 01="))
        area=(h*b)/2
        message=area
        peri=h1+h2+b1
        message01=peri
        print("Area of the triangle: ",area)
        print("Perimeter of the triangle: ",peri)
        return message, message01