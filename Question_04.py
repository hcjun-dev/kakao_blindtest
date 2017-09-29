"""
셔틀버스

- 셔틀은 09:00부터 총 n회 t분 간격으로 역에 도착하며
- 하나의 셔틀에는 최대 m명의 승객이 탈 수 있다
- 셔틀은 도착했을 때 도착한 순간에 대기열에 선 크루까지 포함해서 대기 순서대로
	태우고 바로 출발한다. 예를 들어 09:00에 도착한 셔틀은 자리가 있다면 09:00에
	줄을 선 크루도 탈 수 있다

0< n =10
0<t<= 60
0<n<=45




	# input values
	n, t, m=0
	n = input("input n: ")
	t = input("input t: ")
	m = input("input m: ")
	timetable = []
	while(True):
		input_temp = input("input timetable: ")
		if input_temp == "":
			break
		else:
			timetable.append(input_temp)


	print(timetable)
"""
def main():
	submain(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"])
	submain(2, 10, 2, ["09:00", "09:09", "08:00"])
	submain(2, 1, 2, ["09:00", "09:00","09:00", "09:00"])
	submain(1, 1, 5, ["00:01", "00:01", "00:01", "00:01","00:01"])
	submain(1, 1, 1, ["23:59"])
	submain(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59",
	                     "23:59", "23:59", "23:59", "23:59", "23:59",
	                     "23:59", "23:59", "23:59", "23:59", "23:59",
	                     "23:59", ])



def submain(n,t,m,*timetable):
	print(str(n)+" "+str(t)+" "+str(m)+" "+ str(timetable))











main()