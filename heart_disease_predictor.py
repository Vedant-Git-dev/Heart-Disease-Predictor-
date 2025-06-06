import pandas as pd

data = pd.read_csv("data.csv")

data.head()



data.describe()

data["num"] = data["num"].apply(lambda x: 1 if x > 0 else 0)

data.isnull().sum()

"""## Looking For Corrs"""

corr_mat = data.corr()
corr_mat["num"].sort_values(ascending = False)

"""## Dropping unnecessary cols"""

data.drop(["chol", "fbs"], inplace = True, axis = 1)

"""## Train Test Splitting"""

from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(data, random_state = 42, test_size = 0.2)

"""## Pipeline"""

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

data = train_set.drop("num", axis = 1)
data_lbl = train_set["num"].copy()

pipe = Pipeline([
    ('imputer', SimpleImputer(strategy = "most_frequent")),
    ('scaler', StandardScaler())
])

pipe.fit(data)
scaled_data = pipe.transform(data)

scaled_data.shape

"""## Model Selection"""

# from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# model = KNeighborsClassifier(n_neighbors = 5)
model = RandomForestClassifier(n_estimators = 50, max_depth = 4)

model.fit(scaled_data, data_lbl)

from sklearn.model_selection import cross_val_score
import numpy as np

scores = cross_val_score(model, scaled_data, data_lbl, cv = 10, scoring = "accuracy")

with open("models.txt", "a") as f:
    f.write(f"\n{model}\n\t{scores.mean()}\n")

"""## Model Tuning"""

from sklearn.model_selection import GridSearchCV

params = {
    'n_estimators': [50, 100, 150, 200],
    'max_depth': [4, 8, None]
}

grid = GridSearchCV(model, params, cv = 10)
grid.fit(scaled_data, data_lbl)

grid.best_params_

with open("models.txt", "a") as f:
    f.write(f"\n\t{grid.best_score_}\n\t{grid.best_params_}\n")

"""## Final Model Testing"""

some_data = data.iloc[:5]
some_lbl = data_lbl.iloc[:5]

x_prep = pipe.transform(some_data)

model.predict(x_prep)

some_lbl

"""## Testing on Test Data"""

x_test = test_set.drop("num", axis = 1)
y_test = test_set["num"].copy()

x_prep = pipe.transform(x_test)

model.predict(x_prep)

y_test

cross_val_score(model, x_prep, y_test, cv = 10, scoring = "accuracy").mean()

"""## Saving Model"""

from joblib import dump

dump(model, 'Heart_Disease_Predictor.joblib')
