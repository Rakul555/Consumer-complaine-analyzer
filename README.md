# Consumer Complaint Classification System

An end-to-end machine learning application that automatically classifies consumer financial complaints. This project leverages Natural Language Processing (NLP) to analyze complaint text and predict the relevant **Product** and **Issue** categories. The final models are deployed as an interactive web application using Streamlit.

---

## 🚀 Live Demo

[Try the App on Streamlit](https://comsumercomplaintanalyse.streamlit.app/)

---

## ✨ Features

- **Dual Prediction:** Classifies complaints into both Product and Issue categories.
- **Interactive UI:** Simple, intuitive web interface built with Streamlit for real-time predictions.
- **Prediction Confidence:** Displays confidence scores for each prediction.
- **Real-time Processing:** Handles raw text input, preprocesses, and delivers instant predictions.

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Machine Learning:** scikit-learn
- **Data Manipulation:** pandas, numpy
- **Web Framework:** Streamlit
- **Model Persistence:** joblib / pickle

---

## 📂 Project Structure

```
.
├── issue_model.joblib        # Trained model for 'Issue'
├── product_model.joblib      # Trained model for 'Product'
├── tfidf_vectorizer.joblib   # Fitted TF-IDF Vectorizer
├── app.py                    # Streamlit application script
├── requirements.txt          # Required Python libraries
└── README.md                 # Project documentation
```

---

## ⚙️ Setup and Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/Rakul555/Consumer-complaine-analyzer
    cd Consumer-complaine-analyzer
    ```

2. **Create and Activate a Virtual Environment**

    It's recommended to use a virtual environment to isolate dependencies.

    - **Create the environment:**
      ```bash
      python -m venv venv
      ```
    - **Activate the environment:**
      - On Windows:
         ```bash
         venv\Scripts\activate
         ```
      - On macOS/Linux:
         ```bash
         source venv/bin/activate
         ```

3. **Install Required Libraries**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🖥️ How to Use

1. **Run the Streamlit App**
    ```bash
    streamlit run app.py
    ```

2. **Use the Web Interface**
    - Your browser will open to the app (e.g., http://localhost:8501).
    - Enter a consumer complaint in the text area.
    - Click **Classify Complaint**.
    - View predicted Product and Issue with confidence scores.

---

## 📈 Machine Learning Workflow

- **Data Source:** Trained on public consumer financial complaints (e.g., CFPB dataset).
- **Text Preprocessing:** Lowercasing, removing punctuation, numbers, and extra whitespace.
- **Label Consolidation:** Over 85 granular Issue labels consolidated into 10 broader categories for improved performance.
- **Feature Engineering:** Text converted to numerical vectors using TF-IDF (with unigrams and bigrams).
- **Modeling:** Two Logistic Regression models—one for Product, one for Issue.
- **Deployment:** Models and vectorizer serialized with pickle/joblib and deployed via Streamlit.

---

## 🔮 Future Improvements

- Experiment with advanced models (LightGBM, XGBoost, Transformer-based models like DistilBERT).
- Add a feedback loop for users to flag incorrect predictions.
- Build an analytics dashboard to monitor model performance and visualize complaint types.

---

## ✍️ Author

**Rakul N**  
[LinkedIn](https://www.linkedin.com/in/rakul-natraj-951212280/)
