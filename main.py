from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Form

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

comments=[]

@app.get("/", response_class=HTMLResponse)
async def todo_page(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "name":"바보"
        })


@app.get("/host", response_class=HTMLResponse)
async def comment_page(request:Request):
    return templates.TemplateResponse("submit.html", {
        "request":request,
        "comments": comments
    })
 
@app.post("/host", response_class=HTMLResponse)
async def save_comment(request: Request, submit: str = Form(...)):
    comments.append(submit)
    return RedirectResponse(url ="/host",
        status_code=303
    )


