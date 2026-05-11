principal_amount= input("Enter the principal amount: ")
rate_of_interest= input("Enter the rate of interest (in percentage): ")
time_period= input("Enter the time period (in years): ")

principal_amount= float(principal_amount)
rate_of_interest= float(rate_of_interest)
time_period= float(time_period)


rate_of_interest=(principal_amount*rate_of_interest*time_period)/100
print(f"The interest is: {rate_of_interest}")