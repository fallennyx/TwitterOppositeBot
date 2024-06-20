import os
import pathlib
import textwrap
from dotenv import load_dotenv
import os
load_dotenv()

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
model = genai.GenerativeModel('gemini-1.5-flash')
def googlegemini(string):
    response = model.generate_content(string)
    return response


