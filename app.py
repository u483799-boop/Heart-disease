import os, joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Heart Disease Prediction", layout="wide")
st.title("Heart Disease Prediction")
MODELS_DIR = "models"