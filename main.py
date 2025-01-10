# don't forget to add open api key in langflow and Authentication token in .env file
import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "45424276-0906-4325-b8c8-bcd9d9b238ac" # add from langflow 
FLOW_ID = "c369e213-92ff-48c3-8487-972dbcd7f36f"
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = FLOW_ID


def run_flow(message: str,) -> dict:
    
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
    st.title("Social Media Analysis ")
    st.header("Model use is openai  ")
   

    message = st.text_area("Message", placeholder="Ask something...")

    if st.button("Analysis"):
        if not message.strip():
            st.error("Please enter a message")
            return

        try:
            with st.spinner("Running flow..."):
                response = run_flow(message)

            # response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e))

if _name_ == "_main_":
    main()
