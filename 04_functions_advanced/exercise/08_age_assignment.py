def age_assignment(*args, **kwargs):
    # people = {}
    # for name in args:
    #     people[name] = kwargs[name[0]]
    # people = sorted(people.items())
    people = {name: kwargs[name[0]] for name in args}
    people = sorted(people.items())

    result = []
    for name, age in people:
        result.append(f"{name} is {age} years old.")
    return "\n".join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
