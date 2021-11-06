drive = input('你有沒有開過車?')
age = input('你的年齡?')
age = int(age)
if drive != '有' and drive != '沒有':
	raise SystemExit

if drive == '有':
	if age >= 18:
		print('你通過測驗了!')

	else:
		print('你怎麼會開過呢?')
elif drive == '沒有':
	if age >= 18:
		print('快去學!')
	else:
		print('沒事兒')






