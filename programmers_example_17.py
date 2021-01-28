#문제 설명
#함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

#제한 조건
#n은 1이상 8000000000 이하인 자연수입니다.
#입출력 예
#n	return
#118372	873211

#풀이 방법
#1.자연수를 문자열화 시킨다.
#2.문자열을 리스트화 시킨다.
#3.리스트를 내림차순으로 정렬한다.
#4.리스트의 원소별로 정답 문자열에 더해준다.
#5.정답 문자열을 자연수화 시킨다.
#6.자연수화 된 문자열을 리턴한다.

def solution(n):
    answer = 0
    strn=str(n)
    arrn=list(strn)
    arrn.sort(reverse=True)
    stranswer=''
    for i in arrn:
        stranswer=stranswer+i
    answer=int(stranswer)
    return answer