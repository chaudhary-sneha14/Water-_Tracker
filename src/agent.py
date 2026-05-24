import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()


llm=ChatGoogleGenerativeAI( model="gemini-2.5-flash-lite",  google_api_key=os.getenv("GOOGLE_API_KEY"))

class WaterIntakeAgent:

    def __init__(self):
        self.history=[]

    def analyze_intake(self,intake_ml):

        prompt = f"""You are a hydration assitant. 
        The user will present you their consumed ml of water today.
        Provide a hydration status (keep it short in 1 sentence) and suggest if they have to drink more water (Keep short again with 1-2 sentences).
        Start the response with (You Drank {intake_ml} ml today.) and then the status and suggestion"""

        response = llm.invoke([HumanMessage(content=prompt)])

        return response.content   


if __name__=="__main__": #Run the code below only if this file is the main file being executed.
    agent=WaterIntakeAgent()
    intake=1500
    feedback=agent.analyze_intake(intake)
    print(f"Hydration Analysiis: {feedback}")
    