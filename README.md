# ✈️ Smart Trip Calculator & AI Travel Budget Planner

An automated, AI-driven full-stack travel budgeting prototype built entirely in the cloud using **Python**, **Streamlit**, and the **Google Gemini API**. This system prevents vacation budget overruns by calculating strict budget caps and building an optimized daily travel itinerary.

## 🚀 Core Features
- **Dynamic Budget Allocation Model:** Automatically slices a total budget threshold into itemized categorical expenses (Lodging, Food, Transport, and Activities) based on selected travel matrices (Backpacker, Balanced, Luxury).
- **Interactive Budget Visualization:** Renders real-time dynamic donut pie charts using `Plotly Express`.
- **AI-Powered Itinerary Automation:** Curates day-by-day sightseeing, transit configurations, and micro-budgeting metrics.

## 🛠️ Tech Stack & Dependencies
- **Frontend/UI:** Streamlit (Python Web App Framework)
- **AI Engine:** Google Gemini SDK (`gemini-2.0-flash`)
- **Data Visualization:** Plotly Express
- **Cloud Infrastructure:** GitHub Codespaces & Streamlit Community Cloud

## 🔧 Step-by-Step Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com
   cd smart-trip-planner
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Local Development Server:**
   ```bash
   streamlit run app.py
   ```

4. **API Key Integration:**
   Obtain a free API Key from Google AI Studio, paste it into the sidebar terminal interface, and generate your customized tracking timeline.
