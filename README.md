# ❤️ Heart Stroke Prediction App

<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,2,5,30&height=200&section=header&text=Heart%20Stroke%20Prediction&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Predict%20Heart%20Disease%20Risk%20with%20Machine%20Learning&descAlignY=55&descSize=18)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Accuracy](https://img.shields.io/badge/Accuracy-87.50%25-success?style=for-the-badge)](#-model-performance)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&pause=1000&color=E63946&center=true&vCenter=true&width=600&lines=Predict+Heart+Disease+Risk+Instantly!;Powered+by+Logistic+Regression;87.5%25+Accuracy+%7C+0.89+F1+Score;Simple.+Fast.+Interactive." alt="Typing SVG" />

</div>

---

## 🩺 About The Project

<img align="right" width="380" src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif">

An interactive **Streamlit web app** that predicts the risk of heart disease based on a patient's medical attributes — age, chest pain type, cholesterol, resting ECG, and more.

Five classification models were trained and benchmarked on the dataset. **Logistic Regression** came out on top and was selected as the production model, delivering instant, easy-to-understand risk predictions right in your browser.

- 🎯 Real-time predictions
- 🏆 Best-performing model selected after benchmarking 5 algorithms
- 📊 Trained on the UCI Heart Failure dataset
- ⚡ Lightweight and fast
- 🖥️ Clean, slider-based UI

<br clear="right"/>

---

## ✨ Demo

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/216122065-2f028bae-25d3-4f79-83c1-2bf9f24d7729.gif" width="500">
</div>

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/subhajit404/ML-Heart-Disease.git
cd heart-stroke-prediction

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open automatically at `http://localhost:8501` 🎉

---

## 🏆 Model Performance

Five models were trained and evaluated. **Logistic Regression** achieved the highest accuracy and F1 score, and was selected as the final model powering this app.

<div align="center">

| Rank | Model | Accuracy | F1 Score | Status |
|:---:|---|:---:|:---:|:---:|
| 🥇 | **Logistic Regression** | **87.50%** | **0.8900** | ✅ **Selected** |
| 🥈 | SVM | 86.41% | 0.8804 | — |
| 🥉 | KNN | 84.78% | 0.8654 | — |
| 4 | Naive Bayes | 83.15% | 0.8458 | — |
| 5 | Decision Tree | 80.43% | 0.8182 | — |

</div>

### 📈 Accuracy Comparison

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'xyChart': {'plotColorPalette': '#E63946'}}}}%%
xychart-beta
    title "Model Accuracy Comparison (%)"
    x-axis ["LogisticRegression", "SVM", "KNN", "NaiveBayes", "DecisionTree"]
    y-axis "Accuracy (%)" 75 --> 90
    bar [87.50, 86.41, 84.78, 83.15, 80.43]
```

> ✅ **Logistic Regression selected** — highest accuracy (**87.50%**) and highest F1 score (**0.89**) among all tested models.

---

## 🧠 How It Works

<div align="center">

```mermaid
graph LR
    A[👤 User Input] --> B[📋 Build Feature Vector]
    B --> C[🔧 Fill Missing Columns]
    C --> D[⚖️ Scale with StandardScaler]
    D --> E[🤖 Logistic Regression<br/>87.5% Accuracy]
    E --> F{Prediction}
    F -->|1| G[⚠️ High Risk]
    F -->|0| H[✅ Low Risk]
```

</div>

---

## 📥 Input Parameters

| Feature | Description | Type |
|---|---|---|
| `Age` | Patient's age | Slider (18–100) |
| `Sex` | M / F | Dropdown |
| `ChestPainType` | ATA, NAP, TA, ASY | Dropdown |
| `RestingBP` | Resting blood pressure (mm Hg) | Number (80–200) |
| `Cholesterol` | Serum cholesterol (mg/dL) | Number (100–600) |
| `FastingBS` | Fasting blood sugar > 120 mg/dL | 0 / 1 |
| `RestingECG` | Normal, ST, LVH | Dropdown |
| `MaxHR` | Maximum heart rate achieved | Slider (60–220) |
| `ExerciseAngina` | Exercise-induced angina (Y/N) | Dropdown |
| `Oldpeak` | ST depression induced by exercise | Slider (0.0–6.0) |
| `ST_Slope` | Up, Flat, Down | Dropdown |

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

</div>

---

## 📁 Project Structure

```
heart-stroke-prediction/
├── app.py                   # Streamlit application
├── main.ipynb                # Model training & benchmarking notebook
├── LogisticRegression.pkl    # Trained model (best performer — 87.5% accuracy)
├── scaler.pkl                 # Fitted StandardScaler
├── columns.pkl                # Expected feature columns
├── heart.csv                  # Training dataset
├── requirements.txt           # Dependencies
└── README.md
```

---

## ⚠️ Disclaimer

<img align="left" width="60" src="https://user-images.githubusercontent.com/74038190/216122041-518ac897-8d92-4c6b-9b3f-ca01dcaf38ee.png">

Try this Tool Now and give me suggestion to improve this model

<br clear="left"/>

---

<div align="center">

### 💖 Show some love by starring this repo!

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,2,5,30&height=100&section=footer)

</div>
