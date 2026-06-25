import pandas as pd
import numpy as np

# df1 = pd.DataFrame({'A': [1,2,3,4],'B':[10,20,30,40]})
# df2 = pd.DataFrame({'A': [11,22,33],'B':[100,200,300]}, index = [1,2,3])
# print(df1)
# print(df2)
# print("\n Addition \n",df1 + df2)
# print("\n Subtraction \n",df1 - df2)
# print("\n Multiplication \n",df1 * df2)
# print("\n Division \n",df1/df2)
# print("\n modulous \n",df1 % df2)


# one = pd.DataFrame(
#     {
#         "Name":["b1","c1","p1","q1"],
#         "subject":['sub1','sub2','sub3','sub4'],
#         "marks":[78,90,56,78]
#     },index=[1,2,3,4]
# )
# two = pd.DataFrame(
#     {
#         "Name":["b1","c1","p1","q1"],
#         "subject":['sub1','sub2','sub3','sub4'],
#         "marks":[78,90,56,78]
#     },index=[1,2,3,4]
# )
# res = pd.concat([one,two],keys=['x','y'],axis=1)
# print(res)

# one = pd.DataFrame(
#     {
#         "id":[1,2,3,4],
#         'name':['a1','a2','a3','a4'],
#         'subject': ["sub1","sub2","sub3","sub4"]
#     }
# )
# two = pd.DataFrame(
#     {
#         "id":[1,2,3,4],
#         'name':['b1','b2','b3','b4'],
#         'subject': ["sub1","sub2","sub3","sub4"]
#     }
# )
# res = one.merge(two,on="id",how='inner')
# print(res)

# df = pd.DataFrame({
#     'col1': range(12),
#     'col2':['A']*3 + ['B']*3 + ['C']*3 +['D']*3,
#     'Date': pd.to_datetime(['2026-05-21','2026-05-22','2026-05-23']*4)})
# print(df)

# pivoted = df.pivot(
# index="Date",
# columns ="col2",
# values="col1")
# print(pivoted)

# data = {'one': ["A","B","C","A","B"],
#         'two':[10,43,12,55,11]}


# df = pd.DataFrame(data)
# gd = df.groupby('one')['two'].max()
# print(gd)


# res = df.sort_values(by")

# data={
#     'Name':['ABC','XYZ','PQR'],
#     'Age':[28,22,34]
# }

# df=pd.DataFrame(data, [0,2,3])
# print(df)
# # res=df.sort_values(by='Age')
# res=df.sort_index()
# print(res) 


df = pd.read_csv('tips.csv')
print(pd.options.display.max_rows)





