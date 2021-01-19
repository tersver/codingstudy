#문제 설명
#문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
#s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

#제한 사항
#str은 길이 1 이상인 문자열입니다.
#입출력 예
#s	        return
#"Zbcdefg"	"gfedcbZ"

#풀이 방법
#1.주어진 문자열을 배열에 하나씩 저장한다.
#2.배열의 원소를 정렬한다.
#3.정렬된 배열의 원소를 하나하나씩 붙여서 정답 문자열을 만든다.

def solution(s):
    answer = ''
    string=[]
    index=0
    for i in s:
    	string.insert(index,i)
    	index=index+1
    string.sort(reverse=True)
    for i in string:
        answer=answer+i
    return answer