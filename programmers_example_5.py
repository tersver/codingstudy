def solution(arr, divisor):
    answer = []
    index=0
    for i in arr:
    	if i%divisor==0:
    		answer.insert(index,i)
    		index=index+1
    answer.sort()
    return answer