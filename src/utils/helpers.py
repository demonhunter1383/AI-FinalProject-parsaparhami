import joblib
import os


def save_model_artifact(model, filename):

    path = os.path.join('../models', filename)
    joblib.dump(model, path)
    print(f"Model successfully saved to {path}")
