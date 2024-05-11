import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

train_data = pd.read_csv("train_data.csv",on_bad_lines='skip',delimiter=';')
train_data = train_data.dropna()
train_data.head()

test_data = pd.read_csv("test_data.csv",on_bad_lines='skip',delimiter=';')
test_data = test_data.dropna()
test_data.head()

y = train_data["user_rating"]

features = ["size_bytes","price","rating_count_tot","rating_count_ver","user_rating_ver","rating_count_tot","rating_count_ver","cont_rating","user_rating_ver"]

x = pd.get_dummies(train_data[features])

x_test = pd.get_dummies(test_data[features])

model = RandomForestRegressor()
model.fit(x, y)
predictions = model.predict(x_test)

output = pd.DataFrame({"id": test_data.id, "rating": predictions})
output = output.dropna()
print('outuput columns:')
print(output)

#print(test_eval)

output.to_csv('submission.csv', index=False)
print("Your submission was successfully saved!")

test_eval = pd.read_csv("results_user_raiting.csv",on_bad_lines='skip',delimiter=';')
test_eval = test_eval.dropna()
print('test_eval columns:')
print(test_eval)

mse = mean_squared_error(test_eval["user_rating"], output["rating"])

print('Error cuadrático medio:', mse)