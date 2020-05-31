"""Поиск в глубину"""
graph = {'A': ['B', 'C'],
         'B': ['A', 'C', 'D'],
         'C': ['A', 'B', 'D', 'E'],
         'D': ['B', 'C', 'E', 'F'],
         'E': ['C', 'D', 'F'],
         'F': ['D', 'E']}


def sid(graph, start):
    nodes_was_looked = []
    stack = []
    way = []
    revers_way = False
    current_len = 0

    def counter(array):
        temp_len = len(array)
        if temp_len >= current_len:
            print('идет добавление')
            return temp_len
        else:
            print('идет уменьшение,новых узлов не обнаружено')
            return False

    while not nodes_was_looked or stack:
        while not revers_way:
            for edge in graph[start]:
                if edge not in stack and edge not in nodes_was_looked:
                    stack.append(edge)
            current_len = counter(stack)
            nodes_was_looked.append(start)
            if not current_len:
                current_len = len(stack)
                revers_way = True
                break
            way.append(start)
            start = stack.pop(-1)
            way[-1] += '>' + start
        while revers_way:
            if not stack:
                revers_way=False
            else:
                node_not_looked = stack.pop(-1)
                for node in nodes_was_looked:
                    if node_not_looked in graph[node]:
                        way.append(node + '>' + node_not_looked)
                        break



