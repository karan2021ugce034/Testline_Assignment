import streamlit as st
import numpy as np
import joblib

# Load the trained model
@st.cache_resource
def load_model():
    try:
        model = joblib.load("best_rf_model.pkl")
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

# Streamlit UI
st.title("🎯 NEET Rank Prediction")
st.markdown("Enter the following features to predict the NEET rank.")

# Input fields for only the selected 5 features
score = st.number_input("Score", min_value=0.0)
accuracy = st.number_input("Accuracy (0 to 1)", min_value=0.0, max_value=1.0, step=0.01)
correct_percentage = st.number_input("Correct Percentage (0 to 100)", min_value=0.0, max_value=100.0, step=0.1)
difficulty_adjusted_score = st.number_input("Difficulty Adjusted Score", min_value=0.0)
trophy_level = st.selectbox("Trophy Level", ["Bronze", "Silver", "Gold"])

# Encode trophy level
trophy_mapping = {"Bronze": 0, "Silver": 1, "Gold": 2}
trophy_level_encoded = trophy_mapping[trophy_level]

# Predict button
if st.button("Predict Rank"):
    if model:
        try:
            # Prepare input array with the selected features
            features = np.array([
                score, accuracy, correct_percentage, difficulty_adjusted_score, trophy_level_encoded
            ]).reshape(1, -1)

            # Make prediction
            predicted_rank = model.predict(features)[0]

            # Display prediction
            st.success(f"🏆 Predicted NEET Rank: {int(predicted_rank)}")

        except Exception as e:
            st.error(f"Prediction error: {e}")
    else:
        st.error("Model not loaded. Check if 'best_rf_model.pkl' exists.")
