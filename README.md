# 🚀 Phishing Email Detection

## Overview
It classifies emails into two categories:  

- **phish** – potential phishing email  
- **legit** – normal/legitimate email  

### Key Features
- **Single-file Python script (`phishing.py`)**: Handles both training the model and predicting emails in one place.  
- **Simple preprocessing**: Converts text to lowercase and replaces URLs with tokens, helping the model focus on patterns rather than specific links.  
- **Small CSV dataset (`sample_emails.csv`)**: Contains example emails for quick demonstration and testing.  
- **Minimal dependencies**: Easy to set up without installing heavy libraries.  

## 🗂 Project Structure
phishing_email_simple/
├── phishing.py # Single script for training & prediction
├── sample_emails.csv # Tiny demo dataset
├── README.md # Project instructions
├── requirements.txt # Dependencies
├── LICENSE # MIT License
### Explanation of Files
- **`phishing.py`**: This is the core script. It includes data loading, preprocessing, model training, and prediction logic. Users interact with this file to run the project.  
- **`sample_emails.csv`**: A small dataset used to demonstrate the functionality of the model. Each row typically contains an email text and its label (phish/legit).  
- **`requirements.txt`**: Lists all Python libraries required to run the project. This ensures reproducibility.  
- **`LICENSE`**: Specifies that the project is licensed under the MIT License, allowing free use, modification, and distribution.

## How It Works
The phishing detection process can be summarized in these steps:

1. **Data Loading** – The script reads a CSV dataset containing emails and their labels.  
2. **Preprocessing** – Emails are cleaned by converting to lowercase and replacing URLs with generic tokens. This reduces noise and improves model performance.  
3. **Model Training** – A simple machine learning model (like Naive Bayes or Logistic Regression) is trained using the preprocessed email texts.  
4. **Prediction** – The trained model can classify new email texts as either `phish` or `legit`.  
5. **Output** – The system outputs the predicted category, helping users quickly identify potential phishing emails.

## 🛠 Future Enhancements
-Add more preprocessing features (URL patterns, sender analysis)
-Batch predictions from CSV files
-Convert into a browser extension for Gmail/Outlook
-Include evaluation metrics and visualizations
## License
This project is licensed under the **MIT License**, which allows free use, modification, and distribution. See the LICENSE file for details.
