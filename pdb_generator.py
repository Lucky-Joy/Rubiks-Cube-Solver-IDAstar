# ---- FILE: pdb_generator.py ----

import pickle
from collections import deque
from cube import Cube

MOVES = ['U', "U'", 'D', "D'", 'F', "F'", 'B', "B'", 'L', "L'", 'R', "R'"]

CORNER_INDICES = [
    ('U', 0, 'L', 0, 'B', 2),  # 0
    ('U', 2, 'B', 0, 'R', 2),  # 1
    ('U', 8, 'R', 0, 'F', 2),  # 2
    ('U', 6, 'F', 0, 'L', 2),  # 3
    ('D', 2, 'R', 8, 'B', 6),  # 4
    ('D', 0, 'B', 8, 'L', 6),  # 5
    ('D', 6, 'L', 8, 'F', 6),  # 6
    ('D', 8, 'F', 8, 'R', 6),  # 7
]

MAX_DEPTH = 9  # ✅ Set a safe cap for BFS depth

def encode_corners(cube):
    result = []
    for triplet in CORNER_INDICES:
        colors = [cube.faces[triplet[i]][triplet[i+1]//3][triplet[i+1]%3] for i in range(0, 6, 2)]
        result.append(tuple(colors))
    return tuple(result)

def bfs_generate_corner_pdb():
    visited = set()
    queue = deque()
    pdb = dict()

    solved_cube = Cube()
    key = encode_corners(solved_cube)
    queue.append((solved_cube, 0))
    visited.add(key)
    pdb[key] = 0

    while queue:
        curr, depth = queue.popleft()

        if depth >= MAX_DEPTH:  # ✅ Skip deeper paths
            continue

        for mv in MOVES:
            new_cube = curr.copy()
            new_cube.move(mv)
            k = encode_corners(new_cube)
            if k not in visited:
                visited.add(k)
                pdb[k] = depth + 1
                queue.append((new_cube, depth + 1))

        if len(pdb) % 1000 == 0:
            print(f"{len(pdb)} states explored...")

    return pdb

def save_pdb(pdb, filename='corner_pdb.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(pdb, f)
    print(f"Saved {len(pdb)} entries to {filename}")

if __name__ == "__main__":
    print("Generating corner PDB (limited to MAX_DEPTH = 9)...")
    pdb = bfs_generate_corner_pdb()
    save_pdb(pdb)