# News Clustering
# ex.
# [FRANCE]
# [fr,ra,an,ce]
# [1, 2, 3, 4 ]

# [aa1+aa2] = [aa, aa]
# [AAAA12]  = [aa,aa,aa,aa]
# [2] - [1] = []
#
# 총 원소의 수는 n/2+1

import collections

def main():
	str1 = input("Input str1: ").lower()
	str2 = input("Input str2: ").lower()

	str1 = inputStr(str1)
	str2 = inputStr(str2)
	if (str1 == str2):
		print(65536)
	else:
		print("{:d}".format(int(jaccard(str1, str2))))


def inputStr(stringlist):
	returnList = []
	for i in range(0, len(stringlist) - 1):
		if (not stringlist[i].isalpha() or not stringlist[i + 1].isalpha()):
			continue
		returnList.append(stringlist[i] + stringlist[i + 1])
	print(returnList, "processed inputStr")
	return returnList


def jaccard(list1, list2):
	return unify(list1, list2) / intersect(list1, list2) * 65536


def unify(inputlist1, inputlist2):
	returnCounter = collections.Counter(inputlist1) & collections.Counter(inputlist2)
	print(list(returnCounter), "unified")
	return len(list(returnCounter))


def intersect(inputlist1, inputlist2):
	returnCounter = collections.Counter(inputlist1) | collections.Counter(inputlist2)
	print(list(returnCounter), "intersected")
	return len(list(returnCounter))


main()
