from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Form
from datetime import date, timedelta
import random

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


@app.get("/square/{number}")
async def read_item(number: int):
    return {"result":number **2}


@app.get("/greet")
async def read_name(name:str = "친구"):
    return {"message": f"안녕, {name}"}

@app.get("/alert/{city}")
async def read_city(city:str, temp:int):
    if temp >= 37:
        return {
            "city": city,
            "status": "폭염경보"
        }
    elif 33<=temp<37:
        return {
            "city": city,
            "status": "폭염주의보"
        }
    else:
        return{
            "city": city,
            "status": "정상"
        }
    


@app.get("/forecast/{city}")
async def read_forecast(city:str, days: int = 3):
    today = date.today()
    forecast_data = []
    for i in range(days):
        forecast_data.append({
            "day": str(today + timedelta(days=i)),
            "temp": random.randint(30,38)
        })
    return {
        "city":city,
        "forecast": forecast_data
    }



@app.get("/news")
async def read_news(q:str = None):
    fake_news = [
         {"title": "서울 폭염 주의보 발령"},
    {"title": "부산 체감온도 38도 돌파"},
    {"title": "대구 낮 최고 37도 기록"},
    {"title": "파주 무더위에 전력 사용 급증"},
    ]
    if q is None:
        return {
            "result": fake_news,
        }
    else:
        filtered_news = [news for news in fake_news if q in news["title"]]
        return{
            "return": filtered_news
        }


