"""
CIS 110 - Lab 1 self-check
==========================

Run this from the lab folder:

    python check_my_work.py

It reads your notebook, runs your exercise code, and tells you which parts are
working. It never changes your notebook.

This is a SELF-CHECK, not your grade. Exercise 1 (your plan) and code clarity
are graded by your instructor, and your instructor may run additional checks.
"""

import contextlib
import io
import json
import re
import sys
from pathlib import Path

NOTEBOOK = Path(__file__).with_name("lab1_unit_converter.ipynb")
PROGRAM_MARKER = "LAB 1 PROGRAM"
PLAN_HEADING = "**My plan**"
PLAN_PLACEHOLDER = "Replace this sentence with your plan"
MAX_INPUT_CALLS = 10


class TooManyInputs(Exception):
    pass


def make_fake_input(answers):
    """Stand-in for input(): hands back scripted answers and counts the calls."""
    answers = list(answers)
    state = {"calls": 0}

    def fake_input(prompt=""):
        state["calls"] += 1
        if state["calls"] > MAX_INPUT_CALLS:
            raise TooManyInputs("your program asked for input too many times")
        return answers.pop(0) if answers else "0"

    return fake_input, state


def cell_source(cell):
    src = cell.get("source", "")
    return "".join(src) if isinstance(src, list) else src


def strip_magics(src):
    """Drop Jupyter-only lines (like !pip or %matplotlib) that plain Python cannot run."""
    return "\n".join(
        line for line in src.splitlines() if not line.lstrip().startswith(("!", "%"))
    )


def load_notebook():
    if not NOTEBOOK.exists():
        print(f"Could not find {NOTEBOOK.name} next to this script.")
        print("Run check_my_work.py from inside the lab folder.")
        sys.exit(2)
    with NOTEBOOK.open(encoding="utf-8") as f:
        return json.load(f)


def friendly(err):
    if isinstance(err, NameError) and re.search(r"name '_{3,}' is not defined", str(err)):
        return "still has ____ blanks to fill in"
    if isinstance(err, SyntaxError):
        return f"has a typo Python cannot read (SyntaxError on line {err.lineno})"
    return f"stopped with an error: {type(err).__name__}: {err}"


def exercise_number(src):
    m = re.search(r"#\s*EXERCISE\s+(\d+)", src)
    return int(m.group(1)) if m else None


def build_namespace(code_cells, program_index):
    """Run every code cell except the graded program, the way 'Run All' would.
    Returns the variables created, plus any error raised in an exercise cell."""
    ns = {"__name__": "__lab1__"}
    fake_input, _ = make_fake_input([])
    ns["input"] = fake_input
    errors = {}
    for i, src in enumerate(code_cells):
        if i == program_index:
            continue
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                exec(compile(strip_magics(src), f"<cell {i}>", "exec"), ns)
        except Exception as e:
            # An unfinished exercise raises an error; keep going so the
            # other exercises can still be checked.
            n = exercise_number(src)
            if n:
                errors[n] = friendly(e)
    return ns, errors


def run_program(src, answers, base_ns):
    """Run the graded program cell with scripted answers; return (output, input_calls, error)."""
    ns = dict(base_ns)
    fake_input, state = make_fake_input(answers)
    ns["input"] = fake_input
    out = io.StringIO()
    error = None
    try:
        with contextlib.redirect_stdout(out):
            exec(compile(strip_magics(src), "<Exercise 6>", "exec"), ns)
    except TooManyInputs as e:
        error = str(e)
    except Exception as e:
        error = explain(e)
    return out.getvalue(), state["calls"], error


def explain(e):
    """Turn the two classic Module 1 errors into advice a beginner can act on."""
    text = f"{type(e).__name__}: {e}"
    if isinstance(e, TypeError) and "'str'" in str(e):
        return (text + "\n             This usually means arithmetic on text. input() always"
                "\n             returns a str - convert it with float() before calculating.")
    if isinstance(e, ValueError) and "int()" in str(e):
        return (text + "\n             int() cannot read a decimal like 26.2."
                "\n             Use float() so the user can type decimals.")
    return text


NUMBER = re.compile(r"(?<![\d.])-?\d+\.\d+")


def numbers_in(text):
    """Every decimal number printed, as exact text: '10.00' never counts as '0.00'."""
    return set(NUMBER.findall(text))


def close(a, b, tol=1e-6):
    try:
        return abs(float(a) - float(b)) < tol
    except (TypeError, ValueError):
        return False


class Report:
    def __init__(self):
        self.earned = 0
        self.possible = 0
        self.lines = []

    def check(self, points, passed, label, hint=""):
        self.possible += points
        if passed:
            self.earned += points
            self.lines.append(f"    PASS     {label}")
        else:
            self.lines.append(f"    NOT YET  {label}")
            if hint:
                self.lines.append(f"             hint: {hint}")

    def heading(self, text):
        self.lines.append("")
        self.lines.append(text)

    def note(self, text):
        self.lines.append(f"    {text}")


def find_program(cells):
    """Return (index into code cells, found_by_marker)."""
    code_i = -1
    after_ex6 = False
    fallback = None
    for c in cells:
        src = cell_source(c)
        if c.get("cell_type") == "code":
            code_i += 1
            if PROGRAM_MARKER in src:
                return code_i, True
            if after_ex6 and fallback is None:
                fallback = code_i
        elif "EXERCISE 6" in src:
            after_ex6 = True
    return fallback, False


