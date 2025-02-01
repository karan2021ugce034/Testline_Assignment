You can download and see the video and screenshots to get a brief idea of my assignment

Clone the repository to your local machine:
git clone https://github.com/yourusername/neet-rank-prediction.git
cd neet-rank-prediction


Set up a virtual environment:
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows


Install the required dependencies:
pip install -r requirements.txt


The model is trained using the following features and uses Random Forest:
score: The student's score on the quiz.
accuracy: The accuracy of the student's answers.
correct_percentage: The percentage of correct answers.
difficulty_adjusted_score: The adjusted score considering the difficulty of the quiz.
trophy_level: The student's trophy level, categorized as Bronze, Silver, and Gold.


How to use:
Run the Streamlit app: After installing the dependencies, run the app using the following command in terminal:
streamlit run app.py


Enter Features: Once the app opens in your browser:
score: Enter the student's score in the quiz.
accuracy: Provide the accuracy value (between 0 and 1).
correct_percentage: Enter the percentage of correct answers (between 0 and 100).
difficulty_adjusted_score: Enter the score adjusted for quiz difficulty.
trophy_level: Select the trophy level (Bronze, Silver, or Gold).


Get Prediction: 
After entering the values, click on the "Predict Rank" button to get the predicted NEET rank for the student.
