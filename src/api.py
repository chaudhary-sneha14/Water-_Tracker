from fastapi import FastAPI
from pydantic import BaseModel

from src.agent import WaterIntakeAgent
from src.database import log_intake, get_intake
from src.logger import log_message

# Create FastAPI app
app = FastAPI()

# Create AI agent object
agent = WaterIntakeAgent()

# Request body format for /log-intake
class WaterIntakeRequest(BaseModel):
    user_id: str
    intake_ml: int

# Save water intake and return AI analysis
@app.post("/log-intake")
async def log_water_intake(request: WaterIntakeRequest):

    log_intake(request.user_id, request.intake_ml)      # Save intake in database
    analysis = agent.analyze_intake(request.intake_ml)  # Get AI feedback
    log_message(f"user {request.user_id} logged {request.intake_ml}")  # Save log

    return {
        "Message": "Water Intake Logged Successfully",
        "Analysis": analysis
    }

# Get water intake history of a user
@app.get("/history/{user_id}")  #It takes user_id from the URL and fetches all water intake records of that user from the database.
async def get_water_history(user_id: str):
    history = get_intake(user_id)  # Fetch history from database

    return {
        "user_id": user_id,
        "history": history
    }