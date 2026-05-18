from collections import deque
# 用散列表 构建图
graph =  {}
graph["you"] = ["alice", "bob","claire"]
graph["alice"]=["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom","jonny"]

graph["peggy"] = []
graph["anuj"] = []
graph["thom"] = []
graph["jonny"] = []




def search(name):
    search_que = deque()
    search_que += graph[name]
    searched = []

    while search_que:
        person = search_que.popleft()
        if person not in searched:
            if checkSeller(person):
                print ("找到mango批发商:",person)
                return True
            else:
                search_que+= graph[person]
                searched.append(person)

    return False


def checkSeller(name):
    return name[-1] == "m"

if search("you")==False:
    print("社交网络中未找到mango批发商")

    

