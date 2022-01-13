import requests
import fake_useragent
import json
import datetime


class Parcer:
	def __init__(self):
		self.url = 'https://market.csgo.com/api/v2/prices/class_instance/RUB.json'
		user = fake_useragent.UserAgent().random
		self.headers = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'user-agent': user
		}

	def get_data(self):
		data = []
		current_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
		req = requests.get(self.url, headers=self.headers)
		db = req.json()
		items = db['items']
		for item in items:
			try:
				sale = 100 - (float(db['items'][item]['price'])/float(db['items'][item]['avg_price'])) * 100
				if db['items'][item]['avg_price'] != None and sale > 20:
					title_goods = db['items'][item]['market_hash_name']
					buy_order = db['items'][item]['buy_order']
					rarity = db['items'][item]['ru_rarity']
					quality = db['items'][item]['ru_quality']
					img = 'https://cdn.csgo.com//item/' + title_goods + '/300.png'
					link = 'https://market.csgo.com/item/' + item.replace('_', '-') + '-' + title_goods
					popularity = db['items'][item]['popularity_7d']
					price = db['items'][item]['price']
					avg_price = db['items'][item]['avg_price']
					# print(title_goods, buy_order, rarity, quality, link, popularity, sale, price, '#'*20, sep='\n')
					data.append({
							'img': img,
							'title': title_goods,
							'price': price,
							'avg_price': avg_price,
							'sale': sale,
							'link': link,
							'quality': quality,
							'rarity': rarity,
							'buy_order': buy_order,
							'popularity': popularity
						})
			except:
				continue

		with open('data/content.json', 'w', encoding='utf-8') as json_file:
			json.dump(data, json_file, indent=4, ensure_ascii=False)


	def show_all(self):
		with open('data/content.json', 'r', encoding='utf-8') as json_file:
			src = json.load(json_file)
		text_message = []
		for item in src:

			title_goods = item['title']
			quality = item['quality']
			img = item['img']
			link = item['link']
			price = item['price']
			sale = round(item['sale'], 2)
		
			text_message.append('\n🔥 Успей забрать! 🔥\n' + '💥 ' + title_goods + ' 💥' + '\n🧩 Качество : ' + quality + ' 🧩\n💵 Цена: ' + price + ' 💵\n' '💼 Скидка : ' + str(sale) + '% 💼\n' + '👇🏼 Все остальное тут 👇🏼\n' + '👓 ' + link + ' 👓')

		return text_message

	def run(self):
		self.show_all()


if __name__ == '__main__':
	app = Parcer()
	app.run()