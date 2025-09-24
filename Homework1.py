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
            current_savings += current_savings*r''' # same here 
        current_savings += current_savings*r_montly
        current_savings += portion_saved*(annual_salary/12)
    print(f"Number of months : {nb_months}")


# Part II Salary raise
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



if __name__ == "__main__":
    months4house()