import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import requests
from googletrans import Translator
import google.generativeai as genai
import os

df = pd.read_csv('Crop_recommendation.csv')
features = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
target = df['label']
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)
random_forest_model = RandomForestClassifier(n_estimators=20, random_state=5)
random_forest_model.fit(X_train, y_train)


translator = Translator()

def translate_text(text, target_language):
    try:
        translated = translator.translate(text, dest=target_language).text
        return translated
    except Exception as e:
        return f"Translation failed: {str(e)}"

def get_gemini_guidance(crop_name):
    api_key = os.environ.get("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    try:
        response = model.generate_content(f"Provide guidance for growing {crop_name} effectively")
        return response.text
    except Exception as e:
        return f"Could not fetch guidance. Ensure your API key is correct. Error: {e}"

def predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall):
    
    input_data = pd.DataFrame([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]],
                              columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
    prediction = random_forest_model.predict(input_data)
    return prediction


def get_newsapi_news(crop_name):
    newsapi_key = os.environ.get("NEWS_API_KEY", "YOUR_NEWSAPI_KEY")
    url = f"https://newsapi.org/v2/everything?q={crop_name} agriculture&language=en&pageSize=10&sortBy=relevancy"
    headers = {"X-Api-Key": newsapi_key}

    response = requests.get(url, headers=headers)
    
    
    print(f"Status Code: {response.status_code}")
    if response.status_code != 200:
        print(f"Error Message: {response.text}")
    
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        crop_news = [
            (article['title'], article['url'])
            for article in articles if crop_name.lower() in article['title'].lower() or crop_name.lower() in article['description'].lower()
        ]
        if crop_news:
            return crop_news
        else:
            india_agriculture_url = f"https://newsapi.org/v2/everything?q=agriculture India&language=en&pageSize=10&sortBy=relevancy"
            india_response = requests.get(india_agriculture_url, headers=headers)
            
            if india_response.status_code == 200:
                india_articles = india_response.json().get('articles', [])
                india_agriculture_news = [
                    (article['title'], article['url'])
                    for article in india_articles if 'agriculture' in article['title'].lower()
                ]
                if india_agriculture_news:
                    return india_agriculture_news
                else:
                    return [("No relevant agricultural news found in India.", "")]
            else:
                return [("Failed to fetch news for India.", "")]
    else:
        return [("Failed to fetch news for the crop.", "")]



def main():
    st.set_page_config(layout="wide")  

    st.sidebar.title("Language Selection")
    language_options = {
        'English': 'en',
        'Kannada': 'kn',
        'Hindi': 'hi',
        'Telugu': 'te',
        'Tamil': 'ta'
    }
    selected_language = st.sidebar.selectbox("Select Language for Page", options=list(language_options.keys()))
    target_language = language_options[selected_language]

    
    st.markdown(f"<h1 style='text-align: center;'>SMART CROP RECOMMENDATIONS</h1>", unsafe_allow_html=True)

    
    nitrogen = st.number_input("Nitrogen", min_value=0.0, max_value=140.0, value=0.0, step=0.1)
    phosphorus = st.number_input("Phosphorus", min_value=0.0, max_value=145.0, value=0.0, step=0.1)
    potassium = st.number_input("Potassium", min_value=0.0, max_value=205.0, value=0.0, step=0.1)
    temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=51.0, value=0.0, step=0.1)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, value=0.0, step=0.1)
    rainfall = st.number_input("Rainfall (cm)", min_value=0.0, max_value=500.0, value=0.0, step=0.1)

    if st.button("Predict"):
        inputs = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
        if not inputs.any() or np.isnan(inputs).any() or (inputs == 0).all():
            st.error("Please fill in all input fields with valid values before predicting.")
        else:
            prediction = predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)
            st.success(f"The recommended crop is: {prediction[0]}")
            crop_name = prediction[0]
            
            
            guidance = get_gemini_guidance(crop_name)
            st.info(f"Guidance for {crop_name}: {guidance}")

            
            st.subheader("Crop-Related News")
            news = get_newsapi_news(crop_name)
            if news:
                for title, url in news:
                    st.write(f"[{title}]({url})")
            else:
                st.write("No news available for this crop.")

if __name__ == '__main__':
    main()
