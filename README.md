# CMU-MSBA-26-MLBA-Group12-Flight-Delay-Project
End-to-end ML system for flight delay prediction using AWS and Streamlit

# Flight Delay Prediction Project

This project builds a simple end-to-end machine learning system to predict flight delay probability using flight schedule information. The system includes data processing, model training, and deployment using a Streamlit web application on AWS.

---

## 1. Business Problem

Flight delays are common in real-world operations and can significantly affect passengers and airline efficiency.  
The goal of this project is to estimate the probability that a flight will be delayed (≥15 minutes) based on information available before departure.

---

## 2. Data

The dataset includes flight-level features such as:

- Month  
- Day of month  
- Day of week  
- Scheduled departure time  
- Scheduled arrival time  
- Distance  

### Data Processing

- Removed cancelled flights  
- Handled missing values  
- Removed features that may cause data leakage (e.g., actual delay variables)  
- Focused only on variables available before departure  

### Data Availability

The original dataset is not included in this repository due to size constraints.  
The trained model (`model.pkl`) is provided to reproduce predictions directly.

---

## 3. Model

We experimented with multiple models and selected:

- **Final model: Gradient Boosting Classifier**

### Reasons for Selection

- Good predictive performance  
- Able to capture nonlinear relationships  
- More stable compared to simpler models  

---

## 4. Performance

The model outputs the **probability of delay**.

For user interpretation, we define:

- 🟢 Low Risk: probability < 0.4  
- 🟡 Moderate Risk: 0.4 – 0.7  
- 🔴 High Risk: > 0.7  

(Additional evaluation metrics such as accuracy or AUC can be included if needed.)

---

## 5. User Interface

We built a simple **Streamlit application**.

### User Input

- Month  
- Day of Month  
- Day of Week  
- Departure Time  
- Arrival Time  
- Distance  

### Output

- Delay probability  
- Risk category (Low / Moderate / High)  

This allows users to quickly estimate delay risk for a given flight.

---

## 6. AWS Deployment

The system is deployed using:

- **EC2** to host the Streamlit application  

To deploy on AWS EC2:
1. Launch EC2 instance
2. Open port 8501
3. Upload files using SCP
4. Run:
   streamlit run app/app.py --server.port 8501 --server.address 0.0.0.0

Users can access the application through the EC2 public IP.

---

## 7. How to Run Locally

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the application:
```bash
streamlit run app/app.py
```
---

## 8. Project Structure
app/
  app.py
model.pkl
columns.pkl
requirements.txt
README.md

---

## 9. Notes
This project is a proof-of-concept system that demonstrates the full pipeline from data processing to deployment.
It is designed to be simple, interpretable, and easy to extend.

---

## 10. References
Flight Delay Prediction Study: https://www.mdpi.com/2226-4310/10/4/342 
