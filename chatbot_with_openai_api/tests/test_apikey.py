import pytest
from chatbot_with_openai_api.get_api_key import get_api
import os

def test_api_key():
  assert get_api() == os.environ['api_key']

def test_api_key_None():
  assert get_api() == os.environ['api_key2']