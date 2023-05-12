
import os

def get_api():
  return os.environ['api_key'] if os.environ['api_key'] is not None else None