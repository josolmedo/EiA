# Modelo de Perceptron Multicapa
# MeIA 2023

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

OPT_LAYERS=[15, 5, 8]
data = datasets.load_iris()
X = data['data']
y = data['target']

training_X, testing_X, training_y, testing_y = train_test_split(X, y, test_size = 0.25)
myscaler = StandardScaler()
myscaler.fit(training_X)
training_X = myscaler.transform(training_X)
testing_X = myscaler.transform(testing_X)
mlp = MLPClassifier(hidden_layer_sizes=OPT_LAYERS, activation='relu', solver='adam', max_iter=2500)
mlp.fit(training_X, training_y)
predicted_values = mlp.predict(testing_X)
print("prueba:    ", testing_y)
print("predicción:", predicted_values)
print(confusion_matrix(testing_y, predicted_values))
print(classification_report(testing_y, predicted_values))
