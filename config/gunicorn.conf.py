import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

bind = '127.0.0.1:8000'
workers = 3
user = os.getenv('user')
timeout = 120

