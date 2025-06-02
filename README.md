# vehicle-sales
Car sales app

You can explore the live dashboard here:  
[vehicle-sales Dashboard on Render](https://vehicle-sales-yxxq.onrender.com)

This Streamlit web app allows users to explore U.S. used car advertisement data interactively.

# Features

- Price distribution visualization
- Price vs. year scatter plots
- Compare manufacturers with dropdown filters
- Interactive histograms with normalization

# Dataset

Dataset: `vehicles_us.csv`  
Source: [TripleTen Sample Dataset](https://raw.githubusercontent.com/alex000kim/simple-streamlit-datavis-app/main/vehicles_us.csv)

# How to Deploy This Streamlit App to Render

This guide explains how to deploy this Streamlit web app to the cloud using Render.

# Prerequisites

Before you begin, make sure you have:
- A GitHub account with this project’s files pushed (including app.py, requirements.txt, .streamlit/config.toml, vehicles_us.csv, etc.)
- A Render account (free tier is fine): https://render.com

-------------------------------------------------------------------------------------------------------------

# Step-by-Step Deployment Instructions

1. Go to https://render.com and log in.

2. Click the "New" button → select "Web Service".

3. Connect your GitHub account and choose your repository that contains this project.

4. Fill in the Render service settings:

   - Name: (any name you want for your app)
   - Environment: Python
   - Build Command:
     pip install streamlit && pip install -r requirements.txt
   - Start Command:
     streamlit run app.py
   - Region: (choose your preferred region)
   - Instance Type: Free

5. Click "Create Web Service" and wait 2–5 minutes for the deployment to complete.

6. Once deployed, Render will give you a public URL such as:
   https://your-app-name.onrender.com

   Open the link to access your live app.

-------------------------------------------------------------------------------------------------------------

# Required Files in Your Repository

Make sure your GitHub repo contains the following:

.
├── app.py
├── vehicles_us.csv
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml
└── notebooks/
    └── EDA.ipynb

-------------------------------------------------------------------------------------------------------------

# .streamlit/config.toml

Make a folder called `.streamlit` and add a file named `config.toml` inside it with this content:

[server]
headless = true
port = 10000

[browser]
serverAddress = "0.0.0.0"
serverPort = 10000

-------------------------------------------------------------------------------------------------------------

# Sample requirements.txt

Your `requirements.txt` should list the dependencies like this:

pandas==2.0.3
scipy==1.11.1
streamlit==1.25.0
altair==5.0.1
plotly==5.15.0

-------------------------------------------------------------------------------------------------------------

# Notes

- Render free tier apps may sleep after a few minutes of inactivity. Just refresh the browser to wake the app.
- To redeploy updates, simply push new code to your GitHub repo.