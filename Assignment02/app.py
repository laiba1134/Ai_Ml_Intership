import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_path = "./bert_classifier/checkpoint-1250"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

# Labels
labels = ["World", "Sports", "Business", "Sci/Tech"]

# Streamlit UI
st.title("AG News Classifier (BERT)")
st.write("Fine-tuned BERT model for news classification")

headline = st.text_area("Enter a news headline:")

if st.button("Classify"):

    inputs = tokenizer(
        headline,
        return_tensors="pt",
        truncation=True,
        padding="max_length",
        max_length=128
    )

    with torch.no_grad():
        outputs = model(**inputs)

    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)

    predicted_class_id = predictions.argmax().item()
    confidence = predictions[0][predicted_class_id].item()

    st.success(
        f"Category: {labels[predicted_class_id]}"
    )

    st.info(
        f"Confidence: {confidence:.2f}"
    )
