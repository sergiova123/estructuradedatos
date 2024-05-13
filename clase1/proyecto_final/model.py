import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from tree import build_tree
from sklearn.metrics import mean_squared_error


def make_prediction(tree, app_name, model):
    if app_name in data['track_name'].values:
        app_features = data[data['track_name'] == app_name][features].iloc[0]

        if app_features['user_rating'] is None:
            return "Calificación de usuario no disponible"

        # Predicción utilizando el modelo entrenado
        prediction = model.predict([app_features])[0]
        
        if prediction == 1:
            return "Buena aplicación"
        else:
            return "No tan buena aplicación"
    else:
        return "No se encontró la aplicación"

# Cargar el conjunto de datos desde un archivo CSV
data = pd.read_csv('data.csv', on_bad_lines='skip', delimiter=';')

# Seleccionar todas las columnas como características excepto la columna de destino
features = ["rating_count_tot","rating_count_ver","user_rating_ver", "user_rating"]

# Eliminar filas con datos faltantes
data.dropna(subset=features, inplace=True)

# Convertir las calificaciones de usuario a categorías discretas
data['user_rating'] = data['user_rating'].apply(lambda x: 1 if x >= 4 else 0)

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(data[features], data['user_rating'], test_size=0.2, random_state=42)

# Entrenar un modelo de regresión logística
model = LogisticRegression(max_iter=1000) 
model.fit(X_train, y_train)

# Construir el árbol con los datos de entrenamiento
tree_data = X_train.copy()
tree_data['user_rating'] = y_train
root = build_tree(tree_data.to_dict('records'), 'user_rating')

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Error cuadrático medio:", mse)

# Ejemplo de predicción para una nueva aplicación
continuar = "Si"
while continuar.lower() == "si":
    app_name = input("Ingrese el nombre de la aplicación: ")
    prediction = make_prediction(root, app_name, model)
    print("Predicción para la aplicación", app_name + ":", prediction)
    continuar = input("Desea continuar Si/No: ")