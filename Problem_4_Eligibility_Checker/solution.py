#eligibility checker whether you are eligible to drive cars in Ethiopia or not
age=int(input("enter your age:"))
if age>=16:
    print("you completed the minimum requirement to drive cars in Ethiopia ")
driving_license = input("Do you have a driving license?:")
print(driving_license)
if driving_license=='yes':
    print("you're eligible to drive cars in Ethiopia! ")
elif driving_license== 'no':
    print("you are not eligible to drive cars in Ethiopia ")
# your code here
