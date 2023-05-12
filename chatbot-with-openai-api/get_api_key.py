
api_key_file = "chatbot-with-openai-api/apikey.txt"

def get_api():
  api_key = ""
  with open (api_key_file,"r") as api_file:
    api_key = api_file.read()

  print(api_key)

  return api_key

get_api()