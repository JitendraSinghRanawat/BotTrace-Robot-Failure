# BotTrace: Robot Failure Replay System

BotTrace is a robot black-box style debugging system. It records robot movement data, detects failure points, and replays robot behavior using a Python dashboard.

---

## Problem

Small robots can fail due to low battery, obstacle detection, motor imbalance, wrong sensor readings, or tilt issues.

After failure, it is difficult to understand what exactly happened during the movement.

---

## Solution

BotTrace stores robot data in CSV format and analyzes it using Python.  
It detects robot failure conditions and shows them on a Streamlit dashboard with graphs and 2D movement replay.

---

## Features

- Robot log data analysis
- Battery monitoring
- Distance sensor monitoring
- Motor speed comparison
- Motor imbalance detection
- Obstacle stop detection
- Robot tilt warning
- Failure summary table
- 2D robot movement replay
- Streamlit-based dashboard
- CSV file support

---

## Tech Stack

- Python
- Pandas
- Matplotlib
- Streamlit
- CSV Dataset

---

## Project Structure

```text
BotTrace-Robot-Failure-Replay-System/
├── data/
│   ├── sample_robot_log.csv
│   └── analyzed_robot_log.csv
├── src/
│   └── failure_detector.py
├── dashboard/
│   └── replay_dashboard.py
├── images/
│   ├── dashboard_home.png
│   ├── failure_summary.png
│   ├── graphs.png
│   ├── motor_speed_graph.png
│   ├── robot_replay.png
│   └── current_status.png
├── README.md
└── requirements.txt
'''

## Full project flow

CSV robot data
        ↓
failure_detector.py reads data
        ↓
Python checks battery, motor, distance, tilt
        ↓
Failure type is detected
        ↓
Dashboard displays graphs and replay
        ↓
User understands why robot failed