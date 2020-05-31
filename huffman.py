from collections import Counter as con

data="beep boop beer!"

class Node:
    def __init__(self,name=None,value=None,left=None,right=None):
        self.name=name
        self.value=value
        self.left=left
        self.right=right


count=con(data)
deque=count.most_common()[::-1]


def build_tree(deq):
    new_node=None
    while len(deq)>1:
        name,value=deq.pop(0)
        new_node = Node(left=Node(name, value) if not isinstance(name,Node) else name)
        name_right, value_right = deq.pop(0)
        new_node.right = Node(name_right, value_right) if not isinstance(name_right,Node) else name_right
        new_node.value = new_node.left.value + new_node.right.value
        for n in range(0, len(deq)):
            if n==len(deq)-1:
                deq.insert(n+1,(new_node,new_node.value))
                break
            if new_node.value>deq[n][1] and new_node.value<deq[n+1][1]:
                deq.insert(n,(new_node,new_node.value))
                break
            elif new_node.value<=deq[n][1]:
                deq.insert(n, (new_node, new_node.value))
                break
    return new_node

tree=build_tree(deque)


def travers_tree(tree,way,dict_):
    table=dict_
    path=way
    if tree.left is not None:
        path.append(0)
        travers_tree(tree.left,path,table)
        path.pop(-1)
    else:
        table[tree.name] = "".join(str(x) for x in path)
        return table

    if tree.right is not None:
        path.append(1)
        travers_tree(tree.right,path,table)
        path.pop(-1)
    else:
        table[tree.name] = "".join(str(x) for x in path)
        return table

    return table

table=travers_tree(tree,[],{})

string=""

for char in data:
    string+=table[char]

print(string)



