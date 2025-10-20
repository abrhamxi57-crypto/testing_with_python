#password validator
name=(input("enter the name:"))
print(name)
password=(input("enter the password:"))
print(password)
missing_rules=[]
if len(password)<8:
    missing_rules.append("password must be at least 8 characters long")
if not any(char.isdigit()for char in password):
   missing_rules.append("password must contain at least one digit.")
if password.lower()== name.lower():
    missing_rules.append("password cannot be the same as your name.")
if not missing_rules:
    print("Strong password! You meet all the requirements.")
else:
    print("Weak password.Please fix the following:")
    for rule in missing_rules:
        print("-",rule)# your code here
