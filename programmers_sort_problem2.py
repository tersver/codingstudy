#문제 설명
#배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

#예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

#array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
#1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
#2에서 나온 배열의 3번째 숫자는 5입니다.
#배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

#제한사항
#array의 길이는 1 이상 100 이하입니다.
#array의 각 원소는 1 이상 100 이하입니다.
#commands의 길이는 1 이상 50 이하입니다.
#commands의 각 원소는 길이가 3입니다.
#입출력 예
#array	                commands	                        return
#[1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]
#입출력 예 설명
#[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.
#[1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.
#[1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.

#풀이 방법
#1.커맨드 배열 안 원소를 돌아가면서 연산한다.
#2.커맨드의 0번째원소부터 1번째원소까지 array를 자른다.
#3.자른 array를 sort한다.
#4.sort한 array에서 커맨드의 2번째원소 index에 해당하는 원소를 answer에 저장한다.
#5.answer를 출력
#※주의사항
#k번째 수는 프로그래밍 언어로 표현하면 index인데, 1번째 원소는 index가 0이므로, 각각의 index에 -1을 해줘야 한다.


def solution(array, commands):
	answer = []
	index=0
	for command in commands:
		temparray = array[command[0]-1:command[1]]
		temparray.sort()
		answer.insert(index,temparray[command[2]-1])
		index=index+1
	return answer