
import os

def get_env_value(key):
  print(os.getenv(key))
  return os.environ.get(key)
