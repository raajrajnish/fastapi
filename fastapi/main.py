from fastapi import FastAPI

# initiate the app
app = FastAPI()


# simple fast api
@app.get("/helloWorld")
async def Greeting():
    return "Hello world!"

# how to run fast api - go to root directory main.py where app is defined and run below command
# uvicorn main:app --reload

