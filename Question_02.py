"""
RULES:
다트 게임은 총 3번의 기회로 구성된다.
각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수^1 , 점수^2 , 점수^3 )으로 계산된다.
옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
"""


def main():
	raw_result = input("Please input the result of Dart: ")
	score = []
	final_score = 0
	result = list(raw_result)

	# 세번 던진 결과를 각각 저장한다

	for i in range(3):  # 3 라운드 진행
		# 첫째 숫자 저장
		if (result[1].isdigit()):  # 첫째 숫자가 10일때
			score_temp = 10
			del result[0:1]
		else:
			score_temp = int(result[0])
			del result[0]

		# 둘째 보너스 합산 저장
		if (result[0] == "S"):
			score_temp = score_temp ** 1
		elif (result[0] == "D"):
			score_temp = score_temp ** 2
		elif (result[0] == "T"):
			score_temp = score_temp ** 3
		del result[0]

		#셋째 옵션 계산 - # (이번턴만 마이너스)
		if (len(result) != 0):
			if (result[0] == "#"):
				score_temp = score_temp * (-1)
				del result[0]
		score.append(score_temp)
		#셋째 옵션 계산 - * (이번턴과 바로 전턴 두배)
		if (len(result) != 0):
			if (result[0] == "*"):
				if (len(score) == 1):
					score[i] *= 2
				else:
					score[i - 1] *= 2
					score[i] *= 2
				del result[0]

	for each in score:  # 총 점수 합산
		final_score += each

	print(final_score)


main()
