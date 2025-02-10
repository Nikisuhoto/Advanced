def gather_credits(credits, *args):
    courses_dict = {}
    credit_needed = 0
    for courses, credit in args:
        if credit_needed >= credits:
            continue
        courses_dict[courses] = credit
        credit_needed += credit

    for course, credit in courses_dict.items():

        if credit_needed >= credits:
            sorted_courses = sorted(courses_dict.keys())
            result = f"Enrollment finished! Maximum credits: {credit_needed}.\nCourses: {', '.join(sorted_courses)}"
            return result
        if course not in courses_dict:
            courses_dict[courses] += credit

    else:
        result = f'You need to enroll in more courses! You have to gather {credits - credit_needed} credits more.'
        return result


print(gather_credits(
    80,
    ("Basics", 27),
))
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
