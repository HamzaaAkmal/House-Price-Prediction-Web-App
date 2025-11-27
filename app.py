import pickle
import pandas as pd
from flask import Flask, render_template, request
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the pre-trained model
model_svc = pickle.load(open('model_svc.pkl', 'rb'))

# Load the processed dataset to extract unique values for dropdowns
processed_data = pd.read_csv('processed_data.csv')

# Define the categorical and numeric columns
categorical_columns = ['floors', 'waterfront', 'view', 'condition', 'street', 'city', 'statezip']
numeric_columns = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated']

# Define the exact feature order used during model training
model_feature_order = [
    'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view',
    'condition', 'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'street', 'city', 'statezip'
]

# Initialize label encoders for categorical columns
label_encoders = {
    'street': LabelEncoder(),
    'city': LabelEncoder(),
    'statezip': LabelEncoder(),
}

# Fit label encoders on the categorical columns in the processed data
for col in label_encoders.keys():
    label_encoders[col].fit(processed_data[col])

@app.route('/')
def index():
    # Fetch unique values for dropdowns from processed_data.csv
    sample_data = {
        'floors': processed_data['floors'].unique(),
        'waterfront': processed_data['waterfront'].unique(),
        'view': processed_data['view'].unique(),
        'condition': processed_data['condition'].unique(),
        'street': processed_data['street'].unique(),
        'city': processed_data['city'].unique(),
        'statezip': processed_data['statezip'].unique(),
    }
    return render_template('index.html', sample_data=sample_data)

@app.route('/predict', methods=['POST'])
def predict():
    # Extract the values from the form
    input_data = {col: request.form.get(col) for col in categorical_columns}
    input_data.update({col: float(request.form.get(col)) for col in numeric_columns})

    # Apply label encoding for categorical columns
    for col in ['street', 'city', 'statezip']:
        input_data[col] = label_encoders[col].transform([input_data[col]])[0]

    # Convert input data to a DataFrame
    input_df = pd.DataFrame([input_data])

    # Ensure the input data has the same feature order as the model
    input_df = input_df[model_feature_order]

    # Predict using the pre-trained model
    prediction = model_svc.predict(input_df)
    predicted_price = prediction[0]

    # Fetch unique values for dropdowns from processed_data.csv (for the form)
    sample_data = {
        'floors': processed_data['floors'].unique(),
        'waterfront': processed_data['waterfront'].unique(),
        'view': processed_data['view'].unique(),
        'condition': processed_data['condition'].unique(),
        'street': processed_data['street'].unique(),
        'city': processed_data['city'].unique(),
        'statezip': processed_data['statezip'].unique(),
    }

    # Pass both sample_data and predicted_price to the template
    return render_template('index.html', predicted_price=predicted_price, sample_data=sample_data)

if __name__ == '__main__':
    app.run(debug=True)