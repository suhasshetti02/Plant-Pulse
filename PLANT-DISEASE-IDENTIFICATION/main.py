import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Set the layout to wide to use horizontal space, which helps prevent vertical scrolling
st.set_page_config(page_title="Smart Disease Detection", layout="wide")

# Hide streamlit header and footer for a cleaner screenshot
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            /* Reduce padding at the top to save space */
            .block-container {
                padding-top: 1rem !important;
                padding-bottom: 1rem !important;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>SMART DISEASE DETECTION</h1>", unsafe_allow_html=True)

# Cache the model so it loads instantly and doesn't freeze the UI
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("trained_plant_disease_model.keras")

def model_prediction(test_image):
    model = load_model()
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    predictions = model.predict(input_arr)
    return np.argmax(predictions)

def format_class_name(raw_name):
    # Convert 'Apple___Apple_scab' -> 'Apple — Apple Scab'
    name = raw_name.replace("___", " — ")
    name = name.replace("_", " ")
    return name

# Create two columns to put everything side-by-side, saving vertical space
col1, col2 = st.columns(2)

with col1:
    test_image = st.file_uploader("Upload an Image:", type=['jpg', 'jpeg', 'png'])
    
    if test_image is None:
        # Only show the large reference image if no file is uploaded yet
        img = Image.open("Diseases.png")
        st.image(img, use_container_width=True)
    else:
        # Show the uploaded image with a restricted width so it doesn't push content down
        st.image(test_image, use_container_width=True)

with col2:
    if test_image is not None:
        st.markdown("<br><br>", unsafe_allow_html=True) # add a little padding
        if st.button("Predict Disease", use_container_width=True):
            with st.spinner("Analyzing..."):
                result_index = model_prediction(test_image)
                class_names = [
                    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
                    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy',
                    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
                    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                    'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy',
                    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
                    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew',
                    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot',
                    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
                    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
                    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                    'Tomato___healthy'
                ]
                
                predicted_raw = class_names[result_index]
                predicted_clean = format_class_name(predicted_raw)
                
                st.markdown("---")
                if "healthy" in predicted_raw.lower():
                    st.success(f"### Diagnosis:\n## {predicted_clean}")
                else:
                    st.error(f"### Diagnosis:\n## {predicted_clean}")
                st.markdown("---")
    else:
        st.info("Upload an image on the left to begin diagnosis.")
