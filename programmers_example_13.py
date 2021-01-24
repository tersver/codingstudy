#문제 설명
#어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다. z는 1만큼 밀면 a가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

#제한 조건
#공백은 아무리 밀어도 공백입니다.
#s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
#s의 길이는 8000이하입니다.
#n은 1 이상, 25이하인 자연수입니다.
#입출력 예
#s	        n	result
#"AB"	    1	"BC"
#"z"	    1	"a"
#"a B z"	4	"e F d"

#풀이 방법
#1.s의 문자열 하나하나씩 확인한다.
#2.대문자인지 소문자인지 확인(방법은 여러가지, 여기서는 A-Z, a-z까지의 문자열중에 위치를 찾는것으로 확인)
#3.index를 구하여, n만큼 더함
#4.z다음에는 a이므로,index가26을 넘었을 때는, 26을 빼준다.
#5.조정된 index의 문자를 정답문자열에 붙여준다.
#6.공백일 경우는 공백을 붙여준다.
#7.다 붙여주면 정답 문자열을 리턴

def solution(s, n):
    answer = ''
    capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower="abcdefghijklmnopqrstuvwxyz"
    for letter in s:
    	if letter in capital:
    		index=capital.find(letter)
    		index=index+n
    		if index>=26:
    			index=index-26
    		answer=answer+capital[index]
    	if letter in lower:
    		index=lower.find(letter)
    		index=index+n
    		if index>=26:
    			index=index-26
    		answer=answer+lower[index]
    	if letter == " ":
    		answer=answer+" "
    return answer