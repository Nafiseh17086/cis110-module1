# CIS 110 · Introduction to Programming — Module 1

Welcome. Everything for the **Welcome module** and **Module 1** is in this folder.

> **New here? Start with [`welcome/01_start_here.md`](welcome/01_start_here.md).**
> It has your pre-course checklist.

> **Lab 1 is Unassisted.** Do not use an AI assistant for any part of it —
> not to write code, and not to explain something. You may use the assigned
> readings, the [Python documentation](https://docs.python.org/3/tutorial/), and
> the Q&A discussion on Canvas. See the [AI-Use Policy](welcome/06_ai_use_policy.md).

---

## What's in this folder

### Welcome module — read before class starts
| Page | |
|---|---|
| [Start here](welcome/01_start_here.md) | Introduction and **pre-course checklist** |
| [Course overview](welcome/02_course_overview.md) | Description, objectives, schedule, grading |
| [About the instructor](welcome/03_about_the_instructor.md) · [About the TA](welcome/04_about_the_ta.md) | Who is teaching |
| [Library and university resources](welcome/05_library_and_resources.md) | Library guides, AccessibleNU, advising |
| [**AI-Use Policy**](welcome/06_ai_use_policy.md) | The four permission levels — required reading |
| [Academic integrity](welcome/07_academic_integrity.md) | Where the line sits in this course |
| [How to complete an AI-Use Reflection](welcome/08_how_to_complete_an_ai_use_reflection.md) | Guide and a worked example |
| [Getting help](welcome/09_getting_help.md) | Where to go when you are stuck |
| [Discussions](welcome/10_discussions.md) · [Pre-course survey](welcome/pre_course_survey.md) | Introductions prompt and survey questions |

### Module 1
| File | |
|---|---|
| [Module overview](module1/module1_overview.md) | Objectives, readings, assessments |
| [Videos and media](module1/videos_and_media.md) | The three Module 1 videos |
| [Sync Session 1](module1/sync_session_1.md) | Orientation and environment check — agenda |
| [`lab1_unit_converter.ipynb`](lab1_unit_converter.ipynb) | **The lab.** Work through it top to bottom. |
| [`ai_use_reflection.md`](ai_use_reflection.md) | AI-Use Reflection 1 — fill in and submit |
| `check_my_work.py` | Self-check to run before you submit |

### Setup
| File | |
|---|---|
| [Setup guide](setup/SETUP_GUIDE.md) | Step-by-step install, matching the setup screencast |
| [Troubleshooting](setup/TROUBLESHOOTING.md) | Fixes for common Windows and macOS problems |
| `setup/verify_environment.py` | Checks your setup is ready |

---

## Step 1 — Check your setup

Open a terminal in this folder and run:

```
python setup/verify_environment.py
```

On macOS you may need `python3` instead of `python`. On Windows, `py` also works.

Not set up yet? Follow [`setup/SETUP_GUIDE.md`](setup/SETUP_GUIDE.md) first.
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
- **SPS Learning Studios** — free, self-paced support with an instructor available. See [Getting help](welcome/09_getting_help.md).

Being stuck is a normal part of programming, not a sign you are doing it wrong.
The most useful thing you can do is describe *exactly* where you are stuck.
