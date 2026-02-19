import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# ---------------------------------------------------
# Load Environment Variables
# ---------------------------------------------------
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# ---------------------------------------------------
# Page Setup
# ---------------------------------------------------
st.set_page_config(page_title="Advanced Nutrition Science", layout="wide")
st.title("🥗 Advanced Nutrition Science through Gemini AI")
st.markdown("AI-powered nutritional analysis using Google Gemini API")

# ---------------------------------------------------
# Check API Key
# ---------------------------------------------------
if not api_key:
    st.error("❌ API Key not found. Please add it in .env file.")
    st.stop()

# Set environment variable for LangChain
os.environ["GOOGLE_API_KEY"] = api_key

# ---------------------------------------------------
# Validate API & Fetch Models
# ---------------------------------------------------
try:
    client = genai.Client(api_key=api_key)
    model_objects = list(client.models.list())
    model_names = [m.name for m in model_objects if "gemini" in m.name.lower()]
except Exception:
    st.error("❌ Invalid API Key in .env file.")
    st.stop()

# ---------------------------------------------------
# Model Selection
# ---------------------------------------------------
selected_model = st.sidebar.selectbox(
    "Select Gemini Model",
    model_names
)

st.sidebar.success("✅ Model Loaded Successfully")

# ---------------------------------------------------
# Initialize Model
# ---------------------------------------------------
llm = ChatGoogleGenerativeAI(
    model=selected_model,
    temperature=0.3
)

# ---------------------------------------------------
# Prompt Template
# ---------------------------------------------------
prompt = PromptTemplate(
    input_variables=["food_item"],
    template="""
    You are a certified professional nutritionist.

    Provide detailed nutritional analysis for:

    Food Item: {food_item}

    Include:
    - Calories
    - Protein
    - Carbohydrates
    - Fats
    - Vitamins
    - Minerals
    - Health Benefits

    Format clearly in bullet points.
    """
)

chain = prompt | llm

# ---------------------------------------------------
# User Input
# ---------------------------------------------------
st.header("🍎 Enter Food Items")

food_items = st.text_area(
    "Enter food items (comma separated)",
    placeholder="Rice, Milk, Apple"
)

if st.button("Generate Nutrition Report"):
    if not food_items.strip():
        st.warning("Please enter food items.")
    else:
        items = [item.strip() for item in food_items.split(",") if item.strip()]

        for item in items:
            with st.spinner(f"Analyzing {item}..."):
                response = chain.invoke({"food_item": item})

            st.subheader(f"📊 {item}")
            st.write(response.content)
            st.markdown("---")