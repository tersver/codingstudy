def solution(phone_book):
	result = {}
	answer=True
	for i in range(0,len(phone_book)):
		if phone_book[i] in phone_book[i+i:len(phone_book)]:
			answer = False
			break		
	return answer