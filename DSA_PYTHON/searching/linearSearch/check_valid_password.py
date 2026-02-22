'''
A system store valid password in a list/array.
Given a password atttem verify whether it exits .
password :string
attemp :string (access Granted |Access Denied)


'''


def check_valid_password(passwords,attempt):
    for i in range(len(passwords)):
        if passwords[i] == attempt:
            print("Access Granted")
            return True                  #  stope the loop and return True
    print("Access Denied")
    return False
valid_password = ["pass123","admin@2024","user!@#"]
attempt = "admin@2024"
check_valid_password(valid_password,attempt)