import openai as ai
import gradio as grd
import os
from configparser import ConfigParser

def get_api_key():
  print("Getting api key from env...")
  api_key = os.environ.get("api_key","")

  if not api_key:
    print("key is missing from the env")
    print("Getting api key from config file...")
    config_object = ConfigParser()
    config_object.read("../../config.env")
    api_key = config_object["KEY"]["api_key"]
  return api_key

ai.api_key = get_api_key()

if not ai.api_key:
  raise Exception("Invalid API key")

prompt = [{"role": "system", "content": "You are a tokenization engineer"}]


def generate_response(user_prompt):
  prompt.append({"role": "user", "content": user_prompt})
  response = ai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = prompt)
  output = response["choices"][0]["message"]["content"]
  prompt.append({"role": "assistant", "content": output})
  return output

ui = grd.Interface(fn=generate_response, inputs = "text", outputs = "text", title = "Wiz the Wizard")

ui.launch(share=True)


