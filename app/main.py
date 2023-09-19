# main.py
from fastapi import FastAPI
from routes.route import router  # Import the router

app = FastAPI()

# Include the router with a prefix
app.include_router(router, prefix="/v1")  # Include the router with a prefix