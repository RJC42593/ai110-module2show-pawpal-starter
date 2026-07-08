from dataclasses import dataclass, field


@dataclass
class Task:
    name: str
    duration: int
    priority: int
    category: str
    completed: bool = False

    def mark_complete(self):
        self.completed = True

    def update_priority(self, priority):
        self.priority = priority

    def get_details(self):
        return (
            f"{self.name} ({self.category}) - "
            f"{self.duration} min - Priority {self.priority}"
        )


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks


@dataclass
class Owner:
    name: str
    available_time: int
    pets: list = field(default_factory=list)

    def add_pet(self, pet):
        self.pets.append(pet)

    def remove_pet(self, pet):
        if pet in self.pets:
            self.pets.remove(pet)

    def view_schedule(self):
        for pet in self.pets:
            print(f"\n{pet.name}'s Tasks:")
            for task in pet.tasks:
                print(task.get_details())


class Scheduler:
    def __init__(self):
        self.daily_plan = []

    def generate_schedule(self, owner):
        tasks = []

        for pet in owner.pets:
            tasks.extend(pet.tasks)

        tasks = self.sort_tasks(tasks)
        tasks = self.filter_tasks(tasks, owner.available_time)

        self.daily_plan = tasks
        return self.daily_plan

    def sort_tasks(self, tasks):
        return sorted(tasks, key=lambda task: task.priority, reverse=True)

    def filter_tasks(self, tasks, available_time):
        selected = []
        total_time = 0

        for task in tasks:
            if total_time + task.duration <= available_time:
                selected.append(task)
                total_time += task.duration

        return selected

    def detect_conflicts(self, tasks):
        total_time = sum(task.duration for task in tasks)
        return total_time