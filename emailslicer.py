import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def check(email):
    
    if(re.fullmatch(regex, email)):
        username = email[:email.index('@')]
        domain = email[email.index('@') + 1:]
        print(f"Your username is {username} & domain is {domain}")
    else:
        print("enter the valid Email")
 
if __name__== '__main__':
 
    email = input("Enter Your Email: ").strip()

    check(email)