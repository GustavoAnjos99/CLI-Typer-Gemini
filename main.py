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
def datahoje():
    data = date.today()
    dataFormat = data.strftime('%d/%m/%Y') 
    print(f"\nA data de hoje é: {dataFormat}\n")

@app.command()
def soma(nm: Annotated[Optional[List[float]], typer.Option()] = None):
    total = 0
    for n in nm:
        total += n
    print(f"\n{total}\n")

@app.command()
def expoente(nm: float = typer.Option(), exp: int = typer.Option()):
    try:
        total = nm**exp
        print(f"\n{total}\n")
    except:
        print("Algo deu errado, verifique os dados digitados.")

    



if __name__ == "__main__":
    app()
