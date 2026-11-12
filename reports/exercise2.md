# Bug reports for exercise2.py

Line: 13
Problem: clamp returns max(low, min(x, low)), which is always low, but the docstring says "x, limited to the range from low to high".
Example: clamp(10, 5, 15) returns 5, expected 10.
Fix: return max(low, min(x, high))
