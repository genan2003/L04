---
name: python-bug-finder
description: Find the bugs in a Python file by comparing each function's code with its docstring, and write one bug report per bug in the Line/Problem/Example/Fix format.
---

# Python Bug Finder

You get one Python file with line numbers. Find every bug and write one bug report for each bug.

## How to find bugs
Check every function, one at a time:
1. Read the docstring. The docstring is always right; the code may be wrong.
2. Trace the code by hand with these inputs:
   - a normal value
   - the exact limit named in the docstring (18 for "18 or older", 0, 100)
   - unusual inputs: an empty list [], an empty string "", 0, a negative number, a list with one element
   - a value that avoids coincidences (2 + 2 == 2 * 2, so never test only with 2)
3. It is a bug if any input gives a result different from the docstring, if the code crashes on an input the docstring allows, or if the code is dangerous.

## Kinds of bugs to look for
- Wrong operation: + instead of *, - instead of +, n % 2 == 1 for "even", / instead of //.
- Limits: > instead of >=, < instead of <=, range(1, n) instead of range(1, n + 1), [1:] that skips the first item.
- Unusual inputs: dividing by len([]) or by 0, max([]) or min([]), text[0] on "", a loop that never runs.
- Security: eval() or exec() on user text, os.system() or subprocess with shell=True and user text, SQL built with f-strings or +, pickle.loads() or yaml.load() on untrusted data, hard-coded passwords or keys, random used for tokens or passwords instead of secrets, md5 or sha1 for passwords, open() on a user path without checking for "..".

## Output rules
- Output ONLY bug report blocks. No title, intro, summary, Markdown, bold text or code fences.
- Report only real bugs. If a function is correct, write nothing about it. Never write "no bug found" or "no fix needed".
- One block per bug, in the order of the lines. Separate blocks with one blank line.
- Line is the number, taken from the file, of the line that must change. Never the def line or the docstring line.
- Example uses a real call. "returns" is what the CURRENT code gives (or "raises ZeroDivisionError"); "expected" is what the docstring promises.
- Fix is the one corrected line of code.

## Format

Line: <number>
Problem: <function> <what the code does>, but the docstring says "<docstring text>".
Example: <call> returns <actual>, expected <expected>.
Fix: <corrected line>

## Example output

Line: 12
Problem: is_adult returns False for someone who is exactly 18, but the docstring says "18 or older".
Example: is_adult(18) returns False, expected True.
Fix: return age >= 18

Line: 17
Problem: average divides by len(numbers), which is 0 for an empty list, but the docstring says "returns 0 for an empty list".
Example: average([]) raises ZeroDivisionError, expected 0.
Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 22
Problem: parse_value uses eval, so any Python code in the text runs, but the docstring says it only "converts a literal like '[1, 2]' into a value".
Example: parse_value("__import__('os').getcwd()") returns a folder path, expected ValueError.
Fix: return ast.literal_eval(text)
