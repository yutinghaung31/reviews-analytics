date = []
count = 0
with open('reviews.txt', 'r') as f :
    for line in f :
        date.append(line)
        count += 1 # count = count + 1
        if count % 1000 == 0:
            print(len(date))
print('檔案讀取完了,總共有', len(date), '筆資料')

sum_len = 0
for d in date:
    sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(date))


new = []
for d in date:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])