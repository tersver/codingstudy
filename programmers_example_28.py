#문제 설명
#이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
#별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

#제한 조건
#n과 m은 각각 1000 이하인 자연수입니다.
#예시
#입력

#5 3
#출력

#*****
#*****
#*****

#풀이 방법
#1.a,b값을 받아와서 정수로 변환한다.
#2.a개의 * 문자열을 만든다.
#3.b개만큼 문자열을 프린트한다.

a, b = map(int, input().strip().split(' '))
aststring="*"*a
for i in range(b):
    print(aststring)