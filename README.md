# 🥗 Advanced Nutrition Science through Gemini AI

An AI-powered Nutrition Analysis Web Application built using Streamlit, Google Gemini API, and LangChain.  
This application provides detailed nutritional insights, calorie analysis, health benefits, and dietary recommendations for various food items using Generative AI.

---

## 🚀 Project Overview

The system allows users to:

- 🔍 Search any food item  
- 📊 Get complete nutritional breakdown  
- 🧠 View AI-powered health insights  
- 🍽️ Receive diet recommendations  
- 🤖 See the AI model used for response generation  

The application uses Gemini Pro (Google Generative AI) for intelligent food analysis.

---

## 🛠️ Technologies Used

- Frontend: Streamlit  
- LLM API: Google Gemini  
- Model Used: gemini-pro  
- Framework Support: LangChain  
- Programming Language: Python 3.9+

---

## 📂 Project Structure

📦 Advanced-Nutrition-Science  
 ┣ 📜 app.py  
 ┣ 📜 requirements.txt  
 ┣ 📜 README.md  
 ┗ 📂 assets (optional)  

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/Advanced-Nutrition-Science.git  
cd Advanced-Nutrition-Science  

### 2️⃣ Install Dependencies

pip install -r requirements.txt  

### 3️⃣ Set Up Gemini API Key

- Get API key from Google AI Studio  
- Run the app  
- Enter API key in the sidebar (hidden input field)  

---

## ▶️ Run the Application

streamlit run app.py  

The app will open in your browser at:  
http://localhost:8501  

---

## 🧠 How It Works

1. User enters a food item (e.g., "Apple", "Chicken Biryani").  
2. The input is sent to Gemini Pro.  
3. Gemini generates:  
   - Macronutrients  
   - Micronutrients  
   - Calories  
   - Health Benefits  
   - Diet Suitability  
4. The response is formatted and displayed using Streamlit.  

---

## 📊 Features

- ✅ Real-time AI nutrition analysis  
- ✅ Displays model used  
- ✅ Secure API key (hidden in sidebar)  
- ✅ Clean interactive UI  
- ✅ Works for any food item  

---

## 🔐 API Key Security

The API key:
- Is entered manually  
- Is hidden using type="password"  
- Is not stored in the source code  

---

## 📦 Requirements

streamlit  
google-generativeai  
langchain  
python-dotenv  

---

## 🖥️ Sample Output

Example Input:  
Banana  

Example Output:  
- Calories: 89 kcal  
- Carbohydrates: 23g  
- Protein: 1.1g  
- Fat: 0.3g  
- Rich in Potassium  
- Good for digestion  
- Suitable for weight gain diet  

---

## 🔮 Future Enhancements

- 📷 Image-based food detection  
- 🏋️ Personalized diet plans  
- 📈 Nutrition comparison charts  
- 📱 Mobile optimization  

---

## 📜 License

This project is for educational and research purposes.
