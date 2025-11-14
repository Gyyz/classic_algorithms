# Support Vector Machine (Linear)

Soft-margin linear SVM trained via gradient descent on hinge loss.

Usage:

```python
from algorithm import LinearSVM

X = [[0.0],[1.0],[2.0],[3.0]]
y = [-1,-1,1,1]
svm = LinearSVM().fit(X, y)
print(svm.predict([1.5]))
```