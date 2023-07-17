import os
from configparser import ConfigParser

def get_api_key():
  print("Getting api key from env...")
  api_key = os.environ.get("api_key","")

  if not api_key:
    print("key is missing from the env")
    print("Getting api key from config file...")
    path_current_directory = os.path.dirname(__file__)
    path_config_file = os.path.join(path_current_directory, '.', 'config.ini')
    config_object = ConfigParser()
    config_object.read(path_config_file)
    api_key = config_object["KEY"]["api_key"]
  return api_key
