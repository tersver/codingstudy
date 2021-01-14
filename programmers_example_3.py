#문제 설명
#단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

#제한사항
#s는 길이가 1 이상, 100이하인 스트링입니다.
#입출력 예
#s	        return
#"abcde"	"c"
#"qwer"	    "we"

#풀이 방법
#1.문자열의 길이를 구한다.
#2.문자열의 길이를 2로 나눠본다.
#3.문자열의 길이가 짝수일 때 : 문자열 길이/2인 index변수를 선언, 문자열을 index-1~index까지 자른다.
#4.문자열의 길이가 홀수일 때 : 문자열 길이/2인 index변수를 선언, 문자열의 index번째 원소를 갖고온다.
#※문자열의 index는 0부터 시작하므로, K번째 원소는 K-1 index로 접근한다.
#※문자열을 자를때, 파이썬에서는 끝이 K면 K-1번쨰 index까지 자르기 때문에, 1을 더해준다.

def solution(s):
    answer = ''
    if len(s)%2==0:
        index=int(len(s)/2)
        answer=s[index-1:index+1]
    else:
        index=int(len(s)/2)
        answer=s[index]
    return answer