from pawpal_system import Pet, Task


def test_mark_complete():
    task = Task("Morning Walk", 30, 3, "Exercise")

    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_add_task():
    pet = Pet("Biscuit", "Dog", 4)

    assert len(pet.tasks) == 0

    task = Task("Breakfast", 10, 2, "Feeding")
    pet.add_task(task)

    assert len(pet.tasks) == 1