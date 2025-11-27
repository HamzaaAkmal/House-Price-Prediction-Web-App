# House Price Prediction Web App

This is a web application that predicts the price of a house based on various features such as the number of bedrooms, bathrooms, square footage, and other property and location details. The model uses a pre-trained machine learning model to provide accurate property value predictions.

## Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Installation Instructions](#installation-instructions)
* [Usage](#usage)
* [File Structure](#file-structure)
* [Contributing](#contributing)
* [License](#license)

## Project Overview

This web application allows users to input property details (such as bedrooms, bathrooms, square footage, and location) and get an estimated house price based on a pre-trained machine learning model. The model is built using a Support Vector Classifier (SVC) algorithm, and the app is developed using Flask for the backend and HTML/CSS for the frontend.

### Key Features:

* **Interactive Form**: The user can fill in various property details.
* **Real-time Price Prediction**: The app predicts the house price based on the entered data.
* **Responsive Design**: The interface is mobile-friendly and adapts to various screen sizes.
* **Theme Toggle**: A light/dark theme toggle option for a better user experience.
* **Machine Learning Model**: The app loads a pre-trained SVC model to predict house prices.

## Features

* **Property Details**: Users input details like number of bedrooms, bathrooms, floor count, square footage, and more.
* **Location Details**: Users can select property location data like street, city, and state/zip code.
* **Prediction Result**: After submitting the form, the app predicts the price of the property and displays it.
* **Modern UI**: The user interface is designed with a clean and modern style, utilizing Bootstrap and custom CSS.

## Technologies Used

* **Flask**: A Python web framework for building the backend API.
* **Scikit-learn**: A machine learning library for loading and using the pre-trained model.
* **Bootstrap 5**: For responsive, mobile-first UI design.
* **HTML/CSS**: For structuring and styling the web pages.
* **Jinja2**: For dynamically rendering the web page with Python variables.

## Installation Instructions

To run this project locally, follow these steps:

### Prerequisites:

* Python 3.6 or later
* Pip (Python package manager)

### 1. Clone the repository

```bash
git clone https://github.com/HamzaaAkmal/House-Price-Prediction-Web-App.git
cd House-Price-Prediction-Web-App
```

### 2. Create a virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # For Windows use `venv\Scripts\activate`
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the pre-trained model and processed data

Make sure you have the `model_svc.pkl` and `processed_data.csv` files in the project directory. You can find the model file in the repository or train it yourself and place it in the project folder.

### 5. Run the Flask app

```bash
python app.py
```

The web app should now be running locally at `http://127.0.0.1:5000/`.

## Usage

1. Open the web app in a browser.
2. Fill out the form with the property details.
3. Click the "Predict Property Value" button.
4. After a brief wait, the estimated house price will appear on the page.

## File Structure

The project has the following structure:

```
House-Price-Prediction-Web-App/
│
├── app.py                       # Flask app (backend logic)
├── processed_data.csv            # Processed data for dropdown values
├── model_svc.pkl                 # Pre-trained machine learning model
├── templates/
│   └── index.html                # HTML template for the frontend
└── static/
    └── style.css                 # (if any custom styles are separate)
```

### app.py

Contains the Flask routes and logic for handling requests, loading the model, processing the data, and rendering the results.

### index.html

Contains the HTML for the form and results, as well as JavaScript for handling dynamic interactions like theme toggling and form submission.

## Contributing

If you'd like to contribute to the project, feel free to open an issue or submit a pull request. Please make sure to follow the guidelines for coding style and testing.

### Steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.