Consumer Complaint Classification System
An end-to-end Machine Learning application designed to automatically classify consumer financial complaints. This project uses Natural Language Processing (NLP) to analyze complaint text and predicts the relevant 'Product' and 'Issue' categories. The final models are deployed as an interactive web application using Streamlit.

🚀 Live Demo
https://comsumercomplaintanalyse.streamlit.app/

✨ Features
Dual Prediction: Classifies complaints into two distinct targets: Product and Issue.

Interactive UI: A simple and intuitive web interface built with Streamlit for real-time predictions.

Prediction Confidence: Displays the confidence score for each prediction, providing insight into the model's certainty.

Real-time Processing: Handles raw text input, performs the necessary preprocessing, and delivers predictions instantly.

🛠️ Tech Stack & Libraries
Language: Python 3.10+

Machine Learning: Scikit-learn

Data Manipulation: Pandas, NumPy

Web Framework: Streamlit

Model Persistence: Joblib / Pickle

📂 Project Structure
.
├── issue_model.joblib                          # Trained model for 'Issue'
├── product_model.joblib                        # Trained model for 'Product'
├── tfidf_vectorizer.joblib                     # Fitted TF-IDF Vectorizer
├── app.py                                      # The Streamlit application script
├── requirements.txt                            # Required Python libraries
└── README.md                                   # Project documentation
⚙️ Setup and Installation
To run this project on your local machine, follow these steps:

1. Clone the Repository

Bash

git clone https://github.com/Rakul555/Consumer-complaine-analyzer
cd Consumer-complaine-analyzer
2. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to keep project dependencies isolated.

Create the environment:

Bash

python -m venv venv
Activate the environment:

On Windows:

Bash

venv\Scripts\activate
On macOS/Linux:

Bash

source venv/bin/activate
3. Install Required Libraries

Use the requirements.txt file to install all necessary packages.

Bash

pip install -r requirements.txt
🖥️ How to Use the Application
1. Run the Streamlit App

Once the setup is complete, run the following command in your terminal from the project's root directory:

Bash

streamlit run app.py
2. Use the Web Interface

Your web browser will automatically open to the application's local URL (e.g., http://localhost:8501).

Enter a consumer complaint into the text area.

Click the "Classify Complaint" button.

The application will display the predicted Product and Issue along with their confidence scores.

📈 Machine Learning Workflow
This project followed a standard NLP and machine learning pipeline to achieve its results.

Data Source: The model was trained on a dataset of consumer financial complaints (e.g., the public dataset from the Consumer Financial Protection Bureau - CFPB).

Text Preprocessing: The raw complaint text was cleaned by converting to lowercase, removing punctuation, numbers, and extra whitespace.

Label Consolidation: A key step in improving performance was the strategic consolidation of over 85 granular Issue labels into 10 broader, more distinct categories. This provided a clearer signal for the model to learn from.

Feature Engineering: The cleaned text was converted into numerical vectors using the TF-IDF (Term Frequency-Inverse Document Frequency) technique. N-grams (both unigrams and bigrams) were included to capture more context.

Modeling: Two separate Logistic Regression models were trained: one to predict the Product category and another to predict the Issue category.

Deployment: The final trained models and the TF-IDF vectorizer were serialized using pickle/joblib and deployed in a user-friendly web application built with Streamlit.

🔮 Future Improvements
Experiment with Advanced Models: Test more complex models like LightGBM, XGBoost, or even Transformer-based models (e.g., DistilBERT) to potentially increase accuracy.

Incorporate a Feedback Loop: Add a feature to the Streamlit app allowing users to flag incorrect predictions, which can be used to collect data for future model retraining.

Build an Analytics Dashboard: Create a dashboard to track prediction statistics, monitor model performance over time, and visualize the types of complaints being received.

✍️ Author
Rakul N - https://www.linkedin.com/in/rakul-natraj-951212280/