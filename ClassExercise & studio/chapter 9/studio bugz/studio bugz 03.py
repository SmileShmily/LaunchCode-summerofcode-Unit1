'''
    When registering for an online account, users must create a password.
    For your service, you enforce the following rules on passwords: The password must contain at least one non-alphabetical character,
    and may not contain any spaces. The function below is supposed to check the validity of passwords. But! It’s! Not! Working!

'''
#
def password_checker(password):
    contains_non_alpha = False

    for char in password:
        if char == " ":
            return False
        else :
            contains_non_alpha = True

    return contains_non_alpha

pw1 = "i <3 makonnen"
print(password_checker(pw1))
# should print False

pw2 = "puzzlesr4fun"
print(password_checker(pw2))
# should print True
