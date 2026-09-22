# CIS 110 · Module 1 — Computational Thinking and Your First Programs

Welcome to your first lab. Everything you need for Module 1 is in this folder.

> **This lab is Unassisted.** Do not use an AI assistant for any part of it —
> not to write code, and not to explain something. You may use the assigned
> readings, the [Python documentation](https://docs.python.org/3/tutorial/), and
> the Q&A discussion on Canvas.

---

## What's in this folder

| File | What it is |
|---|---|
| `lab1_unit_converter.ipynb` | **The lab.** Open this and work through it top to bottom. |
| `ai_use_reflection.md` | Your AI-Use Reflection for this lab. Fill it in and submit it. |
| `check_my_work.py` | A self-check. Run it before you submit to see which exercises are working. |
| `setup/verify_environment.py` | Checks that Python and your editor are set up correctly. |
| `setup/TROUBLESHOOTING.md` | Fixes for the most common setup problems on Windows and macOS. |
| `requirements.txt` | The one package the notebook needs. |

---

## Step 1 — Check your setup

Open a terminal in this folder and run:

```
python setup/verify_environment.py
```

On macOS you may need `python3` instead of `python`. On Windows, `py` also works.

If anything says **NOT YET**, fix it using `setup/TROUBLESHOOTING.md` before
going further. If you are still stuck, post the full output to the Q&A
discussion — copy the text, not a photo of your screen.

## Step 2 — Open the lab

**In VS Code (recommended):** open this folder with *File → Open Folder*, then
click `lab1_unit_converter.ipynb`. When VS Code asks you to pick a kernel,
choose your Python 3.12 installation.

**In JupyterLab (alternative):** run `pip install jupyterlab`, then
`jupyter lab` from this folder.

Work through the notebook **in order**. Each section with a crimson heading
teaches one idea with a worked example; each orange **EXERCISE** is yours.

## Step 3 — Check your work

When you think you are done, run:

```
python check_my_work.py
```

It runs your exercises and tells you what is working and what is not yet,
with a hint for each. You can run it as often as you like.

It is a **self-check, not your grade.** Exercise 1 (your plan) and code
clarity are graded by your instructor, who may also run additional checks.

## Step 4 — Submit on Canvas

Upload **both** of these files to the Lab 1 assignment:

1. `lab1_unit_converter.ipynb`
2. `ai_use_reflection.md`

Before you upload, restart the notebook and run every cell from the top, so
that what your instructor sees is what your code actually does.

---

## How Lab 1 is graded — 35 points

| Exercise | Points | Graded by |
|---|---|---|
| 1 · Your plan | 5 | Instructor |
| 2 · Variables and expressions | 5 | Self-check |
| 3 · Predict the type | 4 | Self-check |
| 4 · Type conversion | 5 | Self-check |
| 5 · Formatted output | 4 | Self-check |
| 6 · The converter | 10 | Self-check |
| Code clarity | 2 | Instructor |

The AI-Use Reflection is a separate assignment worth 15 points.

---

## Getting help

- **Q&A discussion on Canvas** — the fastest route. Post what you tried, what
  you expected, and what actually happened. Classmates often answer within the hour.
- **Office hours** — see the syllabus for times.
- **SPS Learning Studios** — free drop-in support for coding.

Being stuck is a normal part of programming, not a sign you are doing it wrong.
The most useful thing you can do is describe *exactly* where you are stuck.
