from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# টেমপ্লেট ফোল্ডার সেটআপ করুন (এখানে আমরা "templates" ফোল্ডার ব্যবহার করব)
templates = Jinja2Templates(directory="templates")

# হোমপেজ রাউট
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=25851)
