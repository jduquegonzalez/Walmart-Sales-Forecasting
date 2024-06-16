import pandas as pd
import numpy as np
from sklearn.metrics import r2_score

def kpi_ML(Y_train, Y_train_pred, Y_test, Y_test_pred, name=""):
    df = pd.DataFrame(columns=['MAE', 'RMSE', 'Bias', 'R²'], index=['Train', 'Test'])
    df.index.name = name

    df.loc['Train', 'MAE'] = 100 * np.mean(np.abs(Y_train - Y_train_pred)) / np.mean(Y_train)
    df.loc['Train', 'RMSE'] = 100 * np.sqrt(np.mean((Y_train - Y_train_pred)**2)) / np.mean(Y_train)
    df.loc['Train', 'Bias'] = 100 * np.mean((Y_train - Y_train_pred)) / np.mean(Y_train)
    df.loc['Train', 'R²'] = r2_score(Y_train, Y_train_pred)

    df.loc['Test', 'MAE'] = 100 * np.mean(np.abs(Y_test - Y_test_pred)) / np.mean(Y_test)
    df.loc['Test', 'RMSE'] = 100 * np.sqrt(np.mean((Y_test - Y_test_pred)**2)) / np.mean(Y_test)
    df.loc['Test', 'Bias'] = 100 * np.mean((Y_test - Y_test_pred)) / np.mean(Y_test)
    df.loc['Test', 'R²'] = r2_score(Y_test, Y_test_pred)

    df = df.astype(float).round(1)  # Round numbers for display
    return df