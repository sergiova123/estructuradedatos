import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(data, feature):
    if len(data) == 0:
        return None

    data.sort(key=lambda x: x[feature])
    split_point = len(data) // 2
    root = TreeNode(data[split_point])

    root.left = build_tree(data[:split_point], feature)
    root.right = build_tree(data[split_point + 1:], feature)

    return root

def make_prediction(tree, app_name, model):
    if (app_name == data['track_name']):
        app_features = data[data['track_name'] == app_name][features].iloc[0]
        if tree is None:
            return "No se encontró la aplicación"

        if app_features['user_rating'] is None:
            return "Calificación de usuario no disponible"

        # Predicción utilizando el modelo entrenado
        prediction = model.predict([app_features])[0]
        

        if prediction == 1:
            return "Buena aplicación"
        else:
            return "No tan buena aplicación"

# Cargar el conjunto de datos desde un archivo CSV
data = pd.read_csv('data.csv',on_bad_lines='skip',delimiter=';')

# Seleccionar todas las columnas como características excepto la columna de destino
features = ["size_bytes","price","rating_count_tot", "user_rating","rating_count_ver","user_rating_ver","rating_count_tot","rating_count_ver", "user_rating_ver"]

print(data[features])
# Eliminar filas con datos faltantes
data.dropna(subset=features, inplace=True)

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(data[features], data['user_rating'], test_size=0.2, random_state=42)

# Entrenar un modelo de regresión logística
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Evaluar la precisión del modelo
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Error cuadrático medio:", mse)

# Construir el árbol con los datos de entrenamiento
tree_data = X_train.copy()
tree_data['user_rating'] = y_train
root = build_tree(tree_data.to_dict('records'), 'user_rating')

# Ejemplo de predicción para una nueva aplicación
continuar = "Si"
while continuar == "Si":
    app_name = input("Ingrese el nombre de la aplicación: ")
    prediction = make_prediction(root, app_name, model)
    print("Predicción para la aplicación", app_name + ":", prediction)
    continuar = input("Desea continuar Si/No: ")


   