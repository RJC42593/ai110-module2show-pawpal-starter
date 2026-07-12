from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import date

owner = Owner("Jake", 90)

dog = Pet("Biscuit", "Dog", 4)
cat = Pet("Mochi", "Cat", 3)

dog.add_task(Task("Breakfast", 10, 2, "Feeding", "09:00"))
dog.add_task(Task("Morning walk", 30, 3, "Exercise", "08:30"))
cat.add_task(Task("Play time", 20, 1, "Enrichment", "14:00"))
cat.add_task(Task("Medication", 15, 3, "Health", "08:30"))

owner.add_pet(dog)
owner.add_pet(cat)

scheduler = Scheduler()

all_tasks = []

for pet in owner.pets:
    all_tasks.extend(pet.tasks)

sorted_tasks = scheduler.sort_by_time(all_tasks)

print("Tasks Sorted by Time")
print("--------------------")

for task in sorted_tasks:
    print(f"{task.time} - {task.get_details()}")

incomplete_tasks = scheduler.filter_by_status(
    all_tasks,
    completed=False,
)

print("\nIncomplete Tasks")
print("----------------")

for task in incomplete_tasks:
    print(task.get_details())

biscuit_tasks = scheduler.filter_by_pet(
    owner,
    "Biscuit",
)

print("\nBiscuit's Tasks")
print("---------------")

for task in biscuit_tasks:
    print(task.get_details())

print("\nTask Conflicts")
print("--------------")

conflicts = scheduler.detect_conflicts(all_tasks)

if not conflicts:
    print("No conflicts found.")
else:
    for task1, task2 in conflicts:
        print(
            f"Warning: '{task1.name}' conflicts with "
            f"'{task2.name}' at {task1.time}."
        )


daily_task = Task(
    name="Evening medication",
    duration=5,
    priority=3,
    category="Health",
    time="20:00",
    frequency="daily",
    due_date=date.today(),
)

cat.add_task(daily_task)

next_task = scheduler.mark_task_complete(daily_task, cat)

print("\nRecurring Task Test")
print("-------------------")
print(f"Original completed: {daily_task.completed}")

if next_task:
    print(f"Next task: {next_task.name}")
    print(f"Next due date: {next_task.due_date}")
    print(f"Next task completed: {next_task.completed}")