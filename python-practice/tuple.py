# Question:

# Given a list of tuples, where each tuple contains a student's name and their score, write a function that returns the name of the student with the highest score. If there are multiple students with the same highest score, return the name that comes first alphabetically.

# Example 1:
# Input: [("Rajat", 92), ("Prateek", 88), ("Nidhi", 95), ("Arpit", 95)]
# Output: "Arpit"
# Explanation: Both Nidhi and Arpit have the highest score of 95, but since "Arpit" comes before "Nidhi" alphabetically, "Arpit" is returned.

# Example 2:
# Input: [("John", 78), ("Mike", 92), ("Emily", 82)]
# Output: "Mike"
# Explanation: Mike has the highest score of 92.

# Example 3:
# Input: [("Lily", 100), ("Emma", 100), ("Ava", 95)]
# Output: "Emma"
# Explanation: Both Lily and Emma have the highest score of 100, but since "Emma" comes before "Lily" alphabetically, "Emma" is returned.


def highest_score(tuple):
    max_score = 0
    student_with_highest_score = ""
    for student,score in tuple:
        if score > max_score:
            max_score = score
            student_with_highest_score = student
        elif max_score == score:
            if student_with_highest_score > student:
                student_with_highest_score = student_with_highest_score > student
    return student_with_highest_score


tuple_one = [("Rajat", 92), ("Prateek", 88), ("Nidhi", 95), ("Arpit", 95)]
tuple_two = [("John", 78), ("Mike", 92), ("Emily", 82)]
tuple_three = [("Lily", 100), ("Emma", 100), ("Ava", 95)]
print(highest_score(tuple_one))
print(highest_score(tuple_two))
print(highest_score(tuple_three))