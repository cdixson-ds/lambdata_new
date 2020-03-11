import pandas as pd
#from sklearn.model_selection import train_test_split

def split(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.22, random_state=42)
    #length of train, test, and df
    len(X_train), len(X_test), len(X_train) + len(X_test)
    return X_train, X_test, y_train, y_test