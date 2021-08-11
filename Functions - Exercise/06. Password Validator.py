def valid_pass(password):
    warnings = []
    counter = 0
    if 6 <= len(password) <= 10:
        pass
    else:
        warnings.append("Password must be between 6 and 10 characters")
    for i in password:
        if 48 <= ord(i) <= 57 or 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            pass
        else:
            warnings.append("Password must consist only of letters and digits")
        if 48 <= ord(i) <= 57:
            counter += 1
    if counter < 2:
        warnings.append("Password must have at least 2 digits")

    if len(warnings) == 0:
        return "Password is valid"
    else:
        if len(warnings) == 3:
            return warnings[0], warnings[1], warnings[2]
        elif len(warnings) == 2:
            return warnings[0], warnings[1]
        elif len(warnings) == 1:
            return warnings[0]


password_input = input()
print(valid_pass(password_input))
