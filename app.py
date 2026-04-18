import streamlit as st
import pickle

# Load saved components
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))  # not used now, but okay to keep

# UI
st.title("Emotion Detection App 😊")

user_input = st.text_area("Enter your text:")

if st.button("Detect Emotion"):
    if user_input.strip() != "":
        
        # Convert text → vector
        vector = vectorizer.transform([user_input])
        
        # Predict (number)
        prediction = model.predict(vector)[0]

        # 🔥 IF-ELSE MAPPING
        if prediction == 0:
            emotion = "sadness 😢"
        elif prediction == 1:
            emotion = "anger 😡"
        elif prediction == 2:
            emotion = "love ❤️"
        elif prediction == 3:
            emotion = "surprise 😲"
        elif prediction == 4:
            emotion = "fear 😨"
        elif prediction == 5:
            emotion = "joy 😄"
        else:
            emotion = "Unknown"

        # Show result
        st.success(f"Detected Emotion: {emotion}")
        
    else:
        st.warning("Please enter some text")