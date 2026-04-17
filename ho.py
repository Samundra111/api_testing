import os
from dotenv import load_dotenv

file=load_dotenv()

print(".env file was found",load_dotenv)
print(f"base url is {os.getenv('BASE_URL')}")
print(f"base name is {os.getenv('API_KEY')}")
