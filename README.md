# Sudoku Solver 🧩

## 📌 Description

This project is a Python-based Sudoku solver that reads a puzzle from a file, solves it using a backtracking algorithm, and writes the completed solution to a new file.

It demonstrates:

* File handling
* 2D data structures (lists)
* Recursion and backtracking
* Problem-solving logic

---

## ⚙️ How It Works

1. The program reads a Sudoku puzzle from a text file (`puzzle.txt`)
2. It converts the input into a 9x9 board
3. It finds empty cells (`0` values)
4. It calculates valid numbers for each position
5. It uses **backtracking** to solve the puzzle
6. The solution is saved to `solved_puzzle.txt`

---

## 📂 Project Structure

```
.
├── puzzle.txt              # Input Sudoku puzzle
├── solved_puzzle.txt       # Output solved puzzle
├── sudoku.py               # Main solver code
└── README.md
```

---

## ▶️ How to Run

### Requirements

* Python 3.x

### Run the program

```bash
python sudoku.py
```

---

## 🧪 Example Input (`puzzle.txt`)

```
530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079
```

---

## ✅ Example Output (`solved_puzzle.txt`)

```
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

---

## 🧠 Key Concepts Used

* Backtracking algorithm
* Constraint checking (row, column, subgrid)
* Recursion
* File I/O in Python

---

## 🚀 Future Improvements

* Add a GUI interface
* Support different puzzle sizes
* Improve performance with heuristics
* Add input validation

---

## 👤 Author

Thato Boshego

