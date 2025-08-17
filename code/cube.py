# ---- FILE: cube.py ----

from copy import deepcopy

class Cube:
    def __init__(self, faces=None, size=3):
        self.size = size
        self.face_order = ['U', 'R', 'F', 'D', 'L', 'B']
        self.colors = ['W', 'R', 'G', 'Y', 'O', 'B']

        if faces:
            self.faces = deepcopy(faces)
        else:
            self.faces = {face: [[color]*size for _ in range(size)]
                          for face, color in zip(self.face_order, self.colors)}

    def copy(self):
        return Cube(deepcopy(self.faces), self.size)

    def display(self):
        for face in self.face_order:
            print(f"{face}:")
            for row in self.faces[face]:
                print("  ", " ".join(row))
            print()

    def rotate_face(self, face, clockwise=True):
        f = self.faces[face]
        if clockwise:
            self.faces[face] = [list(row) for row in zip(*f[::-1])]
        else:
            self.faces[face] = [list(row) for row in zip(*f)][::-1]

    def move(self, move_str):
        if move_str not in ["U", "U'", "D", "D'", "F", "F'", "B", "B'", "L", "L'", "R", "R'"]:
            raise ValueError(f"Invalid move: {move_str}")

        clockwise = not move_str.endswith("'")
        face = move_str[0]
        self.rotate_face(face, clockwise)

        if self.size != 3:
            raise NotImplementedError("Only 3x3 moves are currently implemented.")

        edge_map = {
            'U': [('F', 0), ('R', 0), ('B', 0), ('L', 0)],
            'D': [('F', 2), ('L', 2), ('B', 2), ('R', 2)],
            'F': [('U', 2), ('R', 'col0'), ('D', 0), ('L', 'col2')],
            'B': [('U', 0), ('L', 'col0'), ('D', 2), ('R', 'col2')],
            'L': [('U', 'col0'), ('F', 'col0'), ('D', 'col0'), ('B', 'col2')],
            'R': [('U', 'col2'), ('B', 'col0'), ('D', 'col2'), ('F', 'col2')],
        }

        seq = edge_map[face]
        vals = []
        for f, idx in seq:
            if isinstance(idx, int):
                vals.append(self.faces[f][idx][:])
            else:
                col = int(idx[-1])
                vals.append([self.faces[f][r][col] for r in range(self.size)])

        if not clockwise:
            vals = vals[-1:] + vals[:-1]
        else:
            vals = vals[1:] + vals[:1]

        for (f, idx), v in zip(seq, vals):
            if isinstance(idx, int):
                self.faces[f][idx] = v
            else:
                col = int(idx[-1])
                for r in range(self.size):
                    self.faces[f][r][col] = v[r]