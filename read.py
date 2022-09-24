#讀取資料
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
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

#取出留言中有'good' 的留言
good = []
for d in data:
	if 'good' in d:
		good.append(d)

print('留言中有提到"good"的總共有:', len(good), '筆')

#清單快寫法(補充)
#good = [d for d in data if 'good' in d]
# 		 d 表示要寫進清單裡面的值

#是否有提到 'bad'
#bad = ['bad' in d for d in data]

#文字計數
wc = {} #字典
#用迴圈列出所有評論清單
for d in data:
	#用空白符號分割成小清單，清單中個別儲存單字
	words = d.split(' ')
	#用迴圈列出所有分割後的小清單(單字)
	for word in words:
		#判斷單字是否已在字典裡
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

# #列出 單字 有出現超過一百次的清單
# for word in wc:
# 	if wc[word] > 1000000:
# 		print(word, wc[word])

while True:
	word = input('請問你想查什麼字 : ')
	if word == 'q':
		break
	elif word not in wc:
		print('!這個字沒有出現過!')
		continue
	print(word, '出現過的次數為', wc[word], '次')

print('-----感謝使用-----')