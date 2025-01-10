import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "45424276-0906-4325-b8c8-bcd9d9b238ac"  # Add from Langflow 
FLOW_ID = "c369e213-92ff-48c3-8487-972dbcd7f36f"
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = FLOW_ID

def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    # Page Layout and Styling
    st.set_page_config(page_title="Social Media Analysis", layout="wide")
    
    # Custom Styling for UI
    st.markdown(
        """
        <style>
        body {
            background-color: #f3e5f5;
        }
        .stButton>button {
            background-color: #673ab7;
            color: white;
            border-radius: 10px;
            padding: 8px 15px;
        }
        .stTextArea>div>textarea {
            border: 2px solid #512da8;
            border-radius: 8px;
        }
        .stMarkdown {
            color: #311b92;
            font-weight: bold;
        }
        .stSpinner>div>div>div>div {
            color: #4527a0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.title("📊 Social Analytics")
    st.header("🔍 Model in Use: LLama-70b")

    # Input Text Area
    message = st.text_area("📝 Enter Your Message:", placeholder="Ask something insightful...")

    # Button to Trigger Analysis
    if st.button("🚀 Run Analysis"):
        if not message.strip():
            st.error("⚠️ Please enter a message")
            return

        try:
            with st.spinner("Analyzing message... please wait ⏳"):
                response = run_flow(message)

            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(f"### 🟢 **Analysis Result:**\n{response}")
        
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
