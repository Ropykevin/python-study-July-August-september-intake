            # Nested if 
# series of if statements inside another statement
# nested if statement depend on the result of the previous condition

# if condition1:
    # if condition2:
        # 
    # else:
# else:

1. # write a program that takes users age as input
# if the age is 18 and above ,check if they have  drivers license if they do we print you are eligible to drive
# if they dont have a drivers license print you are not eligible to drive
# otherwise you are too young to drive

# age=input("Enter your age:")
# age=int(age)

# if age>=18:
#     license=input('Do you have a drivers license yes/no?')
#     if license=='yes':
#         print('Eligible to drive')
#     else:
#         print('not eligible to drive')
# else:
#     print("you are too young to drive")


2.  # Write a program that:
# = > Takes the user's credit score and annual income as input.
# =>If the credit score is above 700, check if the income is above 50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."
# =>If the credit score is below 700, print "Credit score too low."

credit_score=input('Enter your credit score:')
annual_income=input('Enter you Annual income:')

credit_score=float(credit_score)
annual_income=float(annual_income)

if credit_score>700:
    if annual_income>50000:
        print("Loan Approved")
    else:
        print("Income requirement not met.")
else:
    print("Credit score too low.")

# slide 56=> 5
# slide 57
# slide 59 =>5