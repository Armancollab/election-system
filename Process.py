from Database import Candids
from Database import members

def check_code(code):
    for x in members:
        if x['Key'] == code:
            return x['Name']
    return None

code = input("Enter your code: ")
mem_name = check_code(code)

if mem_name:
    print("You are allowed to vote")
    print("Your name is: {}".format(mem_name))
    print("Choose a person:")

    while True:
        for x in Candids:
            print(x)

        person = input("Enter the name of the person you want to vote for: ")

        if person in Candids:
            print("You voted for {}".format(person))
            break
        else:
            print("Wrong Name Try again.")

else:
    print("Entered code is wrong")



