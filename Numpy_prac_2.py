import numpy as np  

x_2 = np.random.randint(10, size = (3,4))

print(x_2)

#배열에서 확인할 수 있는 속성.
#number of dimension
print(x_2.ndim)

print(x_2.shape)

#배열 안에 들어있는 원소
print(x_2.size)

print(x_2.dtype)



#Indexing

x_3 = np.arange(7)

print(x_3)

print(x_3[3])

print(x_3[0])

#추출 start ~ end - 1 로 나옴 
print(x_3[1:4])

#처음부터 end - 1까지 
print(x_3[:4])

#2씩 건너뛰면서 출력 
print(x_3[::2])