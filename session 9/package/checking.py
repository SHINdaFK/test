def checkAge(age):
    if (0 <= age <= 6):
        return ("Baby")
    elif (7 <= age <= 15):
        return ("Children")
    elif (16 <= age <= 18):
        return ("Teen")
    else:
        return ("adult")


if __name__ == "__main__":
    checkAge(yourAge)