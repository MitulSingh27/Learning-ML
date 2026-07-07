from fastapi import FastAPI


app= FastAPI()

@app.get("/home") #GET endpoint
              #the / is the root path---> /homepage, /courses, etc etc
def home():
    return{"message":"Hello world"}

# @ ia called a decorator