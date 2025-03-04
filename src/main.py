from fastapi import FastAPI, HTTPException
from models import Signin
import uvicorn

app = FastAPI()


@app.post("/login")
async def login(payload: Signin):
    """Handles user login with basic credential check."""
    if payload.username == "admin" and payload.password == "admin":
        return {"message": "Login successful"}
    
    raise HTTPException(status_code=401, detail="Invalid credentials")



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
