#문제 설명
#길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.

#제한 조건
#n은 길이 10,000이하인 자연수입니다.
#입출력 예
#n   return
#3   "수박수"
#4   "수박수박"

#풀이 방법
#1.n을 2로 나눈 몫을 구한다.
#2.n을 2로 나눈 나머지를 구한다.
#3.몫만큼 수박을 반복해서 붙인다.
#4.나머지가 1이면 수를 붙인다.
#5.정답문자열을 리턴한다.

import math

def solution(n):
    answer = ''
    div=math.floor(n/2)
    nam=n%2
    i=1
    while i<=div: 
        answer=answer+"수박"
        i=i+1
    if nam:
        answer=answer+"수"
    return answer