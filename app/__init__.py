from json import JSONEncoder
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import random
from app.core.authorization import auth_required


class CustomJSONEncoder(JSONEncoder):
    def __init__(self, *args, **kwargs):
        kwargs["ensure_ascii"] = False  # Prevents unicode escapes
        super(CustomJSONEncoder, self).__init__(*args, **kwargs)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.json_encoder = CustomJSONEncoder


@app.get("/api/custom_quote")
async def custom_quote(user: dict = Depends(auth_required)):
    """Return a random inspirational quote."""
    quotes = [
        "'Believe you can and you're halfway there'. - Theodore Roosevelt",
        "'Don't watch the clock; do what it does. Keep going'. - Sam Levenson",
        "'Whether you think you can or you think you can’t, you’re right'. - Henry Ford",
        "'The only way to do great work is to love what you do'. - Steve Jobs",
        "'You are never too old to set another goal or to dream a new dream'. - C.S. Lewis",
        "'The only difference between a rut and a grave is their dimensions'. - Ellen Glasgow",
        "'If you're going through hell, keep going'. - Winston Churchill",
        "'People often say that motivation doesn't last. Well, neither does bathing – that’s why we recommend it daily'. - Zig Ziglar",
        "'If you think you are too small to make a difference, try sleeping with a mosquito'. - Dalai Lama",
        "'I find that the harder I work, the more luck I seem to have'. - Thomas Jefferson",
        "'I have not failed. I’ve just found 10,000 ways that won’t work'. - Thomas A. Edison",
    ]

    return {"quote": random.choice(quotes)}
