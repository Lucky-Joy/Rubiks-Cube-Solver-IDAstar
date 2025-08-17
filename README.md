# Rubik's Cube Solver – IDA* with Pattern Database

A Python-based Rubik’s Cube solver that combines an **Iterative Deepening A*** (IDA*) search algorithm with a **corner pattern database (PDB)** for efficient heuristics.  
Includes a lightweight **pygame-based visualization** for interactive solving.

---

## 🚀 Features
- General **N×N cube engine** (tested on 2×2, 3×3, 4×4)
- Valid move logic for U, D, L, R, F, B (+ inverses, double turns)
- **IDA\*** search algorithm with admissible heuristic
- **Corner pattern database (PDB)** for fast lookups
- Interactive **2D visualizer** built using pygame
- Runs on **Jupyter Notebook** or **Google Colab**

---

## 📂 Project Structure
```

code/
├── cube.py              # Cube logic and move engine
├── pdb\_generator.py     # Corner pattern database generator
├── ida\_star\_solver.py   # IDA\* search logic
├── visual\_ui.py         # Pygame-based cube UI
└── main.py              # Driver script
README.md
requirements.txt
LICENSE

````

---

## 🧠 How It Works
- **Cube Representation** → faces stored as 2D arrays, generic for any size
- **Move Engine** → rotates faces and cycles adjacent edges in O(n)
- **Pattern DB** → precomputes corner configurations up to limited depth
- **IDA\*** → searches with `f = g + h`, where `h` is looked up from PDB
- **UI** → scrambles cube and animates solving sequence

---

## 🛠️ Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/RubiksCube-Solver-IDAstar.git
cd RubiksCube-Solver-IDAstar
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Solver

```bash
python code/main.py
```

---

## 🧪 Example Scrambles

Try with some standard scrambles:

```
R U R' U R U2 R'
F R U R' U' R U R' F'
L' U' L U' L' U2 L
```

---

## 📦 Dependencies

* Python 3.7+
* `pygame`
* Standard Library: `pickle`, `collections`, `os`

---

## 🧑‍💻 Authors & Credits

* Developed independently by Lucky Joy Tutika
* Core components: Cube logic, IDA\* solver, PDB generator, and pygame UI
* Licensed under **MPL 2.0** (see [LICENSE](LICENSE))
