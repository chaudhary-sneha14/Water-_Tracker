@'
# 💧 AI Water Tracker System

AI Water Tracker is a simple hydration tracking system that helps users log daily water intake, view water history, and get AI-powered hydration feedback using Google Gemini.

---

## 🚀 Features

- Log daily water intake in milliliters
- Store intake history in SQLite database
- Get AI hydration suggestions using Gemini
- View water intake history in Streamlit dashboard
- Display daily water intake chart
- FastAPI backend for API routes
- Simple and beginner-friendly project structure

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Uvicorn
- Streamlit
- SQLite
- Pandas
- Google Gemini API
- LangChain Google GenAI
- Python Dotenv

---

## 📁 Project Structure

```txt
Water_Tracker/
│
├── src/
│   ├── api.py
│   ├── agent.py
│   ├── database.py
│   └── logger.py
│
├── dashboard.py
├── requirements.txt
├── .env
└── README.md

⚙️ Create Virtual Environment
Using Conda
conda create -n watertracker python=3.10 -y
conda activate watertracker
Or using Python venv
python -m venv .venv
.venv\Scripts\activate

📦 Install Dependencies

Make sure you are inside the project folder where requirements.txt exists.

pip install -r requirements.txt

If you want to install manually:

pip install fastapi uvicorn streamlit pandas python-dotenv langchain-google-genai google-genai
🔑 Set Up Google API Key
Create a .env file in the project root and add your Google API key:
GOOGLE_API_KEY=PASTE_YOUR_API_KEY_HERE
This key is required for the AI hydration assistant using Gemini.

▶️ Run FastAPI Backend
From the project root folder, run:
uvicorn src.api:app --reload
If you are already inside the src folder, run:
uvicorn api:app --reload
After running, open:
http://127.0.0.1:8000/docs
This will open FastAPI Swagger UI where you can test the APIs.

📌 API Endpoints
1. Log Water Intake
POST /log-intake
Request body:
{  "user_id": "user_123",  "intake_ml": 1500}
Response example:
{  "Message": "Water Intake Logged Successfully",  "Analysis": "You Drank 1500 ml today. Your hydration is moderate..."}

2. Get Water History
GET /history/{user_id}
Example:
GET /history/user_123
Response example:
{  "user_id": "user_123",  "history": [    [1500, "2026-05-18", "10:30:00"]  ]}

📊 Run Streamlit Dashboard
Open a new terminal and run:
streamlit run dashboard.py
This will open the dashboard in your browser.
Usually it opens at:
http://localhost:8501

🧪 Optional: Insert Dummy Data
If your project has a dummy data file, run:
python src/dummy_info.py
Use this only if you want sample water intake records for testing charts.

🧠 How the Project Works
User enters water intake        ↓Streamlit/FastAPI receives the data        ↓Water intake is saved in SQLite database        ↓Gemini AI analyzes the intake        ↓User gets hydration feedback        ↓History and chart show previous intake records

📝 Important Notes


Always run commands from the project root unless mentioned otherwise.


Keep your .env file private.


Do not upload your Google API key to GitHub.


Make sure get_intake() returns records from the database.


Make sure the database table is created before logging water intake.




