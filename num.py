import random
start = input('決定隨機數字開始值: ')
end = input('決定隨機數字結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1 #count = count + 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜對了')
		print('你在第', count, '次, 猜中了')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')	
