"""
Author : JunE_HC
Completed Date: 28/09/2017 DD/MM/YYYY
Kakao_Blind_Test Question 3
"""

# int cacheSize, 0<=cacheSize<=30
cacheSize = int(input("input cache size: "))
cities = []
total_time = 0
# 입력값이 빈 값이 들어올때까지 지금 현재 도시를 입력받는다
while (True):
	input_city = input("input cities: ").lower()
	if (input_city == ""):
		break
	else:
	#입력 받은 도시가 원래 리스트에 없었을 경우
		if (cities.count(input_city) == 0):
			#캐시 사이즈보다 커도 일단 집어넣고 본다
			cities.append(input_city)
			#만약 리스트 사이즈가 캐시 사이즈보다 커지면 맨 처음
			#엔트리를 지운다
			if (len(cities) > cacheSize):
				del cities[0]
			total_time += 5
	#입력 받은 도시가 원래 리스트에 있었을 경우
		else:
			total_time += 1

print(total_time)

"""
[“Jeju”,    5   J
“Pangyo”,   10  JP
“Seoul”,    15  JPS
“NewYork”,  20  JPSN
“LA”,       25  JPSNL
“SanFrancisco”, 30 PSNLF
“Seoul”,    31  PSNLF
“Rome”,     36  SNLFR
“Paris”,    41  NLFRP
“Jeju”,     46  LFRPJ
“NewYork”,  51  FRPJN
“Rome”]     52  FRPJN

"""
