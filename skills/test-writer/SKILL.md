---
name: bug-test
description: Turns one bug report (Line / Problem / Example / Fix) plus the exercise file into exactly one pytest test function that fails on the current buggy code and passes once the bug is fixed.
---

# Bug Test Writer

You receive one bug report and the exercise file it refers to. The report has this format:

Line: <line number>
Problem: <what is wrong and why>
Example: <call> returns <actual>, expected <expected>.
Fix: <corrected code>

Write one test that proves this bug.

## Output rules
- Answer with ONLY Python code: one function whose name starts with test_.
- No text before or after it, no explanation, no Markdown, no code fences, no emoji, no comments, no docstring.
- Do not import the exercise functions; they are already imported. Call them directly, e.g. is_adult(18).
- No other top-level code: no second function, helper, class, print, or if __name__ == "__main__":.

## The test must
1. Fail on the current code. Trace the call on the code exactly as written; the assertion must be false, or the call must crash.
2. Pass on the fixed code. Apply the Fix line in your head and trace again; the assertion must be true.

Check both before answering. A test that passes on the buggy code proves nothing.

## How to write it
1. Start from the Example line and use its input and expected value. If your trace shows the input gives the same result on buggy and fixed code (double(2) gives 4 both ways), pick another input.
2. Write the expected value as a literal taken from the docstring, never computed by calling the function or copying its logic.
3. Test only this bug: one call and one assert.
4. Name it test_<function>_<situation>, lowercase with underscores.

## Special cases
- Limits (> vs >=): test exactly the limit value, e.g. is_adult(18).
- Crash on a valid input (empty list, empty text, zero): just assert the correct result. The crash makes the test fail on the buggy code.
- Float results: assert abs(average([1, 2]) - 1.5) < 1e-9, not ==.
- The function should raise but doesn't, or a security bug where a dangerous input must be rejected:

def test_parse_value_rejects_code():
    try:
        parse_value("__import__('os').getcwd()")
    except (ValueError, SyntaxError):
        return
    assert False

- The function prints instead of returning: take capsys as the parameter and assert on capsys.readouterr().out.

## Example

Bug report:
Line: 12
Problem: is_adult returns False for someone who is exactly 18, but the docstring says "18 or older".
Example: is_adult(18) returns False, expected True.
Fix: return age >= 18

Output:
def test_is_adult_at_18():
    assert is_adult(18) == True
