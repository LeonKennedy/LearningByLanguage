

from sklearn import preprocessing
lb = preprocessing.LabelBinarizer()
lb.fit([1,2,3,4,5,4,3])
print(lb.classes_)
#  [1 2 3 4 5]
print(lb.transform([1,3,4]))
'''
[[1 0 0 0 0]
 [0 0 1 0 0]
  [0 0 0 1 0]]
'''
