import os
import pathlib
import textwrap
from dotenv import load_dotenv
import os
load_dotenv()

import google.generativeai as genai


GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
model = genai.GenerativeModel('gemini-1.5-flash')
def googlegemini(string):
    GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(string)
    return response.text

print(googlegemini("Hello, how are you?"))