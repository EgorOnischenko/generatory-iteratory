nested_list = [
			['a', 'b', 'c'],
			['d', 'e', 'f', 'h', False],
			[1, 2, None]
		]

def gen(nested_list):
	for item_list in nested_list:
		for item in item_list:
			yield item
for item in gen(nested_list):
	print(item)

itemlist= []
for item in gen(nested_list):
	itemlist.append(item)
print(itemlist)
