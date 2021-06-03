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