Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
... import numpy as np
... import pickle
... from sklearn.model_selection import train_test_split
... from sklearn.ensemble import RandomForestClassifier
... from sklearn.metrics import accuracy_score
... 
... # Load dataset
... data = pd.read_csv("dataset.csv")
... 
... # Features and Target
... X = data[['Rainfall', 'Temperature', 'Humidity', 'Water_Level']]
... y = data['Flood']
... 
... # Train-Test Split
... X_train, X_test, y_train, y_test = train_test_split(
...     X, y, test_size=0.2, random_state=42
... )
... 
... # Model
... model = RandomForestClassifier(n_estimators=100, random_state=42)
... model.fit(X_train, y_train)
... 
... # Accuracy
... predictions = model.predict(X_test)
... accuracy = accuracy_score(y_test, predictions)
... print("Model Accuracy:", accuracy)
... 
... # Save Model
... pickle.dump(model, open("flood_model.pkl", "wb"))
