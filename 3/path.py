__author__ = 'Sergei.Ivanov'

def main():
    with open("input.txt") as f, open("output.txt", "w") as g:
        lines = f.readlines()
        N, M = map(int, lines[0].split())
        edges = {i: set() for i in range(1, N+1)}
        e_lines = lines[1:M+1]
        e_order = dict()
        e_weight = dict()
        for ix, e in enumerate(e_lines):
            e1, e2 = map(int, e.split())
            e_order[ix+1] = (e1,e2)
            e_weight[(e1, e2)] = e_weight.get((e1, e2), 0) + 1
            e_weight[(e2, e1)] = e_weight.get((e2, e1), 0) + 1
            edges[e1].add(e2)
            edges[e2].add(e1)
        # find connected components
        CCs = []
        node2CC = dict()
        selected = {i: False for i in range(1, N+1)}
        cc_idx = 0
        for source in range(1, N+1):
            if not selected[source]:
                cc, selected = BFS(edges, source, selected)
                CCs.append(cc)
                for cc_node in cc:
                    node2CC[cc_node] = cc_idx
                cc_idx += 1

        # remove an edge
        cc_number = len(CCs)
        cuts = map(int, lines[M+2].split())
        for cut in cuts:
            e1, e2 = e_order[cut]
            e_weight[(e1, e2)] -= 1
            e_weight[(e2, e1)] -= 1
            if not e_weight[(e1, e2)]:
                edges[e1].remove(e2)
                edges[e2].remove(e1)
                if no_path(edges, e1, e2):
                    cc_number += 1
            g.write("%i " %(cc_number))

def no_path(edges, e1, e2):
    selected = {i: False for i in edges}
    reach, selected = BFS(edges, e1, selected)
    if e2 not in reach:
        return True
    else:
        return False

def BFS(edges, source, selected):
    reach = [source]
    reach.extend(list(edges[source]))
    selected[source] = True
    for node in reach:
        if not selected[node]:
            selected[node] = True
            for u in edges[node]:
                if u not in reach:
                    reach.append(u)
    return reach, selected

main()

console = []