from sklearn import tree
from sklearn import metrics
from sklearn import svm
from sklearn.neural_network import MLPClassifier

# [height, weight, shoe size] 
X = [[181,80,44], [177,70,43], [160,60,38], [154,54,37], [180,85,44],
	 [166,65,40], [190,90,47], [175,64,39], [177,70,40], [159,55,37],
	 [171,75,42], [181,85,43], [155,55,36], [190,89,45], [177,67,43]]

Y = ['male', 'female', 'female', 'female', 'male', 'male', 'male', 
	'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female']

print('Models:')
## Classifier Models
# Decision Tree
clfTree = tree.DecisionTreeClassifier()
clfTree = clfTree.fit(X,Y)
print(clfTree)

# SVM
clfSVM = svm.SVC(gamma = 'scale')
clfSVM.fit(X,Y)
print(clfSVM) 

# MLPClassifier
clfMLPClassifier = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
clfMLPClassifier.fit(X, Y)
print(clfMLPClassifier)

print('\n\n Testing \n\n')

## Testing
# Datasets
X_test = [[190,70,43], [180,65,40], [165,55,36]]
Y_expected = ['male', 'female', 'female']

## Prediction 
# Decision Tree
Y_pred_Tree = clfTree.predict(X_test)

print(Y_pred_Tree)
print(metrics.classification_report(Y_expected,Y_pred_Tree))
print(metrics.confusion_matrix(Y_expected,Y_pred_Tree))

# SVM
Y_pred_SVM = clfSVM.predict(X_test)

print(Y_pred_SVM)
print(metrics.classification_report(Y_expected,Y_pred_SVM))
print(metrics.confusion_matrix(Y_expected,Y_pred_SVM))

# MLPClassifier
Y_pred_MLPClassifier = clfMLPClassifier.predict(X_test)

print(Y_pred_MLPClassifier)
print(metrics.classification_report(Y_expected,Y_pred_MLPClassifier))
print(metrics.confusion_matrix(Y_expected,Y_pred_MLPClassifier))

