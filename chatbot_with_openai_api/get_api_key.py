
# test_api_key_file = "chatbot-with-openai-api/apikey.txt"

def get_api(api_key_file):
  api_key = ""
  try:
    with open (api_key_file,"r") as api_file:
      api_key = api_file.read()
  except:
    api_key = None

  return api_key

# get_api(test_api_key_file)