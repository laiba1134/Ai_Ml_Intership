import gradio as gr
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the fine-tuned model and tokenizer
model_path = "./bert_classifier_final"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

# Define class labels for AG News
# 0: World, 1: Sports, 2: Business, 3: Sci/Tech (Check your dataset details)
labels = ["World", "Sports", "Business", "Sci/Tech"]

def classify_news(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding="max_length", max_length=128)

    with torch.no_grad():
        outputs = model(**inputs)

    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_class_id = predictions.argmax().item()
    confidence = predictions[0][predicted_class_id].item()

    return f"Category: {labels[predicted_class_id]} (Confidence: {confidence:.2f})"

# Create Gradio Interface
iface = gr.Interface(
    fn=classify_news,
    inputs=gr.Textbox(lines=2, placeholder="Enter a news headline here..."),
    outputs="text",
    title="AG News Classifier (BERT)",
    description="Fine-tuned BERT to classify news headlines into World, Sports, Business, or Sci/Tech."
)

if __name__ == "__main__":
    iface.launch()