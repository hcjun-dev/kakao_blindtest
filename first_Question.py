# 입력 부
"""
입력으로 지도의 한 변의 크기 n과 3개의 정수 배열 arr1, arr2가 들어온다
1<=n=16
arr1, arr2는 길이 n인 정수 배열로 주어진다
정수 배열의 각 원소 x를 이진수로 변환했을 때의 길이는 n이하이다 즉
0<= x <=2^n-1을 만족한다

"""
dimension_size = int(input("Enter your desired dimension: "))
print("n = " + str(dimension_size))

arr1 = [] # stores int values in list
arr2 = [] # stores int values in list
final_arr = [] # stores bit values in list
i = 0
array_length = 0
while i < dimension_size:
	temp_input = int(input("Put " + str(i) + "th number for arr1: "))
	arr1.append(temp_input)
	i += 1
array_length = len(arr1)

i = 0
while i < dimension_size:
	temp_input = int(input("Put " + str(i) + "th number for arr2: "))
	arr2.append(temp_input)
	i += 1

#  bit operation OR
for i in range(array_length):
	final_arr.append(str(format(arr1[i] | arr2[i],'05b')))
	final_arr[i] = final_arr[i].replace('1', '#')
	final_arr[i] = final_arr[i].replace('0', ' ')
# now final_arr has the map.


for i in final_arr:
	print(i)