def sum(x,y):
    return (x+y)
def minus(x,y):
    return (x-y)
def divide(x,y):
    return ((x/y))
   
    

def double(x,y):
    return (x*y)


    
cont=False   
while cont==False:

    print("Welcome to The BasicCalculator\n")

    try:
        x=int(input("please enter your first number\n"))

        y=int(input("please enter your second number\n"))


        operation=int(input("Please select your operation with using numbers that you have seen.     1.sum   2.minus   3.divide   4.double  ==>> \n"))
        if operation==1:
           
            print("your solution is : " +  str(sum(x,y)) )
            
        elif operation==2:
            print("your solution is : " +  str(minus(x,y)))
        
        elif operation==3:
            print("your solution is : " +  str(divide(x,y))) 
        elif operation==4:
            print("your solution is : " +  str(double(x,y)))    
        
        else:
            print("invalid input.")
    except ValueError:
        print("please only enter numbers.\n")
    except ZeroDivisionError:
        print("you cannot divide by zero\n") 
    finally:
        verification=False
        while verification==False:
            question = input("Do you want to continue? => y/n:\n") 
            if question.lower()=="n" or question.upper()=="N":
                cont=True
                verification= not False
            elif question.lower()=="y" or question.upper()=="Y":
                cont=False
                verification= not False
            else:
                print("please select only 'y' or 'n' ")
                verification=False
    