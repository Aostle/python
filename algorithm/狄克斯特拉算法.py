# 定义三个散列表

graph = {}
graph ["start"] = {}
graph ["start"]["a"] = 6
graph ["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

infinity = float("inf")
costs ={}
costs["a"]=6
costs["b"]= 2
costs["fin"]= infinity

parents = {}
parents["a"]  = "start"
parents["b"]  = "start"
parents["fin"] = None


# 寻找开销最小节点
def find_lower_cost_node(costs, processed):
    lower_cost = float("inf")
    lower_cost_node = None
    for node in costs:
        if costs[node] < lower_cost and node not in processed:
            lower_cost = costs[node]
            lower_cost_node = node
    return lower_cost_node

# Dijkstra 最短路径算法 ,也是一种贪心算法
def dijkstra(graph, costs, parents):
    processed = []
    node = find_lower_cost_node(costs, processed)

    # 更新相邻节点开销,如果有邻居发生更新,重新设置其父节点,标记为已处理,
    # 只要还有要处理的节点 , 获取离起点最近的节点 
    while node is not None:
        cost = costs[node]
        neighbors = graph.get(node, {})
        for n in neighbors:
            new_cost = neighbors[n] + cost
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lower_cost_node(costs, processed)
    return costs, parents

# 构建从起点到目标点的路径
def build_path(parents, target):
    path = []
    node = target
    while node is not None:
        path.insert(0, node)
        node = parents.get(node)
    return path

if __name__ == "__main__":
    final_costs, final_parents = dijkstra(graph, costs, parents)
    path = build_path(final_parents, "fin")
    print("最短路径:", " -> ".join(path))
    print("最小开销:", final_costs["fin"])
   


