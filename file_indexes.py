#计算（MSD:最大相似深度）和（NSSF：相似空间节点个数） 指标
import csv
# 顶点
import time
import os
import psutil

#startTime = time.time()
class Vertex:
    def __init__(self, num):
        self.id = num
        self.connectedTo = []
        self.color = 'white'
        self.dist = 0

    def addNeighbor(self, nbr):
        self.connectedTo.append(nbr)

    def setColor(self, color):
        self.color = color

    def setDistance(self, d):
        self.dist = d

    def getDistance(self):
        return self.dist

    def getColor(self):
        return self.color

    def __str__(self):
        return str(self.id) + "  color: " + self.color + "  dist: " + str(
                self.dist) + '  connextedTo:' + str(
                [x.id for x in self.connectedTo])


# 图
class Graph():
    def __init__(self):
        # 存放所有顶点
        self.vertices = {}

    def addVertex(self, key):
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getVertex(self, n):
        vertex = self.vertices.get(n)
        return vertex

    def __iter__(self):
        return iter(self.vertices.values())


# 计算最长路径
def bfs(graph_dict, start_index):
    graph = Graph()
    # 生成全部顶点
    for key, value in graph_dict.items():
        vertex = graph.addVertex(key)
        if key == start_index:
            vertex.setColor('black')

    # 生成全部邻接节点
    for key, values in graph_dict.items():
        vertex = graph.getVertex(key)
        for value in values:
            # 排除value大于key的邻接节点指向，避免有向图成环
            if value > key:
                ner_vertex = graph.getVertex(value)
                vertex.addNeighbor(ner_vertex)

    start = graph.getVertex(start_index)
    start.setDistance(1)
    distance = 1
    vertlist = []
    vertlist.append(start)

    while (len(vertlist) > 0):
        currentVert = vertlist.pop()
        for nbr in currentVert.connectedTo:
            nbr.setDistance(currentVert.getDistance() + 1)
            if nbr not in vertlist:
                vertlist.insert(0, nbr)
        if distance < currentVert.getDistance():
            distance = currentVert.getDistance()

    return distance

# 计算所有邻接节点
def get_all_connected_vertexs(graph_dict, start_index):
    graph = Graph()
    # 生成全部顶点
    for key, value in graph_dict.items():
        vertex = graph.addVertex(key)
        if key == start_index:
            vertex.setColor('black')

    # 生成全部邻接节点
    for key, values in graph_dict.items():
        vertex = graph.getVertex(key)
        for value in values:
            ner_vertex = graph.getVertex(value)
            vertex.addNeighbor(ner_vertex)

    start = graph.getVertex(start_index)
    vertlist = []
    vertlist.append(start)
    all_connected_vertexs = []
    all_connected_vertexs.append(start.id)

    while (len(vertlist) > 0):
        currentVert = vertlist.pop()
        for nbr in currentVert.connectedTo:
            if nbr not in vertlist and nbr.id not in all_connected_vertexs:
                vertlist.insert(0, nbr)
            if nbr.id not in all_connected_vertexs:
                all_connected_vertexs.append(nbr.id)

    return all_connected_vertexs

# 广度优先计算两点之间最短路径
def bfs_min(start, end):
    start_v = graph.getVertex(start)
    start_v.setDistance(1)
    vertlist = []
    vertlist.append(start_v)
    # 不断循环直到列表为空
    while vertlist:
        # 弹出队列元素
        currentVert = vertlist.pop()

        # 如果找到目标元素，返回当前元素距离，结束函数
        if currentVert.id == end:
            print(currentVert.dist)
            return currentVert.dist

        for nbr in currentVert.connectedTo:
            # 如果当前顶点邻居节点不在队列中，邻居节点添加到队列，如果在队列中，说明该邻居节点与起点的关系更远，所以舍弃
            if nbr not in vertlist:
                nbr.setDistance(currentVert.getDistance() + 1)
                vertlist.insert(0, nbr)


# 深度优先计算最长、最短路径
def max_dis(start, dist):
    start.dist = dist
    if start.connectedTo:
        start.dist += 1
        print(start.dist)
        # dis+=1
        return max([max_dis(ner, start.dist) for ner in start.connectedTo])
        # return  min([max_dis(ner,start.dist) for ner in start.connectedTo ])
    else:
        return start.dist

