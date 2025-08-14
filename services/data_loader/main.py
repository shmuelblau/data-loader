





from fastapi import FastAPI ,Request
from fastapi.responses import JSONResponse , HTMLResponse , RedirectResponse
from fastapi.templating import Jinja2Templates

from DAL.Eagle_DAL import Eagle_DAL
from Models.Person import Person
from Models.PersonType import PersonType
import jinja2

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
host = os.getenv("HOST")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
dbname = os.getenv("DATABASE")
table_name = os.getenv("TABLE_NAME")




app = FastAPI()

dal = Eagle_DAL(host,user,password, dbname ,table_name)

templates = Jinja2Templates(directory="templates")


@app.get('/get') 
def get():
    
    data = dal.Select()
    return data

@app.get("/", response_class=HTMLResponse)
def home1(request: Request):
    data = dal.Select()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "data": data}
    )





@app.post('/add') 
def add(person:PersonType):
    
    dal.add(person)
    return RedirectResponse(url="/n")


@app.post('/edit' ) 
def edit(person:PersonType):
    
    dal.edit(person)
    return RedirectResponse(url="/n")


@app.post('/delete' ) 
def delete(id : int | str):
    
    person = Person(id=id)
    dal.delete(person)
    return RedirectResponse(url="/n")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)