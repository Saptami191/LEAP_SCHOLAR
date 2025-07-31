# 📊 Leap Brand Pulse – Sentiment Dashboard

This project is a lightweight and interactive sentiment monitoring dashboard designed for LeapScholar’s marketing team. It helps you quickly understand how the brand is being talked about online by analyzing user-generated mentions (e.g., from Twitter, Reddit, etc.).

---

## 🚀 Purpose

Leap’s Head of Marketing is busy and needs to:
- Spot key conversations about the brand without manual searching
- Understand general sentiment at a glance
- Identify positive/negative spikes to take action quickly

This dashboard solves that by offering an intuitive, visual summary of online chatter.

---

## 🧠 Features

- ✅ **Sentiment Analysis** (positive / neutral / negative)
- ☁️ **Word Cloud** for quick visual insights
- 🧵 **Top Mentioned Posts** by sentiment
- 📈 **Interactive Pie Chart** for sentiment distribution
- 📄 **Sample CSV support** for testing (platform-ready)

---

## 🖼️ Project Overview (PDF Preview)

![Project Overview](./assets/leap_overview.png)

> 🔗 [Download full PDF](./leap.pdf)

---

## 📁 Folder Structure

leap_brand_monitor/
│
├── dashboard.py
├── requirements.txt
├── data/
│ └── sample_mentions.csv
├── assets/
│ └── leap_overview.png
│
└── README.md

---

## 🛠️ How to Run the Dashboard

1. **Clone or download this repo**, then navigate into it:
   ```bash
   cd leap_brand_monitor



python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux


pip install -r requirements.txt


streamlit run dashboard.py
