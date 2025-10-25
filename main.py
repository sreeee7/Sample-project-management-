#!/usr/bin/env python3
"""
grade_calculator.py

Simple interactive grade calculator.

Features:
- Enter number of subjects (or components).
- For each subject enter marks obtained and maximum marks (or leave max as 100).
- Optionally provide a weight for each subject (sum of weights can be anything; weights will be normalized).
- Computes total, percentage and a letter grade.
- Example usage: run the script and follow prompts.
"""

from typing import List, Tuple


def read_positive_int(prompt: str) -> int:
    while True:
        try:
            v = int(input(prompt).strip())
            if v > 0:
                return v
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid number. Try again.")


def read_float(prompt: str, allow_zero: bool = False) -> float:
    while True:
        try:
            v = float(input(prompt).strip())
            if v > 0 or (allow_zero and v == 0):
                return v
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid number. Try again.")


def get_subjects(num: int, ask_weight: bool = False) -> Tuple[List[Tuple[float, float]], List[float]]:
    subjects = []
    weights: List[float] = []
    for i in range(1, num + 1):
        print(f"\nSubject #{i}:")
        obtained = read_float("  Marks obtained: ", allow_zero=True)
        maximum = read_float("  Maximum marks (default 100): ") if input("  Use custom max? (y/N): ").lower() == "y" else 100.0
        subjects.append((obtained, maximum))
        if ask_weight:
            w = read_float("  Weight for this subject (relative number, e.g. 1, 2, ...): ")
            weights.append(w)
    return subjects, weights


def compute_percentage(subjects: List[Tuple[float, float]], weights: List[float] = None) -> float:
    if not subjects:
        return 0.0
    if weights:
        # Weighted percentage: compute each subject's percentage

