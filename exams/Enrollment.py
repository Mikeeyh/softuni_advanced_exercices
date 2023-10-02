def gather_credits(num, *args):
    num_credits = int(num)
    courses = []
    total_credits_earned = 0

    for name, value in args:
        if name in courses:
            continue
        courses.append(name)
        total_credits_earned += int(value)
        if total_credits_earned >= num_credits:
            break

    if total_credits_earned >= num_credits:
        courses.sort()
        return f"Enrollment finished! Maximum credits: {total_credits_earned}.\nCourses: {', '.join(courses)}"
    else:
        credits_needed = num_credits - total_credits_earned
        return f"You need to enroll in more courses! You have to gather {credits_needed} credits more."


print(gather_credits(80, ("Basics", 27),))



