# ---- FILE: main.py ----

from cube import Cube
from ida_star_solver import ida_star

if __name__ == "__main__":
    print("Creating solved cube...")
    cube = Cube()
    print("Scrambling: U R U' L D B'")
    scramble = ['U', 'R', "U'", 'L', 'D', "B'"]
    for move in scramble:
        cube.move(move)
    print("Scrambled Cube:")
    cube.display()

    print("Solving...")
    solution = ida_star(cube)
    print("Solution:", solution)

    print("Applying solution to confirm:")
    for mv in solution:
        cube.move(mv)
    cube.display()