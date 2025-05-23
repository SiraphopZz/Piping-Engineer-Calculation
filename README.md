# Piping Engineering Tools 🛠

This repository contains Python tools developed to assist with my tasks when working as piping engineer, including MTO summarization, pipe thickness calculation, and line list validation. It automates and accelerates my daily workflows using data from AutoCAD, Excel, and CSV databases.

I created this project because I enjoy coding and wanted to improve my understanding of piping fundamentals. By combining both interests, I was able to build practical tools while reinforcing core engineering concepts.

## 📁 Project Overview

| Script Name                  | Description |
|-----------------------------|-------------|
| `Sum_MTO.py`                | Summarizes Material Take-Off (MTO) data exported from AutoCAD |
| `Pipe Thickness Calculation.py` | Calculates pipe wall thickness based on ASME B31.3 |
| `GASKET_W_BOLT.py`          | Estimates required gasket and bolt sizes for flanged joints |
| `Line List Validator.py`    | Checks consistency across line list revisions |
| `Pipe Dimension DB.py`      | Looks up pipe dimensions from a CSV database |
| `Line List Rev.A/B.xlsx`    | Example line list inputs for validation tools |
| `Pipe Dimension DB.csv`     | Piping dimensions reference database |

## 🚀 How to Use

### Requirements

- Python 3.8+
- `pandas`, `openpyxl`

### Installation

```bash
git clone https://github.com/SiraphopZz/Piping-Engineering.git
cd Piping-Engineering
pip install -r requirements.txt  # or install pandas manually
