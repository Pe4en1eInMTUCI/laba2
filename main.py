from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def deafult():
    return "Hello!"

