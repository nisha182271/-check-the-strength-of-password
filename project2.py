#PASSWORD STRENGTH CHECKER
#Objective: the objective of this project is to build a password strength checker
#that evaluates the strength of user-provide password based on common 
#security criteria.Theprogram helps users create secure password by providing feedback
#on password qualityand suggestiing improvements

#TOPICS COVERED IN THIS PROJECT: Functions,Conditional statements,Loops,input
# and output handling string manipulation.
# Import library(Regular Expression), logic validation, etc.
import re
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: password must be at least 8 characters"
    
    if not any(char.isdigit() for char in password):
        return "weak: password must contain a digit"
    
    if not any(char.isupper() for char in password):
        return "weak: password must contain an upper char"
    
    if not any(char.islower() for char in password):
        return "weak: password must contain an lower char"
    
    if not re.search(r'[!@#$%^&*(){}<>.?]',password):
        return "Medium: password must contain a special char"
    
    return "Strong: your password is secure!"
123456
def password_checker():
    print("Welcome to the password strength checker")
    while True:
        password = input("Enter your password (or type 'exit' to quite):")
        
        if password.lower() == 'exit':
            print("Thank ypu for using this tool")
            break
        result = check_password_strength(password)
        print(result)
        
        
#Run the password checker tool
if __name__ == "__main__":
    password_checker()