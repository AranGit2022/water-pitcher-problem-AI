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


def get_index(lst=None, item=''):
    tmp = []
    tag = 0
    for i in lst:
        if i == item:
            tmp.append(tag)
        tag += 1
    return tmp


def a_star(jug_sizes, target):
    n = len(jug_sizes) + 1
    rpt = []
    rpt_father = []
    queue = []
    tree = Tree()
    tree.add_node(0, [0] * n)
    Solve = False
    a = 0
    k = 0
    step = 0
    rpt.append([0] * n)
    rpt_father.append([-1] * n)

    while not Solve:
        fn = []
        acceptable_state = []
        #print("current state is ", tree.nodes[a].data)
        for i in range(0, n):
            current_state = list(tree.nodes[a].data)
            past_state = list(tree.nodes[a].data)
            #print("pour jug", i)
            current_state[i] = 0
            #print("now the state = ", current_state)
            if current_state in rpt:
                continue
            rpt_father.append(past_state)
            rpt.append(current_state)
            acceptable_state.append(current_state)
            gn = a + 1
            hn = abs(target - max(current_state)) // max(jug_sizes)
            fn.append(gn + hn)
            if current_state[i] == target:
                Solve = True
                #print(past_state)
                #print(current_state)
                m = len(rpt) - 1
                while m != 0:
                    # print(rpt[m])
                    queue.append(rpt[m])
                    m = rpt.index(rpt_father[m])
                queue.append([0] * n)
                for q in range(len(queue) - 1, -1, -1):
                    print(queue[q])
                    step += 1
                    print("step = ", step)
                break

        for i in range(0, n - 1):
            current_state = list(tree.nodes[a].data)
            past_state = list(tree.nodes[a].data)
            #print("fill jug", i)
            current_state[i] = jug_sizes[i]
            #print("now the state = ", current_state)
            if current_state in rpt:
                continue
            rpt_father.append(past_state)
            rpt.append(current_state)
            acceptable_state.append(current_state)
            gn = a + 1
            hn = abs(target - max(current_state)) // max(jug_sizes)
            fn.append(gn + hn)
            if current_state[i] == target:
                Solve = True
                #print(past_state)
                #print(current_state)
                m = len(rpt) - 1
                while m != 0:
                    # print(rpt[m])
                    queue.append(rpt[m])
                    m = rpt.index(rpt_father[m])
                queue.append([0] * n)
                for q in range(len(queue) - 1, -1, -1):
                    print(queue[q])
                    step += 1
                    print("step = ", step)
                break

        for i in range(0, n):
            for j in range(0, n):
                if i == j:
                    continue
                #print("i = ", i, "j = ", j)
                current_state = list(tree.nodes[a].data)
                past_state = list(tree.nodes[a].data)
                current_state[i] += current_state[j]
                current_state[j] = 0
                if i != n - 1 and current_state[i] > jug_sizes[i]:
                    current_state[j] = current_state[i] - jug_sizes[i]
                    current_state[i] = jug_sizes[i]
                #print("now the state = ", current_state)
                if current_state in rpt:
                    continue
                rpt_father.append(past_state)
                rpt.append(current_state)
                acceptable_state.append(current_state)
                gn = a + 1
                hn = abs(target - max(current_state)) // max(jug_sizes)
                fn.append(gn + hn)
                if current_state[i] == target or current_state[j] == target:
                    Solve = True
                    #print(past_state)
                    #print(current_state)
                    m = len(rpt)-1
                    while m != 0:
                        #print(rpt[m])
                        queue.append(rpt[m])
                        m = rpt.index(rpt_father[m])
                    queue.append([0]*n)
                    for q in range(len(queue)-1, -1, -1):
                        print(queue[q])
                        step += 1
                        print("step = ", step)
                    break

        ln = get_index(fn, min(fn, default=0))
        for i in range(0, len(ln)):
            k += 1
            tree.add_node(k, acceptable_state[ln[i]])
        a += 1
    #for i in range (0, len(tree.nodes)):
        #print(tree.nodes[i].data)
    print("success")


if __name__ == '__main__':
    file = open('C:/Users/Admin/Desktop/project1/test6.txt', 'r')
    s = file.readline().split(',')
    j_size = list(int(i) for i in s)
    t = int(file.readline())
    #j_size = [5, 3]
    #t = 1
    a_star(j_size, t)
