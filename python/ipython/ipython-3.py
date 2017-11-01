

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

#help(preprocessing.LabelBinarizer)

mlb = preprocessing.MultiLabelBinarizer()
print(mlb.fit_transform([(1, 2), (3,)]))
#[[1 1 0], [0 0 1]]
print(mlb.classes_)
# [1 2 3]


le = preprocessing.LabelEncoder()
le.fit([1, 2, 2, 6])
le.classes_
#[1, 2, 6]
le.transform([1, 1, 2, 6])
# [0, 0, 1, 2]
le.inverse_transform([0, 0, 1, 2])
# [1, 1, 2, 6]

le = preprocessing.LabelEncoder()
le.fit(["paris", "paris", "tokyo", "amsterdam"])
list(le.classes_)
# ['amsterdam', 'paris', 'tokyo']
le.transform(["tokyo", "tokyo", "paris"])
# [2, 2, 1]
list(le.inverse_transform([2, 2, 1]))
# ['tokyo', 'tokyo', 'paris']
