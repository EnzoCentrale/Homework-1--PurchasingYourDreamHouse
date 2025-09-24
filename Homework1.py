'''owner = "Ducros Enzo"
date = "2024-09-15"'''

# Part I : Calculating time to save 

def months4house():
    '''function printing the number of months required to save up for a home depending on user_inputs '''
    # User input Variables
    annual_salary = float(input("Enter your annual salary in Lyon: ")) 
    portion_saved = float(input("Enter the portion of salary to be saved , as a decimal : "))
    total_cost = float(input("Enter the cost of your dream home in Lyon : "))
    # Given Variables
    portion_down_payment = 0.25
    current_savings = 0.0
    r = 0.04  # investment returns
    r_montly = ((1+r)**(1/12))-1 # i tried this because the results didn't math 
    # output variables
    nb_months = 0
    # Start of Program 
    while current_savings < total_cost*portion_down_payment:
        nb_months += 1 
        '''if nb_months % 12 == 0:
            current_savings += current_savings*r''' 
        current_savings += current_savings*r_montly  # This line makes sure the investment is per month and not per year for more precision
        current_savings += portion_saved*(annual_salary/12)
    print(f"Number of months : {nb_months}")


# Part II : Salary raise
def months4house_SemiAnRaise(): # ill remove the previous comments and only add things that i change for tidyness
    '''months4house but including semiAnnualSalaryRaise '''
    annual_salary = float(input("Enter your annual salary in Lyon: ")) 
    portion_saved = float(input("Enter the portion of salary to be saved , as a decimal : "))
    total_cost = float(input("Enter the cost of your dream home in Lyon : "))
    semi_annual_raise = float(input("Enter the semi-annual raise , as a decimal : "))
    portion_down_payment = 0.25
    current_savings = 0.0
    r = 0.04  
    r_montly = ((1+r)**(1/12))-1 
    nb_months = 0
    while current_savings < total_cost*portion_down_payment:
        if nb_months % 6 == 0:
            annual_salary += annual_salary*semi_annual_raise # changes the salary every 6 months 
        nb_months += 1 
        current_savings += current_savings*r_montly
        current_savings += portion_saved*(annual_salary/12)
    print(f"Number of months : {nb_months}")



# Part III : Finding the right savings rate 

def months4house2(portion_saved,annual_salary,r,semi_annual_raise,portion_down_payment = 0.25, total_cost = 1000000): # i'm modyfing this function to use it 
    current_savings = 0.0
    r_montly = ((1+r)**(1/12))-1 
    nb_months = 0
    while current_savings < total_cost*portion_down_payment:
        if nb_months % 6 == 0:
            annual_salary += annual_salary*semi_annual_raise # changes the salary every 6 months 
        nb_months += 1 
        current_savings += current_savings*r_montly
        current_savings += portion_saved*(annual_salary/12)
    return nb_months

def Sav_36month(portion_saved,annual_salary,r,semi_annual_raise): # little function to know how much is saved in 36 months 
    current_savings = 0.0
    r_montly = ((1+r)**(1/12))-1 
    nb_months = 36
    for _ in range(36):
        if nb_months % 6 == 0:
            annual_salary += annual_salary*semi_annual_raise # changes the salary every 6 months 
        current_savings += current_savings*r_montly
        current_savings += portion_saved*(annual_salary/12)
    return current_savings

def bijection_saving(bounds : tuple,annual_salary,r,semi_annual_raise,portion_down_payment, total_cost,steps : int):
    Bleft , Bright = bounds
    portion_saved = (Bleft+Bright)/2
    if abs(Sav_36month(portion_saved,annual_salary,r,semi_annual_raise) - total_cost) < 100:
        return (portion_saved ,steps + 1)
    if Sav_36month(portion_saved,annual_salary,r,semi_annual_raise) > total_cost:
        bijection_saving(((Bleft,portion_saved),annual_salary,r,semi_annual_raise,portion_down_payment,total_cost,steps+1))
    else:
        bijection_saving(((portion_saved,Bright),annual_salary,r,semi_annual_raise,portion_down_payment,total_cost,steps+1))

#This overcomplicated recursive function is a way to keep cutting the range in which we seach the portion saved into2

    

def finding_Savings_rate(): 
    # User input Variables
    Salary = float(input("Enter the starting salary in Lyon : "))
    # given variables
    semi_annual_raise = 0.07
    r = 0.04
    r_montly = ((1+r)**(1/12))-1  #for the extra montly precision
    portion_down_payment = 0.25
    if months4house2(1,Salary,r,semi_annual_raise,portion_down_payment) > 36:
        print("your Salary is too low to save for an 1000000 euro house within 36 months")
    (portion_saved , steps) = bijection_saving((0,1),Salary,r,semi_annual_raise,portion_down_payment,1000000,0)







# MAIN FUNCTIONS 

if __name__ == "__main__":
    finding_Savings_rate()