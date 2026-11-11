# Plant Pulse — Smart Farming Assistant

Plant Pulse is a collection of connected, locally run agriculture tools: a static web portal, a crop-recommendation Streamlit application, and a plant-disease identification Streamlit application.

> **Project status:** Academic prototype. The portal links to two separate Streamlit services; it is not a single unified web application or a deployed production API.

## Features present in the repository

- **Crop recommendation:** a scikit-learn Random Forest classifier trained from `Crop_recommendation.csv` using seven input features: N, P, K, temperature, humidity, pH, and rainfall.
- **Plant disease classification:** a TensorFlow/Keras model loaded from `trained_plant_disease_model.keras`; the Streamlit interface maps model output to 38 plant/disease labels.
- **Crop guidance and news:** optional Gemini-generated growing guidance and NewsAPI article lookup in the crop-recommendation app.
- **Language selection / translation helpers:** translation support is present in the crop-recommendation code.
- **Web portal:** static HTML, CSS, and JavaScript pages link to the two Streamlit applications and include guide, explore, chatbot, news, and related sections.

## Technology stack

| Component | Implementation |
|---|---|
| Crop recommendation | Python, Streamlit, pandas, scikit-learn RandomForestClassifier |
| Disease identification | Python, Streamlit, TensorFlow/Keras, NumPy, Pillow |
| Portal | HTML, CSS, JavaScript, Bootstrap |
| External integrations | Gemini API, NewsAPI, Google Translate helper |

## Repository structure

- `CROP-RECOMMENDATION/` — crop recommendation Streamlit app and CSV dataset.
- `PLANT-DISEASE-IDENTIFICATION/` — disease prediction Streamlit app, model artifact, and training history.
- `PLANTPULSE-web-app/` — static web portal and browser-side feature scripts.
- `README.md` — project overview.
- `PROJECT_INTERVIEW_GUIDE.md` — project/interview notes.

## Run locally

Install Python dependencies separately for each Streamlit application (check the requirements file in the corresponding directory).

Crop recommendation:

```bash
cd CROP-RECOMMENDATION
pip install -r requirements.txt
streamlit run app.py
```

Plant disease identification:

```bash
cd PLANT-DISEASE-IDENTIFICATION
pip install -r requirements.txt
streamlit run main.py
```

Open `PLANTPULSE-web-app/index.html` in a browser. The portal's links must point to the actual local addresses/ports where the Streamlit apps are running.

## Important implementation notes

- The crop classifier is fitted when the Python module loads; the code does not load a pre-trained serialized Random Forest artifact.
- The disease app expects `trained_plant_disease_model.keras` and `Diseases.png` relative to its working directory.
- The disease inference code resizes uploaded images to 128×128. The class-name list is embedded in the application.
- The web portal includes a duplicate/older crop app under `CROP-RECOMMENDATION/CROP-RECOMMENDATION/webapp.py`. It is not the documented main entry point.
- Training history is stored in `training_hist.json`; values in this file are historical training metrics, not independently reproduced benchmark results.
- There is no shared application database or unified backend connecting the three parts.

## Security notice

The repository has contained hard-coded third-party API credentials in an older/duplicate application file. Treat any credential committed to GitHub as exposed: revoke or rotate it with the provider, move replacement credentials into environment variables, and remove the old values from Git history. Never put API keys in browser-side JavaScript or committed source files.

## Limitations and future work

- Consolidate the portal and model applications behind a documented API.
- Move external API calls and credentials to a secure server-side service.
- Save and load the crop model rather than fitting it on every application start.
- Add automated tests and a repeatable evaluation protocol for both models.
- Validate image upload limits, model input assumptions, and error handling.

## License

See repository licensing and third-party model/dataset terms before redistribution.
