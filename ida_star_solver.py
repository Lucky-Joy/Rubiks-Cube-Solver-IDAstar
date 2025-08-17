# ---- FILE: ida_star_solver.py ----

import pickle
from cube import Cube
from pdb_generator import encode_corners, MOVES

with open('corner_pdb.pkl', 'rb') as f:
    corner_pdb = pickle.load(f)

def heuristic(cube):
    return corner_pdb.get(encode_corners(cube), 0)

def ida_star(cube):
    threshold = heuristic(cube)
    path = []

    def search(node, g, threshold):
        f = g + heuristic(node)
        if f > threshold:
            return f
        if heuristic(node) == 0:
            return True

        min_cost = float('inf')
        for mv in MOVES:
            node_copy = node.copy()
            node_copy.move(mv)
            path.append(mv)
            result = search(node_copy, g + 1, threshold)
            if result is True:
                return True
            path.pop()
            min_cost = min(min_cost, result)
        return min_cost

    while True:
        temp = search(cube, 0, threshold)
        if temp is True:
            return path
        if temp == float('inf'):
            return None
        threshold = temp