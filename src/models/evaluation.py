from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score


def evaluate_model_performance(model, X_test, y_test):
    """
    ارزیابی جامع مدل و بازگرداندن معیارهای اصلی
    """
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    report = classification_report(y_test, predictions)
    auc_score = roc_auc_score(y_test, probabilities)
    matrix = confusion_matrix(y_test, predictions)

    return {
        "report": report,
        "auc": auc_score,
        "confusion_matrix": matrix
    }
