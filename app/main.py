from fastapi import FastAPI
from seleniumbase import SB

app = FastAPI()

@app.get("/")
def root():
    with SB(headless=True) as sb:
        sb.open("https://example.com")
        title = sb.get_title()
    return {"title": title}
