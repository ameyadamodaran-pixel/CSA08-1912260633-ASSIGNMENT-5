# CSA08-1912260633-ASSIGNMENT-5

# CSA08 – Assignment 5: Data Acquisition, Cleaning, Analysis & AI Applications

**Student Name:** Ameya Damodaran  
**Register Number:** 1912260633  
**Course:** CSA08 – Python Programming  
**Assignment:** Assignment 5  
**Python Version:** Python 3.11+  
**Case Study:** City Air-Quality Monitoring Network

## Assignment Overview

This assignment explores how Python can acquire, inspect, clean, normalise, store, query, visualise, profile and interpret real-world data.
The case study uses air-quality readings from monitoring stations and citizen complaints. Part A contains data and program design, while Part B implements and tests the solutions.

The assignment follows the workflow:

**ACQUIRE → INSPECT → CLEAN → NORMALISE → STORE → QUERY → VISUALISE → PROFILE → INTERPRET**

## Repository Structure
- `PartA/` – Design answers for Tasks A1–A5.
- `PartB/` – Implementation for Tasks B1–B4.
- `REPORT.md` – Detailed assignment report.
- `REPORT.pdf` – PDF version of the report.
- `PNG files` – Charts generated for analysis and performance comparison.
- Each task folder contains the relevant source code, input files, output files and evidence.

## Libraries and Requirements
**Python:** 3.11 or newer

**Standard Libraries Used:**
- csv
- sqlite3
- statistics
- time
- cProfile
- io
- Other required Python standard-library modules

**Optional Library:**
- Pandas – used for DataFrame and groupby comparison in B3.

### Installing Pandas
```bash
python -m pip install pandas
```

No additional packages are required for the standard-library portions of the assignment.

## How to Run the Programs
Run the commands from the repository root directory.

### B1 – Cleaning Pipeline
```bash
python PartB/B1_Cleaning_Pipeline/main.py
```

### B2 – Adversarial Data
```bash
python PartB/B2_Adversarial_Data/main.py
```

### B3 – Loops vs Libraries vs SQL
```bash
python PartB/B3_Loops_Libraries_SQL/main.py
```

### B4 – Final Engineering Decision
```bash
python PartB/B4_Final_Engineering_Decision/main.py
```

B3 can run the Pandas comparison if Pandas is installed. Otherwise, the available standard-library and SQL comparisons can be executed as implemented.
Program outputs are saved in the corresponding task output folders.

---

# Task List and Result Notes

## PART A – DATA AND PROGRAM DESIGN
### A1 – Design the Data Acquisition (K3 – Apply)
Describes the station CSV data source, expected data-quality problems, SQLite database design, and sample questions that can be answered using CSV files or SQL queries.
**Result:** Designed a suitable acquisition and storage approach for air-quality readings and identified expected data-quality issues.

### A2 – Design the Cleaning and Normalisation (K4 – Analyse)
Defines cleaning rules for missing values, duplicates, invalid readings and Fahrenheit temperature conversion. Discusses PM2.5 normalisation and standard data formats.
**Result:** Developed appropriate cleaning and normalisation rules to improve the quality and consistency of the dataset.

### A3 – Design the Analysis and Visualisation (K4 – Analyse)
Selects suitable charts for monthly PM2.5 trends, station comparisons, temperature and PM2.5 relationships, and worst-air hours. Also designs a summary table.
**Result:** Selected suitable visualisation methods and summary statistics for analysing air-quality data.

### A4 – Plan Debugging and Profiling (K4 – Analyse)
Outlines the use of print statements, assertions, logging, debugging tools, timing methods and cProfile.
**Result:** Developed a debugging and profiling plan to identify errors and performance bottlenecks.

### A5 – Design an AI Application for Citizen Complaints (K3 – Apply)
Designs a lexicon-based sentiment scorer, extractive summariser and rule-based chatbot. Discusses limitations and compares simple methods with machine-learning alternatives.
**Result:** Designed basic AI applications for understanding citizen complaints and answering air-quality queries.

---

## PART B – IMPLEMENTATION AND EXPERIMENTAL INVESTIGATION

### B1 – Implement and Validate the Cleaning Pipeline (K3 – Apply)
Implements data cleaning, validates sample air-quality records, separates valid and rejected records, stores data in SQLite, performs SQL queries and generates charts.
**Result:** Implemented a working cleaning pipeline and verified the cleaned data through database queries and visualisation.

### B2 – Engineer Adversarial Data (K4 – Analyse)
Tests malformed files, missing columns, wrong delimiters, encoding problems, empty files, unusual inputs and SQL parameterisation.
**Result:** Evaluated program behaviour under unexpected inputs and demonstrated safer database querying using parameterised SQL.

### B3 – Loops vs Libraries vs SQL (K4 – Analyse)
Compares daily mean calculations using Python loops, Pandas groupby and SQL GROUP BY. Verifies correctness, measures execution time for different dataset sizes and profiles the loop-based implementation.
**Result:** Compared the correctness and performance of different data-analysis approaches and identified their computational trade-offs.

### B4 – Final Engineering Decision (K5 – Evaluate)
Implements a simple sentiment scorer and summariser, tests citizen complaints, checks database indexing and evaluates a suitable strategy for increased data volume.
**Result:** Evaluated the implemented methods and proposed an engineering decision based on performance, scalability, accuracy and practical limitations.

---

## Outputs and Evidence

The repository includes:
- Python source programs for implementation tasks.
- Input CSV and test data files.
- Cleaned data and rejected records.
- SQLite database and query results.
- Sentiment-analysis and chatbot results.
- Benchmark timing results.
- Profiling information.
- Generated charts and visualisations.
- Assignment report in Markdown and PDF formats.

Execution timings may vary depending on the system. Local execution and genuine screenshots should be added wherever required by the instructor.

## Overall Conclusion
This assignment demonstrates the Python data-processing workflow from acquisition and cleaning to storage, querying, visualisation, profiling and interpretation.
It highlights the importance of reliable data cleaning, secure SQL queries, validation, performance measurement and choosing suitable tools according to the size and requirements of the dataset.

