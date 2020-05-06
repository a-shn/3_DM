import csv

BUSKETS = 150000
buckets1 = [[]] * BUSKETS
buckets2 = [[]] * BUSKETS
prod_counter = dict()
baskets = dict()
doubletones = []
with open('transactions.csv', newline='') as csvfile:
	timereader = csv.DictReader(csvfile)
	for w in timereader:
		prod_code = w['PROD_CODE;BASKET_ID'].split(';')[0]
		basket_id = w['PROD_CODE;BASKET_ID'].split(';')[1]
		if not baskets.__contains__(basket_id):
			baskets[basket_id] = []
			baskets[basket_id].append(prod_code)
		else:
			baskets[basket_id].append(prod_code)
		if not prod_counter.__contains__(prod_code):
			prod_counter[prod_code] = 1
		else:
			prod_counter[prod_code] += 1

for basket in baskets:
	for i in range(len(baskets[basket]) - 1):
		for j in range(len(baskets[basket]) - i - 1):
			tmp = set()
			tmp.add(int(baskets[basket][i][3:]))
			tmp.add(int(baskets[basket][i + j + 1][3:]))
			doubletones.append(tmp)


def hash1(i, j):
	return (i + j) % BUSKETS


def hash2(i, j):
	return (2 * i + j) % BUSKETS

for doubletone in doubletones:
	buckets1[hash1(*doubletone)].append(doubletone)
	buckets2[hash2(*doubletone)].append(doubletone)
