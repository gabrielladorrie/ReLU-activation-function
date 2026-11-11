# ReLU Activation Function Visualisation

## 1. Project Overview

This project focuses on developing an interactive web application to visualise the **Rectified Linear Unit (ReLU) activation function** using Python and Streamlit.

The application allows users to adjust input values through an interactive slider and observe how the ReLU activation function transforms the input into an output. The corresponding graph and output value update dynamically based on the selected input.

## 2. Project Objectives

- To understand the concept and behaviour of the ReLU activation function.
- To visualise the relationship between input and output values.
- To demonstrate how ReLU handles negative and positive input values.
- To develop an interactive web application using Python.
- To provide a simple and effective visual learning experience for understanding activation functions in neural networks.

## 3. Tools and Technologies

| Tools | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Develop the interactive web application |
| NumPy | Generate input values and calculate activation outputs |
| Matplotlib | Create and display the ReLU graph |
| GitHub | Store source code and project documentation |
| Streamlit Community Cloud | Deploy the application online |

## 4. ReLU Activation Function

The Rectified Linear Unit (ReLU) is an activation function commonly used in artificial neural networks and deep learning.

The mathematical formula is:

\[
f(x)=\max(0,x)
\]

The ReLU function works as follows:

- **Negative input:** The output is 0.
- **Positive input:** The output is equal to the input.
- **Zero input:** The output is 0.

### Example Outputs

| Input (x) | ReLU Output |
|---:|---:|
| -5 | 0 |
| -2 | 0 |
| 0 | 0 |
| 2 | 2 |
| 5 | 5 |

## 5. Application Features

The application provides several interactive features:

### 5.1 Interactive Input Slider

Users can select an input value ranging from -6 to 6 using the Streamlit slider.

### 5.2 Dynamic Graph Visualisation

The application displays the ReLU activation curve using Matplotlib. The graph updates automatically whenever the input value changes.

### 5.3 Selected Input Indicator

A red point highlights the selected input value and its corresponding output on the graph.

### 5.4 Real-Time Output Display

The application calculates and displays the ReLU output based on the selected input value.

### 5.5 Clear and User-Friendly Interface

The application provides a clear title, graph labels, legend, grid, input slider, and output display to improve user understanding.

## 6. Application Screenshot

The following screenshot shows the developed ReLU Activation Function application.

It demonstrates the interactive input slider, ReLU graph, selected input indicator, and calculated output.

(https://github.com/gabrielladorrie/ReLU-activation-function/blob/main/relu_app.png)

**Figure 1: ReLU Activation Function Web Application**

## 7. Project Structure

The GitHub repository is organised as follows:

```text
ReLU-activation-function/
│
├── relu_app.py
├── requirements.txt
├── README.md
└── relu_app.png
```

| File | Description |
|---|---|
| `relu_app.py` | Main Python script containing the ReLU function and Streamlit application |
| `requirements.txt` | Contains the required Python libraries |
| `README.md` | Project documentation and instructions |
| `relu_app.png` | Screenshot of the ReLU application |

The application is organised in its own Python file, separate from the Sigmoid and Tanh applications. This independent structure makes the application easier to understand, maintain, execute, and update.

## 8. Installation and Setup

Follow the instructions below to run the application locally.

### Step 1: Clone the GitHub Repository

```bash
git clone https://github.com/gabrielladorrie/ReLU-activation-function.git
```

### Step 2: Navigate to the Project Folder

```bash
cd ReLU-activation-function
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run relu_app.py
```

After running the command, Streamlit will open the application in your default web browser.

## 9. Requirements

The application requires the following Python libraries:

```text
streamlit
numpy
matplotlib
```

These dependencies are listed in the `requirements.txt` file to make installation easier and ensure the application can be reproduced in another environment.

## 10. Deployment

The application is deployed using **Streamlit Community Cloud**, allowing users to access the application through a web browser without installing Python locally.

### Deployment Steps

1. Upload the project files to the GitHub repository.
2. Visit [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect your GitHub account.
4. Select the ReLU Activation Function repository.
5. Set `relu_app.py` as the main application file.
6. Click Deploy.
7. Test the deployed application to ensure the slider, graph, and output display work correctly.

**Live Streamlit Application:**

https://relu-activation-function-nzgrg9jjpfsmhapprupbjop.streamlit.app/

**GitHub Repository:**

https://github.com/gabrielladorrie/ReLU-activation-function

## 11. Learning Outcomes

Through this project, users can understand:

- The basic concept of the ReLU activation function.
- How negative input values are converted into zero.
- How positive input values remain unchanged.
- How activation functions are used in artificial neural networks.
- How Python libraries such as Streamlit, NumPy, and Matplotlib can be combined to create interactive visualisations.

## 12. Conclusion

The ReLU Activation Function application successfully demonstrates how the ReLU function transforms input values into outputs through an interactive visualisation.

By using Streamlit, users can adjust input values and observe the corresponding changes in the graph and output immediately. This application provides a simple and interactive way to understand the behaviour of the ReLU activation function in neural networks.

## 13. GitHub Repository Topics

Suggested repository topics:

`python` `streamlit` `relu` `activation-function` `neural-networks` `deep-learning` `machine-learning` `data-visualisation`
