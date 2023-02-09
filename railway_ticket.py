s#project for train reservation system (batchF2)
import random

print(" WELOCOME TO RALIWAY TICKET RESERVATION ")
print('\n-----')
print("please select the suitable option")

option1=("ticket booking")
print("\n1:ticket booking")

option2=("cancelation of the ticket")
print("2.details of ticket cancelation")

option3=("exit")
print("3:exit")

print("\nenter your option:")
operator1 =input("")

#ticket booking -----ticket booking process
if operator1=="1":

    print("\nplease fill the below details")
    
    #details--personal information
    name=input("\nenter your name : ")
    print('')
    age=int(input("enter your age(0-125) : "))
    print('')
    if age>125:
        print("enter the valid age",'\n')
        age=int(input('enter the correct age here:- '))
        print('')
    else:
        None

    aadhar=(input("enter your aadhar number(12 digits):- "))
    print('')
    if len(aadhar)!=12:
        print('enter the aadhar number properly(aadhar must have 12 digit)','\n')
        aadhar=(input("enter your aadhar number(12 digit):- ",))
        print('')
    else:
        None
    print("please enter the details of covid: ")
        
    #status of covid test---covid report details 
    print("\n'Y' if done test before 48hrs of boarding")
    print("'N' if not done test before 48hrs of boarding")
    
    print("\nenter 'Y' or 'N'")
    operator2=input(" ")
           
    if operator2==('y'):#----details if the covid test id done
        print("\n[please continue to fill the below details]",'\n')
        print("Let us begin with your travel details",'\n')
        print("please select the train you wish to travel :",'\n')
        print('')

        
        #lists
        op_no=[1,2,3,4]
        train_no=[16541,17589,23485,95642]
        train_board=['banglore','banglore','banglore','banglore']
        train_dest=['mysore','hubbali','shivamogga','mandya']
        train_cost=[100,200,300,400]
        train_time=['7:15 AM','9:45 AM','1:30 PM','3:45 PM']


        for i in range(0,4):#-------trains
            #train details and their timings 
            print('train',i+1,':',train_no[i],': from',train_board[i],'to',train_dest[i],'- timings : ',train_time[i])

        operator3=input("\n")
        i=int(operator3)-1
        
        #for i in range(0,4):#-------trains
            #train details and their timings 
        print('train',i+1,'from',train_board[i],'to',train_dest[i],'- timings : ',train_time[i])
        print('cost per ticket for',train_board[i],'to',train_dest[i],'is - Rs',train_cost[i])
        pn=int(input("enter the number of seats you want to book : "))
        print("\nyour total amount is :" ,(pn*train_cost[i]),'\n--------\n')
        pnl_name=[]
        pnl_age=[]
        pnl_gen=[]
        i=1
        for i in range(1,pn+1):
                 print('details of the passenger',i)
                 # list for the passengers name
                 p_name=input('enter the name of the passenger:- ')
                 pnl_name.append(p_name)
                 # list for the passengers age
                 p_age=input('enter the age of the passenger:- ')
                 if age>=125:
                    print("enter the valid age",'\n')
                    p_age=int(input('enter the correct age here:- '))
                    print('')
                 else:
                    None
                 pnl_age.append(p_age)
                 # list for the GENDER of the passengers
                 p_gen=input('enter the gender of passenger:- ')
                 pnl_gen.append(p_gen)
                 print('do u need preference for window side?','\n',"If yes type 'Y' otherwise type 'N'")
                 pre=input(' ')
                 i+=1
                 print('\n----------\n')
                 

        #modes of payment
            
        mode1=("online through debit card ")
        mode2=("onine to net banking")
        mode3=("payment in the nearest railway station through cash")   

        print("\nmode1 = online through credit card ")
        print("mode2 = online through net banking ")
        print("mode3 = payment in the nearest railway through cash")
        operator=("mode1","mode2","mode3")
        operator4=input("\n")

        #mode1 debit card

        if operator4=="1":#-------info of the debit card 
            print("\nplease fill the details of the debit card payment")
            number=int(input("enter your debit card number(16 digits) : "))
            n=str(number)
            if len(n)!=16:
                print('enter the debit  card number properly(16 digits)')
                number=int(input("enter your debit card number : "))
            else:
                None
            print("\ndetails of your debit card expry month and year")
            month=int(input("enter your debit card expiry month : "))
            if month>12 or month<1:
                print("please enter a valid month")
                month=int(input("enter your debit card expiry month : "))
            else:
                None
            year=int(input("enter your debit card expiry year : "))
            if (year>2100 or year<2021):
                print('enter the debit  card number properly(from 2021 to 2100)')
                year=int(input("enter your debit card expiry year : "))
            else:
                None

        elif operator4=="2":#--------info of the net banking
            print("/n please enter the details of the net banking - ")
            bankno=int(input("enter your acc no:- "))
            print("please enter the bank you want to do your transaction :-")
            bank=input("enter the bank :-")
            ifsc=input('Enter the ifsc code of your bank:- ')

        elif operator4=="3":#------info of the cash paid in the nearest railway station
            print('''Your ticket will be confirmed after payment is done in the railway station.
So please reach early to the station. ALL modes of payments are accepted in the station''')

        if operator4!='3': 
                print("\n Here is the summary of the ticket you booked -- ")
                print('\n-----------------------------------------------------------\n')
                tick_num=random.randint(500000,999999)
                print("the ticket number is :",tick_num,)
                print("the train you selected is : ",train_no[int(operator3)-1])
                print('Your journey is from',train_board[int(operator3)-1],'to',train_dest[int(operator3)-1])
                print("the number  of tickets that you have booked :",pn,)
                print("aadhar of the account holder: ",aadhar,'\n------------\n')
                for i in range(1,pn+1):
                    print('Details of passenger',i)
                    print("Name : ",pnl_name[i-1])
                    print("Age : ",pnl_age[i-1])
                    print('gender : ',pnl_gen[i-1])
                    seat_num=random.randint(1,121)
                    coach_num=random.randint(1,16)
                    print('coach number: ',coach_num)
                    print('seat number: ',seat_num)
                    
                    print('\n-----------------------------------------------------------\n')
                print('Wish you a happy and safe journey')
                
# covid test not done
    else:#--------if covid test not done
        print("[you are not supposed to travel,please get your test done before travelling]")
        print('thank you','\n---------')
    

#cancelation of ticket
elif operator1=="2":
    print("view the details of ticket cancelation process")

    print("here are the terms and condition for the cancelation of your ticket")
    print("\n1)there will be no deduction in the money for cancelation of your ticket ")
    print("2)you can also cancel the ticket online ")

    tick=int(input("enter your ticket number:- "))
    
    if (tick<500000 or tick>999999):
        print("please enter the correct ticket number and try again")
        tick=int(input("enter your ticket number "))
    else:
        None

    print('''your ticket has been canceled.
                 Your money will be refunded to your account within 3 working days
                 Thank You''')
    
    
#exit
elif operator1=="3":
    print("thanks you : wear mask : stay safe",'\n-----------')