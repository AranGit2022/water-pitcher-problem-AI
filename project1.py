global j_size
j_size = {}

class Node:
    def __init__(self, self_id, data=[0] * (len(j_size) + 1)):
        self.id = self_id
        self.data = data

class Tree:
    def __init__(self):
        self.nodes = []

    def add_node(self, self_id, data):
        node = Node(self_id, data)
        self.nodes.append(node)

def get_index1(lst=None, item=''):
    tmp = []
    tag = 0
    for i in lst:
        if i == item:
            tmp.append(tag)
        tag += 1
    return tmp

def search_father(n):
    if n == 0:
        return 1
    else:
        return search_father(rpt.index(rpt_father(n)))

def a_star(jug_sizes, target):
    n = len(jug_sizes) + 1
    rpt = []
    rpt_father = []
    queue = []
    g = Tree()
    g.add_node(0, [0] * n)
    Solveable = False
    a = 0
    k = 0
    step = 0
    rpt.append([0] * n)
    rpt_father.append([-1] * n)

    while not Solveable:
        fn = []
        acceptable_state = []
        #print("Current state is ", g.nodes[a].data)
        for i in range(0, n):
            current_state = list(g.nodes[a].data)
            past_state = list(g.nodes[a].data)
            #print("Pour jug", i, "off")
            current_state[i] = 0
            #print("Now the state = ", current_state)
            if current_state in rpt:
                continue
            rpt_father.append(past_state)
            rpt.append(current_state)
            acceptable_state.append(current_state)
            gn = a + 1
            hn = abs(target - max(current_state)) // max(jug_sizes)
            fn.append(gn + hn)
            if current_state[i] == target:
                Solveable = True
                #print(past_state)
                #print(current_state)
                break

        for i in range(0, n - 1):
            current_state = list(g.nodes[a].data)
            past_state = list(g.nodes[a].data)
            #print("Fill jug", i)
            current_state[i] = jug_sizes[i]
            #print("Now the state = ", current_state)
            if current_state in rpt:
                continue
            rpt_father.append(past_state)
            rpt.append(current_state)
            acceptable_state.append(current_state)
            gn = a + 1
            hn = abs(target - max(current_state)) // max(jug_sizes)
            fn.append(gn + hn)
            if current_state[i] == target:
                Solveable = True
                #print(past_state)
                #print(current_state)
                break

        for i in range(0, n):
            for j in range(0, n):
                if i == j:
                    continue
                #print("i = ", i, "j = ", j)
                current_state = list(g.nodes[a].data)
                past_state = list(g.nodes[a].data)
                current_state[i] += current_state[j]
                current_state[j] = 0
                if i != n - 1 and current_state[i] > jug_sizes[i]:
                    current_state[j] = current_state[i] - jug_sizes[i]
                    current_state[i] = jug_sizes[i]
                #print("Now the state = ", current_state)
                if current_state in rpt:
                    continue
                rpt_father.append(past_state)
                rpt.append(current_state)
                acceptable_state.append(current_state)
                gn = a + 1
                hn = abs(target - max(current_state)) // max(jug_sizes)
                fn.append(gn + hn)
                if current_state[i] == target or current_state[j] == target:
                    Solveable = True
                    #print(past_state)
                    #print(current_state)
                    m = len(rpt)-1
                    while m != 0:
                        #print(rpt[m])
                        queue.append(rpt[m])
                        m = rpt.index(rpt_father[m])
                    queue.append([0]*n)
                    for i in range(len(queue)-1, -1, -1):
                        print(queue[i])
                        step += 1
                        print("step = ", step)
                    break

        ln = get_index1(fn, min(fn))
        for i in range(0, len(ln)):
            k += 1
            g.add_node(k, acceptable_state[ln[i]])
        a += 1
    #for i in range (0, len(g.nodes)):
        #print(g.nodes[i].data)
    print("success")


if __name__ == '__main__':
    j_size = [5, 3]
    tt = 1
    a_star(j_size, tt)
