data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_length = 0
for d in data:
	sum_length += len(d)
average = sum_length / 1000000
print('留言的平均長度為:', average)