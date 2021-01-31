#문제 설명
#정수 num이 짝수일 경우 Even을 반환하고 홀수인 경우 Odd를 반환하는 함수, solution을 완성해주세요.

#제한 조건
#num은 int 범위의 정수입니다.
#0은 짝수입니다.
#입출력 예
#num	return
#3	    "Odd"
#4	    "Even"

#풀이 방법
#1.주어진 수를 2로 나눈 나머지가 0일 경우(짝수) : "Even" 리턴
#2.주어진 수를 2로 나눈 나머지가 0이 아닐 경우(홀수) : "Odd" 리턴

def solution(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"