def main():
    nb = load_notebook()
    cells = nb.get("cells", [])
    code_cells = [cell_source(c) for c in cells if c.get("cell_type") == "code"]
    md_cells = [cell_source(c) for c in cells if c.get("cell_type") == "markdown"]
    program_index, by_marker = find_program(cells)
    ns, errors = build_namespace(code_cells, program_index)
    r = Report()

    def show_error(n):
        if n in errors:
            r.note(f"NOTE     your Exercise {n} cell {errors[n]}")

    # ---- Exercise 1: plan (quality graded by instructor) ----------------
    r.heading("Exercise 1 - Your plan   (graded by your instructor)")
    plan = next((m for m in md_cells if m.strip().startswith(PLAN_HEADING)), None)
    if plan is None:
        r.note("NOT FOUND  keep the **My plan** heading at the top of your plan cell")
    elif PLAN_PLACEHOLDER in plan:
        r.note("NOT YET    your plan cell still has the placeholder sentence")
    else:
        body = plan.replace(PLAN_HEADING, "")
        sentences = [s for s in re.split(r"[.!?]+", body) if len(s.split()) >= 3]
        if len(sentences) >= 3:
            r.note(f"WRITTEN    {len(sentences)} sentences found")
        else:
            r.note(f"SHORT      only {len(sentences)} sentence(s) found - aim for three to five")

    # ---- Exercise 2: variables and expressions --------------------------
    r.heading("Exercise 2 - Variables and expressions")
    show_error(2)
    r.check(3, close(ns.get("fahrenheit"), 212),
            "fahrenheit is correct",
            "100 degrees Celsius should be 212 Fahrenheit - check the formula in the task table")
    r.check(2, close(ns.get("celsius_back"), 100),
            "celsius_back converts back to 100",
            "use parentheses: subtract 32 first, then multiply")

    # ---- Exercise 3: predict the type -----------------------------------
    r.heading("Exercise 3 - Predict the type")
    show_error(3)
    expected = {1: "int", 2: "float", 3: "str", 4: "bool"}
    for n, answer in expected.items():
        given = str(ns.get(f"prediction_{n}", "")).strip().strip("'\"").lower()
        r.check(1, given == answer, f"prediction_{n}",
                "run the checking cell below the exercise and compare" if given else
                "write your prediction as text, for example \"int\"")

    # ---- Exercise 4: type conversion ------------------------------------
    r.heading("Exercise 4 - Type conversion")
    show_error(4)
    un = ns.get("user_number")
    r.check(2, isinstance(un, float) and close(un, 37.5),
            "user_number is the float 37.5", "convert user_text with float()")
    r.check(1, close(ns.get("doubled"), 75.0), "doubled", "multiply user_number by 2")
    wp = ns.get("whole_part")
    r.check(1, isinstance(wp, int) and not isinstance(wp, bool) and wp == 7,
            "whole_part", "int() cuts off the decimal - it does not round")
    r.check(1, ns.get("rounded") == 8, "rounded", "use round(), not int()")

    # ---- Exercise 5: formatted output -----------------------------------
    r.heading("Exercise 5 - Formatted output")
    show_error(5)
    msg = str(ns.get("message", "")).strip()
    r.check(1, "98.60" in numbers_in(msg), "shows 98.60", "use :.2f inside the braces")
    r.check(1, "37.00" in numbers_in(msg), "shows 37.00", "use :.2f inside the braces")
    r.check(2, msg == "98.60 F is 37.00 C", "matches exactly: 98.60 F is 37.00 C",
            "check spaces and capital letters")

    # ---- Exercise 6: the converter --------------------------------------
    r.heading("Exercise 6 - The converter")
    if program_index is None:
        r.check(10, False, "program cell found",
                "put '# LAB 1 PROGRAM' back as the first line of your Exercise 6 cell")
    else:
        if not by_marker:
            r.note("NOTE     the '# LAB 1 PROGRAM' line is missing - found your program by")
            r.note("         its position instead. Please put that first line back.")
        program = code_cells[program_index]
        # Test values deliberately differ from the example in the instructions,
        # so copying the example output does not pass.
        cases = [
            (("25", "5"), "77.00", "8.05"),
            (("-40", "26.2"), "-40.00", "42.16"),
            (("37", "0"), "98.60", "0.00"),
        ]
        calls_ok = True
        first_error = None
        for i, (answers, want_f, want_km) in enumerate(cases, start=1):
            out, calls, error = run_program(program, answers, ns)
            found = numbers_in(out)
            first_error = first_error or error
            calls_ok = calls_ok and calls == 2
            pts = 2 if i == 1 else 1   # test 1 is worth 2+2, tests 2-3 are 1+1
            r.check(pts, error is None and want_f in found,
                    f"test {i}: {answers[0]} C gives {want_f} F",
                    "ask for Celsius FIRST; print the result with :.2f")
            r.check(pts, error is None and want_km in found,
                    f"test {i}: {answers[1]} miles gives {want_km} km",
                    "ask for miles SECOND; 1 mile = 1.609344 km; print with :.2f")
        r.check(2, calls_ok, "asks the user exactly two questions",
                "use input() once for the temperature and once for the distance")
        if first_error:
            r.note(f"NOTE     your program stopped with an error: {first_error}")

    # ---- Summary ---------------------------------------------------------
    print("=" * 62)
    print("  CIS 110 - Lab 1 self-check")
    print("=" * 62)
    for line in r.lines:
        print(line)
    print()
    print("-" * 62)
    print(f"  Self-check: {r.earned} / {r.possible} points on the auto-checked exercises")
    print("  Your plan (5) and code clarity (2) are graded by your instructor.")
    print("-" * 62)
    return 0 if r.earned == r.possible else 1


if __name__ == "__main__":
    sys.exit(main())
