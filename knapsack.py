import numpy as np

values = np.array([3,4,3,5,8,10])
weights = np.array([2,3,4,4,5,9])
items = len(weights)
capacity = 20


class item:
    def __init__(self,value,weight,number=0):
        self.value=value
        self.weight=weight
        self.number=number

class knapsack:
    def __init__(self,capacity=0):
        self.capacity=capacity
        self.items=[]
        self.weight=0

    def push_item(self,item):
        if self.weight+item.weight <= self.capacity:
            self.items.append(item)
            self.weight=self.get_weight()
        else:
            print('мешок переполнен')

    def __len__(self):
        return len(self.items)

    def get_value(self):
        return sum(x.value for x in self.items)

    def get_weight(self):
        return sum(x.weight for x in self.items)

    def get_numbers_of_items(self):
        return [item.number for item in self.items]



items=[item(v,w,n+1) for v,w,n in zip(values,weights,range(len(values)))]

items_max_value=sorted(items,key=lambda x: x.value,reverse=True)

knap= knapsack(20)

for item in items_max_value:
    print(item.weight)
    knap.push_item(item)

print(knap.get_value(),knap.get_weight(),knap.get_numbers_of_items())