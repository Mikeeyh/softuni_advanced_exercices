def gather_credits(num, *args):
    courses = []
    total_credits_earned = 0

    for name, value in args:
        if total_credits_earned >= num:
            break
        if name in courses:
            continue
        courses.append(name)
        total_credits_earned += value

    if total_credits_earned >= num:
        courses.sort()
        return f"Enrollment finished! Maximum credits: {total_credits_earned}.\nCourses: {', '.join(sorted(courses))}"
    else:
        credits_needed = num - total_credits_earned
        return f"You need to enroll in more courses! You have to gather {credits_needed} credits more."


print(gather_credits(80, ("Basics", 27),))



