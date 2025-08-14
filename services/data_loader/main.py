from fastapi import FastAPI
from fastapi.responses import JSONResponse , HTMLResponse , RedirectResponse

from DAL.Eagle_DAL import Eagle_DAL
from Models.Person import Person
from Models.PersonType import PersonType


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


@app.get('/')
def home():

    data = dal.Select()
    html_content = """ <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Agent List</title>
    <style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        input[type="text"], input[type="number"] {
            width: 100%;
        }
    </style>
</head>
<body>
    <h1>PERSONS</h1>
    <table>
        <tr>
            <th>id</th>
            <th>first_name</th>
            <th>last_name</th>
           
        </tr>

        {% for agent in data %}
        <tr>
            <form action="/edit" method="POST">
                <td><input type="text" name="id" value="{{ agent[0] }}"></td>
                <td><input type="text" name="first_name" value="{{ agent[1] }}"></td>
                <td><input type="text" name="last_name" value="{{ agent[2] }}"></td>
                
                <td>
                    <input type="hidden" name="id" value="{{ agent[0] }}">
                    <input type="submit" value="Edit">
            </form>
            <form action="/delete" method="POST" style="display:inline;">
                <input type="hidden" name="id" value="{{ agent[0] }}">
                <input type="submit" value="Delete">
            </form>
                </td>
        </tr>
        {% endfor %}

        <tr>
            <form action="/add" method="POST">
                <td><input type="text" name="id" placeholder="New Code Name"></td>
                <td><input type="text" name="first_name" placeholder="New Real Name"></td>
                <td><input type="text" name="last_name" placeholder="Location"></td>

                <td><input type="submit" value="Add"></td>
            </form>
        </tr>
    </table>
</body>
</html>"""
    return HTMLResponse(content=html_content)

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