import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Wczytanie danych
data = pd.read_csv('diabetes.csv')

# Przygotowanie danych
X = data.drop('class', axis=1).values
y = data['class'].values

# Podział na zbiór treningowy i testowy
train_data, test_data, train_labels, test_labels = train_test_split(X, y, test_size=0.3)

# Standaryzacja danych
scaler = StandardScaler()
train_data = scaler.fit_transform(train_data)
test_data = scaler.transform(test_data)

# Utworzenie modelu sieci neuronowej
mlp = MLPClassifier(hidden_layer_sizes=(6, 3), activation='relu', max_iter=500)

# Trenowanie modelu na danych treningowych
mlp.fit(train_data, train_labels)

# Ewaluacja modelu na danych testowych
predictions = mlp.predict(test_data)
accuracy = accuracy_score(predictions, test_labels)
conf_matrix = confusion_matrix(predictions, test_labels)

# Wyświetlenie wyników
print("Dokładność: ", accuracy)
print("Macierz błędu: \n", conf_matrix)