# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.


## 🖥️ Sample Output

```
Tasks Sorted by Time
--------------------
08:30 - Morning walk (Exercise) - 30 min - Priority 3
08:30 - Medication (Health) - 15 min - Priority 3
09:00 - Breakfast (Feeding) - 10 min - Priority 2
14:00 - Play time (Enrichment) - 20 min - Priority 1

Incomplete Tasks
----------------
Breakfast (Feeding) - 10 min - Priority 2
Morning walk (Exercise) - 30 min - Priority 3
Play time (Enrichment) - 20 min - Priority 1
Medication (Health) - 15 min - Priority 3

Biscuit's Tasks
---------------
Breakfast (Feeding) - 10 min - Priority 2
Morning walk (Exercise) - 30 min - Priority 3

Task Conflicts
--------------
Warning: 'Morning walk' conflicts with 'Medication' at 08:30.

Recurring Task Test
-------------------
Original completed: True
Next task: Evening medication
Next due date: 2026-07-13
Next task completed: False

```



## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Sorts tasks by their scheduled time using `sorted()`. |
| Filtering | `Scheduler.filter_by_status()`, `Scheduler.filter_by_pet()` | Filters tasks by completion status or by pet name. |
| Conflict handling | `Scheduler.detect_conflicts()` | Detects tasks that are scheduled for the same time and returns the conflicting task pairs. |
| Recurring tasks | `Scheduler.mark_task_complete()` | Marks recurring tasks complete and automatically creates the next occurrence using `timedelta`. |

## 📸 Demo Walkthrough


1. Open the PawPal+ Streamlit app.
2. Enter a task title, duration, priority, and scheduled time.
3. Click **Add Task** to add the task to the list.
4. Repeat until all desired pet care tasks have been entered.
5. Click **Generate Schedule** to create a daily schedule.
6. The schedule is displayed in chronological order.
7. If two tasks share the same scheduled time, the app displays a warning message identifying the conflict.


**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->


## 🧪 Testing PawPal+


### Running the Tests

Run the automated test suite with:

```bash
python -m pytest
```

### What the Tests Cover

The test suite verifies:

- Tasks are sorted into chronological order.
- Filtering returns the correct tasks.
- Recurring daily tasks create a new task for the next day.
- Conflict detection identifies tasks scheduled at the same time.
- Task completion updates the completed status correctly.

### Successful Test Run

```
============================= test session starts =============================
platform win32 -- Python 3.11.4, pytest-9.0.3, pluggy-1.6.0
collected 5 items

tests/test_pawpal.py .....                                           [100%]

============================== 5 passed in 0.10s ==============================
```

### Confidence Level

(5/5)

All automated tests pass successfully, including sorting, filtering, recurring task creation, conflict detection, and task completion behavior. While additional edge cases could always be added, the current test suite provides strong confidence that the core functionality works as intended.