#문제 설명
#행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

#제한 조건
#행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
#입출력 예
#arr1	        arr2	        return
#[[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
#[[1],[2]]	    [[3],[4]]	    [[4],[6]]

#풀이 방법
#1.행의 길이만큼 for루프를 돈다.
#2.열의 길이만큼 for루프를 돈다.
#3.각각 원소를 더한다.
#4.정답 배열에 추가한다.
#5.정답 배열을 리턴

def solution(arr1, arr2):
    answer = []
    for i in range(0,len(arr1)):
        element=[]
        for j in range(0,len(arr1[i])):
            element.append(arr1[i][j]+arr2[i][j])
        answer.append(element)
    return answer