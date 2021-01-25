#문제 설명
#문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

#제한 사항
#문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
#첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
#입출력 예
#s                 return
#"try hello world" "TrY HeLlO WoRlD"
#입출력 예 설명
#"try hello world"는 세 단어 "try", "hello", "world"로 구성되어 있습니다. 각 단어의 짝수번째 문자를 대문자로, 홀수번째 문자를 소문자로 바꾸면 "TrY", "HeLlO", "WoRlD"입니다. 따라서 "TrY HeLlO WoRlD" 를 리턴합니다.

#풀이 방법
#1.index라는 변수를 선언한다.
#2.문자열의 문자를 하나하나 확인한다.
#3.문자열이 공백일 경우: 단어가 끝났으므로 index를 0으로 초기화 하고 정답문자열에 공백을 더해줌
#4.index를 2로 나눈 나머지가 0일 경우(짝수): 대문자로 변경upper() 하고 정답문자열에 더해줌
#5.index를 2로 나눈 나머지가 0이 아닐 경우(홀수): 소문자로 변경lower() 하고 정답문자열에 더해줌
#6.정답문자열 리턴

def solution(s):
    answer = ''
    index=0
    for i in s:
        if i==" ":
            index=0
            answer=answer+" "
        elif index%2==0:    
            answer=answer+i.upper()
            index=index+1
        else:
            answer=answer+i.lower()
            index=index+1
    return answer