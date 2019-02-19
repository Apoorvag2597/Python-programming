import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
dataset = pd.read_csv('iris.csv')
X = dataset.iloc[:, -1].values # Here first : means fetch all rows :-1 means except last column
y = dataset.iloc[:, 3].values# : is fetch all rows 3 means 3rd column
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state = 2)
# Create a SVC classifier using an RBF kernel
svm = SVC(kernel='rbf', random_state=0, gamma=.01, C=1)
# Train the classifier
svm.fit(X_train, y_train)

# Visualize the decision boundaries
plot_decision_regions(X_train, y_train, classifier=svm)
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()