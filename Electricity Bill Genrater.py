#Write a program to calculate the electricity bill
#Create a Electricity bill
#0 to 500 unit = RS 5 per unit
#501 to 700 unit = RS 10 per unit
#701 to 1000 unit = RS 15 per unit
#more then 1000 unit = RS 20 per unit

from datetime import datetime,date,timedelta
#global charge
def electricity_bill(unit):
    
        if unit<=500:
            charge=unit*5
        elif unit<=700:
            charge=unit*10
        elif unit<=1000:
            charge=unit*15
        elif unit>1000:
            charge=unit*20
        
        return charge

        
def create_bill(unit, customer_name, customer_id, address):
        charge=electricity_bill(unit)
        today=datetime.today()
        due_date=today+timedelta(days=7)
        fixed_charges=100
        gst=(charge*0.08)
        final_bill=charge+fixed_charges+gst
        penalty_charges=1000


        print()
        print(f"Customer Name: {customer_name}")
        print(f"Customer Id: {customer_id}")
        print(f"Customer Adress: {address}")
        print("Bill Date: ",today,today.strftime("%A"))
        print(f"Unit is used by customer: {unit}")
        print(f"Charges on Unit: {charge}")
        print(f"Fixed charges on the bill : {fixed_charges}")
        print(f"GST on the bill : {gst}")
        print(f"Final Bill : {final_bill}")
        print("Last date to pay this bill is: ", due_date,due_date.strftime("%A"))
        print(f"Rs. {penalty_charges} applied if {customer_name} pay after", due_date,due_date.strftime("%A"),"\nThe Payable bill after due date :",(final_bill + penalty_charges))
        print()
        

while True:
    customer_name = str(input("Entre the name of Customer: "))
    while True:
        customer_id = input("Entre the Customer Id: ")
        if len(customer_id)==12 and customer_id.isdigit():
            #print(customer_id)
            break
        else:
            print("Please entered a valid Customer Id")
    address=str(input(f"Entered the {customer_name}'s address: "))
    unit=float(input("Entered the Unit: "))
    create_bill(unit,customer_name,customer_id,address)
    

    

   
