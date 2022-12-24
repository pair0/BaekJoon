import sys

N = int(sys.stdin.readline())
book_hash = {}

for i in range(N):
    book_name = sys.stdin.readline().strip()
    book_hash[book_name] = book_hash.get(book_name, 0) + 1

sorted_book = dict(sorted(book_hash.items())) #딕셔너리 key 기준으로 정렬
print(max(sorted_book, key=sorted_book.get)) #딕셔너리 value 기준으로 max 값 추출 (만약 같은 값이 있다면 가장 앞에 있는 key 값 추출)