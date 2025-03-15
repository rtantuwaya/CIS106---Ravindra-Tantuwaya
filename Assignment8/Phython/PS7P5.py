# Initialize variables
total_tuition_owed = 0  # Accumulator for total tuition owed
student_count = 0  # Counter for the number of students

# Define the file name
file_name = 'students.txt'

try:
    # Open the file in read mode
    with open(file_name, 'r') as file:
        while True:
            # Read the student last name, district code, and credits taken in sequence
            last_name = file.readline().strip()  # Read student last name
            if not last_name:  # If there's no last name, break out of the loop
                break
            district_code = file.readline().strip()  # Read district code
            credits_taken = file.readline().strip()  # Read credits taken as a string

            # Check if credits_taken is valid and convert it to integer
            try:
                credits_taken = int(credits_taken)
            except ValueError:
                print(f"Error: Invalid number of credits for {last_name}. Skipping this student.")
                continue  # Skip this student and move to the next one

            # Determine the cost per credit based on district code
            if district_code == 'I':  # In-district
                cost_per_credit = 250.00
            elif district_code == 'O':  # Out-of-district
                cost_per_credit = 500.00
            else:
                print(f"Error: Invalid district code for {last_name}. Skipping this student.")
                continue  # Skip if the district code is invalid

            # Calculate the tuition owed
            tuition_owed = credits_taken * cost_per_credit

            # Output the details for the current student
            print(f"Student: {last_name}")
            print(f"Credits Taken: {credits_taken}")
            print(f"Tuition Owed: {tuition_owed}")
            print("-" * 30)

            # Accumulate the total tuition owed and count the number of students
            total_tuition_owed += tuition_owed
            student_count += 1

    # After the loop, display the summary
    print("\nSummary:")
    print(f"Total Tuition Owed: {total_tuition_owed}")
    print(f"Number of Students: {student_count}")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
