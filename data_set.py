import pandas as pd
import numpy as np
import random
from faker import Faker

# Initialize Faker for generating random names
fake = Faker()

# Function to generate random quiz data
def generate_quiz_data(num_students=150):
    data = []
    for student_id in range(1, num_students + 1):
        user_id = f"YcDFSO4ZukTJnnFMgRNVwZTE4j42_{student_id}"  # Unique user_id for each student
        for quiz_num in range(1, random.randint(2, 6)):  # Each student takes 2 to 5 quizzes
            quiz_id = random.choice([6, 18, 20, 24, 25, 51, 57])  # Random quiz_id
            score = random.randint(20, 120)  # Random score between 20 and 120
            trophy_level = random.randint(1, 3)  # Random difficulty level (1 to 3)
            accuracy = random.randint(70, 100)  # Random accuracy between 70% and 100%
            total_questions = random.randint(10, 30)  # Random total questions
            correct_answers = int((accuracy / 100) * total_questions)  # Correct answers based on accuracy
            incorrect_answers = total_questions - correct_answers  # Incorrect answers
            quiz_topic = random.choice([
                "Body Fluids and Circulation", "Human Physiology", "Human Reproduction",
                "Principles of Inheritance", "Microbes in Human Welfare", "Reproductive Health"
            ])  # Random quiz topic
            submitted_at = fake.date_time_between(start_date="-1y", end_date="now").isoformat()  # Random submission time
            neet_rank = random.randint(1000, 10000)  # Random NEET rank between 1000 and 10000

            # Append the data for this quiz attempt
            data.append([
                len(data) + 1,  # id (unique for each quiz attempt)
                quiz_id,  # quiz_id
                user_id,  # user_id
                submitted_at,  # submitted_at
                score,  # score
                trophy_level,  # trophy_level
                accuracy,  # accuracy
                correct_answers,  # correct_answers
                incorrect_answers,  # incorrect_answers
                quiz_topic,  # quiz_topic
                total_questions,  # total_questions
                neet_rank  # neet_rank
            ])
    return data

# Generate the dataset
data = generate_quiz_data(num_students=150)

# Convert to DataFrame
columns = [
    "id", "quiz_id", "user_id", "submitted_at", "score", "trophy_level", "accuracy",
    "correct_answers", "incorrect_answers", "quiz_topic", "total_questions", "neet_rank"
]
df = pd.DataFrame(data, columns=columns)

# Save to Excel
output_file = "neet_student_data_150.xlsx"
df.to_excel(output_file, index=False)

print(f"Dataset for 150 students saved to {output_file}")