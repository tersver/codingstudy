#문제 설명
#문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

#제한 사항
#s는 길이 1 이상, 길이 8 이하인 문자열입니다.
#입출력 예
#s	    return
#"a234"	false
#"1234"	true

#풀이 방법
#1.문자열의 길이가 4 혹은 6인지 계산한다.
#2.문자열이 숫자로 이루어져 있지 않으면 False 반환
#3.아니면 True 반환
#4.문자열의 길이가 4 혹은 6이 아니면 False 반환

def solution(s):
    if len(s)==4 or len(s) ==6:
        if s.isdigit()==False:
            return False
        return True
    return False