# Fridge Pilot: Smart Pantry & Recipe Manager
  
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/arsh199965/fridgepilot)

Fridge Pilot is an AI-powered full-stack web application that helps you manage your pantry inventory, predict expiry dates, and receive personalized recipe recommendations based on your available ingredients. Designed to minimize food waste and simplify meal planning, Fridge Pilot leverages modern web technologies and machine learning to deliver a seamless user experience.

---

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features
- **Inventory Tracking:** Add, update, and manage your pantry items and monitor expiry dates.
- **Expiry Prediction:** AI-driven expiry forecasts to help you use items before they spoil.
- **Personalized Recipe Recommendations:** Tailored recipes based on your current pantry, prioritizing ingredients nearing expiry.
- **Modern UI:** Responsive and sleek interface built with Next.js, TypeScript, and Tailwind CSS.
- **Robust Backend:** Flask-powered API with scikit-learn integration for predictive analytics.

---

## Tech Stack
- **Frontend:** Next.js, TypeScript, Tailwind CSS  
- **Backend:** Flask, Python  
- **Machine Learning:** scikit-learn  
- **Database:**  PostgreSQL

---

## Installation

### Prerequisites
- Node.js (v14+)
- Python 3.8+
- Git

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/arsh199965/fridgepilot.git
   cd fridgepilot
   ```
2. **Install Frontend Dependencies**  
Navigate to the frontend folder, install dependencies, and run the development server:
    ```bash
    cd frontend
    npm install
    npm run dev
    ```
Your frontend will be available at http://localhost:3000.

3. **Install Backend Dependencies**
Switch to the backend folder, create a virtual environment, and install the required packages:

    ```bash
    cd ../backend
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
3. **Configure Environment Variables**
Create a .env file in the backend directory with the following content:

    ```
    POSTGRES_DB=your_db
    POSTGRES_USER=your_user
    POSTGRES_PASSWORD=your_password
    POSTGRES_HOST=your_host
    POSTGRES_PORT=5432
    DATABASE_URL=your_url
    FRONTEND_URL=http://localhost:3000
    MODEL_PATH=improved_shelf_life_model.pkl
    ```
4. **Run the Backend**
Start your Flask application:

    ```bash
    python app.py
    ```
Your backend will be available at http://localhost:5000.