def all_connected_vertex(start, vertices):
    if start.connectedTo:
        vertices.append(start)
        return (all_connected_vertex(ner, vertices) for ner in start.connectedTo)
    else:
        vertices.append(start)
        return vertices

# 计算两点之间所有路径总数
def bfs_all_path(start, end):
    start_v = graph.getVertex(start)

    count = 0
    start_v.setDistance(1)
    vertlist = []
    vertlist.append(start_v)
    # 不断循环直到列表为空
    while vertlist:
        # 弹出队列元素
        currentVert = vertlist.pop()
        # 如果找到目标元素，说明找一条路径，路径数+1
        if currentVert.id == end:
            count += 1
        for nbr in currentVert.connectedTo:
            nbr.setDistance(currentVert.getDistance() + 1)
            vertlist.insert(0, nbr)
    print(count)
    return count


# 获取最长路径
def find_max_dist(graph):
    for v in graph:
        if v.getColor() == 'black':
            return max_dis(graph.getVertex(v.id), 1)

# 获取最大连通图
def find_max_connected_graph(graph):
    graph = Graph()
    n = 0
    # 生成全部顶点
    for key, value in graph_dict.items():
        vertex = graph.addVertex(key)
        if key == 1:
            vertex.setColor('black')
        n += 1

    # 生成全部邻接节点
    for key, values in graph_dict.items():
        vertex = graph.getVertex(key)
        for value in values:
            # 排除value大于key的邻接节点指向，避免有向图成环
            if value > key:
                ner_vertex = graph.getVertex(value)
                vertex.addNeighbor(ner_vertex)
    for v in graph:
        if v.getColor() == 'black':
            return all_connected_vertex(graph.getVertex(v.id), [])

# 获取最长路径
# def find_max_dist(graph, num):
#     for v in graph:
#         if v.getColor() == 'black':
#             return bfs(graph.getVertex(v.id)), graph.getVertex(num).dist

def get_max_dist_from_graph(graph_dict):
    graph = Graph()
    n = 0
    # 生成全部顶点
    for key, value in graph_dict.items():
        vertex = graph.addVertex(key)
        if key == 0:
            vertex.setColor('black')
        n += 1

    # 生成全部邻接节点
    for key, values in graph_dict.items():
        vertex = graph.getVertex(key)
        for value in values:
            # 排除value大于key的邻接节点指向，避免有向图成环
            if value > key:
                ner_vertex = graph.getVertex(value)
                vertex.addNeighbor(ner_vertex)

    # print('g.vertices.keys():', graph.vertices.keys())
    total_max_dis = find_max_dist(graph)
    # print("The longest distance is", total_max_dis)
    return total_max_dis


def file_indexs(Write_path):
    with open(Write_path +'_dict.txt', "r") as f:  # 打开文件
        graph_dict = f.read()
    graph_dict=eval(graph_dict)

    # print(graph_dict)
    start_index = 0

    # 依次将所有文件放置到第一个文件，生成新的图
    for key_replace in graph_dict.keys():
        # print(key_replace)
        graph_dict_tmp = {}
        for key, values in graph_dict.items():
            new_key = start_index if key == key_replace else key
            new_key = key_replace if key == start_index else new_key
            new_values = []
            for value in values:
                new_value = start_index if value == key_replace else value
                new_value = key_replace if value == start_index else new_value
                new_values.append(new_value)
            graph_dict_tmp[new_key] = new_values
        # graph_dict_tmp = sorted(graph_dict_tmp.items(), key=lambda x:x[0])
        print(graph_dict_tmp)

        # 1、求根节点最长路径
        dist = bfs(graph_dict_tmp, start_index)
        print("第%d个文件起始，最长距离为: %d" % (key_replace, dist))
        result = [key_replace, dist]
        with open(Write_path+"_all_files_longest_path.csv", "a", encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            print(result)
            writer.writerow(result)


        # 2、求连通图的所有节点
        vertex_list = get_all_connected_vertexs(graph_dict, key_replace)
        print("第%d个文件起始，所有连通图节点为: %s" % (key_replace, vertex_list))
        result = [key_replace, len(vertex_list), vertex_list]
        with open(Write_path+"_all_files_connected_vertexs.csv", "a", encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            print(result)
            writer.writerow(result)
#print('程序运行所需时间为: %.4f sec' % (time.time() - startTime))
#print('当前进程的内存使用：%.4f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024))