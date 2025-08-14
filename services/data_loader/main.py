from fastapi import FastAPI
from fastapi.responses import JSONResponse , HTMLResponse , RedirectResponse

from DAL.Eagle_DAL import Eagle_DAL
from Models.Person import Person

app = FastAPI()
dal = Eagle_DAL()


@app.get('/')
def home():

    data = dal.Select()
    
    return render_template('index.html' , data=data )

@app.post('/add') 
def add():
    new = Person.from_post_request(request.form)
    dal.add(new)
    return RedirectResponse(url="/n")


@app.post('/edit' ) 
def edit():
    new = Agent.from_post_request(request.form)
    dal.edit(new)
    return RedirectResponse(url="/n")


@app.post('/delete' ) 
def delete():
    agent_id = request.form.get('id')
    agent = Agent(id=agent_id)
    dal.delete(agent)
    return RedirectResponse(url="/n")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)