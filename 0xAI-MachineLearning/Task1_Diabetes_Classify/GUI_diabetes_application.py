# GUI_diabetes_application.py
import tkinter as tk
from tkinter import messagebox
import joblib
import os
import numpy as np

# --- Load the model ---
# Model is inside the "Decision tree" subfolder
MODEL_FOLDER = os.path.join(os.path.dirname(__file__), "Decision tree")
MODEL_FILENAME = "DecisionTree_model.pkl"
MODEL_PATH = os.path.join(MODEL_FOLDER, MODEL_FILENAME)

# Check if model exists
if not os.path.exists(MODEL_PATH):
    messagebox.showerror("Error", f"Model file not found at:\n{MODEL_PATH}")
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

# Load the trained model
model = joblib.load(MODEL_PATH)

# --- Define features expected by your model ---
FEATURES = [
    "age",
    "hypertension",
    "heart_disease",
    "bmi",
    "HbA1c_level",
    "blood_glucose_level",
    "gender",
    "smoking_status",
    "physical_activity",
    "cholesterol",
    "triglycerides",
    "insulin_level",
    "family_history",
    "medication",
    "diet",
    "alcohol_use"
]

# --- Create GUI window ---
root = tk.Tk()
root.title("Diabetes Classifier")
root.geometry("400x800")
root.resizable(False, False)

# Dictionary to store input entries
entries = {}

# Create labels and entry boxes for each feature
for i, feat in enumerate(FEATURES):
    lbl = tk.Label(root, text=f"{feat.replace('_', ' ').capitalize()}:")
    lbl.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    ent = tk.Entry(root)
    ent.grid(row=i, column=1, padx=10, pady=5)
    entries[feat] = ent

# --- Prediction function ---
def predict():
    try:
        # Collect values from entries
        values = []
        for feat in FEATURES:
            val = entries[feat].get().strip()
            if val == "":
                messagebox.showerror("Error", f"Please enter {feat.replace('_', ' ')}")
                return
            values.append(float(val))

        # Reshape for prediction
        X_input = np.array(values).reshape(1, -1)

        # Predict using the loaded model
        pred = model.predict(X_input)[0]
        result = "Diabetic" if pred == 1 else "Not Diabetic"

        messagebox.showinfo("Prediction Result", f"Prediction: {result}")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# --- Predict button ---
btn = tk.Button(root, text="Predict", command=predict, bg="blue", fg="white")
btn.grid(row=len(FEATURES), column=0, columnspan=2, pady=20)

# --- Run the GUI ---
root.mainloop()
