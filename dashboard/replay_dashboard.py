import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# This line helps Python find files from the main project folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import the failure detection function from the src folder
from src.failure_detector import detect_failures

# Set dashboard page title and layout
st.set_page_config(
    page_title="BotTrace Robot Replay",
    layout="wide"
)

# Main title of the dashboard
st.title("BotTrace: Robot Failure Replay System")

st.write(
    "BotTrace works like a black box for small robots. "
    "It reads robot data, detects possible failures, and shows movement replay."
)

# User can upload a custom robot log CSV file.
# If no file is uploaded, sample CSV data will be used.
uploaded_file = st.file_uploader("Upload robot log CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/sample_robot_log.csv")


# Analyze robot data and detect failures
df = detect_failures(df)

# Show complete robot log data
st.subheader("Robot Log Data")
st.dataframe(df)

# Filter only failure rows
failure_rows = df[df["detected_error"] != "NORMAL"]

st.subheader("Failure Summary")

if failure_rows.empty:
    st.success("No failure detected in the robot log.")
else:
    st.error(f"{len(failure_rows)} failure points detected.")
    st.dataframe(
        failure_rows[["time", "detected_error", "battery", "distance", "tilt"]]
    )


# Create two columns for battery and distance graphs
col1, col2 = st.columns(2)

with col1:
    st.subheader("Battery Graph")

    fig, ax = plt.subplots()
    ax.plot(df["time"], df["battery"], marker="o")
    ax.set_xlabel("Time")
    ax.set_ylabel("Battery Voltage")
    ax.set_title("Battery Voltage Over Time")

    st.pyplot(fig)

with col2:
    st.subheader("Distance Sensor Graph")

    fig, ax = plt.subplots()
    ax.plot(df["time"], df["distance"], marker="o")
    ax.set_xlabel("Time")
    ax.set_ylabel("Distance")
    ax.set_title("Distance Sensor Value Over Time")

    st.pyplot(fig)


# Motor speed comparison graph
st.subheader("Motor Speed Graph")

fig, ax = plt.subplots()
ax.plot(df["time"], df["left_motor"], marker="o", label="Left Motor")
ax.plot(df["time"], df["right_motor"], marker="o", label="Right Motor")

ax.set_xlabel("Time")
ax.set_ylabel("Motor Speed")
ax.set_title("Left Motor vs Right Motor Speed")
ax.legend()

st.pyplot(fig)


# Robot movement replay section
st.subheader("2D Robot Movement Replay")

selected_time = st.slider(
    "Select replay time",
    int(df["time"].min()),
    int(df["time"].max()),
    int(df["time"].min())
)

# Show robot path only up to the selected time
current_data = df[df["time"] <= selected_time]

fig, ax = plt.subplots()

# Draw robot path
ax.plot(current_data["x"], current_data["y"], marker="o")

# Highlight current robot position
ax.scatter(
    current_data["x"].iloc[-1],
    current_data["y"].iloc[-1],
    s=150
)

ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")
ax.set_title(f"Robot Position at {selected_time} seconds")
ax.grid(True)

st.pyplot(fig)


# Show current robot status based on selected time
current_row = df[df["time"] == selected_time].iloc[0]

st.subheader("Current Robot Status")

st.write(f"Time: {current_row['time']} sec")
st.write(f"Battery: {current_row['battery']} V")
st.write(f"Distance: {current_row['distance']} cm")
st.write(f"Tilt: {current_row['tilt']} degree")
st.write(f"Detected Error: {current_row['detected_error']}")

if current_row["detected_error"] != "NORMAL":
    st.warning(f"Failure detected: {current_row['detected_error']}")