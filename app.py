import streamlit as st
import pickle
import re
import string

# Text preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

@st.cache_resource
def load_assets():
    with open('best_logistic_regression_model_issue.pkl', 'rb') as f_issue:
        model_issue = pickle.load(f_issue)
    with open('best_logistic_regression_model_product.pkl', 'rb') as f_product:
        model_product = pickle.load(f_product)
    with open('tfidf_vectorizer.pkl', 'rb') as f_vectorizer:
        vectorizer = pickle.load(f_vectorizer)
    return model_issue, model_product, vectorizer

model_issue, model_product, vectorizer = load_assets()

st.set_page_config(page_title="Complaint Classifier", layout="wide")
st.title("Consumer Complaint Classification")
st.markdown("Enter a consumer complaint below, and the app will predict the **Product** and **Issue** categories.")

user_input = st.text_area("Enter Complaint Text:", "", height=250)

if st.button("Classify Complaint"):
    if user_input:
        cleaned_input = preprocess_text(user_input)
        input_vector = vectorizer.transform([cleaned_input])
        predicted_product = model_product.predict(input_vector)[0]
        product_probas = model_product.predict_proba(input_vector)[0]
        product_confidence = product_probas.max()
        predicted_issue = model_issue.predict(input_vector)[0]
        issue_probas = model_issue.predict_proba(input_vector)[0]
        issue_confidence = issue_probas.max()
        st.subheader("Classification Results")
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**Predicted Product:**")
            st.success(f"**{predicted_product}**")
            st.write(f"Confidence: **{product_confidence:.2%}**")
        with col2:
            st.info(f"**Predicted Issue:**")
            st.success(f"**{predicted_issue}**")
            st.write(f"Confidence: **{issue_confidence:.2%}**")
    else:
        st.warning("Please enter some complaint text before classifying.")
