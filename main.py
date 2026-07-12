from pawpal_system import Owner, Pet, Task, Scheduler


owner = Owner("Jake", 90)

dog = Pet("Biscuit", "Dog", 4)
cat = Pet("Mochi", "Cat", 3)

dog.add_task(Task("Morning walk", 30, 3, "Exercise"))
dog.add_task(Task("Breakfast", 10, 2, "Feeding"))
cat.add_task(Task("Medication", 15, 3, "Health"))
cat.add_task(Task("Play time", 20, 1, "Enrichment"))

owner.add_pet(dog)
owner.add_pet(cat)

scheduler = Scheduler()
today_schedule = scheduler.generate_schedule(owner)

print("Today's Schedule")
print("----------------")

for task in today_schedule:
    print(task.get_details())