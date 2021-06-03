# 讀取檔案

data = []
count = 0
data_len = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		data_len += len(line.strip())
		if count % 10000 ==0:
			print(len(data)) 
print('file has benn read, there are', len(data), 'data')
print('the average len of this file is %.5f longs' % (data_len / len(data)))

sum_len = 0
for d in data:
	sum_len += len(d)
print('average is', sum_len/len(data))

small_len = []
for s in data:
	if len(s) < 100:
		small_len.append(s)
print(len(small_len))

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print(len(good))


#list comprehension 清單快寫法

good_f = [d for d in data if 'good' in d] 
#清單名=  運算   變數 清單     篩選條件
#運算d就是append(d)的d，將其裝進good_f,所以如果appen(d)改成append(1),則會有一大堆1寫入
print(len(good_f))


bad_f = ['bad' in d for d in data ] #運算可以有好幾種，像這個範例就是布林值

bad = []
for d in data:
	bad.append('bad' in d)