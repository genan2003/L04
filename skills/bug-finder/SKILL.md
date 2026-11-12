---
name: python-bug-finder
description: Find bugs in Python functions by comparing each function's code with its docstring. Use whenever the user shares Python code and asks to find, check, or fix bugs. Output only bug reports in the Line/Problem/Example/Fix format.
---

# Python Bug Finder

## Steps
1. Number every line of the code, starting at 1 and counting blank lines.
2. For each function, read the docstring and state what it should return.
3. Read the code and work out what it actually returns.
4. Test each function with at least three inputs:
   - a typical value (e.g. 5)
   - an edge case (0, a negative number, or a boundary like exactly 18)
   - a value that avoids coincidences (2 + 2 == 2 * 2, so never test only with 2)
5. Look for these common bugs:
   - wrong operator (+ instead of *, - instead of /)
   - wrong comparison (> instead of >=, == 1 instead of == 0)
   - off-by-one errors at boundaries
   - wrong variable returned
   - logic that is the opposite of the docstring
6. Any input whose result doesn't match the docstring is a bug.

## Output rules
- Output ONLY the blocks below. No titles, intro, summary, or explanation.
- One block per bug, in the order the bugs appear in the code.
- Separate blocks with one blank line.
- Line is the line number of the faulty code, not the def line.
- Example must use a real input that shows the bug.
- Fix is the corrected line of code only.

## Output format

Line: <number>
Problem: <what the code does>, but the docstring says "<docstring text>".
Example: <call> returns <actual>, expected <expected>.
Fix: <corrected code>

## Example output

Line: 12
Problem: is_adult returns False for someone who is exactly 18, but the docstring says "18 or older".
Example: is_adult(18) returns False, expected True.
Fix: return age >= 18
