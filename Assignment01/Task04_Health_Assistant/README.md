# General Health Query Chatbot

A simple health query chatbot built with Python using the Hugging Face Inference API and Mistral-7B-Instruct model. The chatbot answers general health-related questions using prompt engineering and includes safety filters to avoid harmful medical advice.


# Requirements

- Python 3.x
- requests library
- Hugging Face account and API token



# Installation

1. Clone or download the project files.

2. Install the required library in your terminal:

pip install requests

3. Get a free Hugging Face API token:
   - Go to https://huggingface.co/settings/tokens
   - Click New Token, select Read role, and copy the token.

4. Open `health_chatbot.py` and replace the placeholder on line 10:

python
HF_API_KEY = "hf_YOUR_TOKEN_HERE"

# Usage

Navigate to the project folder and run:

cd Task04_Health_
python health_chatbot.py


Type your health question when prompted. Type `quit` or `exit` to stop the chatbot.



# Example Queries

You: What causes a sore throat?
You: Is paracetamol safe for children?
You: How can I improve my sleep?
You: What are the symptoms of dehydration?


# Features:

  # Prompt Engineering

  A system prompt instructs the model to behave as a friendly health information assistant. It sets the tone, limits response length, and defines strict rules such as never diagnosing conditions, never recommending specific dosages, and always referring users to a doctor.

  # Safety Filter

  Before every API call, the user input is checked against a list of emergency keywords such as "chest pain", "stroke", "overdose", and "seizure". If a match is found, the API is not called and an emergency alert is returned immediately directing the user to contact emergency services.

  # Conversation Memory

  The chatbot stores the conversation history and passes the last 3 turns to the model with each new request, allowing it to maintain context across multiple questions.

  # Disclaimer

  Every response from the model automatically includes a reminder that the information provided is general only and that the user should consult a qualified healthcare professional for personal medical decisions.



  # Project Structure

  Task04_Health_Assitant/
      health_chatbot.py
      README.md

  # Model

  - Model: mistralai/Mistral-7B-Instruct-v0.2
  - API: Hugging Face Inference API (free tier)


  # Notes

  - The model may take 20 to 60 seconds to respond on first use as it loads on Hugging Face servers.
  - If a timeout error occurs, wait a moment and try again.
  - This chatbot provides general health information only and is not a substitute for professional medical advice.