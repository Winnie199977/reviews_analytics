#讀取資料
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')
#計算平均留言長度
sum_length = 0
for d in data:
	sum_length += len(d)
average = sum_length / len(data)
print('留言的平均長度為:', average)

#統計留言長度小於100的有幾筆
new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('留言長度小於100的總共有 : ', len(new), '筆')