# Heart Disease Prediction using Machine Learning

This project aims to predict the presence of heart disease using various machine learning models. The dataset used is the **UCI Heart Disease dataset**.

## 📊 Dataset

- Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/45/heart+disease)
- Target Column: `num`
  - `0`: Less than 50% diameter narrowing (No heart disease)
  - `1`: More than 50% diameter narrowing (Heart disease)

## 🧠 Models Tested

The following models were tested using cross-validation:

| Model                      | Accuracy  |
|----------------------------|-----------|
| KNeighborsClassifier       | 0.8187    |
| RandomForestClassifier     | 0.8148    |
| LogisticRegression         | 0.7980    |
| GradientBoostingClassifier | 0.7650    |

📄 *For detailed scores, refer to `models testing.txt` file.*

## ⚙️ Technologies Used

- Python
- Pandas, NumPy
- scikit-learn (for preprocessing, modeling, and evaluation)
- Jupyter Notebook 

## 🚀 Steps Performed

1. Loaded and cleaned the data
2. Filled missing values (using `SimpleImputer`)
3. Scaled features
4. Split dataset into training and testing sets
5. Applied cross-validation on multiple classifiers
6. Evaluated using accuracy score

## 📁 Files

- `heart_disease_predictor.ipynb`: Main notebook
- `models testing.txt`: Model-wise accuracy results
- `README.md`: Project documentation
- `data.csv`: Data used for model building
- `heart_disease_predictor.py`: Python Script

## ✅ Conclusion

The best performance was achieved with **KNeighborsClassifier** and **RandomForestClassifier**, both giving over **81% accuracy**. Further improvement can be done via hyperparameter tuning (`GridSearchCV` or `RandomizedSearchCV`).

## 🔗 GitHub

Feel free to fork or contribute improvements!

