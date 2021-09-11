import re
regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
#regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w{2,20}+[.]\w{2,3}$'


def checkemail(email):
    print("checkemail function")
    if (regex.match(email)):
        print("Correct Email")
        return 1
    else:
        print("Incorrect Email")
        return 0

    #True email is correct
#False email is incorrect


def checkcontact(contact):
    pattern = r"^[1|8|9][0-9]*$"
    if re.match(pattern, contact) and len(contact) == 8:
        return 1
        print("Valid")
    else:
        return 0
        print("Invalid")
