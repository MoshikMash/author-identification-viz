# Author Identification Visualization App

Streamlit web app for viewing author identification visualizations.

## Files Included

- `visualization_app.py` - Main Streamlit application
- `requirements_app.txt` - Python dependencies
- `.streamlit/config.toml` - Streamlit configuration
- `inference/output/` - Book similarity heatmaps
- `evaluation/output/` - Author evaluation visualizations

## Local Setup

```bash
pip install -r requirements_app.txt
streamlit run visualization_app.py
```

## Deploy to Streamlit Cloud

1. Push this repository to GitHub
2. Go to https://share.streamlit.io/
3. Sign in with GitHub
4. Click "New app"
5. Select this repository
6. Main file: `visualization_app.py`
7. Click "Deploy!"

The app will be available at: `https://your-app-name.streamlit.app`

## Requirements

- Python 3.9+
- Streamlit 1.48.0+

