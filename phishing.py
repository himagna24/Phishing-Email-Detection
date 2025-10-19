import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

def preprocess(text):
    return text.lower().replace("http", "URL")

def train():
    df = pd.read_csv("sample_emails.csv")
    X = df['text'].apply(preprocess)
    y = df['label']
    model = LogisticRegression(max_iter=1000)
    vectorizer = TfidfVectorizer()
    X_vec = vectorizer.fit_transform(X)
    model.fit(X_vec, y)
    joblib.dump((vectorizer, model), "model.pkl")
    print("Model trained and saved as model.pkl")

def predict(email):
    vectorizer, model = joblib.load("model.pkl")
    email_vec = vectorizer.transform([preprocess(email)])
    pred = model.predict(email_vec)[0]
    print(f"Prediction: {pred}")

if __name__ == "__main__":
    choice = input("Type 'train' to train model or 'predict' to predict email: ").strip().lower()
    if choice == "train":
        train()
    elif choice == "predict":
        email = input("Enter email text: ")
        predict(email)
    else:
        print("Invalid option!")
