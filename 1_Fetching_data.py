import pandas as pd
import requests

# URLs to fetch data from
current_quiz_url = 'https://api.jsonserve.com/rJvd7g'
historical_quiz_url = 'https://api.jsonserve.com/XgAgFJ'

# Function to fetch data from URL and extract relevant information
def fetch_and_process_data(url):
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # If the data is list, we'll iterate through each element
        if isinstance(data, list):
            processed_data = []
            for item in data:
                extracted_data = {
                    'id': item.get('id'),
                    'quiz_id': item.get('quiz_id'),
                    'user_id': item.get('user_id'),
                    'submitted_at': item.get('submitted_at'),
                    'created_at': item.get('created_at'),
                    'updated_at': item.get('updated_at'),
                    'score': item.get('score'),
                    'trophy_level': item.get('trophy_level'),
                    'accuracy': item.get('accuracy'),
                    'speed': item.get('speed'),
                    'final_score': item.get('final_score'),
                    'negative_score': item.get('negative_score'),
                    'correct_answers': item.get('correct_answers'),
                    'incorrect_answers': item.get('incorrect_answers'),
                    'source': item.get('source'),
                    'type': item.get('type'),
                    'started_at': item.get('started_at'),
                    'ended_at': item.get('ended_at'),
                    'duration': item.get('duration'),
                    'better_than': item.get('better_than'),
                    'total_questions': item.get('total_questions'),
                    'rank_text': item.get('rank_text'),
                    'mistakes_corrected': item.get('mistakes_corrected'),
                    'initial_mistake_count': item.get('initial_mistake_count'),
                    'quiz_title': item.get('quiz', {}).get('title'),
                    'quiz_topic': item.get('quiz', {}).get('topic'),
                    'quiz_time': item.get('quiz', {}).get('time'),
                    'quiz_end_time': item.get('quiz', {}).get('end_time'),
                    'quiz_questions_count': item.get('quiz', {}).get('questions_count'),
                    'next_steps': item.get('next_steps')
                }
                processed_data.append(extracted_data)
            return processed_data
        else:
            # Handle case where the response is not a list
            extracted_data = {
                'id': data.get('id'),
                'quiz_id': data.get('quiz_id'),
                'user_id': data.get('user_id'),
                'submitted_at': data.get('submitted_at'),
                'created_at': data.get('created_at'),
                'updated_at': data.get('updated_at'),
                'score': data.get('score'),
                'trophy_level': data.get('trophy_level'),
                'accuracy': data.get('accuracy'),
                'speed': data.get('speed'),
                'final_score': data.get('final_score'),
                'negative_score': data.get('negative_score'),
                'correct_answers': data.get('correct_answers'),
                'incorrect_answers': data.get('incorrect_answers'),
                'source': data.get('source'),
                'type': data.get('type'),
                'started_at': data.get('started_at'),
                'ended_at': data.get('ended_at'),
                'duration': data.get('duration'),
                'better_than': data.get('better_than'),
                'total_questions': data.get('total_questions'),
                'rank_text': data.get('rank_text'),
                'mistakes_corrected': data.get('mistakes_corrected'),
                'initial_mistake_count': data.get('initial_mistake_count'),
                'quiz_title': data.get('quiz', {}).get('title'),
                'quiz_topic': data.get('quiz', {}).get('topic'),
                'quiz_time': data.get('quiz', {}).get('time'),
                'quiz_end_time': data.get('quiz', {}).get('end_time'),
                'quiz_questions_count': data.get('quiz', {}).get('questions_count'),
                'next_steps': data.get('next_steps')
            }
            return [extracted_data]
    else:
        print(f"Failed to fetch data from {url}")
        return None

# Fetch current quiz data
current_quiz_data = fetch_and_process_data(current_quiz_url)

# Fetch historical quiz data
historical_quiz_data = fetch_and_process_data(historical_quiz_url)

# Convert the data to DataFrame if they were fetched successfully
if current_quiz_data:
    current_quiz_df = pd.DataFrame(current_quiz_data)
    
    # Convert columns to numeric, coercing errors (i.e., converting invalid values to NaN)
    numeric_columns = ['accuracy', 'speed', 'score', 'final_score', 'negative_score', 'correct_answers', 'incorrect_answers']
    for col in numeric_columns:
        current_quiz_df[col] = pd.to_numeric(current_quiz_df[col], errors='coerce')
    
    current_quiz_df.to_excel('current_quiz_data.xlsx', index=False)
    print("Current quiz data has been saved to current_quiz_data.xlsx")

if historical_quiz_data:
    historical_quiz_df = pd.DataFrame(historical_quiz_data)
    
    # Convert columns to numeric, coercing errors (i.e., converting invalid values to NaN)
    for col in numeric_columns:
        historical_quiz_df[col] = pd.to_numeric(historical_quiz_df[col], errors='coerce')
    
    historical_quiz_df.to_excel('historical_quiz_data.xlsx', index=False)
    print("Historical quiz data has been saved to historical_quiz_data.xlsx")
