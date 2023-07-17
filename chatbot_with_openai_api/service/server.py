import openai
import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..\\..\\')))
from utils.utils import get_api_key


# Set up your OpenAI API key
openai.api_key = get_api_key()

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
def handle_user_input(chatbot_prompt, user_input):
    chatbot_prompt = "You are a " + chatbot_prompt
    prompt = f"{chatbot_prompt} {user_input}"
    response = generate_response(prompt)
    return response

# Define a loop to handle multiple user interactions
while True:
    user_purpose = input("> input role eg. software developer, doctor, financial analyst, etc. [To exit, type exit or quit]: \n")
    if user_purpose.lower() in ["exit", "quit"]:
        break
    user_input = input("> input query. [To exit, type exit or quit]: \n")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = handle_user_input(user_purpose, user_input)
    print(response)
