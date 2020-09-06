import numpy as np  

#Broadcasting 연산

#=> shape 이 다른 array끼리 연산하는 것을 말한다.

#EX_1
matrix = np.arange(9).reshape((3,3))

matrix_2 = matrix + 5
# 5 * np.ones((3,3))을 더하는 셈임.
print(matrix_2)

#EX_2
print(matrix + np.array([1,2,3]))
#[1,2,3] 을 밑으로 쭉 복사해서 사이즈 맞춰서 더한 것.


#EX_3

print(np.arange(3).reshape((3,1)) + np.arange(3))
