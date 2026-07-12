# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.

### 1a. Initial Design

I designed the PawPal+ system using four main classes: **Owner**, **Pet**, **Task**, and **Scheduler**.

* **Owner** represents the pet owner and stores information about the owner's pets. It is responsible for adding, removing, and viewing pets and their schedules.
* **Pet** represents an individual pet. It stores information such as the pet's name, species, age, and a list of care tasks. It is responsible for managing those tasks.
* **Task** represents a pet care activity such as feeding, walking, medication, or grooming. Each task stores information like its duration, priority, category, and completion status.
* **Scheduler** is responsible for organizing tasks into a daily schedule. It will sort tasks by priority, filter tasks based on available time, detect scheduling conflicts, and generate the daily plan.

These classes separate responsibilities clearly and provide a modular foundation that can be expanded as more scheduling features are implemented.


## System Design

1. Add and manage pets
   - The user should be able to create a pet profile and store information such as the pet's name, species, age, and care notes.

2. Create and manage pet care tasks
   - The user should be able to add tasks such as feeding, walks, medication, grooming, and enrichment activities. Each task should include a duration and priority level.

3. Generate and view a daily care schedule
   - The user should be able to generate a daily plan that organizes tasks based on priorities and available time, then view the recommended schedule along with an explanation of why tasks were selected.
   
- What classes did you include, and what responsibilities did you assign to each?

**b. Design changes**

- Did your design change during implementation?

### 1b. Design Changes

After reviewing my initial design, I decided not to make any major changes. The four classes (Owner, Pet, Task, and Scheduler) clearly separate responsibilities and provide a good foundation for implementing the scheduling logic in later phases. I may add additional attributes or methods later as new features are implemented.

- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.

   One tradeoff in my scheduler is that conflict detection only checks whether two tasks have the exact same start time. For example, it identifies a conflict if two tasks are both scheduled for 8:30 AM, but it does not detect overlapping durations, such as one task running from 8:00 AM to 8:45 AM and another starting at 8:30 AM.

- Why is that tradeoff reasonable for this scenario?

This approach is reasonable for the current version of PawPal+ because it keeps the algorithm simple, readable, and easy to verify. A future version could calculate each task's ending time and detect partial overlaps for more accurate scheduling.

I also reviewed a more efficient dictionary-based conflict detection algorithm. Although it could perform better with a very large number of tasks, I kept the nested-loop version because the app is expected to manage a relatively small task list and the original algorithm is easier to understand and maintain.


---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
