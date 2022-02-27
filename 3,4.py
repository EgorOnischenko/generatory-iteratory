


nested_list = [
		['a', 'b', 'c'],
		['d', 'e', 'f', 'h', False],
		[1, 2, None]
	]


class myclass:

    def __init__(self, items):
        self.items = items


    def __iter__(self):

        self.currentArray = 0
        self.currentItem = 0
        return self

    def __next__(self):

        if self.currentArray < len(self.items):

            if self.currentItem < len(self.items[self.currentArray]):
                self.currentItem += 1

                return self.items[self.currentArray][self.currentItem-1]
            else:

                self.currentItem = 0
                self.currentArray += 1

                return next(self)
        else:
            raise StopIteration

myclass = myclass(nested_list)
print(myclass)
for i in myclass:
    print (i)

flat_list = [item for item in myclass]
print(flat_list)

