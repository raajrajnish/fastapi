from fastapi import FastAPI

# initiate the app
myCustomApp = FastAPI()


# simple fast api
@myCustomApp.get("/helloWorld")
async def Greeting():
    return "Hello world!"


@myCustomApp.get("/home")
async def Home():
    return {"message":"i am home!"}

# how to run fast api, go to root directory where app is define in our case it is Custom.py and run below command
# uvicorn Custom:myCustomApp --reload

# How to see api documentation from swagger or re docs
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc