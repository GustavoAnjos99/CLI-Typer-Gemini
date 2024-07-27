import typer
from typing_extensions import Annotated
from typing import List, Optional

from apikeygemini import API_KEY
from datetime import date
import google.generativeai as genai

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
app = typer.Typer()

@app.command()
def gemini(query: str):
    response = model.generate_content(query)
    print(f"\n{response.text}\n")

@app.command()
def gemini_file(file, query: str):
    f = open(file, "r")
    response = model.generate_content([f.read(), query])
    print(f"\n{response.text}\n")


if __name__ == "__main__":
    app()
