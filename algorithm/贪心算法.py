states_needed = set(["mt","wa","or","id","nv","ut","ca","az"])

stations = {}
stations["kone"] = set(["id","nv","ut"]) 
stations["ktwo"] = set(["wa","id","mt"])
stations["kthree"] = set(["or","nv","ca"])
stations["kfour"] = set(["nv","ut"])
stations["kfive"] = set(["ca","az"])

final_stations = set()



while states_needed:
    best_station = None
    states_covered = set()

    # 每次寻找覆盖洲 最多的那个电台 , 将其添加进来 , 再从states_needed 排除掉对应的洲

    for station ,states in stations.items():

        coverd = states_needed & states
        if len(coverd) >len(states_covered):
            states_covered = coverd
            best_station = station

    states_needed-= states_covered
    final_stations.add(best_station)

print(sorted(final_stations) )
   



