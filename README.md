# IPL Dataset Analysis

A Python project that analyzes Indian Premier League (IPL) match and ball-by-ball delivery datasets (`matches.csv` and `deliveries.csv`) to generate statistical insights and `matplotlib` visualizations.

## Prerequisites

- Python 3.10+
- IPL dataset files (`matches.csv` and `deliveries.csv`) placed in the project data directory

## Setup & Installation

1. **Navigate to the project directory:**
   ```bash
   cd ipl_dataset
   ```

2. **Create and activate a virtual environment:**
   - **macOS / Linux:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - **Windows:**
     ```cmd
     python -m venv .venv
     .venv\Scripts\activate
     ```

3. **Install required libraries:**
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is not generated yet, run: `pip install matplotlib pylint`)*

## Running the Solutions

Ensure your virtual environment `(.venv)` is active, then execute any solution script from the root directory:

```bash
python solutions/solution1.py
python solutions/solution2.py
python solutions/solution3.py
python solutions/solution4.py
python solutions/solution5.py
python solutions/solution6.py
python solutions/solution7.py
python solutions/solution8.py
```

## Code Quality Check

Run `pylint` across all solution and helper modules to verify code quality:

```bash
pylint solutions/*.py
```
