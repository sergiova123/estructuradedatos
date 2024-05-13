import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Carga tu dataset (reemplaza 'tu_dataset.csv' con el nombre de tu archivo)
df = pd.read_csv('sentiment_tweets3.csv', on_bad_lines='skip', delimiter=',')

# Divide los datos en características (X) y etiquetas (y)
X = df['message to examine']
y = df['label (depression result)']

# Divide los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectoriza los mensajes utilizando TF-IDF
vectorizer = TfidfVectorizer(max_features=1000)  # Ajusta el número de características según tus necesidades
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Entrena el modelo de árbol de decisión
clf = DecisionTreeClassifier()
clf.fit(X_train_vec, y_train)

# Realiza predicciones en el conjunto de prueba
y_pred = clf.predict(X_test_vec)

# Evalúa la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: ',accuracy)

# Ahora puedes usar el modelo entrenado para predecir si un nuevo mensaje tiene depresión o no
nuevo_mensaje = "RT Depression Could Be Improved With Vitamin D Deficiency Treatment <Emoji: Rightwards arrow>  http://aboutdepressionfacts.com/4wxuÃ‚Â   pic.twitter.com/QGgbqPZUMR #health #well"
nuevo_mensaje_vec = vectorizer.transform([nuevo_mensaje])
prediccion = clf.predict(nuevo_mensaje_vec)
print(f'Predicción para el nuevo mensaje: {"Depresión" if prediccion[0] == 1 else "No depresión"}')

