# 😊 Emotion Detection App (NLP + Streamlit)

This project is a **machine learning-based Emotion Detection Web App** built using **Natural Language Processing (NLP)** and deployed with Streamlit.

It takes user input text and predicts the underlying emotion such as **joy, sadness, anger, fear, love, or surprise**.

---

## 🚀 Features

* 🔤 Converts text into numerical features using CountVectorizer
* 🤖 Uses a trained Logistic Regression model
* 🎯 Predicts emotions from user input
* 🌐 Interactive web app using Streamlit
* ⚡ Fast and lightweight

---

## 🧠 Emotions Supported

* 😢 Sadness
* 😡 Anger
* ❤️ Love
* 😲 Surprise
* 😨 Fear
* 😄 Joy

---

## 🏗️ Project Structure

```
emotion-detection/
│── app.py
│── model.pkl
│── vectorizer.pkl
│── label_encoder.pkl
│── README.md
```

---

## 📦 Installation

### 1. Clone the repository

```
git clone <your-repo-link>
cd emotion-detection
```

---

### 2. Create and activate environment (Recommended)

Using conda:

```
conda create -n emotion_env python=3.10
conda activate emotion_env
```

---

### 3. Install dependencies

```
pip install streamlit scikit-learn pandas numpy
```

---

## ▶️ Run the App

```
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## ⚙️ How It Works

1. User enters text
2. Text is converted into vectors using CountVectorizer
3. Model predicts a numerical label
4. Label is mapped to emotion using if-else logic
5. Emotion is displayed on screen

---

## 🧾 Example

Input:

```
I am feeling very happy today!
```

Output:

```
Detected Emotion: joy 😄
```

---

## 📜 Code Reference

Main application file:
👉 

---

## ⚠️ Important Notes

* Make sure all `.pkl` files are in the same folder as `app.py`
* Do not retrain or remap labels in the app (use saved model)
* Ensure consistent preprocessing between training and app

---

## 🚀 Future Improvements

* 📊 Show prediction probabilities
* 🎨 Better UI (charts, colors, animations)
* 🎤 Voice-based emotion detection
* 🌍 Deploy on Streamlit Cloud / Hugging Face

---

## 👨‍💻 Author

Arnav Adhikary

---

## ⭐ If you like this project

Give it a star ⭐ and share it!

---
