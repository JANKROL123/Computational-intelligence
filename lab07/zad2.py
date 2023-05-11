
# Zadanie 2

# Celem zadania jest wykorzystanie sieci konwolucyjnych do rozpoznawania psów i kotów 
# z obrazków. Wykorzystujemy do tego specjalistyczne paczki (np. keras, tensorflow, 
# pytorch).
# Paczka ze zdjęciami (miniaturki) została dołączona na stronie (dogs-cats-mini.zip) 
# i zwiera dokładnie 12500 zdjęć kotów i 12500 zdjęć psów (razem około 26 MB)
# Jaki jest plan działania:
# a)Zapoznaj się z wybranym samouczkiem np.
# a.keras:
# https://machinelearningmastery.com/how-to-develop-a-convolutional-neural-network-to-classify-photos-of-dogs-and-cats/
# https://www.kaggle.com/code/uysimty/keras-cnn-dog-or-cat-classification
# b.tensorflow:
# https://pythonprogramming.net/convolutional-neural-network-kats-vs-dogs-machine-learning-tutorial/
# b)Załaduj bazę danych i dokonaj jej obróbki (przetworzenie obrazów, wyciągnięcie 
# klasy cat/dog z nazwy obrazka).
# c)Podziel dane na zbiór testowy i treningowy, i być może też walidacyjny.
# d)Skonstruuj, wytrenuj model sieci konwolucyjnej na zbiorze treningowym. Sieć może 
# mieć standardową, zaproponowaną w Internecie konfigurację.
# e)Podaj krzywą uczenia się dla zbioru treningowego i walidacyjnego.
# f)Podaj dokładność sieci na zbiorze testowym.
# g)Podaj macierz błędu na zbiorze testowym. 
# (Pytania dodatkowe: Czy są koty przypominające psy, albo psy przypominające koty?
# Ile? Potrafisz może wskazać konkretne zdjęcia omyłkowo zakwalifikowanych zwierząt?)
# h)Powtórz parę razy eksperymentd-g z inną konfiguracją sieci (optimizer, funkcje 
# aktywacji, inna struktura sieci, dropout, itp.). 
# Wskaż jaka konfiguracja działała najlepiej i pokaż jej wyniki (krzywa uczenia się, 
# dokładność, macierz błędu).


# import os

# import cv2
# import numpy as np
# from sklearn.model_selection import train_test_split

# # ścieżka do katalogu z obrazami
# data_dir = 'dogs-cats-mini'

# # lista klas (nazwy podkatalogów)
# classes = ['cat', 'dog']

# # przechowujemy obrazy i ich klasy
# data = []
# labels = []

# # wczytujemy obrazy i przetwarzamy je
# for label, class_name in enumerate(classes):
#     dir_path = os.path.join(data_dir, class_name)
#     file_names = os.listdir(dir_path)
#     for file_name in file_names:
#         file_path = os.path.join(dir_path, file_name)
#         # wczytanie obrazu przy użyciu OpenCV
#         image = cv2.imread(file_path)
#         # przekształcenie rozmiaru obrazu na 32x32 pikseli
#         image = cv2.resize(image, (32, 32))
#         # dodanie obrazu i jego klasy do list
#         data.append(image)
#         labels.append(label)

# # konwersja danych na numpy array
# data = np.array(data)
# labels = np.array(labels)

import os

import numpy as np
from PIL import Image

# ścieżka do folderu z danymi
data_dir = 'dogs-cats-mini'

# funkcja do przetwarzania obrazów
def process_image(img_path):
    img = Image.open(img_path)
    # zmiana rozmiaru obrazu na 64x64 piksele
    img = img.resize((64, 64))
    # konwersja obrazu na tablicę numpy
    img_array = np.array(img)
    # normalizacja wartości pikseli do zakresu [0, 1]
    img_array = img_array / 255.
    # wyciągnięcie klasy (cat/dog) z nazwy pliku
    label = os.path.splitext(os.path.basename(img_path))[0]
    label = label.split('.')[0]
    label_number = 0 if label == 'cat' else 1
    return (img_array, label_number)
    # (szerokosc x wysokosc x 3, 0/1)


# lista z danymi (obraz i etykieta)
data = []
# przetworzenie wszystkich obrazów w folderze
for filename in os.listdir(data_dir)[::20]:
    if filename.endswith('.jpg'):
        img_path = os.path.join(data_dir, filename)
        img_data = process_image(img_path)
        data.append(img_data)

# podział danych na tablicę z obrazami i tablicę z etykietami
images = np.array([x[0] for x in data])
labels = np.array([x[1] for x in data])

# print(data)

from sklearn.model_selection import train_test_split

# podział danych na zbiór treningowy i testowy
train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42)

from tensorflow.keras.layers import (Conv2D, Dense, Dropout, Flatten,
                                     MaxPooling2D)
from tensorflow.keras.models import Sequential

# definicja modelu sieci konwolucyjnej
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

# kompilacja modelu
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# wytrenowanie modelu
history = model.fit(train_images, train_labels, epochs=30, validation_split=0.2)

import matplotlib.pyplot as plt

print(history)

# wykres krzywej uczenia się
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')
plt.show()


test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print(test_acc)

# macierz błędu
from sklearn.metrics import confusion_matrix

# predykcja na zbiorze testowym
predictions = model.predict(test_images)
# zamiana prawdopodobieństw na klasy
predictions = np.where(predictions > 0.5, 1, 0)
# wygenerowanie macierzy błędu
cm = confusion_matrix(test_labels, predictions)
# wyświetlenie macierzy błędu
print(cm)
