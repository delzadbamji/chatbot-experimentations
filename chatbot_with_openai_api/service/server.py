import openai
import os

# Set up your OpenAI API key
openai.api_key = os.environ["api_key"]

# Define your chatbot's purpose
chatbot_prompt = "I...am the oracle. What answer do you seek?"

# Define your GPT-3 model and its parameters
model_engine = "davinci"
max_tokens = 100
temperature = 0.7

# Define a function to generate responses using the GPT-3 model
def generate_response(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature
    )
    return response.choices[0].text.strip()

# Define a function to handle user input and generate a response
def handle_user_input(user_input):
    prompt = f"{chatbot_prompt} {user_input}"
    response = generate_response(prompt)
    return response

# Define a loop to handle multiple user interactions
while True:
    user_input = input("> ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = handle_user_input(user_input)
    print(response)
