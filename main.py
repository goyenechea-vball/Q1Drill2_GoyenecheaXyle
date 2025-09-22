rom pyscript import display, clear

def generate_message(*args, **kwargs):
    # Get input values from the DOM
    name = Element("name").value
    age = Element("age").value
    school = Element("school").value

    # Assign strings to variables
    student_name = name
    student_age = age
    student_school = school

    # Multiline string with escape characters (\n for newline, \t for tab)
    profile_message = (
        f"Student Profile:\n"
        f"\tName: \"{student_name}\"\n"
        f"\tAge: {student_age}\n"
        f"\tSchool: \"{student_school}\"\n"
        f"\nWelcome, {student_name}! It's great to have you at {student_school}."
    )

    # Clear previous message
    clear("output")

    # Display the formatted message
    display(profile_message, target="output")