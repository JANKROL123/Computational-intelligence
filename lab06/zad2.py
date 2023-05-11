from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


iris = load_iris()
datasets = train_test_split(iris.data, iris.target,
                            test_size=0.7)

train_data, test_data, train_labels, test_labels = datasets

scaler = StandardScaler()

scaler.fit(train_data)
train_data = scaler.transform(train_data)
test_data = scaler.transform(test_data)

mlp = MLPClassifier(hidden_layer_sizes=(3,3), max_iter=1000)

mlp.fit(train_data, train_labels)
predictions_train = mlp.predict(train_data)
print("Dokładność na zbiorze treningowym: ",accuracy_score(predictions_train, train_labels))
predictions_test = mlp.predict(test_data)
print("Dokładność na zbiorze testowym: ",accuracy_score(predictions_test, test_labels))



# Najlepiej działa ostatnia sieć neuronowa z 2 warstwami ukratymi po 3 neurony.
# Dokładność w zbiorze testowym to 95%, podczas gdy 2 poprzednie to 92% i 83%.