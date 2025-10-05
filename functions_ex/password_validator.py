def length_checker(some_password:str):
    if 6 <= len(some_password) <= 10:
        return True
    else:
        return "Password must be between 6 and 10 characters"

def is_only_digits(some_password:str):
    if some_password.isalnum():
        return True
    else:
        return "Password must consist only of letters and digits"

def have_at_least_two_digits(some_password:str):
    digits = 0
    for num in some_password:
        if num.isdigit():
            digits += 1
    if digits >= 2:
        return True
    return "Password must have at least 2 digits"

def password_validator(some_password:str) -> list:
    is_valid = []
    is_valid.append(length_checker(some_password))
    is_valid.append(is_only_digits(some_password))
    is_valid.append(have_at_least_two_digits(some_password))
    for index in range(len(is_valid)-1,-1,-1):
        if isinstance(is_valid[index], bool):
            is_valid.pop(index)
    return is_valid

password = input()
password_is_not_valid = password_validator(password)
if password_is_not_valid:
    print("\n".join(password_is_not_valid))
else:
    print("Password is valid")



