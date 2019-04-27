#body mass index
def BMI():
    a=int(input("Enter Your Age: "))
    w=float (input("enter weight of person"))
    h=float(input("enter height of person"))

    BMI=float(format((w*703)/(h**2), ".2f"))

    if(BMI>=18.5) and (BMI<=25):
            print("balanced" , BMI)
    elif(BMI<18.5):
        print("underweight" , BMI)
    else:
        print("overweight" , BMI)

print(BMI())  