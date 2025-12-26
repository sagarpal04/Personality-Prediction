# 🧠 Personality Prediction using Logistic Regression

This project predicts a person’s personality type — **Introvert, Ambivert, or Extrovert** — using Logistic Regression based on psychological, social, and behavioral traits. The model is trained on a synthetic dataset and evaluated using standard machine learning metrics.

<p align="center">
  <img src="https://github.com/user-attachments/assets/5b30b0e8-532d-488b-a2d7-8dab8e6849f3" width="800" />
</p>

---

## 🌐 Live Demo
👉 **Try the app here:**  
🔗 https://ai-personality-test.streamlit.app/

---

## 📁 Dataset
- **File name:** `personality_synthetic_dataset.csv`
- **Target column:** `personality_type`
- **Classes:**
  - Introvert
  - Ambivert
  - Extrovert

**Features include:**
- Social energy
- Talkativeness
- Empathy
- Creativity
- Emotional stability
- Stress handling
- Other behavioral traits

---

## 🛠️ Libraries Used
- `numpy`
- `pandas`
- `seaborn`
- `matplotlib`
- `scikit-learn`
- `scipy`
- `pickle`

---

## 🔍 Exploratory Data Analysis (EDA)
1. **Data Cleaning:** Checked missing and duplicate values  
2. **Structural Inspection:** Column types and shape  
3. **Visualizations:**
   - Personality type distribution (Count Plot)
   - Social energy distribution (Histogram + KDE)
   - Feature relationships (Pair Plot)
4. **Statistical Analysis:** ANOVA (F-test) for feature significance  

---

## 🧪 Feature Engineering & Preprocessing
- Encoded `personality_type` using `LabelEncoder`
- Selected features based on ANOVA results
- Scaled features using `StandardScaler`

---

## ✂️ Train-Test Split
- Training: **80%**
- Testing: **20%**
- Random State: **42**

---

## 🤖 Model Information
- **Algorithm:** Logistic Regression  
- **Library:** `sklearn.linear_model`

---

## 📊 Model Evaluation
- Accuracy Score
- Confusion Matrix (Blue colormap)
- Classification Report (Precision, Recall, F1-score)

---

## 💾 Model Saving
Saved using `pickle`:
- `personality_model.pkl`
- `scaler.pkl`

---

## 🚀 How to Run the Project

```bash
git clone https://github.com/sagarpal04/Personality-Prediction.git
cd Personality-Prediction
pip install -r requirements.txt
streamlit run app.py
