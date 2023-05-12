import pytest
from chatbot_with_openai_api.get_api_key import get_api

def test_api_key():
  api_key_file = "chatbot-with-openai-api/apikey.txt"
  test_key = ""
  with open(api_key_file) as file:
    test_key = file.read()

  assert get_api(api_key_file) == test_key
