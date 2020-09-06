import numpy as np  

#집계함수 및 마스킹 연산

#집계 : 궁금한 데이터에 대해 요약 통계를 볼 수 있다.

x = np.arange(8).reshape((2,4))

#sum(x)
print(np.sum(x))

print(np.sum(x,axis = 0))
print(np.sum(x,axis = 1))

#min, max
print(np.min(x))
print(np.max(x))

#mean, standard deviation

print(np.mean(x))
print(np.std(x))


#마스킹 연산 : True, False Array를 통해서 특정 값들을 뽑아내는 연산법

y = np.arange(5)

print(x < 3)

print(x < 5)

#True인 index의 array를 추출 
print(x[x < 3])