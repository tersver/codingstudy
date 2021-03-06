#프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

#또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

#먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

#제한 사항
#작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
#작업 진도는 100 미만의 자연수입니다.
#작업 속도는 100 이하의 자연수입니다.
#배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
#입출력 예
#progresses	speeds	return
#[93, 30, 55]	[1, 30, 5]	[2, 1]
#[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
#입출력 예 설명
#입출력 예 #1
#첫 번째 기능은 93% 완료되어 있고 하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능합니다.
#두 번째 기능은 30%가 완료되어 있고 하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능합니다. 하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 첫 번째 기능이 배포되는 7일째 배포됩니다.
#세 번째 기능은 55%가 완료되어 있고 하루에 5%씩 작업이 가능하므로 9일간 작업 후 배포가 가능합니다.

#따라서 7일째에 2개의 기능, 9일째에 1개의 기능이 배포됩니다.

#입출력 예 #2
#모든 기능이 하루에 1%씩 작업이 가능하므로, 작업이 끝나기까지 남은 일수는 각각 5일, 10일, 1일, 1일, 20일, 1일입니다. 어떤 기능이 먼저 완성되었더라도 앞에 있는 모든 기능이 완성되지 않으면 배포가 불가능합니다.

#따라서 5일째에 1개의 기능, 10일째에 3개의 기능, 20일째에 2개의 기능이 배포됩니다.

#풀이 방법
#1.먼저 작업진도에 개발속도를 더하여 해당 작업들이 끝나는 일수를 구한다.(if 작업진도<=100)
#2.끝나는 일수를 저장한 배열에서 하나씩 빼서 비교한다.
#2-1.앞에 일수가 뒤에 일수보다 크거나 같을 경우 : 끝나는 일수에서 하나 더 빼고 카운트 변수 증가(if앞에 일수>=뒤에 일수)
#2-2.앞에 일수가 뒤에 일수보다 작을 경우 : 현재까지 카운트 변수를 정답배열에 저장, 카운트 변수 초기화
#3.끝나는 일수를 저장한 배열의 원소가 없어질때까지 반복, 없어지면 answer 정답 배열 리턴



def solution(progresses, speeds):
	answer = []
	days=[]
	for i in range(0,len(progresses)):
		count=0
		while progresses[i]<100:
			count=count+1
			progresses[i]=progresses[i]+speeds[i]
		days.insert(i,count)
	index=0
	while len(days)>0:
		count=1
		day = days.pop(0)
		if len(days)>0:
			while day>=days[0]:
				days.pop(0)
				count=count+1
				if len(days) == 0:
					break
			answer.insert(index,count)
			index=index+1
		else:
			answer.insert(index,1)
	return answer
