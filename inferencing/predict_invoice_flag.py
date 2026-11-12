import joblib
import pandas as pd
MODEL_PATH = "invoice_flagging/models/predict_flag_invoice.pkl"
SCALER_PATH = "invoice_flagging/models/scaler.pkl"


def load_model(model_path: str = MODEL_PATH):
    """
    Load trained classifier model.
    """
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    return model


def predict_invoice_flag(input_data):
    """
    Predict invoice flag for new vendor invoices.

    Parameters
    ----------
    input_data : dict

    Returns
    -------
    pd.DataFrame with predicted flag
    """
    model = load_model()
    scaler = joblib.load(SCALER_PATH)

    input_df = pd.DataFrame(input_data)

    input_scaled = scaler.transform(input_df)

    input_df["Predicted_Flag"] = model.predict(input_scaled).round()

    return input_df


if __name__ == "__main__":

    # Example inference run (local testing)
    sample_data = {
    "invoice_quantity": [100, 200, 150],
    "invoice_dollars": [15000, 9000, 7000],
    "Freight": [200, 350, 250],
    "total_item_quantity": [100, 200, 150],
    "total_item_dollars": [5000, 9000, 7000]
    }

    prediction = predict_invoice_flag(sample_data)

    print(prediction)
