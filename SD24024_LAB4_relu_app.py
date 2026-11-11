
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page title
st.title("ReLU Activation Function")
st.write("Visualisation of the Rectified Linear Unit (ReLU) activation function.")

# Generate input values
xgrid = np.linspace(-6, 6, 400)

# Activation function
def act_curve(name, x):
    if name == "relu":
        return np.maximum(0, x)
    return x

# User input
input_value = st.slider("Select input value (x)", -6.0, 6.0, 1.0)

# Calculate output
ygrid = act_curve("relu", xgrid)
output = act_curve("relu", input_value)

# Plot graph
fig, ax = plt.subplots(figsize=(6, 4))

ax.plot(xgrid, ygrid, label="ReLU")
ax.scatter(input_value, output, color="red", label="Selected input")

ax.set_title("ReLU Activation Function")
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output f(x)")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# Display output
st.write("### Output")
st.metric("ReLU Output", f"{output:.4f}")
