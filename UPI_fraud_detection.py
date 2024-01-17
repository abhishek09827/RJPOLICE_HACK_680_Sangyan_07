from flask import Flask, request, jsonify
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

app = Flask(__name__)

# Load the trained model
model_path = "/Users/lavishvaishnav/Desktop/OLD_RJPOLICE_HACK_680_Sangyan_07/UPI_model.pkl"
model = joblib.load(model_path)

# Load the dataset
dataset_path = "/Users/lavishvaishnav/Desktop/OLD_RJPOLICE_HACK_680_Sangyan_07/upi_fraud_dataset.csv"
dataset = pd.read_csv(dataset_path)

# Create a StandardScaler object
scaler = StandardScaler()

# Handle CORS (if needed)
# from flask_cors import CORS
# CORS(app)

@app.route('/predict', methods=['POST'])
def predict():

    try:
        # Get the data from the request
        data = request.get_json()

        # Create a DataFrame from the data
        data_df = pd.DataFrame([data])

        # Check if any values are zero and identify the field
        zero_fields = data_df.columns[data_df.iloc[0, :-1].eq(0)].tolist()

        if zero_fields:
            return jsonify({"error": f"Invalid input. The following fields have zero values: {', '.join(zero_fields)}"})

        # Assuming 'upi_number' is a key in your data, use it to filter the dataset
        user_upi_number = data['upi_number']
        user_data = dataset[dataset['upi_number'] == user_upi_number].drop(columns=['fraud_label'])
        
        # Scale the features using the previously created scaler
        data_scaled = scaler.transform(user_data)

        # Make the prediction
        prediction = model.predict(data_scaled)
        prediction_label = "Yes, it is fraud" if prediction[0] == 1 else "No, it is not fraud"

        result = {"prediction_label": prediction_label}
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
