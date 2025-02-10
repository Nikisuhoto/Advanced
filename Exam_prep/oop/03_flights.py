def flights(*args):
    courses_dict = {}
    credit = 0
    for i in range(0, len(args), 2):
        destination = args[i]
        if destination == "Finish":
            return courses_dict
        credit = args[i+1]
        if destination not in courses_dict.keys():
            courses_dict[destination] = credit
        else:
            courses_dict[destination] += credit
    return courses_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
