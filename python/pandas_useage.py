import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), index=[11, 4, 13], columns=['a', 'b', 'c'])
df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), index=[25, 23, 4], columns=['a', 'b', 'c'])
concated = df2.combine_first(df1)
print(concated)

# def cc(a, b):
#     print(a)
#
# newdf = df.combine(df2, cc)
