# -*- coding: utf-8 -*-
"""tamilmani phase2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cxLxlMt79OunSArNtaaQH1uJpP3KYC6G
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
import io

# Get the actual filename from the uploaded dictionary keys
filename = list(uploaded.keys())[0]
import pandas as pd
import io

# Get the actual filename from the uploaded dictionary keys
filename = list(uploaded.keys())[0]

# Read the file using the correct filename
df = pd.read_csv(io.BytesIO(uploaded[filename]), sep=';')

import pandas as pd

# Update the file path to the correct location of your CSV file
file_path = 'global_traffic_accidents.csv'  # Or the actual path if different

# Load the dataset using the updated file path
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: File not found at '{file_path}'. Please check the file path and ensure the file exists.")
    # Handle the error, e.g., exit the script or use a default dataset
    # ...

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset, ensure file_path is correct for your environment
# If using Google Colab with uploaded files:
# try:
#     from google.colab import drive
#     drive.mount('/content/drive')
#     file_path = '/content/drive/My Drive/global_traffic_accidents.csv'  # Update to your file's location in Google Drive
#     df = pd.read_csv(file_path)
# except ModuleNotFoundError:  # If not in Google Colab
#     file_path = 'global_traffic_accidents.csv' # Replace with the actual path if different
#     df = pd.read_csv(file_path)
# except FileNotFoundError:
#     print(f"Error: File not found at '{file_path}'. Please check the file path and ensure the file exists.")
#     # Handle the error, e.g., exit the script or use a default dataset
#     # ...

# OR
# If the file was uploaded, use this:
# import io
# filename = list(uploaded.keys())[0]
# df = pd.read_csv(io.BytesIO(uploaded[filename]), sep=';') # Adjust sep if needed


# Alternatively, if you are sure about the path, but might have a permissions issue
# try:
#     df = pd.read_csv('/mnt/data/global_traffic_accidents.csv')
# except PermissionError:
#     print("Permission denied. Make sure you have read access to the file.")
#     # Handle the error, e.g., exit or change permissions

# Assuming the file is in the same directory as the notebook (replace with actual path if needed)
file_path = 'global_traffic_accidents.csv'
df = pd.read_csv(file_path)


# Set a consistent style
sns.set(style="whitegrid")

# --- 1. Count Plot: Accidents by Weather Condition ---
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Weather Condition', order=df['Weather Condition'].value_counts().index)
plt.title('Number of Accidents by Weather Condition')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- 2. Count Plot: Accidents by Cause ---
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Cause', order=df['Cause'].value_counts().index)
plt.title('Number of Accidents by Cause')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- 3. Histogram: Casualties ---
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='Casualties', bins=10, kde=True)
plt.title('Distribution of Casualties per Accident')
plt.tight_layout()
plt.show()

# --- 4. Boxplot: Vehicles Involved ---
plt.figure(figsize=(6, 5))
sns.boxplot(data=df, y='Vehicles Involved')
plt.title('Boxplot of Vehicles Involved in Accidents')
plt.tight_layout()
plt.show()

import pandas as pd

# Assume the file is in the same directory as the notebook
# If not, replace 'global_traffic_accidents.csv' with the actual file path
file_path = 'global_traffic_accidents.csv'

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: File not found at '{file_path}'. Please make sure the file is in the correct location or specify the full path.")
    # You can add further error handling here, like exiting the script
except PermissionError:
    print(f"Error: Permission denied when trying to access '{file_path}'. Please check file permissions.")
    # Handle permission error

# --- Step 1: Show all column names ---
print("🔍 All Columns:")
print(df.columns.tolist())

# --- Step 2: Choose a target variable (example: 'Casualties') ---
# You can change this based on your analysis goal
target = 'Casualties'

# --- Step 3: Identify features (all columns except target) ---
features = df.columns[df.columns != target].tolist()

# --- Step 4: Display target and features ---
print("\n🎯 Target Variable:")
print(target)

print("\n🧾 Feature Columns:")
print(features)

import pandas as pd

# If the file is not in /mnt/data/, specify the correct path here
file_path = 'global_traffic_accidents.csv'  # Replace with the actual path if different

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: File not found at '{file_path}'. Please make sure the file is in the correct location or specify the full path.")
    # You can add further error handling here, like exiting the script
except PermissionError:
    print(f"Error: Permission denied when trying to access '{file_path}'. Please check file permissions.")
    # Handle permission error

# --- Step 1: Identify categorical columns ---
categorical_cols = df.select_dtypes(include='object').columns.tolist()
print("📋 Categorical Columns:", categorical_cols)

# --- Step 2: Apply One-Hot Encoding ---
# One-hot encode all categorical columns
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# --- Step 3: Show result ---
print("\n✅ Encoded DataFrame (first 5 rows):")
print(df_encoded.head())

print("\n🧮 New Shape:", df_encoded.shape)

import pandas as pd

# Update the file path to the actual location of your CSV file
# Make sure the file exists and you have read permissions.
file_path = 'global_traffic_accidents.csv'  # Replace with the correct file path

# Load the dataset
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: File not found at '{file_path}'. Please ensure the file exists and the path is correct.")
except PermissionError:
    print(f"Error: Permission denied when trying to access '{file_path}'. Please check file permissions.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# --- Step 1: Identify categorical columns ---
categorical_cols = df.select_dtypes(include='object').columns.tolist()
print("📋 Categorical Columns to Encode:", categorical_cols)

# --- Step 2: Apply One-Hot Encoding ---
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# --- Step 3: Show results ---
print("\n✅ Data after One-Hot Encoding (first 5 rows):")
print(df_encoded.head())

print("\n📐 New Dataset Shape:", df_encoded.shape)

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load the dataset
file_path = "global_traffic_accidents.csv"  # Update the path if needed
df = pd.read_csv(file_path)

# Select numeric columns to scale
numeric_cols = ['Latitude', 'Longitude', 'Vehicles Involved', 'Casualties']

# Initialize scalers
minmax_scaler = MinMaxScaler()
zscore_scaler = StandardScaler()

# Apply Min-Max Scaling
df_minmax = pd.DataFrame(minmax_scaler.fit_transform(df[numeric_cols]), columns=[f"{col}_minmax" for col in numeric_cols])

# Apply Z-score Standardization
df_zscore = pd.DataFrame(zscore_scaler.fit_transform(df[numeric_cols]), columns=[f"{col}_zscore" for col in numeric_cols])

# Combine the original (non-scaled) data with scaled results
df_scaled = pd.concat([df.drop(columns=numeric_cols), df_minmax, df_zscore], axis=1)

# Save the new DataFrame to CSV
output_file = "global_traffic_accidents_scaled.csv"
df_scaled.to_csv(output_file, index=False)

print(f"Scaling complete. Output saved to: {output_file}")

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split

# Load the dataset
file_path = "global_traffic_accidents.csv"  # Change path if needed
df = pd.read_csv(file_path)

# Select numeric columns for scaling
numeric_cols = ['Latitude', 'Longitude', 'Vehicles Involved', 'Casualties']

# Initialize scalers
minmax_scaler = MinMaxScaler()
zscore_scaler = StandardScaler()

# Apply scaling
df_minmax = pd.DataFrame(minmax_scaler.fit_transform(df[numeric_cols]), columns=[f"{col}_minmax" for col in numeric_cols])
df_zscore = pd.DataFrame(zscore_scaler.fit_transform(df[numeric_cols]), columns=[f"{col}_zscore" for col in numeric_cols])

# Combine with non-numeric data
df_scaled = pd.concat([df.drop(columns=numeric_cols), df_minmax, df_zscore], axis=1)

# For demonstration, use one of the scaled feature sets for modeling
X = df_minmax  # You can also use df_zscore
y = df['Casualties']  # Example target (change based on your use case)

# Split into train and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Train and test split complete.")
print(f"X_train shape: {X_train.shape}, X_test shape: {X_test.shape}")

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
file_path = "global_traffic_accidents.csv"  # Update if needed
df = pd.read_csv(file_path)

# Select numeric columns
numeric_cols = ['Latitude', 'Longitude', 'Vehicles Involved', 'Casualties']

# Scale features using Min-Max Scaling
scaler = MinMaxScaler()
scaled_features = pd.DataFrame(scaler.fit_transform(df[numeric_cols]), columns=[f"{col}_minmax" for col in numeric_cols])

# Combine with non-numeric features if needed (not used here for modeling)
# Use scaled features (excluding the target 'Casualties') as input
X = scaled_features.drop(columns=['Casualties_minmax'])
y = df['Casualties']

# Split data into train and test sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the model (Random Forest Regressor)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model training complete.")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "global_traffic_accidents.csv"  # Update with correct path if needed
df = pd.read_csv(file_path)

# Select numeric columns and scale
numeric_cols = ['Latitude', 'Longitude', 'Vehicles Involved', 'Casualties']
scaler = MinMaxScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df[numeric_cols]), columns=numeric_cols)

# Features and target
X = df_scaled.drop(columns=['Casualties'])
y = df['Casualties']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation metrics
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Evaluation Metrics:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R²): {r2:.2f}")

# Visualization: Actual vs Predicted
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Actual Casualties")
plt.ylabel("Predicted Casualties")
plt.title("Actual vs Predicted Casualties")
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.tight_layout()
plt.show()

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Step 1: Load dataset
file_path = "global_traffic_accidents.csv"
df = pd.read_csv(file_path)

# Step 2: Select features and scale them
numeric_cols = ['Latitude', 'Longitude', 'Vehicles Involved', 'Casualties']
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df[numeric_cols])
df_scaled = pd.DataFrame(scaled_data, columns=numeric_cols)

# Step 3: Split features and target
X = df_scaled.drop(columns=['Casualties'])
y = df['Casualties']

# Step 4: Train/test split and model training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Step 5: New input for prediction
# Replace these values with real input as needed
new_data = {
    "Latitude": 34.05,
    "Longitude": -118.25,
    "Vehicles Involved": 3
}

# Step 6: Scale new input the same way
new_input_df = pd.DataFrame([new_data])
# Add dummy Casualties to match columns (will be removed after scaling)
new_input_df["Casualties"] = 0
new_input_scaled = scaler.transform(new_input_df)[0][:-1]  # Exclude Casualties column

# Step 7: Predict
prediction = model.predict([new_input_scaled])
print(f"Predicted number of casualties: {prediction[0]:.2f}")

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Load dataset
file_path = "global_traffic_accidents.csv"
df = pd.read_csv(file_path)

# Step 1: Encode categorical columns
categorical_cols = ['Weather Condition', 'Road Condition', 'Cause', 'Location']
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le  # Store encoder for future decoding if needed

# Step 2: Convert date and time to features
df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

df['Time'] = pd.to_datetime(df['Time'], format='%H:%M')
df['Hour'] = df['Time'].dt.hour
df['Minute'] = df['Time'].dt.minute

# Step 3: Drop unneeded columns
df = df.drop(columns=['Accident ID', 'Date', 'Time'])

# Step 4: Scale numeric features
numeric_cols = ['Latitude', 'Longitude', 'Vehicles Involved', 'Casualties', 'Day', 'Month', 'Year', 'Hour', 'Minute']
scaler = MinMaxScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Final encoded and scaled DataFrame
print("Processed DataFrame:")
print(df.head())

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_csv("global_traffic_accidents.csv")

# Features and target
X = df.drop(columns=["Accident ID", "Date", "Time", "Casualties"])
y = df["Casualties"]

# Identify categorical and numeric columns
categorical_cols = ["Location", "Weather Condition", "Road Condition", "Cause"]
numeric_cols = ["Latitude", "Longitude", "Vehicles Involved"]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numeric_cols)
    ]
)

# Create pipeline
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)

print(f"Mean Absolute Error: {mae:.2f}")

!pip install streamlit
import streamlit as st # Import streamlit to use its features
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer



# Title
st.title("Traffic Accident Casualty Predictor")

# User inputs
location = st.selectbox("Location", ["Mumbai, India", "São Paulo, Brazil", "Sydney, Australia", "Tokyo, Japan", "Beijing, China"])
weather = st.selectbox("Weather Condition", ["Clear", "Rain", "Snow", "Storm"])
road = st.selectbox("Road Condition", ["Dry", "Wet", "Snowy", "Icy"])
cause = st.selectbox("Cause", ["Reckless Driving", "Drunk Driving", "Speeding", "Distraction"])
latitude = st.number_input("Latitude", value=0.0)
longitude = st.number_input("Longitude", value=0.0)
vehicles = st.slider("Number of Vehicles Involved", 1, 10, 2)

# Prepare input for model
input_data = pd.DataFrame({
    "Location": [location],
    "Weather Condition": [weather],
    "Road Condition": [road],
    "Cause": [cause],
    "Latitude": [latitude],
    "Longitude": [longitude],
    "Vehicles Involved": [vehicles]
})

# Load model (alternatively, you can include training in the app)
@st.cache_resource
def load_model():
    # Define preprocessing and model inline if not using joblib
    categorical_cols = ["Location", "Weather Condition", "Road Condition", "Cause"]
    numeric_cols = ["Latitude", "Longitude", "Vehicles Involved"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
            ("num", "passthrough", numeric_cols)
        ]
    )

    model = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    df = pd.read_csv("global_traffic_accidents.csv")
    X = df.drop(columns=["Accident ID", "Date", "Time", "Casualties"])
    y = df["Casualties"]
    model.fit(X, y)

    return model

model = load_model()

# Predict button
if st.button("Predict Casualties"):
    prediction = model.predict(input_data)
    st.subheader(f"Predicted Number of Casualties: {int(prediction[0])}")

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load dataset
df = pd.read_csv("global_traffic_accidents.csv")

# Prepare features and target
X = df.drop(columns=["Accident ID", "Date", "Time", "Casualties"])
y = df["Casualties"]

# Define categorical and numerical columns
categorical_cols = ["Location", "Weather Condition", "Road Condition", "Cause"]
numeric_cols = ["Latitude", "Longitude", "Vehicles Involved"]

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numeric_cols)
    ]
)

# Full model pipeline
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
])

# Fit the model
model.fit(X, y)

# Prediction function
def predict_casualties(location, weather, road, cause, latitude, longitude, vehicles):
    input_df = pd.DataFrame([{
        "Location": location,
        "Weather Condition": weather,
        "Road Condition": road,
        "Cause": cause,
        "Latitude": latitude,
        "Longitude": longitude,
        "Vehicles Involved": vehicles
    }])
    prediction = model.predict(input_df)[0]
    return int(prediction)

# Example usage
if __name__ == "__main__":
    result = predict_casualties(
        location="Mumbai, India",
        weather="Clear",
        road="Dry",
        cause="Reckless Driving",
        latitude=18.96,
        longitude=72.82,
        vehicles=3
    )
    print("Predicted casualties:", result)
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load dataset
df = pd.read_csv("global_traffic_accidents.csv")

# Prepare features and target
X = df.drop(columns=["Accident ID", "Date", "Time", "Casualties"])
y = df["Casualties"]

# Define categorical and numerical columns
categorical_cols = ["Location", "Weather Condition", "Road Condition", "Cause"]
numeric_cols = ["Latitude", "Longitude", "Vehicles Involved"]

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numeric_cols)
    ]
)

# Full model pipeline
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
])

# Fit the model
model.fit(X, y)

# Prediction function
def predict_casualties(location, weather, road, cause, latitude, longitude, vehicles):
    input_df = pd.DataFrame([{
        "Location": location,
        "Weather Condition": weather,
        "Road Condition": road,
        "Cause": cause,
        "Latitude": latitude,
        "Longitude": longitude,
        "Vehicles Involved": vehicles
    }])
    prediction = model.predict(input_df)[0]
    return int(prediction)

# Example usage
if __name__ == "__main__":
    result = predict_casualties(
        location="Mumbai, India",
        weather="Clear",
        road="Dry",
        cause="Reckless Driving",
        latitude=18.96,
        longitude=72.82,
        vehicles=3
    )
    print("Predicted casualties:", result)

!pip install gradio  # Install Gradio if you haven't already
import gradio as gr  # Import the Gradio library
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load dataset
df = pd.read_csv("global_traffic_accidents.csv")

# Prepare training data
X = df.drop(columns=["Accident ID", "Date", "Time", "Casualties"])
y = df["Casualties"]

# Define feature types
categorical_cols = ["Location", "Weather Condition", "Road Condition", "Cause"]
numeric_cols = ["Latitude", "Longitude", "Vehicles Involved"]

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numeric_cols)
    ]
)

# Create and train the model pipeline
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
])
model.fit(X, y)

# Prediction function
def predict_casualties(location, weather, road, cause, latitude, longitude, vehicles):
    input_df = pd.DataFrame([{
        "Location": location,
        "Weather Condition": weather,
        "Road Condition": road,
        "Cause": cause,
        "Latitude": latitude,
        "Longitude": longitude,
        "Vehicles Involved": vehicles
    }])
    pred = model.predict(input_df)[0]
    return f"Estimated Casualties: {int(pred)}"

# Gradio Interface
iface = gr.Interface(
    fn=predict_casualties,
    inputs=[
        gr.Dropdown(choices=df["Location"].unique().tolist(), label="Location"),
        gr.Dropdown(choices=df["Weather Condition"].unique().tolist(), label="Weather Condition"),
        gr.Dropdown(choices=df["Road Condition"].unique().tolist(), label="Road Condition"),
        gr.Dropdown(choices=df["Cause"].unique().tolist(), label="Cause"),
        gr.Number(label="Latitude"),
        gr.Number(label="Longitude"),
        gr.Slider(1, 10, step=1, label="Vehicles Involved")
    ],
    outputs=gr.Textbox(label="Prediction"),
    title="Traffic Accident Casualty Predictor"
)

iface.launch()