#문제 설명
#두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

#제한 사항
#두 수는 1이상 1000000이하의 자연수입니다.
#입출력 예
#n   m   return
#3   12  [3, 12]
#2   5   [1, 10]
#입출력 예 설명
#입출력 예 #1
#위의 설명과 같습니다.

#입출력 예 #2
#자연수 2와 5의 최대공약수는 1, 최소공배수는 10이므로 [1, 10]을 리턴해야 합니다.

#풀이 방법
#1.최대공약수, 최소공약수 변수를 1로 선언한다.
#2.첫번째 숫자가 두번째 숫자보다 클경우: 두번째 숫자로 첫번째 숫자를 나눈 나머지를 비교한다.
#  첫번째 숫자가 두번째 숫자보다 작을 경우 : 첫번째 숫자로 두번째 숫자를 나눈 나머지를 비교한다.
#2-1.나머지가 0이 아닐 경우 : 두번째 숫자를 첫번째 숫자로 하고, 나머지를 두번째 숫자로 한다.
#                           나머지를 최대공약수에 곱하고, 2를 반복한다.
#2-2.나머지가 0일 경우 : 두번째 수를 최대공약수에 곱하고, 최종 최대공약수로 설정한다.
#3.최소공배수 : 첫번째 숫자 x 두번째 숫자 / 최대공약수
#4. 최대공약수와 최소공배수를 배열에 담고, 리턴한다.

def solution(n, m):
    answer = []
    gcd = 1
    lcm = 1
    tempn = n
    tempm = m
    if n >= m:
        if tempm % tempn ==0:
            gcd=tempn
        else:
            while tempn % tempm != 0:
                gcd = gcd * tempm
                temp = tempn % tempm
                if temp==0:
                    break
                tempn = tempm
                tempm = temp
        gcd=tempm
        answer.append(gcd)
        lcm = int(lcm * n * m / gcd)
        answer.append(lcm)
    else:
        if tempm % tempn ==0:
            gcd=tempn
        else:
            while tempm % tempn != 0:
                gcd = gcd * tempn
                temp = tempm % tempn
                if temp ==0:
                    break
                tempm = tempn
                tempn = temp
        gcd=tempn
        answer.append(gcd)
        lcm = int(lcm * n * m / gcd)
        answer.append(lcm)

    return answer