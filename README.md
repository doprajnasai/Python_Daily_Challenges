# **Python 60 Day Challenge**

Welcome to my Python 60 Day Challenge repository! This is a daily log of solved Python programming challenges.

## **Progress Tracker**

| Day | Challenge Title                      | Status      |
| --- | ------------------------------------ | ----------- |
| 1   | User Profile Validation System       | ✅ Completed |
| 2   | Smart ID & Credential Validator      | ✅ Completed |
| 3   | Student Performance Analyzer         | ✅ Completed |
| 4   | Cyber Activity Risk Analyzer         | ✅ Completed |
| 5   | Emergency Resource Dispatch Analyzer | ✅ Completed |
| 6   | Smart Transaction Risk detector      | ✅ Completed |


## **Repository Format**

Each day’s folder includes:

* **Problem Description** – Description of the Challenge
* **Python Solution Code** – Complete working implementation
* **Core Concepts** – Important Python topics used

---

## **Challenge Objectives**

* Solve **one Python project/problem daily**
* Improve coding consistency and analytical skills
* Build strong knowledge of both basic and advanced Python concepts

---

## **How to Explore**

1. Open the folder for a specific day
2. Read the problem statement
3. Go through the Python solution
4. Run the program locally and experiment with inputs

---

## **Tech Stack Used**

* **Python 3.x**
* Built-in Python Standard Libraries

---

* **Start Date:** 28 Jan 2026
* **Target Completion:** Day 60

---

## **Concepts Covered (Day-wise)**


### ✅ Day 1 – User Profile Validation System

Key topics practiced:

* User input and string manipulation
* Validation using conditional statements
* Basic error-checking logic
* Clean and structured output formatting

---

### ✅ Day 2 – Smart ID & Credential Validator

Concepts included:

* Using lists to store and compare credentials
* Iterative checks with `for` loops
* Rule-based ID validation
* Logical filtering and handling invalid entries

---

### ✅ Day 3 – Student Performance Analyzer

Main learning points:

* This Python program takes marks of N students and stores them in a list.
* It processes each mark using loops and classifies students into performance categories (Fail, Average, Good, Very Good, Excellent).
* A personalization rule is applied by comparing the last digit of the entered roll number with a predefined roll number (AP24110011623).
* If both last digits match (3), a +1 bonus mark is added to all students.
* The program also counts total valid students and total failed students.
* Finally, it displays updated marks and performance statistics.

---

### ✅ Day 4 – Cyber Activity Risk Analyzer

Important concepts:

* Activity log management using lists
* Risk level classification (Low / Medium / High)
* Logical removal of unwanted entries
* Personalization using last digit of Register Number (D):
* If **D is odd** → Low-risk logs removed
* If **D is even** → Critical logs removed
* Count of removed logs tracked

---

### ✅ Day 5 – Emergency Resource Dispatch Analyzer

Concepts applied:

* Lists for categorizing requests
* for loops for classification
* Conditional statements for demand levels
* Counting valid and removed requests
* Personalized filtering using PLI (L % 3 rule)
* Calculated L (length of full name excluding spaces)
* Computed PLI = L % 3 and applied Rule A/B/C accordingly

---
### ✅ Day 6 – Smart Transaction Risk detector

Concepts Applied

* Lists for storing and categorizing transactions  
* Dictionary for grouping transactions into normal, large, high-risk, and invalid  
* for loops for iterating and classifying each transaction   **Conditional statements** for applying transaction category rules  
* List comprehension to filter valid transactions (`t > 0`)  
* Counting logic to track number of high-risk transactions  
* Summation logic to compute total transaction value  
* Tuples for storing transaction summary (total, high-risk count, number of valid transactions)  
* **Personalization:** Implemented a custom risk classification system where the final risk level is determined using a combination of conditions (high-risk         transaction count, total transactions, and total spending) instead of relying on a single factor, making the detection more accurate
  and realistic.
* Multi-condition decision making** (frequent transactions, large spending, suspicious activity) to determine final risk level  
