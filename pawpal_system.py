from dataclasses import dataclass, field


@dataclass
class Task:
    name: str
    duration: int
    priority: int
    category: str
    completed: bool = False

    def mark_complete(self):
        pass

    def update_priority(self, priority):
        pass

    def get_details(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        pass

    def remove_task(self, task):
        pass

    def get_tasks(self):
        pass


@dataclass
class Owner:
    name: str
    available_time: int
    pets: list = field(default_factory=list)

    def add_pet(self, pet):
        pass

    def remove_pet(self, pet):
        pass

    def view_schedule(self):
        pass


class Scheduler:
    def __init__(self):
        self.tasks = []
        self.daily_plan = []

    def generate_schedule(self):
        pass

    def sort_tasks(self):
        pass

    def filter_tasks(self):
        pass

    def detect_conflicts(self):
        pass