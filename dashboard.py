import streamlit as st
import pandas as pd
from datetime import datetime

from src.agent import WaterIntakeAgent
from src.database import log_intake, get_intake


st.set_page_config(page_title="AI Water Tracker", page_icon="💧")

st.title("💧 AI Water Tracker")

# Create AI agent
agent = WaterIntakeAgent()

# Input fields
user_id = st.text_input("UserName",placeholder="Please enter username")
intake_ml = st.number_input("Water Intake (ml)",placeholder="Please enter water Intake", min_value=0, step=100)

# Submit button
if st.button("Submit"):
    if intake_ml > 0:
        # Save intake in database
        log_intake(user_id, intake_ml)

        # Get AI feedback
        feedback = agent.analyze_intake(intake_ml)

        # Show success message
        st.success(f"Saved {intake_ml} ml water for {user_id}")

        # Show AI feedback immediately
        st.subheader("AI Feedback")
        st.info(feedback)

    else:
        st.warning("Please enter water intake greater than 0.")


st.divider() #add line

st.subheader("Water History")

# Show history button
if st.button("Show History"):
    history = get_intake(user_id)

    if history:
        df = pd.DataFrame(history, columns=["Water", "Date", "Time"])

        st.dataframe(df, use_container_width=True) #create table

        # Convert Date column for chart
        df["Date"] = pd.to_datetime(df["Date"])

        daily_data = df.groupby("Date")["Water"].sum().reset_index()

        st.bar_chart(daily_data, x="Date", y="Water")

    else:
        st.info("No history found.")