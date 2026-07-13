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

Although my original class structure remained the same, I added new scheduling features during implementation. The Scheduler class gained methods for sorting tasks, filtering tasks, detecting conflicts, and handling recurring tasks. The Task class also supports recurring tasks by storing recurrence information and creating the next occurrence when a recurring task is completed. These additions expanded the scheduler's capabilities while keeping the original design organized.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?

My scheduler considers several constraints when generating a schedule. It sorts tasks by scheduled time so they appear in chronological order, filters tasks based on user-selected criteria, detects tasks scheduled at the same time, and supports recurring daily and weekly tasks. Priority values are also stored with each task so more important tasks can easily be identified.

- How did you decide which constraints mattered most?

I considered time to be the most important constraint because pet owners need to know exactly when each task should be completed. Organizing tasks chronologically creates a schedule that is easy to follow, while conflict detection helps identify situations where multiple tasks occur at the same time.

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

I used AI throughout the project to help brainstorm the system design, explain new programming concepts, debug errors, review my code, generate test cases, and improve documentation. Rather than simply copying code, I asked for explanations of how each algorithm worked so I could understand the implementation before adding it to my project.

- What kinds of prompts or questions were most helpful?

•  "How can I implement this feature?" 
•  "Explain this code line by line." 
•  "Where should I place this code?" 
•  "Why is this test failing?"


**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.

One example of not accepting an AI suggestion as-is was during the conflict detection feature. I reviewed both a nested-loop solution and a dictionary-based solution. Although the dictionary approach was more efficient, I chose to keep the nested-loop implementation because it was easier to read, understand, and maintain for a relatively small number of tasks.

- How did you evaluate or verify what the AI suggested?

I verified AI suggestions by running my program, executing my pytest test suite, checking that all five tests passed, and making sure the program produced the expected output before keeping the changes.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?

I created tests to verify that:
•	tasks are sorted into chronological order, 
•	filtering returns the correct tasks, 
•	conflict detection identifies tasks scheduled at the same time, 
•	recurring tasks create a new task with the correct future due date, and 
•	the scheduler behaves correctly under normal conditions. 

- Why were these tests important?

These tests were important because they verified the core scheduling algorithms and ensured that new features did not break existing functionality.

**b. Confidence**

- How confident are you that your scheduler works correctly?

I am confident that my scheduler works correctly because all five automated tests pass successfully and the application behaves as expected during manual testing.

- What edge cases would you test next if you had more time?

If I had more time, I would add tests for additional edge cases such as:
•	empty task lists, 
•	multiple tasks sharing the same time, 
•	overlapping task durations, 
•	weekly recurring tasks, and 
•	larger task lists to evaluate performance.


---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

The part I am most satisfied with is building the scheduling logic step by step while learning how each algorithm worked. I also enjoyed seeing the final application organize tasks, detect conflicts, and handle recurring tasks successfully.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

If I continued developing PawPal+, I would improve the scheduler by detecting overlapping task durations instead of only exact matching start times. I would also add support for editing and deleting tasks directly from the interface and allow users to customize scheduling preferences.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

One important lesson I learned is that AI is most effective when it is used as a learning and collaboration tool rather than simply generating code. I found it valuable to ask questions, review the suggestions carefully, test the results, and make my own decisions about which solutions best fit my project.