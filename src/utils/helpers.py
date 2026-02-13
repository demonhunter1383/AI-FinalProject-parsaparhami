import joblib
import os


def save_model_artifact(model, filename):
    """
    ذخیره فیزیکی مدل در پوشه models
    """
    path = os.path.join('../models', filename)
    joblib.dump(model, path)
    print(f"Model successfully saved to {path}")
