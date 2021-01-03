#문제 설명
#스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.

#예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.

#종류	이름
#얼굴	동그란 안경, 검정 선글라스
#상의	파란색 티셔츠
#하의	청바지
#겉옷	긴 코트
#스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

#제한사항
#clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
#스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
#같은 이름을 가진 의상은 존재하지 않습니다.
#clothes의 모든 원소는 문자열로 이루어져 있습니다.
#모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
#스파이는 하루에 최소 한 개의 의상은 입습니다.
#입출력 예
#clothes	                                                                           return
#[[yellow_hat, headgear], [blue_sunglasses, eyewear], [green_turban, headgear]]	          5
#[[crow_mask, face], [blue_sunglasses, face], [smoky_makeup, face]]	                      3
#입출력 예 설명
#예제 #1
#headgear에 해당하는 의상이 yellow_hat, green_turban이고 eyewear에 해당하는 의상이 blue_sunglasses이므로 아래와 같이 5개의 조합이 가능합니다.

#1. yellow_hat
#2. blue_sunglasses
#3. green_turban
#4. yellow_hat + blue_sunglasses
#5. green_turban + blue_sunglasses#
#예제 #2
#face에 해당하는 의상이 crow_mask, blue_sunglasses, smoky_makeup이므로 아래와 같이 3개의 조합이 가능합니다.

#1. crow_mask
#2. blue_sunglasses
#3. smoky_makeup


#풀이방법
#1.clothes 배열에는, 복수의 옷(1번째 원소: 의상 이름, 2번째 원소: 의상 종류)이 들어있음.
#  clothes 배열의 각 원소에 대하여, 해당 원소의 두번째 원소 종류를 해시에 등록
#2.clothes 배열의 각 원소에 대하여, 두번째 원소의 갯수를 카운트. 초기값은 1
#  같은 이름을 가진 의상은 존재하지 않으므로, 중복체크 없이 카운트 플러스
#3.서로 다른 옷의 조합의 수를 계산
#  계산 방법 : 각 의상 종류의 갯수를 다 곱함 - 1
#  계산 결과에 -1을 하는 이유 : 스파이는 하루에 최소 한개의 의상은 입으므로, 전부 안입는 경우의 수를 뺌


def solution(clothes):
	variation = {}
	answer=1
	for vary in clothes:
		variation[vary[1]]=1
	for cloth in clothes:
		variation[cloth[1]]=variation[cloth[1]]+1
	for summ in variation.values():
		answer = int(answer) * int(summ)
	answer=answer-1
	return answer