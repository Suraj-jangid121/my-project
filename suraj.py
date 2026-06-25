import numpy as  np
import pandas as pd
import matplotlib.pyplot as plt


# a = np.array([
#     1,2,3],dtype='S')
# print(a,type(a),a.dtype)

# a = np.ones((6,2,3))
# print(a)

# a = np.arange(0,10,1)
# print(a)

# a = np.linspace(0,5,num=10)
# print(a)

# a = np.random.rand(3,4,4)
# print(a)

# a  = np.full((3,4),6)
# print(a)

# a = np.array(
#     [[[1,2,3,4,5],
#              [6,7,8,9,10]],
#      [[11,12,13,14,15],
#              [16,17,18,19,20]]])
# # print((a[2]))
# # print(a[2]+a[3])

# print(a[1,1,3])


# a = np.array([1,2,3,4,5,6,7,8,9,10])
# print(a[::-1])
# print(a[0:10])
# print(a[0:5:2])

# a =  np.array([[1,2,3,4,5],
#                [6,7,8,9,10]])
# print(a[0:2,1:3])


# a = np.array(
#     [
#         [[1,2,3,4,5],
#          [6,7,8,9,10]],
#         [[11,12,13,14,15],
#          [16,17,18,19,20]]
#     ]
# )
# print(a[1,0,3])

# a = np.array([1,2,3,4,5,6,7,8,9])
# x = a.copy()
# print(a)
# a[0]=50
# print(a)
# print(x)
# x = a.view()
# print(x)


# a = np.array([[1,2,3],[5,6,7],[4,8,9]])

# print(a.shape)

# res = np.transpose(a)
# print(res)


# a = np.array([[1,2,3],[5,6,7]])
# b = np.array([[7,4,19],[12,13,14]])
# res  = np.concatenate((a,b),axis=1)
# print(res)

# a = np.arange(9)
# print(a)
# res = np.split(a,3)
# res = np.resize(a,(3,2))
# print(res)

# for i,arr in enumerate(res):
#     print("splited array",i+1)
#     print(arr)

# res = np.append(a,[[7,8,9]],axis=0)#bottom
# print(res)

# res =  np.append(a,[[7,8,9],[10,11,12]],axis=1)#right side
# print(res)

# res  = np.insert(a,3,[11,12,13])
# print(res)

# a = np.arange(12).reshape(3,4)
# print(a)
# print(np.delete(a,6))

# res =  np.flip(a)
# print(res)

# a = np.array([24,11,67,2,63])

# res = np.sort(a)
# print(res)

# res = np.argmax(a)
# print(res)

# res = np.argmin(a)
# print(res)

# a = np.arange(10)
# res = a[-1::-1]
# print(res)

# a = np.array([[1,2,3],[4,5,6]])
# b = a.reshape(3,2)
# a.shape = (3,2)
# print(a.shape)


# a = np.arange(24)
# a.ndim
# res = a.reshape(2,4,3)
# print(res)

# a = np.array(
#     [
#         [[123,4,5],[2,3,4]],
#         [[123,4,5],[2,3,4]]
#     ], dtype=np.int8
# )
# # print(a.size)
# # print(a,a.dtype)
# print(a.itemsize)


# a = np.array([[21,22,23],[12,13,14]])
# b = np.array([[24,25,26],[27,28,29]])
                        
# print(a+b)
# print(a-b)
# print(a * b)
# print(a/b)
# print(a%b)
# print(a**b)


# a = np.array([[21,22,23],[12,13,14]])
# res = np.mean(a,axis=1)
# print(a)
# print(res)


# a = np.array([3.4j,2.8j,6.,1+3j])
# print(np.real(a))
# print(np.imag(a))
# print(np.conj(a))
# print(np.angle(a,deg=True))

# a = np.array([1,2,3,4,5])
# a[1],a[4] = a[4],a[1]
# print(a)


# a = np.array([
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ])
# print(a)

# a[[0,1,2],:] = a[[2,0,1],:]
# print(a)

# a[:,[1,3]] = a[:,[3,1]]
# print(a)

# a = np.array([
#     [
#         [1,2,3],
#         [2,3,4]
#     ],
#     [
#         [11,12,13],
#         [14,15,16]
#     ],
#     [
#         [23,24,25],
#         [26,27,28]
#     ]
# ])
# print(a)
# a[0,:,:] = a[3,:,:]       
# print(a)

# a = np.array(
#     [1,2,np.nan,4,np.nan,6]
# )
# res = a[~np.isnan(a)]
# print(a)
# print(res)

# res = np.nan_to_num(a,nan = 0)
# print(res)

# a = np.array(
#     [[1,2,3,4,5],[11,12,13,14]]
# )
# np.save('data.npy',a)
# res = np.load('data.npy')     
# print(res)

# with open('data.txt','w') as f:
#     f.write("1.0 2.0 3.0\n4.0 5.0 6.0\n7.0 8.0 9.0")

# data = np.loadtxt('data.txt')
# print(data)

# with open('data1.csv','w') as f:
#     f.write("1.0,2.0,3.0\n4.0,5.0,6.0\n7.0,8.0,9.0")

# data = np.genfromtxt('data1.csv',delimiter=',')
# print(data)

#3x+2y=5
# x+2y=5

# arr1 = np.array([
#     [4,2],[5,3]
# ])
# arr2 = np.array([8,9])

# res = np.linalg.solve(arr1,arr2)
# print(res)
# arr1_inv = np.linalg.inv(arr1)
# res = np.dot(arr1_inv,arr2)

# x = np.linspace(0,10,100)
# y = np.sin(x)

# plt.plot(x,y,label="sinx",color = "red",linestyle = "--")
# plt.title("line graph for sin(x)")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend()
# plt.grid(True)
# plt.show()

# x = np.random.rand(50)
# y = np.random.rand(50)
# plt.scatter(x,y)
# plt.show()

# categories = ["A","B","C","D"]
# values = [10,20,4,30]

# plt.bar(categories,values, color = "red")
# plt.title("bar graph")
# plt.xlabel("categories")
# plt.ylabel("values")
# plt.show()

# data = np.random.rand(1000)
# plt.hist(data,bins=30,color =  "red",alpha=0.8)
# plt.title("histogram")
# plt.xlabel("bins")
# plt.ylabel("frequency")
# plt.show()


labels = ["pyhton","java","c","ruby"]
size = [50,30,15,5]
plt.pie(size,labels=labels,autopct='%1.1f%%',startangle=140)
plt.show()
