#문제 설명
#두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
#예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

#제한 조건
#a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
#a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
#a와 b의 대소관계는 정해져있지 않습니다.
#입출력 예
#a	b	return
#3	5	12
#3	3	3
#5	3	12

#풀이 방법
#1.a부터b까지의 숫자 갯수를 센다.
#2.a와 b의 중간값을 구한다.
#3.중간값 곱하기 갯수가 정답.
#4.a와b가 같을경우, 해당숫자 1개뿐이므로 해당숫자를 리턴.


def solution(a, b):
    answer = 0
    length=0
    mid=0
    if a>b:
    	length=a-b+1
    elif a<b:
    	length=b-a+1
    elif a==b:
        return a
    mid=(a+b)/2
    answer=mid*length
    return answer