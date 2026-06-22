print("hello")
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("GROQ_API_KEY"))
