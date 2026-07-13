import streamlit as st

from pawpal_system import Owner, Pet, Task, Scheduler

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jake", 90)

owner = st.session_state.owner

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])


pet_age = st.number_input(
    "Pet age",
    min_value=0,
    max_value=50,
    value=1,
)

if st.button("Add pet"):
    new_pet = Pet(
        name=pet_name,
        species=species,
        age=int(pet_age),
    )

    owner.add_pet(new_pet)
    st.success(f"{pet_name} was added successfully!")

if owner.pets:
    st.write("Your pets:")

    for pet in owner.pets:
        st.write(
            f"- {pet.name} — {pet.species}, age {pet.age}"
        )
else:
    st.info("No pets have been added yet.")

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3, col4 = st.columns(4)

with col1:
    task_title = st.text_input("Task title", value="Morning walk")

with col2:
    duration = st.number_input(
        "Duration (minutes)",
        min_value=1,
        max_value=240,
        value=20,
    )

with col3:
    priority = st.selectbox(
        "Priority",
        ["low", "medium", "high"],
        index=2,
    )

with col4:
    task_time = st.time_input("Scheduled time")

if st.button("Add task"):
    st.session_state.tasks.append(
        {
            "title": task_title,
            "duration_minutes": int(duration),
            "priority": priority,
            "time": task_time.strftime("%H:%M"),
        }
    )

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("Generate a schedule using your PawPal+ scheduling logic.")

if st.button("Generate schedule"):
    if not owner.pets:
        st.warning("Please add a pet first.")

    elif not st.session_state.tasks:
        st.warning("Please add at least one task.")

    else:
        pet = owner.pets[0]
        pet.tasks.clear()

        priority_map = {
            "low": 1,
            "medium": 2,
            "high": 3,
        }

        for task_data in st.session_state.tasks:
            task = Task(
                name=task_data["title"],
                duration=task_data["duration_minutes"],
                priority=priority_map[task_data["priority"]],
                category="Pet Care",
                time=task_data["time"],
            )

            pet.add_task(task)

        scheduler = Scheduler()
        sorted_tasks = scheduler.sort_by_time(pet.tasks)
        conflicts = scheduler.detect_conflicts(sorted_tasks)

        if conflicts:
            for task1, task2 in conflicts:
                st.warning(
                    f"{task1.name} conflicts with "
                    f"{task2.name} at {task1.time}."
                )
        else:
            st.success("Schedule generated with no conflicts.")

        schedule_rows = []

        for task in sorted_tasks:
            schedule_rows.append(
                {
                    "Time": task.time,
                    "Task": task.name,
                    "Duration": f"{task.duration} minutes",
                    "Priority": task.priority,
                    "Pet": pet.name,
                }
            )

        st.table(schedule_rows)
