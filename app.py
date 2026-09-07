import streamlit as st
import pandas as pd
import joblib

model = joblib.load('LogisticRegression.pkl')
model = joblib.load('scaler.pkl')
model = joblib.load('LogisticRegression.pkl')