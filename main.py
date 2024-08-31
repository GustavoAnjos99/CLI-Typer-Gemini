import typer
import google.generativeai as genai
from apikeygemini import API_KEY

from supportfunctions import *
from PIL import Image
import os
from pathlib import Path
from typing_extensions import Annotated
from typing import Optional, Tuple


genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
app = typer.Typer()

@app.command()
def gemini(query: str, createfileMD: Annotated[Optional[tuple[str, str]], typer.Option("-md")] = (None,None), createfileTXT: Annotated[Optional[Tuple[str, str]], typer.Option("-txt")] = (None, None)):
    response = model.generate_content(query)
    dirmd, nomemd = createfileMD
    dirtxt, nometxt = createfileTXT
    
    txt_or_md(dirmd, nomemd, dirtxt, nometxt, response.text)

@app.command()
def gemini_file(file, query: str):
    f = open(file, "r")
    response = model.generate_content([f.read(), query])
    print(f"\n{response.text}\n")

@app.command()
def gemini_img(file, query: str):
    img = Image.open(file)
    response = model.generate_content([img, query])
    print(f"\n{response.text}\n")



if __name__ == "__main__":
    app()
