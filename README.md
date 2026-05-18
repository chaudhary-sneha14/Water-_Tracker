# 💧 AI Water Tracker System

AI Water Tracker is a simple hydration tracking system that helps users log their daily water intake, view intake history, and get AI-powered hydration feedback using Google Gemini.

---

## 🚀 Features

- Log daily water intake in milliliters
- Store water intake history in SQLite database
- Get AI-powered hydration feedback
- View water intake history in a Streamlit dashboard
- Display daily water intake chart
- FastAPI backend for API endpoints
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
```

---

## ⚙️ Create Virtual Environment

### Using Conda

```bash
conda create -n watertracker python=3.10 -y
conda activate watertracker
```

### Using Python venv

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 🚰 UI

<img width="860" height="331" alt="image" src="https://github.com/user-attachments/assets/754c59f5-fd7f-4106-9e70-66e779653518" />


---


<img width="792" height="395" alt="image" src="https://github.com/user-attachments/assets/68b4f5c9-c0f7-43dd-83b2-a56485e8dad3" />


---



<img width="859" height="435" alt="image" src="https://github.com/user-attachments/assets/fa43679a-fe5e-4538-8bbd-0ea456497961" />

---


## 📦 Install Dependencies

Make sure you are inside the project folder where `requirements.txt` exists.

```bash
pip install -r requirements.txt
```

If you want to install packages manually, run:

```bash
pip install fastapi uvicorn streamlit pandas python-dotenv langchain-google-genai google-genai
```

---

## 🔑 Set Up Google API Key

Create a `.env` file in the project root folder.

Add your Google API key inside the `.env` file:

```env
GOOGLE_API_KEY=PASTE_YOUR_API_KEY_HERE
```

This key is required for the AI hydration assistant using Gemini.

---

## ▶️ Run FastAPI Backend

From the project root folder, run:

```bash
uvicorn src.api:app --reload
```

If you are already inside the `src` folder, run:

```bash
uvicorn api:app --reload
```

After running the backend, open this URL in your browser:

```txt
http://127.0.0.1:8000/docs
```

This will open FastAPI Swagger UI where you can test the APIs.

---

## 📌 API Endpoints

### 1. Log Water Intake

```txt
POST /log-intake
```

Request body:

```json
{
  "user_id": "user_123",
  "intake_ml": 1500
}
```

Response example:

```json
{
  "Message": "Water Intake Logged Successfully",
  "Analysis": "You Drank 1500 ml today. Your hydration is moderate..."
}
```

---

### 2. Get Water History

```txt
GET /history/{user_id}
```

Example:

```txt
GET /history/user_123
```

Response example:

```json
{
  "user_id": "user_123",
  "history": [
    [1500, "2026-05-18", "10:30:00"]
  ]
}
```

---

## 📊 Run Streamlit Dashboard

Open a new terminal and run:

```bash
streamlit run dashboard.py
```

This will open the dashboard in your browser.

Usually it opens at:

```txt
http://localhost:8501
```

---

## 🧪 Optional: Insert Dummy Data

If your project has a dummy data file, run:

```bash
python src/dummy_info.py
```

Use this only if you want sample water intake records for testing charts.

---

## 🧠 How the Project Works

```txt
User enters water intake
        ↓
Streamlit dashboard receives the data
        ↓
Water intake is saved in SQLite database
        ↓
Gemini AI analyzes the intake
        ↓
User gets hydration feedback
        ↓
History and chart show previous intake records
```

---

## 📝 Important Notes

- Always run commands from the project root unless mentioned otherwise.
- Keep your `.env` file private.
- Do not upload your Google API key to GitHub.
- Make sure `get_intake()` returns records from the database.
- Make sure the database table is created before logging water intake.

---

## 👩‍💻 Author

Built as a beginner-friendly AI hydration tracker project using Python, FastAPI, Streamlit, SQLite, and Gemini.
```
