import numpy as np 

#모양 바꾸기(reshape)
x = np.arange(8)
print(x.shape)

x_2 = x.reshape((2,4))
print(x_2)


#concatenate

x = np.array([0,1,2])
y = np.array([3,4,5])

#concatenate 할 것 들을 list로 포함시켜야됨.
xy = np.concatenate([x,y])
print(xy)


#다차원 concatenate

matrix = np.arange(4).reshape((2,2))

col_base_concat = np.concatenate([matrix,matrix], axis = 0)

row_base_concat = np.concatenate([matrix,matrix], axis = 1)

print(col_base_concat)
print(row_base_concat)


#split

matrix_2 = np.arange(16).reshape((4,4))

#[3] 이 어느 사이를 자를지 구분함. 3번째 열까지 upper, 아니면 lower
upper, lower = np.split(matrix_2, [3], axis = 0)

print(upper, lower)

left, right = np.split(matrix_2, [3], axis =1)

print(left, right)
