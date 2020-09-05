import math
import sys
args = sys.argv
  

def number_of_periods():
    credit_principal = int(args[2][args[2].find("=") + 1:])
    monthly_payment = int(args[3][args[3].find("=") + 1:])
    interest_rate = float(args[4][args[4].find("=") + 1:])
    if credit_principal < 0 or monthly_payment < 0 or interest_rate < 0:
        print("Incorrect parameters")
    else:         
        nominal_interest_rate = interest_rate / 1200
        number_of_periods = math.ceil(math.log((monthly_payment / (monthly_payment - nominal_interest_rate * credit_principal)), 1 + nominal_interest_rate))
        if number_of_periods > 11:
            year = number_of_periods // 12
            month = number_of_periods % 12
            if month > 1:
                if year > 1:
                    print(f"It will take {year} years and {month} months to repay this credit!")
                else:
                    print(f"It will take 1 year and {month} months to repay this credit!")            
            elif month == 1:
                if year > 1:
                    print(f"It will take {year} years and 1 month to repay this credit!")
                else:
                    print(f"It will take 1 year and 1 month to repay this credit!")
            elif month == 0:
                if year > 1:
                    print(f"It will take {year} years to repay this credit!")
                else:
                    print(f"It will take 1 year to repay this credit!")
        else:
            print(f"It will take {number_of_periods} months to repay this credit!")
        overpayment = number_of_periods * monthly_payment - credit_principal
        print(f'Overpayment = {overpayment}')

def monthly_payment():
    credit_principal = int(args[2][args[2].find("=") + 1:])
    number_of_periods = int(args[3][args[3].find("=") + 1:])
    interest_rate = float(args[4][args[4].find("=") + 1:])
    if credit_principal < 0 or number_of_periods < 0 or interest_rate < 0:
        print("Incorrect parameters")
    else:    
        nominal_interest_rate = interest_rate / 1200
        annuity_payment = credit_principal * nominal_interest_rate * pow((1 + nominal_interest_rate), number_of_periods) / (pow((1 + nominal_interest_rate), number_of_periods) - 1)
        print(f"Your monthly payment = {math.ceil(annuity_payment)}!")
        
def credit_principal():
    monthly_payment = float(args[2][args[2].find("=") + 1:])
    number_of_periods = int(args[3][args[3].find("=") + 1:])
    interest_rate = float(args[4][args[4].find("=") + 1:])
    if monthly_payment < 0 or number_of_periods < 0 or interest_rate < 0:
        print("Incorrect parameters")
    else:    
        nominal_interest_rate = interest_rate / 1200
        credit_principal = monthly_payment / (nominal_interest_rate * pow(1 + nominal_interest_rate, number_of_periods) / (pow(1 + nominal_interest_rate, number_of_periods) - 1))
        print(f"Your credit principal = {round(credit_principal)}!")
    
def differentiated_payment():
    credit_principal = int(args[2][args[2].find("=") + 1:])
    number_of_periods = int(args[3][args[3].find("=") + 1:])
    interest_rate = float(args[4][args[4].find("=") + 1:])
    if credit_principal < 0 or number_of_periods < 0 or interest_rate < 0:
        print("Incorrect parameters")
    else:
        nominal_interest_rate = interest_rate / 1200
        overpayment = - credit_principal
        for month in range(1, number_of_periods + 1):
            differentiated_payment =  math.ceil(credit_principal / number_of_periods + (nominal_interest_rate * (credit_principal - (credit_principal * (month - 1)) / number_of_periods)))   
            print(f'Month {month}: payment is {differentiated_payment}')
            overpayment +=  differentiated_payment   
        print(f'Overpayment = {overpayment}')

if len(args) < 5:
    print("Incorrect parameters")
elif args[1].find("type") == -1:
    print("Incorrect parameters")
elif args[1][args[1].find("=") + 1:] == "diff":
    if "payment" in str(args):
        print("Incorrect parameters")
    else:
        differentiated_payment()
elif args[1][args[1].find("=") + 1:] == "annuity":
    if "periods" not in str(args):
        number_of_periods()
    elif "payment" not in str(args):
        monthly_payment()
    elif "principal" not in str(args):
        credit_principal()   
    
