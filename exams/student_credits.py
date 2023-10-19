def students_credits(*args):
    total_credits_earned = 0
    courses = {}
    result = ''

    for current_course in args:
        data = current_course.split('-')
        course_name = data[0]
        course_credits = float(data[1])
        max_course_points = float(data[2])
        user_points = float(data[3])

        credits_per_point = course_credits / max_course_points
        current_score = credits_per_point * user_points
        total_credits_earned += current_score

        if course_name not in courses:
            courses[course_name] = 0
        courses[course_name] = current_score

    sorted_courses = sorted(courses.items(), key=lambda x: -x[1])

    if total_credits_earned >= 240:
        result += f"Diyan gets a diploma with {total_credits_earned:.1f} credits.\n"
    else:
        result += f"Diyan needs {240 - total_credits_earned:.1f} credits more for a diploma.\n"

    for course in sorted_courses:
        result += f"{course[0]} - {course[1]:.1f}\n"

    return result.strip()


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print(
    students_credits(
            "Discrete Maths-40-500-450",
            "AI Development-20-400-400",
            "Algorithms Advanced-50-700-630",
            "Python Development-15-200-200",
            "JavaScript Development-12-500-480",
            "C++ Development-30-500-405",
            "Game Engine Development-70-100-70",
            "Mobile Development-25-250-225",
            "QA-20-300-300",
        )
)