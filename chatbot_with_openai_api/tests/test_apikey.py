import pytest
from chatbot_with_openai_api.get_env_value import get_env_value
import os

def test_api_key():
  assert get_env_value('api_key') == os.environ.get('api_key')

def test_api_key_None():
  assert get_env_value('api_key2') == None