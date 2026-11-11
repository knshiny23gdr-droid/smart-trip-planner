import streamlit as st
import plotly.express as px
import requests

# --- PAGE SETUP ---
st.set_page_config(page_title="AI Smart Trip Calculator", page_icon="✈️", layout="wide")
st.title("✈️ Smart Trip Calculator & AI Travel Budget Planner")
st.write("Plan your next adventure without breaking the bank!")

# --- API CONFIGURATION ---
api_key = st.sidebar.text_input("Enter your Gemini API Key:", type="password")

# --- USER INPUT FORM ---
with st.form("trip_form"):
    col1, col2 = st.columns(2)
    with col1:
        destination = st.text_input("Where are you going?", placeholder="e.g., Kyoto, Japan", value="Kyoto, Japan")
        days = st.number_input("Number of Days", min_value=1, max_value=30, value=7)
    with col2:
        total_budget = st.number_input("Total Budget (INR/USD)", min_value=100, value=2500)
        travel_style = st.selectbox("Travel Style", ["Backpacker (Budget)", "Balanced (Mid-range)", "Luxury"])
        
    submit_button = st.form_submit_button("Generate Optimized Budget Itinerary")

# --- DATA GENERATION AND PROCESSING ---
if submit_button:
    if not api_key:
        st.error("Please enter your API Key in the sidebar to generate the plan.")
    else:
        with st.spinner("AI is calculating options and building your optimal itinerary..."):
            try:
                # Engineering the prompt for the AI
                prompt = f"""
                You are an expert AI Travel Planner and Financial Analyst.
                Create a strict budget allocation and day-by-day itinerary for a trip to {destination} for {days} days.
                The total budget is {total_budget}. The travel style is {travel_style}.
                Provide clear day-by-day travel details and estimated daily costs.
                """
                
                # Direct HTTP post call bypassing the heavy SDK entirely
                url = f"https://googleapis.com{api_key}"
                headers = {"Content-Type": "application/json"}
                payload = {
                    "contents": [{
                        "parts": [{"text": prompt}]
                    }]
                }
                
                res = requests.post(url, headers=headers, json=payload)
                
                if res.status_code == 200:
                    itinerary_text = res.json()['candidates'][0]['content']['parts'][0]['text']
                    
                    st.success("🎉 Your Budget-Optimized Plan is Ready!")
                    
                    # --- GRAPHICAL CHART ---
                    st.header("📊 Interactive Expense Distribution Model")
                    
                    if travel_style == "Backpacker (Budget)":
                        labels = ['Hostels/Stays', 'Local Food/Shacks', 'Public Transport', 'Activities', 'Emergency Fund']
                        values = [40, 25, 15, 10, 10]
                    elif travel_style == "Balanced (Mid-range)":
                        labels = ['3-Star Stays', 'Cafes & Dining', 'Cabs/Trains', 'Tours & Tickets', 'Shopping/Misc']
                        values = [35, 25, 15, 15, 10]
                    else:  # Luxury
                        labels = ['Resorts/Ryokans', 'Fine Dining', 'Private Transfers', 'Exclusive Tours', 'Premium Experience']
                        values = [45, 25, 15, 10, 5]
                    
                    amounts = [(v / 100) * total_budget for v in values]
                    
                    fig = px.pie(names=labels, values=amounts, title="Budget Slices", hole=0.4)
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # --- TIMELINE SUMMARY ---
                    st.header("🗺️ Day-Wise AI Itinerary Timeline")
                    st.markdown(itinerary_text)
                else:
                    st.error(f"API Error Connection: {res.status_code}. Make sure your key is valid.")
                
            except Exception as e:
                st.error(f"System processing update required. Details: {e}")
