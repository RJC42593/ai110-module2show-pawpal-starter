from pawpal_system import Pet, Task, Scheduler
from datetime import date, timedelta


def test_mark_complete():
    task = Task("Morning Walk", 30, 3, "Exercise")

    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_mark_task_complete_creates_recurring_task():
    scheduler = Scheduler()

    pet = Pet("Mochi", "Cat", 3)

    task = Task(
        "Medication",
        15,
        3,
        "Health",
        frequency="daily",
        due_date=date.today()
    )

    pet.add_task(task)

    new_task = scheduler.mark_task_complete(task, pet)

    assert task.completed is True
    assert new_task is not None
    assert new_task.completed is False
    assert new_task.due_date == task.due_date + timedelta(days=1)


def test_add_task():
    pet = Pet("Biscuit", "Dog", 4)

    assert len(pet.tasks) == 0

    task = Task("Breakfast", 10, 2, "Feeding")
    pet.add_task(task)

    assert len(pet.tasks) == 1


def test_sort_by_time():
    scheduler = Scheduler()

    task1 = Task("Walk", 30, 3, "Exercise", time="09:00")
    task2 = Task("Breakfast", 10, 2, "Feeding", time="08:00")
    task3 = Task("Medication", 15, 3, "Health", time="10:00")

    tasks = [task1, task2, task3]

    sorted_tasks = scheduler.sort_by_time(tasks)

    assert sorted_tasks[0].name == "Breakfast"
    assert sorted_tasks[1].name == "Walk"
    assert sorted_tasks[2].name == "Medication"


def test_detect_conflicts():
    scheduler = Scheduler()

    task1 = Task("Walk", 30, 3, "Exercise", time="08:30")
    task2 = Task("Medication", 15, 3, "Health", time="08:30")
    task3 = Task("Breakfast", 10, 2, "Feeding", time="09:00")

    conflicts = scheduler.detect_conflicts([task1, task2, task3])

    assert len(conflicts) == 1
    assert conflicts[0] == (task1, task2)           