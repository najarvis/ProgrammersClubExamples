import math

option=-1
while option!=0:
    print "*******menu*******"
    print "00. more options"
    print "0. quit"
    print "1. addition"
    print "2. subtraction"
    print "3. multiplication"
    print "4. division"
    print "5. exponent"
    print "6. square root"
    print "7. convert to mpg"
    print "8. convert distance and force to joules"
    print "9. how many joules it takes to heat up X grams of Y"
    print "10. km to Miles or vice versa"
    print "*" *20

    option= input ("what do you want to do? ")
    if option==00:
        print "********MENU*********"
    elif option==1:
        a= input ("first number: ")
        b= input ("second number: ")
        print a, "plus", b, "equals", a+b
    elif option==2:
        a= input ("first number: ")
        b= input ("second number: ")
        print a, "subtracted by", b, "equals", a-b
    elif option==3:
        a= input ("first number: ")
        b= input ("second number: ")
        print a, "multiplied by", b, "equals", a*b
    elif option==4:
        a= input ("first number: ")
        b= input ("second number: ")
        print a, "divided by", b, "equals", a/b
    elif option==5:
        a= input ("enter number: ")
        b= input ("enter exponent: ")
        print a, "to the", b, "power equals", a**b
    elif option==6:
        a= input ("enter number: ")
        print "the square root of", a, "is", math.sqrt(a)
    elif option==7:
        a=input ("how many miles? ")
        b=input ("how many gallons where used? ")
        print "your vehicle gets", a/b, "miles per gallon"
    elif option==8:
        a=input ("how much force? ")
        b=input ("how much distance? ")
        print "this would create", a*b, "joules"
    elif option==9:
        a= input ("how much does it weigh in grams? ")
        b= input ("what is the specific temperature? ")
        c= input ("what temperature are you heating the material to? ")
        d= raw_input ("what is the material? ")
        f=input ("how many sig figs? ")
        print "calculating....\n\n"
        e=a*b*c
        print "it takes", e, "joules to heat", a, "grams of ", d, "to a temperature of", c, "degres celcius."
        print "USE", f, "SIG FIGS!"
    elif option==10:
        a= raw_input ("kilometers or Miles? (no caps) \n")
        if a=="kilometers":
            a= input ("how many kilometers? \n")
            b= a*0.62
            print a, "kilometers is", b, "miles"
        elif a=="miles":
            a= input ("how many miles? \n")
            b= a*1.61
            print a, "miles is", b, "kilometers"
    print "\n\n\n"
