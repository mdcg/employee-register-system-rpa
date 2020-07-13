import os
from dotenv import load_dotenv

load_dotenv()

EMPLOYEE_REGISTER_USERNAME = os.getenv("EMPLOYEE_REGISTER_USERNAME")
EMPLOYEE_REGISTER_PASSWORD = os.getenv("EMPLOYEE_REGISTER_PASSWORD")
