def calculate_salary ( hourly_rate, hours_worked, tax_rate=0.15):
                    gross_salary = (hours_worked * hourly_rate)
                    tax = (gross_salary * 0.15)
                    print("total tax deducted is ")
                    print (tax)
                    net_salary= (gross_salary - tax)
                    print (f"Net salary is")
                    print (net_salary)
#calculates the gross salary, net salary and tax based on user input

                    
input(calculate_salary(500,40))
#accepts user input of hourly rate and hours worked

