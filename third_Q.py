"""
Author : JunE_HC
Completed Date: 28/09/2017 DD/MM/YYYY
Kakao_Blind_Test Question 3
"""

# int cacheSize, 0<=cacheSize<=30
cacheSize = int(input("input cache size: "))
cities = []
total_time = 0
while (True):
	input_city = input("input cities: ").lower()
	if (input_city == ""):
		break
	else:

		if (cities.count(input_city) == 0):
			cities.append(input_city)
			if (len(cities) > cacheSize):
				del cities[0]
			total_time += 5
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
