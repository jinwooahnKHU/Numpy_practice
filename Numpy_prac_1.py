#Numpy(Numerical Python)
#List보다 연산이 빠름!
import numpy as np  

#python list 와 다르게 array는 단일 타입으로 구성됨 => dtype 사용

arr = np.array([1,2,3,4], dtype = float)

print(arr)

#array의 dtype을 알 수 있는 방법
print(arr.dtype)

#array dtype 변경하기
arr.astype(int)

#여러가지 array 생성
arr_1 = np.array(range(10))

print(arr_1)

#1로 구성된 array
arr_2 = np.ones((3,5), dtype = float)

print(arr_2)

#0으로 구성된 array
arr_3 = np.zeros(10, dtype = float)

print(arr_3)

#arange는 range함수와 같은 역할. (start, end, step)
arr_4 = np.arange(0,20,2)

print(arr_4)

#(start, end, n) : 시작과 끝 사이에 n 개의 원소를 갖는 array
arr_5 = np.linspace(0,1,5)

print(arr_5)

#난수 활용 array
arr_6 = np.random.random((2,2))

print(arr_6)

#평균이 0, 표준편차가 1이고 사이즈 2by2 인 array생성
arr_7 = np.random.normal(0,1,(2,2))

print(arr_7)

#0과 10 사이에 정수로 정해줌
arr_8 = np.random.randint(0,10,(2,2))

print(arr_8)
