from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routes.gamesRoutes as routes

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174",
                   "http://localhost:3000", "http://localhost:4000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Game Catalogue Service!"}

print("Game Catalogue Service is running...")
