# 🧠 Personality Prediction using Logistic Regression

This project predicts a person’s personality type — **Introvert, Ambivert, or Extrovert** — using Logistic Regression based on psychological, social, and behavioral traits. The model is trained on a synthetic dataset and evaluated using standard machine learning metrics.

<p align="center">
  <img src="https://github.com/user-attachments/assets/5b30b0e8-532d-488b-a2d7-8dab8e6849f3" width="800" />
</p>

---

## 📁 Dataset
* **File name:** `personality_synthetic_dataset.csv`
* **Target column:** `personality_type`
* **Classes:** * Introvert
  * Ambivert
  * Extrovert

The dataset contains features such as:
* Social energy
* Talkativeness
* Empathy
* Creativity
* Emotional stability
* Stress handling
* Other behavioral traits

---

## 🛠️ Libraries Used
The following Python libraries are required to run this project:
* `numpy`
* `pandas`
* `seaborn`
* `matplotlib`
* `scikit-learn`
* `scipy`
* `pickle`

---

## 🔍 Exploratory Data Analysis (EDA)
The following steps were performed to understand the data:
1. **Data Cleaning:** Checked for missing values and duplicate records.
2. **Structural Inspection:** Inspected column types and data structure.
3. **Visualizations:**
    * **Personality Type Distribution:** Count Plot.
    * **Social Energy Distribution:** Histogram + KDE.
    * **Feature Relationships:** Pair Plot.
4. **Statistical Analysis:** Used **ANOVA (F-test)** to identify statistically significant features across different personality groups.

---

## 🧪 Feature Engineering & Preprocessing
* **Encoding:** Converted `personality_type` into numeric labels using `LabelEncoder`.
* **Feature Selection:** Dropped less significant features based on ANOVA results.
* **Scaling:** Normalized features using `StandardScaler` to improve model convergence.

---

## ✂️ Train-Test Split
The dataset was split to validate the model's performance:
* **Training Set:** 80%
* **Testing Set:** 20%
* **Random State:** 42

---

## 🤖 Model Information
* **Algorithm:** Logistic Regression
* **Implementation:** `sklearn.linear_model`


---

## 📊 Model Evaluation
The model was evaluated using the following metrics:
* **Accuracy Score**
* **Confusion Matrix** (Visualized using a blue color map)
* **Classification Report** (Precision, Recall, F1-score)



---

## 💾 Model Saving
The trained model and scaler were exported using `pickle` for easy deployment:
* `personality_model.pkl`
* `scaler.pkl`

---

## 🚀 How to Run the Project

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sagarpal04/Personality-Prediction.git
