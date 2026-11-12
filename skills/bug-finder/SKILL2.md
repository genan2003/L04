
# Bug Test Writer

You receive one bug report and the exercise file it refers to. The report has this format:

Line: <line number>
Problem: <what is wrong and why>
Example: <call> returns <actual>, expected <expected>.
Fix: <corrected code>

Write one test that proves this bug.

## Output rules
- Answer with ONLY Python code: one function whose name starts with `test_`.
- No text before or after it, no explanation, no Markdown code fences, no comments, no docstring.
- Do not import the exercise functions; they are already imported. Call them directly, e.g. `is_adult(18)`.
- No other top-level code: no second function, helper, class, `print`, or `if __name__ == "__main__":`.

## The test must
1. Fail on the current code. Trace the call on the code exactly as written; the assertion must be false (or the call must crash).
2. Pass on the fixed code. Apply the `Fix:` line in your head and trace again; the assertion must be true.

Check both before answering. A test that passes on the buggy code proves nothing.

## How to write it
1. Start from the `Example:` line and use its input and expected value. If your trace shows the example doesn't separate buggy and fixed code (e.g. `double(2)` gives 4 both ways), pick a different input.
2. Write the expected value as a literal taken from the docstring, never computed by calling the function or copying its logic.
3. Test only this bug: one call and one `assert`. Don't check unrelated behaviour.
4. Name it `test_<function>_<situation>`, lowercase with underscores.
5. Special cases:
   - Float results: `assert abs(average([1, 2]) - 1.5) < 1e-9`, not `==`.
   - Function should raise but doesn't: use `try` / `except` with `return` in the except block, then `assert False` after it.
   - Function prints instead of returning: take `capsys` as the parameter and assert on `capsys.readouterr().out`.

## Example

Bug report:
Line: 12
Problem: is_adult returns False for someone who is exactly 18, but the docstring says "18 or older".
Example: is_adult(18) returns False, expected True.
Fix: return age >= 18

Output:
def test_is_adult_at_18():
    assert is_adult(18) == True

(Current code: 18 > 18 is False, so it fails. Fixed code: 18 >= 18 is True, so it passes. Your real answer is only the function.)
