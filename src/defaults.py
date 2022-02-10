from dotenv import load_dotenv
from os import getenv

load_dotenv()

STUDENT_ID = getenv('STUDENT_ID')
EMAIL_LOGIN = getenv('EMAIL_LOGIN')
EMAIL_PASSWORD = getenv('EMAIL_PASSWORD')
DATABASE_URL = getenv('DATABASE_URL')
