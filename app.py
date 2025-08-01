import streamlit as st
import numpy as np
import joblib  

# Load the trained model
model = joblib.load("Farm_Irrigation_System.pkl")  

# Title and description
st.title("💧 Smart Sprinkler System")
st.markdown("### AICTE Internship Cycle 2 Project")
st.write("Developed by **Kashish Pherwani**")

st.subheader("Enter scaled sensor values (0 to 1) to predict sprinkler status")
st.info("Note: Values should be scaled between **0 and 1**. Example: 0.0 means low reading, 1.0 means high reading.")

# Collect sensor inputs (scaled values)
sensor_values = []
for i in range(20):
    val = st.slider(f"Sensor {i+1}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    sensor_values.append(val)

# Predict button
if st.button("🔍 Predict Sprinklers"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown("### Prediction Results:")
    for i, status in enumerate(prediction):
        st.write(f"🌱 Sprinkler {i+1} (Parcel {i+1}): **{'ON' if status == 1 else 'OFF'}**")
    
    st.success("Prediction complete!")
