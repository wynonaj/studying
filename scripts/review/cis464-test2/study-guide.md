# **CIS 464 Complete Exam Study Guide**

Chapters 4–7 | Schwalbe | Based on all four uploaded lecture PowerPoints

This will be your comprehensive study guide for tomorrow's exam. I'm organizing each chapter exactly how you requested:

1. **Every learning objective, answered individually.** Definitions, explanations, examples, comparisons, and calculations.
2. **All remaining chapter material.** Additional concepts, vocabulary, theories, examples, and details from your professor's slides.
3. **Exam preparation.** Commonly confused terms, calculation practice, and what to memorize.

I'll also explain technical vocabulary in ordinary language, so you don't have to already understand project management to follow along.

The four chapters cover different parts of managing a project:

| Chapter                                           | Main question                                                         |
| ------------------------------------------------- | --------------------------------------------------------------------- |
| **4. Project Scope Planning**                     | What exactly are we supposed to deliver?                              |
| **5. Schedule and Budget Planning**               | How long will it take, and how much will it cost?                     |
| **6. Stakeholders, Resources, and Risk**          | Who is involved, what resources do we need, and what could happen?    |
| **7. Communications, Leadership, and Motivation** | How do we communicate, lead, motivate, and work effectively together? |

Your slides sometimes introduce concepts without giving a complete definition. Where necessary, I'll add a standard project management explanation or a worked example and distinguish that from what the slides explicitly teach.

# **Chapter 4: Project Scope Planning**

## **Part 1. All five learning objectives**

## **Objective 1: Define scope**

**Project scope** is all the work and processes required to create the project's deliverables, including supporting activities and documentation.

The scope establishes the boundaries of a project: what is included and what is excluded.

### **Important definitions**

| Term           | Definition                                                                              |
| -------------- | --------------------------------------------------------------------------------------- |
| Project        | A temporary effort undertaken to create a unique product, service, or result            |
| Scope          | All work required to complete the project                                               |
| Deliverable    | A product, service, document, or result that the project must produce                   |
| Product scope  | The features and functions of the product or service being created                      |
| Project scope  | The work required to deliver that product or service                                    |
| In scope       | Work that is included in the project                                                    |
| Out of scope   | Work that is excluded from the project                                                  |
| Scope baseline | The approved scope statement, WBS, and WBS dictionary used to measure and control scope |
| Stakeholder    | A person, group, or organization that can affect or be affected by a project            |

### **What counts as project scope?**

Imagine you're creating a league management system for a county recreation department.

**In scope:** Configuring the system, migrating registration data, testing features, training staff, and preparing documentation.

**Out of scope:** Replacing every computer in the county, redesigning unrelated county websites, or developing a separate application not included in the agreement.

Your professor specifically lists these exclusions:

- Work that is not part of the project.
- Changes intended for future projects.
- Work already performed in previous projects.
- Unrelated ongoing business operations.

### **Why define what is out of scope?**

Because otherwise stakeholders may expect work that was never agreed upon.

Defining exclusions protects the budget, schedule, project team, and customer expectations.

**Exam distinction:** Product scope describes what the product does. Project scope describes the work needed to create it.

## **Objective 2: Prepare the five scope management deliverables**

### **A. Scope statement**

A **scope statement** is a detailed description of the project's deliverables and boundaries.

Your slides identify the following contents:

- Product scope description.
- User acceptance criteria.
- Detailed deliverables.
- Boundaries.
- Constraints.
- Assumptions.

**Product scope description:** Explains the features and characteristics of the final product.

**Acceptance criteria:** Specific conditions that must be satisfied before a deliverable can be accepted.

**Constraints:** Restrictions on the project, such as a deadline, budget, or legal requirement.

**Assumptions:** Things believed to be true for planning purposes, even though they may not yet be confirmed.

**Project boundaries:** The dividing line between what the project includes and excludes.

Example scope statement:

A project will configure an online league management system that supports participant registration, team assignments, payment processing, and scheduling. Staff training and system testing are included. Developing a custom mobile application is excluded. The system must be operational before the next registration period.

**Relationship to the project charter:** The charter authorizes the project and provides a starting point. The scope statement develops its requirements and deliverables in greater detail.

### **B. Work Breakdown Structure (WBS)**

A **Work Breakdown Structure** is a hierarchical breakdown of project work, generally organized by deliverables.

Hierarchical means arranged in levels, from the largest component down to smaller components.

Example:

**1.0 League Management System**

1.1 System Configuration

Registration, payments, scheduling

1.2 Data Migration

Existing participant and team records

1.3 Testing

Functional tests and acceptance tests

1.4 Training

Staff guides and training sessions

**Work package:** The lowest-level component of the WBS, representing work that can be estimated, assigned, monitored, and controlled.

**WBS dictionary:** A supporting document that describes WBS components in more detail.

A WBS dictionary may contain a work package's description, assigned owner, requirements, assumptions, acceptance criteria, and estimated resources.

Your professor emphasizes that **WBS deliverables should generally be described using nouns, while schedule activities use verbs**.

For example:

- WBS deliverable: *Training materials*
- Schedule activity: *Prepare training materials*

The WBS is used as a foundation for scheduling, cost estimation, resource assignment, and monitoring.

### **C. Scope management plan**

A **scope management plan** explains how the project's scope will be defined, developed, validated, and controlled.

Your slides list five key activities:

1. Preparing the detailed scope statement.
2. Creating the WBS.
3. Maintaining and approving the WBS.
4. Obtaining formal acceptance of completed deliverables.
5. Controlling scope change requests.

It is part of the overall project management plan.

**Example:** A scope management plan might require all feature requests to be documented, evaluated for cost and schedule impacts, and approved by the project sponsor.

### **D. Requirements management plan**

A **requirements management plan** explains how project requirements will be analyzed, documented, and managed.

It may describe:

- How requirements are planned and collected.
- How requirements are tracked and reported.
- How requirements are prioritized.
- How configuration management is performed.
- How product metrics are used.
- How requirement attributes are recorded and traced.

**Configuration management:** A structured process for identifying, tracking, and controlling changes to project products, documents, and their versions.

**Product metrics:** Measurements used to evaluate whether a product meets requirements, such as response time or error rate.

### **E. Requirements Traceability Matrix (RTM)**

A **Requirements Traceability Matrix** is a table that lists requirements, their attributes, and their status.

Its purpose is to make sure every requirement is addressed.

| ID | Requirement               | Priority | Status      | Validation        |
| -- | ------------------------- | -------- | ----------- | ----------------- |
| R1 | Users can register online | High     | Complete    | Registration test |
| R2 | System accepts payments   | High     | In progress | Payment test      |
| R3 | Staff can export reports  | Medium   | Not started | Report review     |

**Traceability** means being able to follow a requirement from its original business need through development and verification.

### **Memorize the differences**

| Document                     | What question does it answer?          |
| ---------------------------- | -------------------------------------- |
| Scope statement              | What are we delivering?                |
| WBS                          | How is the project's work broken down? |
| Scope management plan        | How will we manage scope?              |
| Requirements management plan | How will we manage requirements?       |
| RTM                          | Have all requirements been addressed?  |

## **Objective 3: List methods for collecting and validating requirements**

### **What is a requirement?**

A requirement is a condition or capability necessary for a product, service, or result to satisfy a business need.

Requirements should be clear enough that the project team can implement and measure them.

### **Types of requirements**

Your professor's slides list several overlapping categories.

| Type                     | Meaning                                        | Example                               |
| ------------------------ | ---------------------------------------------- | ------------------------------------- |
| Business                 | Organizational goal or need                    | Reduce registration processing time   |
| Stakeholder              | Need of a particular stakeholder               | Coaches need access to rosters        |
| User                     | What an end user needs                         | Participants need to view schedules   |
| Functional               | What a system must do                          | Send confirmation emails              |
| Nonfunctional            | How well a system must operate                 | Pages load within two seconds         |
| Technical                | Technical specifications or constraints        | Integrate with a payment gateway      |
| Operational              | Needs related to ongoing use and support       | Support staff can reset accounts      |
| Feasibility              | Whether a solution is practical                | Can the system run within the budget? |
| Solution                 | Capabilities required of the selected solution | Provide role-based access             |
| Transition               | Needs for moving from old to new systems       | Migrate existing records              |
| Product                  | Requirements of the final product              | Include a registration dashboard      |
| Process                  | Requirements for how work is performed         | Follow an approval procedure          |
| Quality                  | Standards the result must satisfy              | Pass specified acceptance tests       |
| Implementation           | Requirements for putting the solution into use | Complete staff training               |
| Architectural            | Requirements affecting system structure        | Use an approved integration approach  |
| Quality of Service (QoS) | Expected level of service or performance       | Meet an availability target           |
| Project                  | Conditions for carrying out the project        | Finish before the season begins       |

### **Methods of collecting requirements**

Your professor lists the following methods:

| Method                         | Definition                                                    | When useful                                       |
| ------------------------------ | ------------------------------------------------------------- | ------------------------------------------------- |
| Interviews                     | One-on-one or small-group conversations                       | Getting detailed stakeholder needs                |
| Focus groups                   | Structured discussion with selected participants              | Collecting opinions and preferences               |
| Facilitated workshops          | Guided sessions where stakeholders work together              | Resolving disagreements and defining requirements |
| Brainstorming                  | Generating many ideas before evaluating them                  | Identifying possible features                     |
| Questionnaires and surveys     | Standardized questions answered by respondents                | Collecting input from many people                 |
| Observation                    | Watching users perform their normal work                      | Discovering needs users may not mention           |
| Prototyping                    | Creating an early representation of a product                 | Helping users visualize requirements              |
| Document analysis              | Reviewing existing policies, forms, records, or procedures    | Understanding existing requirements               |
| Benchmarking                   | Comparing practices or performance with other organizations   | Identifying useful standards or improvements      |
| Joint Application Design (JAD) | Collaborative workshops involving users and system developers | Defining system requirements efficiently          |
| Use case modeling              | Describing interactions between actors and a system           | Understanding what users need the system to do    |

**Actor:** A person or external system interacting with the system being designed.

**Use case:** A description of how an actor interacts with a system to accomplish a goal.

### **Why requirements collection is difficult**

Your professor identifies several problems:

- Limited time.
- Stakeholders may not know what they want.
- Stakeholders may have unrealistic expectations.
- People may describe needs unclearly.
- Different stakeholders may disagree.
- IT systems are often difficult to visualize.
- Technology changes quickly.
- Existing products may require enhancements that affect other functions.

### **What is requirements validation?**

Requirements validation confirms that requirements accurately represent stakeholder needs and that the project is satisfying them.

Your slides emphasize two actions:

1. Confirm that the project team understands the requirements as the customer intended.
2. Check that requirements continue to be satisfied as the project progresses.

**Validation versus verification:** As an additional distinction, verification generally checks whether something meets its specifications, while validation checks whether it satisfies the intended need.

## **Objective 4: List approaches to building a WBS**

Your professor identifies these approaches:

| Approach      | Definition                                                                  |
| ------------- | --------------------------------------------------------------------------- |
| Top-down      | Begin with the entire project and decompose it into smaller components      |
| Bottom-up     | Identify detailed work components and combine them into higher-level groups |
| Mind mapping  | Visually arrange project ideas and their relationships                      |
| Brainstorming | Generate potential project components collaboratively                       |
| Analogy       | Adapt the WBS of a similar previous project                                 |
| Guidelines    | Follow established organizational or industry guidance                      |

**Decomposition** means breaking something large into smaller, manageable components.

Top-down is especially useful when the major deliverables are already known.

Bottom-up can be useful when team members understand detailed work but the overall structure is not yet finalized.

## **Objective 5: Explain how to control scope creep**

**Scope creep** is the gradual, uncontrolled expansion of project scope through added requirements or work.

### **Causes**

- Vague or incomplete requirements.
- Unclear scope boundaries.
- No formal change control process.
- Stakeholders adding features without considering consequences.
- Failure to validate requirements early.
- Poor stakeholder communication.

### **Methods of control**

**Integrated change control:** A formal process for evaluating, approving, rejecting, and documenting project changes.

**Variance analysis:** Comparing actual results with planned results to identify differences.

**Scope validation:** Inspecting deliverables with the customer, sponsor, or user to determine whether they meet agreed requirements.

**Better requirements collection:** Clarifying needs before substantial work begins.

**Continuous user involvement:** Keeping users engaged throughout the project to identify misunderstandings early.

A scope change can be appropriate. What matters is that its impact on time, cost, resources, and deliverables is evaluated and approved.

## **Part 2. Additional Chapter 4 material**

### **Agile scope management**

Your professor introduces several Agile techniques.

**Agile:** An approach to project delivery that emphasizes adaptability, frequent feedback, and incremental results.

**Iteration:** A short cycle of work.

**Sprint:** A fixed-length iteration used in Scrum.

**Increment:** A usable addition to the product.

### **Value Breakdown Structure (VBS)**

A VBS resembles a WBS but assigns value estimates to work packages.

The hierarchy introduced in your slides is:

Theme

Broad organizational goal

Initiative

Group of related epics

Epic

Large requirement spanning more than one sprint

User story

Small requirement from a user's perspective

### **MoSCoW prioritization**

A method of ranking requirements:

- **Must have:** Essential for success.
- **Should have:** Important but not absolutely essential.
- **Could have:** Desirable if time and resources allow.
- **Won't have:** Excluded from the current delivery.

### **INVEST rule for user stories**

| Letter | Meaning     | Explanation                               |
| ------ | ----------- | ----------------------------------------- |
| I      | Independent | Can be completed separately               |
| N      | Negotiable  | Details can be discussed and refined      |
| V      | Valuable    | Provides customer or business value       |
| E      | Estimable   | The team can reasonably estimate the work |
| S      | Small       | Can fit within an iteration               |
| T      | Testable    | Has criteria for determining completion   |

### **Definition of Done**

An agreed-upon list of conditions that must be met before a user story or product increment is considered complete.

For example, a registration feature may need to be implemented, tested, documented, and approved before it is done.

### **Big Visual Charts (BVCs)**

Also called **information radiators**.

These are visible displays showing current project information, such as tasks, progress, or issues, so team members can quickly understand the project's status.

### **Chapter 4 terms to know**

| Term                      | Meaning                                                |
| ------------------------- | ------------------------------------------------------ |
| Scope creep               | Uncontrolled expansion of project scope                |
| Scope baseline            | Approved scope documentation used for comparison       |
| Scope validation          | Confirming completed deliverables satisfy requirements |
| Requirements elicitation  | Discovering requirements from stakeholders             |
| Requirements traceability | Tracking requirements through the project              |
| Work package              | Lowest WBS level                                       |
| WBS dictionary            | Detailed descriptions of WBS components                |
| Acceptance criteria       | Conditions required for approval                       |
| Constraint                | A restriction                                          |
| Assumption                | Something treated as true for planning                 |
| Deliverable               | A required project output                              |
| Decomposition             | Breaking work into smaller parts                       |
| Integrated change control | Coordinated evaluation and approval of changes         |
| Variance                  | Difference between planned and actual performance      |
| Epic                      | Large body of Agile work                               |
| User story                | Requirement expressed from the user's perspective      |
| Definition of Done        | Agreed completion conditions                           |
| Information radiator      | Visible project status display                         |

**Chapter 4 exam focus:** Be able to distinguish the five scope documents, explain requirement collection and validation, identify WBS approaches, recognize Agile terminology, and explain how to prevent scope creep.

# **Chapter 5: Project Schedule and Budget Planning**

This chapter has two major sections: **schedule management** and **cost management**.

The schedule section includes the objectives you listed. Your PowerPoint also has a separate set of cost learning objectives, so I'm covering those too. That is important because the slides specifically include cost estimates, cost baselines, reserves, and earned value management.

## **Part 1. All schedule learning objectives**

## **Objective 1: Plan schedule management**

### **What is schedule management?**

**Project schedule management** is the process of planning, developing, monitoring, and controlling the timing of project activities.

It helps answer:

- What activities must be completed?
- What order should they happen in?
- How long will they take?
- When should they start and finish?
- Which delays would affect the entire project?

Your professor emphasizes that **time itself is fixed**. A project manager can adjust the schedule, but cannot change the number of hours in a day.

### **What is a schedule management plan?**

A **schedule management plan** explains how the project schedule will be created, measured, maintained, and controlled.

According to your slides, it includes:

| Component                     | Meaning                                                             |
| ----------------------------- | ------------------------------------------------------------------- |
| Schedule model                | The method or structure used to produce the schedule                |
| Level of accuracy             | How precise estimates should be                                     |
| Units of measure              | Hours, days, weeks, or other units                                  |
| Control thresholds            | How much schedule variation is acceptable before action is required |
| Performance measurement rules | How progress will be measured                                       |
| Reporting formats             | How schedule information will be presented                          |
| Process descriptions          | Procedures for managing the schedule                                |
| Scheduling methodology        | Approach such as Agile or critical path scheduling                  |
| Scheduling software           | Tools used to build and maintain the schedule                       |
| Schedule baseline             | Approved version of the schedule                                    |
| Contingency plans             | Planned actions if schedule problems occur                          |
| Change control procedures     | Rules for approving schedule changes                                |
| Reporting frequency           | How often progress is reported                                      |

### **Questions a project manager should ask**

Your professor lists these planning questions:

1. Who needs to participate in schedule planning?
2. Are there special terms or definitions the team must understand?
3. Which documents must be reviewed or secured?
4. Who approves the schedule and changes to it?
5. Which external influences could affect the schedule?
6. How will activities be defined?

**Example:** If the county needs its league registration system ready before spring registration, that deadline must be considered when planning activities and dependencies.

## **Objective 2: Develop the schedule on a project**

A **project schedule** shows activities, their estimated durations, dependencies, and planned start and finish dates.

### **Steps for developing a schedule**

Your slides explain the process as follows:

1. Identify the activities.
2. Put the activities in a logical order.
3. Determine which activities depend on other activities.
4. Identify why those dependencies exist.
5. Establish dependency relationships.
6. Determine how the activities depend on one another.

You also need to estimate durations and consider available resources before finalizing the schedule.

### **Activity**

An **activity** is a specific action required to produce a project deliverable.

Example: *Configure online registration.*

### **Activity list**

An **activity list** identifies the scheduled activities and generally includes their names, identifiers, and descriptions.

| ID | Activity            | Description                       |
| -- | ------------------- | --------------------------------- |
| A1 | Gather requirements | Confirm registration requirements |
| A2 | Configure system    | Set up required features          |
| A3 | Test system         | Verify functionality              |
| A4 | Train employees     | Prepare staff to use the system   |

### **Activity attributes**

**Activity attributes** provide additional information about activities.

Your slides list:

- Predecessors.
- Successors.
- Logical relationships.
- Leads and lags.
- Resource requirements.
- Constraints.
- Imposed dates.
- Assumptions.

**Predecessor:** An activity that comes before another activity in a dependency relationship.

**Successor:** An activity that follows another activity.

**Lead:** Allows an activity to begin earlier relative to its predecessor.

**Lag:** A waiting period between dependent activities.

**Imposed date:** A start or finish date required by an external condition or management decision.

The activity list should agree with the WBS and WBS dictionary.

### **Methods for estimating schedules**

Your professor identifies:

- Brainstorming.
- Benchmarking.
- Educated estimates.
- Reviewing project documents.
- Bottom-up estimating.
- Top-down estimating.

**Top-down estimating:** Use a high-level estimate and break it into smaller components.

**Bottom-up estimating:** Estimate individual activities and combine them into an overall estimate.

**Benchmarking:** Use similar projects or industry information as a comparison.

## **Objective 3: Classify dependencies by type and sequence**

This is one of the most important sections in Chapter 5.

### **What is a dependency?**

A **dependency** is a relationship between project activities that affects the order in which they can start or finish.

Example: You generally need to configure a feature before you can finish testing it.

Your professor separates dependencies into two different classifications:

1. **Why** the activities are dependent.
2. **How** the activities are dependent.

### **A. Four categories explaining WHY tasks are dependent**

| Category      | Definition                                                       | Example                                                                     |
| ------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Mandatory     | Required by the nature of the work; hard logic                   | Install software before testing it                                          |
| Discretionary | Chosen by the project team; soft logic                           | Complete one report before starting another, even though both could overlap |
| Internal      | Relationship between activities under the project team's control | Team testing follows team configuration                                     |
| External      | Relationship involving activities outside the project            | Waiting for vendor approval                                                 |

These categories can overlap.

A dependency might be both mandatory and internal, or discretionary and external.

**Mandatory versus discretionary:** Is the order required, or did the team choose it?

**Internal versus external:** Is the relationship controlled within the project, or does it involve something outside the project?

### **B. Four dependency relationships explaining HOW tasks are dependent**

## **FS**

**Finish-to-Start**

Task B cannot start until Task A finishes.

Example: Finish configuration → Start testing

## **SS**

**Start-to-Start**

Task B cannot start until Task A starts.

Example: Start dismantling → Start cleanup

## **FF**

**Finish-to-Finish**

Task B cannot finish until Task A finishes.

Example: Complete documentation and review together

## **SF**

**Start-to-Finish**

Task B cannot finish until Task A starts.

Example: Old support shift cannot end until replacement shift starts

**Finish-to-Start (FS)** is the most common relationship.

**Start-to-Finish (SF)** is uncommon and can be confusing.

A dependency does not necessarily mean one task must finish before the next starts. That is only the FS relationship.

## **Objective 4: Identify the critical path**

### **What is the critical path?**

The **critical path is the longest-duration path through the project's dependency network**.

It determines the shortest possible time in which the project can be completed, given the scheduled activities and dependencies.

Your professor specifically emphasizes:

- Every required activity must be completed.
- Critical does not mean the activity is more important than other work.
- Critical refers to whether delaying the activity will delay the project.
- A delay in a critical activity can delay the entire project.

### **Example: Find the critical path**

Suppose a project has two paths.

**Path 1: A → B → D**

12 days

A

3 days

B

5 days

D

4 days

3 + 5 + 4 = 12 days

**Path 2: A → C → D**

9 days

A

3 days

C

2 days

D

4 days

3 + 2 + 4 = 9 days

**Critical path = A → B → D, because it takes 12 days.**

The project cannot finish in fewer than 12 days under these assumptions.

### **What is slack or float?**

**Slack, also called float, is the amount of time an activity can be delayed without delaying a dependent activity or the project.**

For exam calculations, distinguish total float from free float:

**Total float:** How long an activity can be delayed without delaying the project's completion date.

**Free float:** How long an activity can be delayed without delaying the early start of a successor.

Your slides introduce these four scheduling values:

| Abbreviation | Meaning      |
| ------------ | ------------ |
| ES           | Early Start  |
| EF           | Early Finish |
| LS           | Late Start   |
| LF           | Late Finish  |

**Early Start (ES):** Earliest time an activity can begin.

**Early Finish (EF):** Earliest time an activity can finish.

**Late Start (LS):** Latest time an activity can begin without delaying the project.

**Late Finish (LF):** Latest time an activity can finish without delaying the project.

### **Slack formulas**

\\[ \text{Total Slack}=LS-ES \\]

or

\\[ \text{Total Slack}=LF-EF \\]

Example:

- ES = 2
- EF = 7
- LS = 5
- LF = 10

Slack = 5 − 2 = **3 days**.

An activity on the critical path generally has zero total slack in the basic critical path problems used in introductory courses.

### **Forward pass and backward pass**

These are standard calculation techniques that expand on your slides' ES, EF, LS, and LF terminology.

**Forward pass:** Calculate earliest start and finish times.

\\[ EF=ES+\text{Duration} \\]

The successor's ES is determined by the latest EF of its predecessors in a basic FS network.

**Backward pass:** Calculate latest finish and start times.

\\[ LS=LF-\text{Duration} \\]

The predecessor's LF is determined by the earliest LS of its successors in a basic FS network.

For a basic network beginning at time zero, a critical path activity generally has ES = LS and EF = LF.

## **Objective 5: Compare Murphy's Law and Parkinson's Law**

Your professor explicitly includes both.

| Law             | Definition                              | Example                                                        |
| --------------- | --------------------------------------- | -------------------------------------------------------------- |
| Murphy's Law    | If something can go wrong, it will      | A system fails during an important demonstration               |
| Parkinson's Law | Work expands to fill the time available | A task that could take two days takes the entire allotted week |

**Murphy's Law** is about problems and uncertainty.

**Parkinson's Law** is about how available time influences work.

A project manager can respond to Murphy's Law through risk planning and contingencies.

A project manager can respond to Parkinson's Law by setting realistic deadlines, milestones, and progress checks.

Your slides also discuss multitasking. Switching among multiple tasks can reduce efficiency because people lose time and attention moving between activities.

## **Objective 6: Calculate a PERT estimate**

**PERT** stands for **Program Evaluation and Review Technique**.

PERT uses three duration estimates to calculate a weighted expected duration.

| Symbol | Estimate    | Meaning                |
| ------ | ----------- | ---------------------- |
| O      | Optimistic  | Best reasonable case   |
| M      | Most likely | Most probable duration |
| P      | Pessimistic | Worst reasonable case  |

### **Formula**

\\[ \boxed{\text{PERT}=\frac{O+4M+P}{6}} \\]

The most likely estimate is multiplied by four, so it receives more weight.

### **Your professor's example**

Optimistic = 8 workdays

Most likely = 10 workdays

Pessimistic = 24 workdays

\\[ \frac{8+4(10)+24}{6} =\frac{72}{6} =\boxed{12\text{ days}} \\]

**Answer: 12 workdays.**

The result is not simply the average of the three numbers.

### **Another example**

O = 3, M = 6, P = 15

\\[ \frac{3+4(6)+15}{6} =\frac{42}{6} =\boxed{7} \\]

### **Additional PERT formulas**

These are standard PERT calculations beyond the main expected-duration formula shown in your slides.

**Standard deviation:**

\\[ \sigma=\frac{P-O}{6} \\]

**Variance:**

\\[ \sigma^2=\left(\frac{P-O}{6}\right)^2 \\]

For O = 3 and P = 15:

Standard deviation = (15 − 3)/6 = 2.

Variance = 2² = 4.

The slides emphasize the weighted duration calculation, so prioritize that formula first.

## **Objective 7: Prepare the schedule management plan and Gantt chart**

### **Schedule management plan**

Explains the procedures for building, approving, measuring, and controlling the schedule.

### **Gantt chart**

A **Gantt chart is a bar chart that illustrates a project schedule**.

Your professor specifically emphasizes knowing how to recognize and spell *Gantt*.

Example Gantt chart

Illustrative schedule only. Horizontal bars show when activities are planned.

A Gantt chart can show:

- Tasks.
- Start and finish dates.
- Durations.
- Dependencies.
- Milestones.
- Progress.
- Planned versus actual timing.

**Tracking Gantt chart:** Compares actual progress against the schedule baseline to identify delays.

**Schedule baseline:** The approved schedule used as the reference for performance measurement.

## **Objective 8: Define all specified schedule terms**

| Term                      | Definition                                                                  |
| ------------------------- | --------------------------------------------------------------------------- |
| Activity                  | Specific action required to complete project work                           |
| Activity list             | Document identifying scheduled activities                                   |
| Activity attributes       | Details such as dependencies, resources, and constraints                    |
| Milestone                 | Important event, achievement, or date in the project                        |
| Effort                    | Total amount of work required, often measured in person-hours               |
| Duration                  | Elapsed working time needed to complete an activity                         |
| Slack/float               | Time an activity can be delayed without causing a specified delay           |
| Crashing                  | Shortening the schedule by adding resources or making time-cost trade-offs  |
| Fast tracking             | Performing activities in parallel that were originally planned sequentially |
| Critical chain scheduling | Scheduling that considers resource limitations and availability             |
| Critical path             | Longest-duration path through the schedule network                          |
| Predecessor               | Activity that precedes another in a dependency                              |
| Successor                 | Activity that follows another                                               |
| Lead                      | Planned overlap between dependent activities                                |
| Lag                       | Waiting time between dependent activities                                   |
| Schedule baseline         | Approved schedule used for comparison                                       |
| Schedule variance         | Difference between planned and actual schedule performance                  |
| Gantt chart               | Bar chart illustrating a project schedule                                   |

### **Effort versus duration**

This distinction is important.

Suppose a task requires 16 hours of effort.

One person working eight hours per day might need two days.

Two people could theoretically complete 16 hours of effort in one day if the work can be divided efficiently.

Therefore:

**Effort measures the amount of work. Duration measures the time required to complete it.**

They are not interchangeable.

### **SMART milestones**

Your professor says milestones should be:

- **S**pecific.
- **M**easurable.
- **A**ssignable.
- **R**ealistic.
- **T**ime-framed.

A milestone is usually represented as a zero-duration event in scheduling software.

### **Crashing versus fast tracking**

| Crashing                                     | Fast tracking                                                                 |
| -------------------------------------------- | ----------------------------------------------------------------------------- |
| Adds resources or makes time-cost trade-offs | Overlaps activities                                                           |
| Often increases cost                         | Often increases risk                                                          |
| Aims to shorten the schedule                 | Aims to shorten the schedule                                                  |
| Example: Add extra testers                   | Example: Begin testing completed modules before all configuration is finished |

Neither technique guarantees success.

**Critical chain scheduling** differs because it explicitly considers limited resources when planning the schedule.

## **Part 2. Chapter 5 cost management objectives**

Your PowerPoint has seven additional cost learning objectives.

## **Cost objective 1: Plan cost management**

**Cost management** includes estimating, budgeting, and controlling project costs.

A **cost management plan** describes how costs will be estimated, measured, reported, and controlled.

Your slides say it should identify:

- Required accuracy of estimates.
- Units of measurement.
- Organizational accounting procedures.
- Cost control thresholds.
- Reporting formats.
- Cost management procedures.

### **Basic financial vocabulary**

| Term          | Definition                                                  |
| ------------- | ----------------------------------------------------------- |
| Cost          | A resource sacrificed or given up to achieve an objective   |
| Benefit       | Something received or gained                                |
| Revenue       | Income generated by business activities                     |
| Expenditure   | Money spent                                                 |
| Profit        | Revenue minus expenditures or expenses                      |
| Profit margin | Profit divided by revenue, expressed as a percentage        |
| Budget        | Approved financial plan for the project                     |
| Cost estimate | Approximation of the resources or money needed              |
| Cost overrun  | Actual cost exceeds the planned amount                      |
| Cash flow     | Movement of money into and out of a project or organization |

### **Profit formula**

\\[ \text{Profit}=\text{Revenue}-\text{Expenses} \\]

### **Profit margin formula**

\\[ \text{Profit Margin}=\frac{\text{Profit}}{\text{Revenue}}\times100 \\]

Example:

Revenue = $100,000

Expenses = $75,000

Profit = $25,000

Profit margin = 25%.

## **Cost objective 2: Develop the project budget**

A project budget combines estimated costs and appropriate reserves.

The slides introduce the **cost baseline**.

**Cost baseline:** A time-phased budget used to measure and monitor project cost performance.

**Time-phased** means costs are allocated across periods, such as weeks or months, rather than shown only as one total.

Example:

| Month    | Planned spending |
| -------- | ---------------- |
| January  | $10,000          |
| February | $20,000          |
| March    | $15,000          |
| Total    | $45,000          |

The timing matters because a project manager needs to know not just how much money is required, but when it will be spent.

### **Full-Time Equivalent (FTE)**

**FTE** means Full-Time Equivalent.

It measures work capacity relative to a full-time schedule.

For example, assuming 40 hours per week:

- 40 hours = 1.0 FTE.
- 20 hours = 0.5 FTE.
- 80 combined hours = 2.0 FTE.

## **Cost objective 3: Define cost categories and reserves**

### **Tangible versus intangible**

**Tangible costs and benefits:** Can be measured directly in monetary terms.

Examples: Software licenses, equipment purchases, reduced labor expenses.

**Intangible costs and benefits:** Difficult to quantify financially.

Examples: Improved morale, better reputation, greater customer satisfaction.

### **Direct versus indirect costs**

**Direct costs:** Can be attributed directly to a particular project.

Examples: Project-specific software, contractor fees, dedicated labor.

**Indirect costs:** Shared costs that support multiple projects or operations.

Examples: Office utilities, general administrative support, shared facilities.

### **Sunk costs**

**Sunk costs are expenses that have already occurred and cannot be recovered.**

Example: A company spent $50,000 developing software that no longer meets its needs.

That $50,000 is a sunk cost.

The decision about whether to continue should focus on future costs and benefits, not simply on the money already spent.

### **Learning curve theory**

The idea that people often become faster or more efficient at performing work as they gain experience.

### **Life cycle costing**

Evaluating the total cost of a product or system over its useful life, rather than only its purchase or development cost.

Costs can include acquisition, operation, maintenance, support, and disposal.

### **Cradle-to-grave analysis**

Considering a product or project from its beginning through the end of its life.

Your professor notes that **life cycle assessment** also considers environmental impacts.

### **Reserves**

**Reserves are money set aside to address uncertainty and risk.**

| Reserve             | Purpose                                 | Included in cost baseline? |
| ------------------- | --------------------------------------- | -------------------------- |
| Contingency reserve | Known risks or known unknowns           | Yes                        |
| Management reserve  | Unforeseeable risks or unknown unknowns | No                         |

**Known unknown:** A risk that has been identified but whose occurrence or impact is uncertain.

**Unknown unknown:** An event that was not reasonably identified or anticipated during planning.

Example:

Contingency reserve: Extra money for potential employee turnover.

Management reserve: Money for an unexpected major event not included in identified project risks.

**Important distinction:** Management reserves are outside the cost baseline but may be included in the total project budget.

## **Cost objective 4: Describe cost estimation techniques**

| Technique            | Explanation                                            | Example                                 |
| -------------------- | ------------------------------------------------------ | --------------------------------------- |
| Top-down / analogous | Estimate using similar past projects                   | Previous deployment cost $40,000        |
| Bottom-up            | Estimate each component and add them together          | Labor + licenses + equipment + training |
| Three-point / PERT   | Use optimistic, most likely, and pessimistic estimates | Weighted cost estimate                  |
| Parametric           | Use a mathematical relationship or unit rate           | 100 users × $20 per license             |

### **Bottom-up example**

Labor: $20,000

Software: $8,000

Training: $2,000

Testing: $5,000

Subtotal = $35,000.

If the contingency reserve is 10%:

Contingency = $3,500.

Cost baseline = **$38,500**.

Management reserve, if authorized, would be added outside that baseline.

## **Cost objective 5: Explain why people estimate poorly**

Your professor asks why estimating is particularly difficult in IT.

Relevant factors include:

- Unclear requirements.
- Rapid technological change.
- Limited experience with new technology.
- Optimism about how quickly work can be completed.
- Underestimating complexity.
- Ignoring dependencies.
- Failing to account for interruptions or risks.
- Overlooking testing, documentation, and rework.

### **Ways to improve estimates**

Use historical data, multiple estimation methods, subject matter experts, detailed work breakdowns, and explicit assumptions.

**Subject Matter Expert (SME):** A person with specialized knowledge in a particular area.

Your slides discuss why estimates can be inaccurate rather than providing one universal rule that everyone always underestimates or overestimates.

## **Cost objective 6: Conduct earned value management analysis**

Your slides introduce **Earned Value Management (EVM)** and say it is covered further in Chapter 8.

Because Chapter 5 lists it as a learning objective, know the following foundational formulas. These are standard EVM definitions supplementing the Chapter 5 slide content.

### **Three core EVM values**

| Abbreviation | Meaning       | Definition                                       |
| ------------ | ------------- | ------------------------------------------------ |
| PV           | Planned Value | Budgeted value of work scheduled to be completed |
| EV           | Earned Value  | Budgeted value of work actually completed        |
| AC           | Actual Cost   | Actual amount spent on completed work            |

### **EVM formulas**

| Metric                           | Formula | Interpretation                                           |
| -------------------------------- | ------- | -------------------------------------------------------- |
| Cost Variance (CV)               | EV − AC | Positive = under budget; negative = over budget          |
| Schedule Variance (SV)           | EV − PV | Positive = ahead of schedule; negative = behind schedule |
| Cost Performance Index (CPI)     | EV / AC | Greater than 1 = favorable cost efficiency               |
| Schedule Performance Index (SPI) | EV / PV | Greater than 1 = favorable schedule performance          |

### **Worked example**

Suppose:

PV = $10,000

EV = $8,000

AC = $9,000

Cost variance:

\\[ CV=8,000-9,000=\boxed{-1,000} \\]

The project is over budget relative to the value of work completed.

Schedule variance:

\\[ SV=8,000-10,000=\boxed{-2,000} \\]

The project is behind schedule in earned-value terms.

Cost Performance Index:

\\[ CPI=\frac{8,000}{9,000}\approx\boxed{0.89} \\]

Schedule Performance Index:

\\[ SPI=\frac{8,000}{10,000}=\boxed{0.80} \\]

Both indices are below 1, indicating unfavorable performance.

**Do not confuse EVM with EMV.** EVM measures project performance. EMV evaluates monetary outcomes associated with risk.

## **Cost objective 7: Prepare cost deliverables**

### **Cost management plan**

Explains how project costs will be estimated, measured, and controlled.

### **Cost estimate**

An approximation of expected project expenses, supported by assumptions and reasoning.

### **Cost baseline**

The approved time-phased budget used for cost performance comparisons.

## **Part 3. Remaining Chapter 5 material**

### **Black swan event**

A **black swan event** is a rare, unexpected event with major consequences.

Your professor discusses black swan events in relation to large IT project overruns.

### **Cost control tools**

Your slides identify:

- Expert judgment.
- Data analysis.
- Project Management Information Systems.
- Earned Value Management.

**Project Management Information System (PMIS):** Software or systems used to organize, track, and report project information.

### **Additional AI cost-management discussion**

Your professor's slides also discuss enterprise AI spending and cost overruns.

They identify five possible causes of excessive AI spending:

1. **FOMO:** Choosing the newest or most expensive models when cheaper options would work.
2. **Unbounded agents:** Automated AI processes consuming more tokens than expected.
3. **Wrong tools:** Using unnecessarily expensive tools for simple tasks.
4. **Recreating the wheel:** Failing to reuse prompts or cached results.
5. **Poor growth planning:** Underestimating future demand and usage.

The slides also describe practices associated with high-performing organizations:

- Formal AI strategy.
- Executive sponsorship.
- Governance and monitoring.
- Matching AI models to workloads.
- Tracking cost per completed task.
- Willingness to change vendors.

These examples reinforce the chapter's main lesson: **costs need to be estimated, monitored, and controlled throughout a project.**

### **Chapter 5: Critical distinctions**

| Don't confuse                      | Difference                                        |
| ---------------------------------- | ------------------------------------------------- |
| Effort vs. duration                | Amount of work vs. elapsed time                   |
| Activity vs. milestone             | Work performed vs. significant event              |
| Mandatory vs. discretionary        | Required order vs. chosen order                   |
| Internal vs. external              | Within project control vs. outside relationship   |
| FS vs. SS vs. FF vs. SF            | Different start/finish dependency relationships   |
| Critical path vs. WBS              | Schedule's longest path vs. breakdown of work     |
| Crashing vs. fast tracking         | Add resources vs. overlap work                    |
| Contingency vs. management reserve | Known risks vs. unknown risks                     |
| Direct vs. indirect cost           | Project-specific vs. shared costs                 |
| Tangible vs. intangible            | Readily quantifiable vs. difficult to quantify    |
| PERT vs. EVM                       | Estimate duration vs. measure project performance |

**Chapter 5 exam focus:** Know all four dependency relationships, all four dependency categories, how to identify the critical path, PERT calculations, slack, crashing versus fast tracking, Gantt charts, cost categories, and the two reserve types.

# **Chapter 6: Stakeholders, Resources, and Risk**

Chapter 6 has three major subjects:

1. Stakeholder management.
2. Resource management.
3. Risk management.

Your professor's objectives emphasize **creating management documents, assigning responsibility, balancing resources, analyzing risk, and selecting risk responses**.

## **Part 1. All Chapter 6 learning objectives**

## **Objective 1: Design the project deliverables**

Your professor lists ten deliverables. You should know what each one is, what it contains, and why it is useful.

### **1. Stakeholder engagement plan**

A **stakeholder engagement plan** explains how the project team will involve, communicate with, and manage stakeholders.

Your slides identify these contents:

- Current stakeholder engagement levels.
- Desired engagement levels.
- Relationships among stakeholders.
- Communication requirements.
- Strategies for managing stakeholders.
- Procedures for updating the plan.

### **Stakeholder engagement levels**

The following are standard categories used in project management:

| Level      | Meaning                                         |
| ---------- | ----------------------------------------------- |
| Unaware    | Does not know about the project                 |
| Resistant  | Knows about the project but opposes it          |
| Neutral    | Aware but neither supportive nor opposed        |
| Supportive | Supports the project                            |
| Leading    | Actively promotes and helps the project succeed |

Example:

A department manager is resistant because the new system changes how employees work.

The engagement plan might include demonstrations, training, and regular meetings to address concerns and move the manager toward a supportive position.

### **Expectations management matrix**

Your slides introduce this as a separate stakeholder management tool.

An **expectations management matrix** is a table documenting stakeholders' major expectations and how the project team will manage them.

| Stakeholder   | Expectation           | Management approach            |
| ------------- | --------------------- | ------------------------------ |
| Sponsor       | Stay within budget    | Monthly budget reports         |
| Staff         | Easy-to-use system    | Training and usability testing |
| Customers     | Reliable registration | Acceptance testing             |
| IT department | Secure system         | Security review                |

Your professor emphasizes that major expectations may be identified and ranked by multiple stakeholders.

### **2. Communications management plan**

A **communications management plan** defines how project information will be created, distributed, and managed.

Your slides identify these contents:

- Stakeholder communication requirements.
- Information to communicate.
- Format, content, and level of detail.
- Who produces the information.
- Who receives the information.
- Communication methods or technology.
- Communication frequency.
- Escalation procedures.
- Revision procedures.
- Common terminology or glossary.

**Escalation:** Referring an issue to someone with greater authority or responsibility when it cannot be resolved at the current level.

Your professor notes that small projects may include the communications plan in the team contract, while large projects generally need a separate document.

### **3. Project organizational chart**

A **project organizational chart** shows project roles and reporting relationships.

It answers: Who reports to whom?

**Project Sponsor**

**Project Manager**

Technical Lead

Business Analyst

Testing Lead

Your slides mention:

**Deputy:** A person who can serve as a backup or substitute for a project role.

**Subproject manager:** Someone who manages a smaller project within a larger project.

A person's role in the project may differ from their normal organizational role.

### **4. Responsibility Assignment Matrix (RAM)**

A **Responsibility Assignment Matrix** is a table showing project work and the people responsible for ensuring that work gets done or performing it.

Your professor emphasizes that there should be **one person ultimately accountable for each deliverable**.

A common form of RAM is a **RACI chart**.

### **RACI definitions**

| Letter | Meaning     | Role                       |
| ------ | ----------- | -------------------------- |
| R      | Responsible | Performs the work          |
| A      | Accountable | Ultimately owns the result |
| C      | Consulted   | Provides input or advice   |
| I      | Informed    | Receives updates           |

**Responsible versus accountable** is particularly important.

Responsible = Does the work.

Accountable = Ensures the result is delivered correctly.

Several people can be responsible for performing work, but there should be only one accountable person for a particular deliverable.

### **RACI example**

| Task                | Project Manager | Analyst | Developer | Sponsor |
| ------------------- | --------------- | ------- | --------- | ------- |
| Gather requirements | A               | R       | C         | I       |
| Configure system    | A               | C       | R         | I       |
| Approve scope       | R               | C       | I         | A       |
| Report progress     | A/R             | I       | I         | C       |

A person can sometimes hold more than one role for a task.

### **5. Resource histogram**

A **resource histogram** is a column chart showing resource usage over time.

Your professor uses it to illustrate resource allocation and over-allocation.

Example: Staff hours required each week

Illustrative resource histogram showing uneven staffing demand.

0 hrs15 hrs30 hrs45 hrs60 hrsWeek 1Week 2Week 3Week 4Week 5

If one employee is available for only 40 hours per week but is assigned 55 hours in Week 3, that employee is overallocated.

**Overallocation:** Assigning more work to a resource than it can realistically complete within the available time.

### **6. Staffing management plan**

A **staffing management plan** describes when and how people will be added to and removed from the project.

It can include:

- Skills needed.
- Number of workers required.
- Timing of assignments.
- Staffing availability.
- Training needs.
- Procedures for releasing staff.

**Example:** A project may need business analysts during requirements collection, developers during configuration, and testers near the end.

### **7. Team charter or team contract**

A **team charter**, also called a team contract or team operating principles, establishes ground rules for how the team will work together.

It may address:

- Roles and responsibilities.
- Communication expectations.
- Attendance.
- Deadlines.
- Decision-making.
- Conflict resolution.
- Accountability.
- Professional behavior.

Your professor describes it as a guide for how the team will function.

### **8. Risk management plan**

A **risk management plan** explains how the team will identify, assess, analyze, respond to, and monitor risks.

It is part of the overall project management plan.

It can specify:

- Risk identification methods.
- Risk assessment procedures.
- Risk response responsibilities.
- Monitoring frequency.
- Risk reporting.
- Reserves and contingency planning.

### **9. Risk register**

A **risk register** is a table documenting identified project risks and information about them.

Your slides specifically mention **triggers**, which are warning signs that a risk may be occurring.

Example:

| Risk                   | Probability | Impact | Response                   | Owner            |
| ---------------------- | ----------- | ------ | -------------------------- | ---------------- |
| Vendor delivery delay  | Medium      | High   | Prepare alternate vendor   | Procurement lead |
| Data migration failure | Low         | High   | Test backups and migration | Technical lead   |
| Staff turnover         | Medium      | Medium | Cross-train employees      | Project manager  |

**Risk owner:** The person responsible for monitoring a risk and carrying out its response plan.

**Risk trigger:** A warning sign or event indicating that a risk may be developing or occurring.

### **10. Probability/Impact Matrix**

A **Probability/Impact Matrix** is used to assess and prioritize risks according to their likelihood and consequences.

**Probability:** Likelihood that an event will occur.

**Impact:** Consequence if the event occurs.

Illustrative probability/impact matrix



Low impact

Medium

High impact

High probability

Medium

Low

Illustration of relative risk priority. Actual organizations may use different scales and thresholds.

A high-probability, high-impact threat generally requires more attention than a low-probability, low-impact threat.

### **Qualitative versus quantitative analysis**

**Qualitative risk analysis:** Uses descriptive categories or judgments, such as low, medium, and high.

**Quantitative risk analysis:** Uses numerical values and calculations.

Your professor associates the probability/impact matrix with qualitative analysis and Expected Monetary Value with quantitative analysis.

### **11. Expected Monetary Value (EMV) analysis**

Your professor also lists EMV analysis as a deliverable.

**Expected Monetary Value** is a calculation used to evaluate potential financial outcomes based on their probabilities.

### **EMV formula**

\\[ \boxed{EMV=\sum(\text{Probability}\times\text{Monetary Outcome})} \\]

The symbol \\(\sum\\) means to add the results together.

For each possible outcome:

1. Convert its probability to a decimal.
2. Multiply the probability by the monetary outcome.
3. Add all the weighted outcomes.

A loss is represented by a negative number.

### **Your professor's EMV example**

The slides provide four possible projects.

| Project | Outcomes                                                    | EMV     |
| ------- | ----------------------------------------------------------- | ------- |
| 1       | 50% × $120,000; 50% × −$50,000                              | $35,000 |
| 2       | 30% × $100,000; 40% × $50,000; 30% × −$60,000               | $32,000 |
| 3       | 70% × $20,000; 30% × −$5,000                                | $12,500 |
| 4       | 30% × $40,000; 30% × $30,000; 20% × $20,000; 20% × −$50,000 | $15,000 |

Let's calculate Project 1:

\\[ EMV=(0.50\times120,000)+(0.50\times-50,000) \\]

\\[ =60,000-25,000=\boxed{\\$35,000} \\]

Project 2:

\\[ 30,000+20,000-18,000=\boxed{\\$32,000} \\]

Project 3:

\\[ 14,000-1,500=\boxed{\\$12,500} \\]

Project 4:

\\[ 12,000+9,000+4,000-10,000=\boxed{\\$15,000} \\]

**Project 1 has the highest EMV at $35,000.**

If the decision is based solely on the highest expected monetary outcome, Project 1 is preferred.

However, a risk-averse organization might consider the probability and size of potential losses rather than EMV alone.

**EMV versus EVM:**

EMV = Expected Monetary Value, used in risk analysis.

EVM = Earned Value Management, used to measure project cost and schedule performance.

## **Objective 2: Explain why only one person should be responsible for a deliverable**

Your professor's RAM discussion distinguishes between people who perform work and the person who ensures its completion.

The main reason for assigning one ultimately accountable person is **clear ownership**.

If multiple people believe someone else is responsible for the final result, work may be delayed, duplicated, or overlooked.

One accountable person:

- Makes responsibility clear.
- Prevents confusion.
- Coordinates work.
- Ensures deadlines are monitored.
- Provides a clear point of contact.
- Can be held accountable for completion.

Several team members may still perform the work.

**Exam answer:** One person should be accountable for each deliverable so there is clear ownership and no confusion about who is responsible for ensuring it is completed.

## **Objective 3: Explain how resource leveling works**

### **Resource loading**

**Resource loading**, also called resource allocation, refers to the amount of work assigned to a resource.

Resources can include people, equipment, facilities, materials, and other assets needed for the project.

Your professor emphasizes that employees cannot realistically work at 100% productive capacity all the time. The slides use approximately 80% as an illustration of productive time.

### **Resource leveling**

**Resource leveling is a scheduling technique that rearranges activities to account for resource availability and reduce periods of over-allocation.**

Example:

A developer has two tasks requiring 30 hours each in the same week.

Total assigned work = 60 hours.

Available work time = 40 hours.

The developer is overallocated by 20 hours.

The project manager could move one task into the following week.

### **How it works**

1. Identify resource availability.
2. Identify activities assigned to each resource.
3. Locate over-allocation.
4. Rearrange or delay activities.
5. Recalculate the schedule.
6. Review the effect on deadlines.

**Important:** Resource leveling can extend the project schedule.

### **Resource leveling versus resource smoothing**

This is an additional standard distinction beyond the main definition in your slides.

**Resource leveling:** Adjusts the schedule to address resource limits, potentially changing the completion date.

**Resource smoothing:** Adjusts resource use within available scheduling flexibility without changing the critical completion date.

### **Resource Breakdown Structure (RBS)**

Your slides introduce the **Resource Breakdown Structure**.

An RBS is a hierarchical outline of project resources organized by category and type.

It resembles a WBS, but it organizes resources rather than project deliverables.

Example:

Resources → People → Analysts, Developers, Testers.

Resources → Equipment → Computers, Servers, Network Devices.

## **Objective 4: Explain how risk utility affects project management**

### **What is risk?**

A **project risk is an uncertain event or condition that could affect project objectives if it occurs**.

Risks can be negative or positive.

### **What is risk utility?**

**Risk utility describes the satisfaction or value a person or organization associates with different levels of risk and potential outcomes.**

It helps explain why different decision-makers may choose different projects even when the financial outcomes appear similar.

### **Three risk preferences**

| Preference   | Meaning                                                              | Example                                             |
| ------------ | -------------------------------------------------------------------- | --------------------------------------------------- |
| Risk-averse  | Prefers greater certainty and less risk                              | Chooses a reliable project with modest returns      |
| Risk-neutral | Focuses on expected outcomes rather than risk itself                 | Selects the highest EMV                             |
| Risk-seeking | Willing to accept greater uncertainty for potentially larger rewards | Chooses a high-risk project with substantial upside |

**Risk appetite:** The amount and type of risk an organization is willing to accept.

**Risk tolerance:** The degree of variation or uncertainty the organization is willing to withstand.

### **Why does risk utility matter?**

Two organizations can evaluate the same project and make different decisions.

A startup might accept significant uncertainty to pursue rapid growth.

A government agency might prioritize stability, predictability, and service continuity.

The project manager must consider the organization's risk preferences when selecting projects and developing risk responses.

## **Objective 5: Identify good risks versus bad risks**

### **Negative risks: threats**

A **threat** is an uncertain event that could harm the project.

Examples:

- A vendor fails to deliver.
- Project costs increase.
- A key employee leaves.
- A security breach occurs.
- Testing identifies serious defects.

### **Positive risks: opportunities**

An **opportunity** is an uncertain event that could benefit the project.

Examples:

- A vendor offers an unexpected discount.
- Work finishes earlier than expected.
- New technology improves performance.
- A partnership provides additional resources.

### **Risk versus issue**

**Risk:** Something uncertain that may happen.

**Issue:** A problem or situation that already exists and requires attention.

Example:

Risk: The vendor might miss its delivery date.

Issue: The vendor has already missed the delivery date.

Your professor describes risk management as proactive and issue management as reactive.

### **Issue log**

An **issue log** is a document used to record, monitor, and track problems requiring resolution.

It may include:

- Issue description.
- Date identified.
- Priority.
- Assigned owner.
- Status.
- Planned resolution.
- Due date.

Your professor emphasizes addressing issues quickly rather than allowing them to remain unresolved.

## **Objective 6: List potential sources of risk and how to address them**

### **Potential sources of project risk**

| Source              | Example                              | Possible response                           |
| ------------------- | ------------------------------------ | ------------------------------------------- |
| Technical           | Software integration fails           | Prototype and test early                    |
| Schedule            | Activities take longer than expected | Build realistic estimates and contingencies |
| Financial           | Costs exceed budget                  | Monitor costs and maintain reserves         |
| Staffing            | Important employee leaves            | Cross-train employees                       |
| Vendor              | Supplier misses delivery             | Identify alternate suppliers                |
| Requirements        | Customer changes expectations        | Use formal change control                   |
| Security            | Unauthorized data access             | Apply security controls and testing         |
| Legal or regulatory | New compliance requirement           | Review applicable requirements              |
| Organizational      | Leadership changes priorities        | Maintain sponsor engagement                 |
| External            | Severe weather disrupts operations   | Develop contingency plans                   |
| Quality             | Deliverable fails acceptance testing | Improve testing and quality control         |

### **Methods of identifying risks**

Your slides identify:

**Brainstorming:** Generate possible risks as a group.

**Delphi technique:** Gather expert opinions through structured rounds, often anonymously, to develop informed consensus.

**Interviewing:** Ask stakeholders or experts about potential problems.

**SWOT analysis:** Examine Strengths, Weaknesses, Opportunities, and Threats.

**Root cause analysis:** Identify the underlying reason a problem occurs or could occur.

### **Qualitative risk analysis**

Uses descriptive or categorical assessments.

Examples: High probability, medium impact, low priority.

### **Quantitative risk analysis**

Uses numerical measurements and models.

Examples: EMV, Monte Carlo simulation, sensitivity analysis.

**Monte Carlo simulation:** Runs many possible scenarios using probability distributions to estimate the range and likelihood of outcomes.

**Sensitivity analysis:** Examines how changes in individual assumptions or variables affect project outcomes.

**Decision tree analysis:** Maps possible decisions, uncertain events, probabilities, and outcomes to compare alternatives.

## **Part 2. Additional Chapter 6 risk management material**

### **Risk management plan**

Your slides define this as the section of the project management plan describing how to identify, assess, analyze, and respond to risk.

### **Contingency plan**

A planned response to use if a particular risk occurs.

Example: If the primary vendor misses its deadline, use an alternate supplier.

### **Fallback plan**

An alternative plan to use when the original response is ineffective or fails.

Example: If the alternate supplier is also unavailable, reduce the initial deployment scope through approved change control.

### **Contingency reserve**

Money included in the cost baseline for identified risks.

### **Management reserve**

Money outside the cost baseline but within the overall budget for unforeseen risks.

### **Five response strategies for negative risks**

Your professor lists:

| Strategy | Definition                                                                           | Example                                      |
| -------- | ------------------------------------------------------------------------------------ | -------------------------------------------- |
| Avoid    | Eliminate the threat or exposure to it                                               | Remove a risky feature                       |
| Accept   | Acknowledge the risk without taking preventive action beyond any planned contingency | Accept a minor delay risk                    |
| Transfer | Shift financial or contractual responsibility to another party                       | Purchase insurance                           |
| Mitigate | Reduce probability or impact                                                         | Perform additional testing                   |
| Escalate | Refer the risk to someone with appropriate authority                                 | Send an organization-wide risk to executives |

### **Five response strategies for positive risks**

| Strategy | Definition                                                            | Example                                                   |
| -------- | --------------------------------------------------------------------- | --------------------------------------------------------- |
| Exploit  | Take action to ensure the opportunity occurs                          | Assign the strongest team to capture an important benefit |
| Share    | Partner with another party to realize the opportunity                 | Form a joint venture                                      |
| Enhance  | Increase probability or positive impact                               | Add resources to accelerate a promising improvement       |
| Accept   | Take advantage if the opportunity occurs without actively pursuing it | Accept an unexpected discount                             |
| Escalate | Refer an opportunity beyond project authority                         | Ask executives to pursue an enterprise-wide benefit       |

### **Avoid versus mitigate**

**Avoid:** Remove the threat entirely.

**Mitigate:** Reduce the chance or consequences of the threat.

### **Transfer versus accept**

**Transfer:** Shift some responsibility or financial impact to another party.

**Accept:** Acknowledge the risk and live with its possible consequences.

Transferring risk does not necessarily eliminate the risk itself.

### **Exploit versus enhance**

**Exploit:** Work to make a positive opportunity happen.

**Enhance:** Improve the probability or benefits of the opportunity.

### **Residual risk**

**Residual risk is the risk remaining after responses have been implemented.**

Example: Security controls reduce the likelihood of unauthorized access, but cannot eliminate every possibility.

### **Secondary risk**

**Secondary risk is a new risk caused by implementing a response to another risk.**

Example: Introducing backup software reduces data-loss risk but creates a new risk of compatibility problems.

### **Inherent risk**

**Inherent risk is the level of risk before considering controls or response actions.**

### **Risk monitoring**

Your professor emphasizes that risk management is continuous.

The team should:

1. Assign each risk an owner.
2. Monitor identified risks regularly.
3. Update the risk register.
4. Identify new risks.
5. Evaluate whether response strategies work.
6. Implement changes when necessary.

### **Top Ten Risk Item Tracking**

A technique for regularly reviewing the project's ten most important risks.

### **Risk Breakdown Structure**

A hierarchical classification of risks by category.

It is similar in format to a WBS, but organizes risks rather than deliverables.

### **Risk-related project management advice**

Your professor also emphasizes:

- Establish expectations early.
- Explain the consequences of decisions.
- Have a Plan B.
- Communicate problems honestly.
- Avoid surprises.
- Be willing to say no when necessary.
- Address issues before they grow.
- Be proactive rather than reactive.

## **Chapter 6: Vocabulary summary**

| Term                           | Definition                                              |
| ------------------------------ | ------------------------------------------------------- |
| Stakeholder                    | Anyone who can affect or be affected by a project       |
| Stakeholder engagement         | Involving and managing stakeholder participation        |
| Stakeholder engagement plan    | Strategy for managing stakeholder relationships         |
| Expectations management matrix | Tracks stakeholder expectations and responses           |
| Resource                       | Something needed to complete project work               |
| Human resource                 | Person contributing to the project                      |
| Physical resource              | Equipment, facility, material, or supply                |
| Resource management            | Planning and controlling project resource use           |
| RAM                            | Matrix assigning work responsibilities                  |
| RACI                           | Responsible, Accountable, Consulted, Informed           |
| Project org chart              | Shows project reporting relationships                   |
| Team charter                   | Establishes team operating rules                        |
| Staffing management plan       | Describes staffing needs and timing                     |
| Resource histogram             | Chart showing resource usage over time                  |
| Resource loading               | Amount of work assigned to a resource                   |
| Resource leveling              | Adjusting the schedule to address resource availability |
| Overallocation                 | Assigning more work than available capacity             |
| RBS                            | Hierarchical breakdown of resources                     |
| Risk                           | Uncertain event that could affect objectives            |
| Threat                         | Negative risk                                           |
| Opportunity                    | Positive risk                                           |
| Risk utility                   | Value or satisfaction associated with risky outcomes    |
| Risk appetite                  | Willingness to accept risk                              |
| Risk register                  | Document tracking identified risks                      |
| Risk owner                     | Person assigned to manage a risk                        |
| Risk trigger                   | Warning sign of a risk                                  |
| Issue                          | Existing problem requiring attention                    |
| Issue log                      | Document tracking issues                                |
| Qualitative analysis           | Descriptive risk assessment                             |
| Quantitative analysis          | Numerical risk assessment                               |
| EMV                            | Probability-weighted monetary outcome                   |
| Probability/Impact Matrix      | Risk prioritization tool                                |
| Contingency plan               | Planned response if a risk occurs                       |
| Fallback plan                  | Backup response if the initial plan fails               |
| Residual risk                  | Risk remaining after treatment                          |
| Secondary risk                 | Risk created by a response                              |
| Inherent risk                  | Risk before controls                                    |
| Risk mitigation                | Reducing probability or impact                          |
| Risk transfer                  | Shifting financial or contractual responsibility        |
| Monte Carlo simulation         | Repeated probability-based scenario analysis            |
| Sensitivity analysis           | Examines which variables most affect outcomes           |
| Delphi technique               | Structured expert consultation                          |
| SWOT                           | Strengths, Weaknesses, Opportunities, Threats           |

**Chapter 6 exam focus:** Know all ten deliverables, RACI, why one person must be accountable, resource leveling, risk utility, positive and negative risks, all ten risk response strategies, risk versus issue, residual versus secondary risk, and EMV calculations.

# **Chapter 7: Communications, Leadership, and Motivation**

Chapter 7 focuses on the people involved in a project and how project managers communicate, motivate, influence, lead, and resolve conflict.

Your professor includes several named theories. **Memorize which person developed each theory and the key concepts associated with it.**

## **Part 1. All seven learning objectives**

## **Objective 1: Calculate the number of communication channels**

### **What is a communication channel?**

A **communication channel** is a potential connection through which two project participants can communicate.

As the number of people increases, the number of possible communication relationships grows rapidly.

### **Formula**

\\[ \boxed{\text{Channels}=\frac{n(n-1)}{2}} \\]

Where \\(n\\) = number of people.

### **Example: 5 people**

\\[ \frac{5(5-1)}{2} =\frac{5(4)}{2} =\boxed{10} \\]

Five people create ten potential communication channels.

### **Example: 10 people**

\\[ \frac{10(10-1)}{2} =\frac{90}{2} =\boxed{45} \\]

### **Communication channels reference table**

| People | Channels |
| ------ | -------- |
| 2      | 1        |
| 3      | 3        |
| 4      | 6        |
| 5      | 10       |
| 6      | 15       |
| 7      | 21       |
| 8      | 28       |
| 9      | 36       |
| 10     | 45       |
| 12     | 66       |
| 15     | 105      |
| 20     | 190      |

### **Practice calculator**

**Number of project participants**

## **8**

Potential communication channels

# **28**

\\(\frac{8(8-1)}{2}=28\\)

### **Brooks' Law**

Your professor introduces **Brooks' Law**, associated with Fred Brooks:

Adding people to a late software project can make it even later.

### **Why can adding people cause more delays?**

Your slides identify several reasons:

- New employees need training.
- Existing employees must spend time helping them.
- Communication channels increase.
- New employees may repeat work already completed.
- Team development may have to occur again.
- Coordination becomes more difficult.

**Exam connection:** More people do not automatically mean faster project completion.

## **Objective 2: Plan and conduct an effective meeting**

Your professor provides specific guidance for meetings.

### **Before the meeting**

**1. Determine whether a meeting is necessary.**

Could the issue be resolved with an email instead?

**2. Identify the meeting's purpose.**

What decision, discussion, or outcome is needed?

**3. Determine who needs to attend.**

Only invite people who need to contribute or receive the information.

**4. Schedule an appropriate time and location.**

Consider participant availability and reserve the necessary space.

**5. Prepare and distribute an agenda.**

An **agenda** is a list of topics and activities planned for a meeting.

Send it in advance so participants can prepare.

### **During the meeting**

Your professor recommends:

- Start and finish at the scheduled times.
- Assign a note taker.
- Review the meeting's purpose.
- Keep discussion focused.
- Encourage participation.
- Clarify misunderstandings.
- Summarize decisions.
- Confirm that participants understand the results.

### **After the meeting**

**Meeting minutes** are the written record of what happened during the meeting.

They should document important discussions, decisions, and follow-up actions.

Your professor says minutes should be prepared and distributed before the next meeting.

For important individual meetings, send a short follow-up email summarizing what was agreed upon and ask the recipient to confirm the understanding.

### **Meeting vocabulary**

| Term            | Definition                                               |
| --------------- | -------------------------------------------------------- |
| Agenda          | Planned topics and structure of a meeting                |
| Meeting minutes | Written record of meeting discussions and outcomes       |
| Action item     | Specific task assigned after a meeting                   |
| Facilitator     | Person guiding the meeting                               |
| Note taker      | Person recording important information                   |
| Follow-up       | Action taken after a meeting to confirm or complete work |
| Escalation      | Referring an unresolved issue to higher authority        |

## **Objective 3: Differentiate push, pull, and interactive communication**

These are three major communication methods from your slides.

**Interactive communication**

Two-way exchange of information among participants.

Examples: Meetings, phone calls, video conferences, live discussions.

Best when immediate feedback or clarification is needed.

**Push communication**

Information is sent directly to recipients.

Examples: Emails, newsletters, status reports, notifications.

Best for distributing information to identified recipients without requiring immediate discussion.

**Pull communication**

Information is stored somewhere and recipients access it when needed.

Examples: Project websites, shared folders, document repositories, knowledge bases.

Best when large amounts of information need to be available on demand.

### **Examples for exam questions**

**Scenario:** The project manager emails a weekly report to every stakeholder.

Answer: Push communication.

**Scenario:** Employees access documentation from a shared project website.

Answer: Pull communication.

**Scenario:** The team discusses a technical problem during a video call.

Answer: Interactive communication.

### **Key distinction**

Push = Information is sent to you.

Pull = You retrieve the information.

Interactive = Participants exchange information.

## **Objective 4: Determine which communication tool works best**

Your professor emphasizes matching the communication medium to the situation.

### **Factors to consider**

- How complicated is the message?
- Does the message require immediate discussion?
- Is the information routine or unusual?
- Could the message be misunderstood?
- Does it involve humor, irony, or sarcasm?
- Is the message positive or negative?
- Should there be a written record?
- How familiar are the participants with one another?

### **Communication tool selection**

| Situation                      | Appropriate tool                         | Reason                             |
| ------------------------------ | ---------------------------------------- | ---------------------------------- |
| Simple status update           | Email                                    | Fast and creates a record          |
| Complex disagreement           | Meeting or call                          | Allows immediate discussion        |
| Urgent problem                 | Phone or live message                    | Rapid response                     |
| Detailed project documentation | Shared repository                        | Easy access and version management |
| Important decision             | Meeting followed by written confirmation | Discussion plus documentation      |
| Routine announcements          | Email or newsletter                      | Efficient distribution             |
| Sensitive feedback             | Private conversation                     | Reduces misunderstanding           |
| Large reference document       | Project portal                           | Information available when needed  |

### **Email etiquette from your slides**

Your professor recommends:

- Attach files before writing the message so you don't forget.
- Keep emails brief and readable.
- Use one major subject per email.
- Write descriptive subject lines.
- Think before using Reply All.
- Be careful when forwarding email chains.
- Use direct conversation when email is not working.
- Avoid sending emails while emotionally upset.
- Use BCC appropriately when protecting recipient privacy.

**BCC:** Blind Carbon Copy. Recipients listed in BCC are hidden from other recipients.

**CC:** Carbon Copy. Recipients listed in CC are visible to other recipients.

### **Effective listening**

Your professor emphasizes:

- Stop and think before responding.
- Ask clarifying questions.
- Take notes.
- Consider the context.
- Prepare for meetings.
- Be present and attentive.

**Active listening** means intentionally focusing on understanding another person's message rather than merely waiting to respond.

## **Objective 5: List major theories of motivation, influence, power, effectiveness, emotional intelligence, personality, and team building**

This is the largest objective in Chapter 7.

## **A. Motivation theories**

### **1. Self-Determination Theory: Ryan and Deci**

This theory distinguishes between intrinsic and extrinsic motivation.

**Intrinsic motivation:** Doing something because the activity itself is interesting, enjoyable, or personally meaningful.

**Extrinsic motivation:** Doing something because of an external reward, pressure, or consequence.

Example:

Intrinsic: An employee enjoys solving technical problems.

Extrinsic: An employee works overtime to earn a bonus.

A project manager should understand what motivates individual team members rather than assuming everyone responds to the same incentives.

### **2. Maslow's Hierarchy of Needs**

Maslow proposed that human needs can be arranged in levels.

Maslow's hierarchy

Higher-level needs appear at the top. Your slides emphasize that unmet basic needs can make higher-level motivation more difficult.

### **The five levels**

**1. Physiological needs**

Basic survival needs such as food, water, and rest.

**2. Safety needs**

Security, stability, protection, and a safe environment.

**3. Love and belonging**

Friendship, relationships, acceptance, and connection.

**4. Esteem**

Recognition, achievement, confidence, and respect.

**5. Self-actualization**

Personal growth and realizing one's potential.

### **Project management application**

An employee worried about job security may not be motivated by promises of future recognition alone.

Your professor's main point is that unmet basic needs can interfere with motivation toward higher-level goals.

### **3. Herzberg's Motivation-Hygiene Theory**

Herzberg distinguishes between **hygiene factors** and **motivators**.

#### **Hygiene factors**

Conditions whose absence can cause dissatisfaction.

Examples:

- Salary.
- Company policies.
- Working conditions.
- Supervision.
- Job security.
- Relationships with coworkers.

#### **Motivators**

Factors that encourage satisfaction and engagement.

Your slides specifically list:

- Achievement.
- Recognition.
- The work itself.
- Responsibility.
- Advancement.
- Growth.

**Important distinction:** Improving hygiene factors can reduce dissatisfaction, but it does not necessarily create strong motivation.

Example:

An employee may receive a fair salary but still feel unmotivated if the work is meaningless and there are no growth opportunities.

### **4. McClelland's Acquired-Needs Theory**

McClelland identified three major motivational needs.

| Need        | Abbreviation | Meaning                                |
| ----------- | ------------ | -------------------------------------- |
| Achievement | nAch         | Desire to accomplish challenging goals |
| Affiliation | nAff         | Desire for relationships and belonging |
| Power       | nPow         | Desire to influence others or outcomes |

Your professor notes that people are often strongly motivated by two of these needs.

### **Examples**

**High achievement:** Wants challenging tasks and measurable results.

**High affiliation:** Enjoys teamwork and strong relationships.

**High power:** Wants influence, responsibility, and opportunities to lead.

A good project manager can match responsibilities and incentives to these needs.

### **5. McGregor's Theory X and Theory Y**

#### **Theory X**

Assumes workers generally dislike work and need close supervision, direction, or pressure.

Associated with a controlling management approach.

#### **Theory Y**

Assumes people can be self-directed, responsible, and motivated when conditions support them.

Associated with participation and empowerment.

Your professor describes X as the *stick* approach and Y as the *carrot* approach.

### **6. Ouchi's Theory Z**

Emphasizes:

- Trust.
- Quality.
- Collective decision-making.
- Cultural values.
- Long-term relationships and commitment.

### **Motivation theory comparison**

| Theory             | Person        | Main concept                                 |
| ------------------ | ------------- | -------------------------------------------- |
| Self-Determination | Ryan and Deci | Intrinsic versus extrinsic motivation        |
| Hierarchy of Needs | Maslow        | Five levels of human needs                   |
| Motivation-Hygiene | Herzberg      | Hygiene factors versus motivators            |
| Acquired Needs     | McClelland    | Achievement, affiliation, power              |
| Theory X and Y     | McGregor      | Controlling versus participative assumptions |
| Theory Z           | Ouchi         | Trust, collective decisions, cultural values |

## **B. Theories of influence and power**

### **Thamhain and Wilemon's nine influence bases**

Your professor identifies nine ways project managers may influence others.

| Influence base       | Meaning                                                  |
| -------------------- | -------------------------------------------------------- |
| Legitimate authority | Influence from an official position                      |
| Future assignment    | Influence through control of future work assignments     |
| Budgetary control    | Influence through control of project funds               |
| Promotion            | Influence through career advancement opportunities       |
| Money                | Influence through financial rewards                      |
| Penalty              | Influence through punishment or negative consequences    |
| Work challenge       | Influence through interesting or challenging assignments |
| Expertise            | Influence through specialized knowledge                  |
| Friendship           | Influence through personal relationships                 |

### **Positive versus negative influence**

Your professor asks you to consider which methods are positive or negative.

Methods such as expertise, friendship, meaningful work, and recognition tend to support positive influence.

Penalty-based influence relies on fear or punishment and can damage morale.

The effectiveness of a method depends on the person and situation.

### **French and Raven's five bases of social power**

| Power      | Definition                                  | Example                             |
| ---------- | ------------------------------------------- | ----------------------------------- |
| Coercive   | Power through punishment or threats         | Threatening disciplinary action     |
| Legitimate | Power from formal authority                 | Manager assigns responsibilities    |
| Expert     | Power from knowledge and skill              | Team trusts an experienced engineer |
| Reward     | Power from providing incentives             | Manager awards bonuses              |
| Referent   | Power from admiration, respect, or charisma | Team follows a respected leader     |

### **Key distinctions**

**Legitimate power:** People follow because of the person's formal position.

**Expert power:** People follow because of the person's knowledge.

**Referent power:** People follow because they admire or identify with the person.

**Reward power:** People follow because of incentives.

**Coercive power:** People comply because of possible punishment.

## **C. Effectiveness: Covey's Seven Habits**

Your professor includes Stephen Covey's **Seven Habits of Highly Effective People**.

| Habit                                              | Meaning                                                    |
| -------------------------------------------------- | ---------------------------------------------------------- |
| 1. Be proactive                                    | Take initiative instead of only reacting                   |
| 2. Begin with the end in mind                      | Know your goal before acting                               |
| 3. Put first things first                          | Prioritize important activities                            |
| 4. Think win-win                                   | Seek mutually beneficial outcomes                          |
| 5. Seek first to understand, then to be understood | Listen before trying to persuade                           |
| 6. Synergize                                       | Combine strengths through cooperation                      |
| 7. Sharpen the saw                                 | Maintain and develop yourself through learning and renewal |

**Synergy:** A result created through cooperation that is greater than what individuals could achieve separately.

**Proactive:** Taking action in anticipation of needs or problems.

**Reactive:** Responding after events have occurred.

## **D. Leadership styles**

Your professor presents several different leadership classifications.

### **General leadership styles**

| Style              | Definition                                                             |
| ------------------ | ---------------------------------------------------------------------- |
| Laissez-faire      | Gives team members substantial independence                            |
| Transactional      | Uses rewards, expectations, and consequences to manage performance     |
| Servant leadership | Prioritizes supporting and developing team members                     |
| Transformational   | Inspires people around a shared vision and change                      |
| Charismatic        | Influences others through personality and personal appeal              |
| Interactional      | Combines leadership behaviors based on relationships and circumstances |

### **Examples**

**Transactional:** Complete the required milestone and receive a performance reward.

**Transformational:** Inspire the team to embrace a new vision and improve how the organization operates.

**Servant leadership:** Remove obstacles, support employees, and help the team succeed.

**Laissez-faire:** Allow an experienced team to decide how to complete assigned work.

### **Kurt Lewin's leadership styles**

Your professor lists three.

**Autocratic:** Leader makes decisions with little team participation.

**Democratic:** Leader involves team members in decisions.

**Laissez-faire:** Leader gives team members substantial autonomy.

### **When might each be useful?**

Autocratic leadership may help during urgent situations requiring immediate decisions.

Democratic leadership may help when team knowledge and commitment are important.

Laissez-faire leadership may work well with experienced, self-directed employees.

Your professor emphasizes that effective leaders adjust their approach to the situation.

### **Six emotional leadership styles**

| Style        | Meaning                                                     |
| ------------ | ----------------------------------------------------------- |
| Visionary    | Provides a clear direction and inspires people toward it    |
| Coaching     | Helps individuals improve and develop                       |
| Affiliative  | Builds relationships and team harmony                       |
| Democratic   | Encourages participation in decisions                       |
| Pace-setting | Establishes high performance standards and leads by example |
| Commanding   | Gives clear directions and expects compliance               |

### **Leadership legacy styles**

Your slides list six additional styles:

| Style             | General focus                                            |
| ----------------- | -------------------------------------------------------- |
| Ambassador        | Building relationships and representing the team         |
| Advocate          | Supporting people or causes and speaking on their behalf |
| People Mover      | Developing people and helping them advance               |
| Truth Seeker      | Pursuing accuracy, honesty, and sound judgment           |
| Creative Builder  | Creating new ideas, solutions, or opportunities          |
| Experienced Guide | Providing direction based on experience                  |

These descriptions are general explanations of the styles named in the slides; the PowerPoint lists the labels and points to an external assessment rather than defining each one.

### **Blake-Mouton Managerial Grid**

Your professor introduces the **Blake-Mouton Managerial Grid**.

It evaluates leadership based on two dimensions:

- Concern for people.
- Concern for results or production.

The standard model includes:

| Style                         | People concern | Results concern |
| ----------------------------- | -------------- | --------------- |
| Impoverished management       | Low            | Low             |
| Country club management       | High           | Low             |
| Produce-or-perish management  | Low            | High            |
| Middle-of-the-road management | Moderate       | Moderate        |
| Team management               | High           | High            |

**Team management** emphasizes both people and results.

## **E. Leader versus manager: Warren Bennis**

Your professor provides an extensive comparison.

| Leader                    | Manager                          |
| ------------------------- | -------------------------------- |
| Inspires and motivates    | Plans and coordinates            |
| Innovates and develops    | Administers and maintains        |
| Focuses on people         | Focuses on systems and structure |
| Inspires trust            | Relies on control                |
| Has a long-term view      | Has a shorter-term view          |
| Asks what and why         | Asks how and when                |
| Originates ideas          | Implements established ideas     |
| Challenges the status quo | Maintains the status quo         |
| Does the right thing      | Does things right                |

**Leadership** focuses on direction, inspiration, and people.

**Management** focuses on planning, organizing, coordination, and execution.

A successful project manager needs both.

### **Can leadership be learned?**

Your professor explicitly says yes.

The slides emphasize:

- Taking initiative.
- Developing critical thinking.
- Listening effectively.
- Accepting feedback.
- Motivating others.
- Practicing self-discipline.
- Continuing to learn.
- Delegating without micromanaging.
- Managing conflict.
- Knowing when to follow others.

**Micromanagement:** Excessive supervision or control over how someone performs their work.

**Delegation:** Assigning responsibility for work to another person while retaining appropriate oversight.

## **F. Emotional intelligence and personality**

### **Emotional intelligence (EQ)**

**Emotional intelligence** is the ability to recognize, understand, and manage emotions in yourself and respond effectively to emotions in others.

Your professor emphasizes that successful teams often benefit from emotional awareness and psychological safety.

### **Important EQ-related abilities**

- Self-awareness.
- Self-regulation.
- Empathy.
- Motivation.
- Social skills.

**Self-awareness:** Recognizing your own emotions and behavior.

**Self-regulation:** Managing emotional reactions and impulses.

**Empathy:** Understanding another person's feelings or perspective.

**Psychological safety:** A team environment in which people feel able to ask questions, raise concerns, admit mistakes, and share ideas without fear of humiliation.

### **Personality and team development**

Your professor suggests using personality assessments to help team members understand differences in communication, motivation, and working styles.

The slides do not require memorizing a specific personality assessment framework.

The main point is that **people have different personalities and motivations, so a project manager should adapt their approach rather than treating everyone identically.**

## **G. Team development: Tuckman's Model**

Your professor includes Tuckman's Model of Team Formation.

The commonly taught five-stage version is:

1

**1. Forming**

Team members meet, learn their roles, and seek direction.

2

**2. Storming**

Disagreements emerge as people establish roles and expectations.

3

**3. Norming**

The team develops trust, shared rules, and cooperation.

4

**4. Performing**

The team works effectively toward its goals.

5

**5. Adjourning**

The team completes its work and disbands.

### **Exam examples**

A newly formed team is getting acquainted: **Forming**.

Team members argue over responsibilities: **Storming**.

The team establishes shared expectations: **Norming**.

The team collaborates efficiently: **Performing**.

The project ends and the team separates: **Adjourning**.

### **Ways to develop a team**

Your professor recommends:

- Training.
- Team-building activities.
- Getting to know team members.
- Understanding what motivates them.
- Discussing personality differences.
- Recognizing conflict early.
- Building trust.

## **Objective 6: Decide how to motivate and develop people**

This objective combines the theories above with actual project management decisions.

### **How to motivate team members**

**Step 1: Understand individual needs.**

Determine whether someone is motivated by achievement, relationships, power, recognition, growth, or other factors.

**Step 2: Match responsibilities to strengths.**

Give people tasks that fit their skills and provide opportunities for development.

**Step 3: Provide appropriate recognition.**

Acknowledge good work and meaningful contributions.

**Step 4: Remove obstacles.**

Provide necessary resources, training, support, and clear expectations.

**Step 5: Encourage participation.**

Allow team members to contribute ideas and make decisions when appropriate.

**Step 6: Provide feedback.**

Give specific, constructive information about performance.

**Step 7: Support growth.**

Offer mentoring, training, and challenging assignments.

### **Applying the theories**

| Situation                               | Relevant theory or approach          |
| --------------------------------------- | ------------------------------------ |
| Employee wants challenging goals        | McClelland: Achievement              |
| Employee values strong relationships    | McClelland: Affiliation              |
| Employee wants leadership opportunities | McClelland: Power                    |
| Employee lacks job security             | Maslow: Safety                       |
| Employee wants recognition              | Herzberg: Motivators                 |
| Employee enjoys the work itself         | Intrinsic motivation                 |
| Employee works for a bonus              | Extrinsic motivation                 |
| Experienced team wants autonomy         | Theory Y or laissez-faire leadership |
| Team needs inspiration for major change | Transformational leadership          |
| Employee needs help developing skills   | Coaching leadership                  |

### **How motivation supports project success**

Motivated employees may demonstrate stronger engagement, cooperation, initiative, and commitment.

However, motivation alone cannot compensate for unrealistic schedules, inadequate staffing, or unclear requirements.

A project manager must support people while also managing the project's constraints.

## **Objective 7: Minimize the negative effects of conflict**

### **What is conflict?**

**Conflict** is a disagreement or incompatibility between individuals or groups involving goals, priorities, opinions, resources, or behavior.

Conflict is not automatically harmful.

Constructive disagreement can reveal problems and improve decisions.

The danger occurs when conflict is ignored, becomes personal, or prevents the team from working effectively.

### **Common causes of project conflict**

- Unclear responsibilities.
- Competing priorities.
- Limited resources.
- Schedule pressure.
- Personality differences.
- Poor communication.
- Different technical opinions.
- Unequal workloads.
- Unresolved expectations.

### **Five common conflict management approaches**

These are standard project management definitions that supplement your professor's discussion of recognizing and addressing conflict.

| Approach                    | Meaning                                                  | Example                                                 |
| --------------------------- | -------------------------------------------------------- | ------------------------------------------------------- |
| Collaborate / problem-solve | Work together to address underlying causes               | Team develops a solution satisfying both needs          |
| Compromise / reconcile      | Each side gives up something                             | Two teams split a limited resource                      |
| Smooth / accommodate        | Emphasize agreement or give priority to the relationship | One person accepts another's preference                 |
| Force / direct              | Use authority to impose a decision                       | Manager makes an urgent decision                        |
| Withdraw / avoid            | Delay or step away from the disagreement                 | Postpone discussion until more information is available |

### **Five team dysfunctions**

Your professor specifically lists these:

1. **Absence of trust:** Team members do not feel comfortable relying on one another.
2. **Fear of conflict:** Team members avoid necessary disagreements.
3. **Lack of commitment:** Team members do not fully support decisions.
4. **Avoidance of accountability:** Team members fail to hold one another responsible.
5. **Inattention to results:** Individual interests take priority over team success.

### **How to prevent these dysfunctions**

Your slides recommend:

- Build trust.
- Discuss disagreements openly.
- Follow through on commitments.
- Hold people accountable.
- Reward results.
- Address problems early.

### **Groupthink**

**Groupthink** occurs when a group's desire for agreement discourages critical thinking and alternative viewpoints.

Example:

Everyone agrees with a poor project decision because nobody wants to challenge the manager.

### **Death march project**

A **death march project** is a project with extremely demanding or unrealistic expectations that can place excessive pressure on the team.

These projects may involve unreasonable deadlines, insufficient resources, and sustained overwork.

Your professor identifies groupthink and death march projects as situations to avoid.

## **Part 2. Additional Chapter 7 material**

### **Communication and project success**

Your professor emphasizes that project managers may spend up to 90% of their time communicating.

The main lesson is that communication is a central project management responsibility, not a minor administrative activity.

Poor communication can lead to:

- Misunderstood requirements.
- Missed deadlines.
- Conflicting expectations.
- Duplicated work.
- Delayed decisions.
- Unresolved problems.
- Lower stakeholder satisfaction.

### **Communication planning**

Your Chapter 7 slides repeat the communications management plan introduced in Chapter 6.

Remember the key questions:

**What** information is needed?

**Who** needs it?

**Who** prepares it?

**How** will it be delivered?

**When** and **how often** will it be delivered?

**What happens** when problems require escalation?

### **Communication barriers**

Additional common barriers to understand include:

- Unclear wording.
- Technical jargon.
- Cultural differences.
- Assumptions.
- Information overload.
- Emotional reactions.
- Lack of feedback.
- Poor listening.

**Jargon:** Specialized terminology that may be difficult for people outside a field to understand.

**Information overload:** Receiving more information than someone can effectively process.

### **Microaggressions**

Your professor defines **microaggressions** as everyday, often subtle interactions or behaviors that communicate bias toward historically marginalized groups.

They can be intentional or unintentional.

The slides emphasize that people may not realize their behavior has this effect.

### **Bias**

**Bias** is a tendency or preference that can affect how someone interprets information or treats others.

**Unconscious bias:** Bias that operates without deliberate awareness.

Your professor includes examples of hiring and technology-related bias to demonstrate how assumptions can influence workplace decisions.

### **Intent versus impact**

Your slides emphasize that a person's intention does not erase the effect of their behavior.

A project manager should:

- Listen openly.
- Seek to understand others.
- Avoid becoming defensive.
- Take concerns seriously.
- Apologize when appropriate.
- Learn from mistakes.
- Encourage an inclusive environment.

### **Psychological safety**

Psychological safety allows team members to communicate concerns and mistakes without fear of embarrassment or punishment.

This supports effective collaboration, learning, and early problem identification.

## **Chapter 7: Complete vocabulary summary**

| Term                        | Definition                                                   |
| --------------------------- | ------------------------------------------------------------ |
| Communication channel       | Potential communication connection between participants      |
| Brooks' Law                 | Adding people to a late software project can make it later   |
| Agenda                      | Planned meeting topics                                       |
| Meeting minutes             | Written meeting record                                       |
| Interactive communication   | Two-way exchange                                             |
| Push communication          | Information sent to recipients                               |
| Pull communication          | Information retrieved by recipients                          |
| Active listening            | Attentive listening to understand a message                  |
| Intrinsic motivation        | Motivation from interest or satisfaction in the activity     |
| Extrinsic motivation        | Motivation from external rewards or pressures                |
| Self-Determination Theory   | Theory involving intrinsic and extrinsic motivation          |
| Maslow's hierarchy          | Five levels of human needs                                   |
| Hygiene factor              | Condition whose absence causes dissatisfaction               |
| Motivator                   | Factor encouraging satisfaction and motivation               |
| nAch                        | Need for achievement                                         |
| nAff                        | Need for affiliation                                         |
| nPow                        | Need for power                                               |
| Theory X                    | Assumption that employees require close control              |
| Theory Y                    | Assumption that employees can be self-directed               |
| Theory Z                    | Emphasis on trust, collective decisions, and cultural values |
| Legitimate power            | Power from formal authority                                  |
| Coercive power              | Power through threats or punishment                          |
| Reward power                | Power through incentives                                     |
| Expert power                | Power through specialized knowledge                          |
| Referent power              | Power through admiration or respect                          |
| Autocratic leadership       | Leader makes decisions with little participation             |
| Democratic leadership       | Team members participate in decisions                        |
| Laissez-faire leadership    | Team members receive substantial independence                |
| Transactional leadership    | Leadership through rewards and expectations                  |
| Transformational leadership | Leadership through vision and inspiration                    |
| Servant leadership          | Leadership focused on supporting others                      |
| Charismatic leadership      | Influence through personal appeal                            |
| Emotional intelligence      | Ability to understand and manage emotions                    |
| Empathy                     | Understanding another person's perspective                   |
| Psychological safety        | Feeling safe to speak up and take interpersonal risks        |
| Forming                     | Initial team development stage                               |
| Storming                    | Stage involving disagreement and role negotiation            |
| Norming                     | Stage involving shared rules and cooperation                 |
| Performing                  | Stage involving effective teamwork                           |
| Adjourning                  | Stage involving team completion and separation               |
| Conflict                    | Disagreement involving goals, needs, or perspectives         |
| Collaboration               | Working together to solve a problem                          |
| Compromise                  | Each side gives up something to reach agreement              |
| Groupthink                  | Pressure for agreement suppresses critical thinking          |
| Death march project         | Project with extreme or unrealistic demands                  |
| Microaggression             | Subtle interaction or behavior communicating bias            |
| Unconscious bias            | Bias operating without deliberate awareness                  |
| Delegation                  | Assigning work to another person                             |
| Micromanagement             | Excessive control over another person's work                 |
| Synergy                     | Combined results greater than individual contributions       |

**Chapter 7 exam focus:** Communication channels formula, Brooks' Law, push/pull/interactive communication, meeting procedures, all motivation theories and their authors, French and Raven's power bases, leadership styles, Tuckman's stages, conflict, and team dysfunctions.

# **Final Exam Review: Chapters 4–7**

## **1. Every calculation you should practice**

**PERT expected duration**

\\[ \frac{O+4M+P}{6} \\]

Used to estimate an activity's duration from three estimates.

**Communication channels**

\\[ \frac{n(n-1)}{2} \\]

Used to calculate potential communication relationships.

**Expected Monetary Value (EMV)**

\\[ EMV=\sum(p\times\text{Outcome}) \\]

Used to evaluate probability-weighted financial outcomes.

**Total slack / float**

\\[ LS-ES=LF-EF \\]

Used to determine scheduling flexibility.

**Profit margin**

\\[ \frac{\text{Profit}}{\text{Revenue}}\times100 \\]

**Earned Value Management**

\\[ CV=EV-AC \qquad SV=EV-PV \\]

\\[ CPI=\frac{EV}{AC}\qquad SPI=\frac{EV}{PV} \\]

## **2. Terms that are especially easy to confuse**

| Term A                  | Term B                  | Key difference                                                    |
| ----------------------- | ----------------------- | ----------------------------------------------------------------- |
| Scope statement         | Scope management plan   | What is included vs. how scope is managed                         |
| WBS                     | Activity list           | Deliverable-oriented breakdown vs. scheduled actions              |
| Requirements collection | Requirements validation | Discover needs vs. confirm needs are understood and met           |
| Work package            | Milestone               | Work component vs. significant event                              |
| Effort                  | Duration                | Amount of work vs. time required                                  |
| Crashing                | Fast tracking           | Add resources vs. overlap tasks                                   |
| Critical path           | Critical chain          | Dependency-based longest path vs. resource-constrained scheduling |
| Contingency reserve     | Management reserve      | Known risks vs. unforeseen risks                                  |
| EMV                     | EVM                     | Risk-based expected money vs. performance measurement             |
| Responsible             | Accountable             | Performs work vs. ultimately owns the result                      |
| Resource loading        | Resource leveling       | Assigning work vs. rearranging work to address capacity           |
| Risk                    | Issue                   | Might happen vs. already exists                                   |
| Threat                  | Opportunity             | Negative risk vs. positive risk                                   |
| Residual risk           | Secondary risk          | Risk remaining vs. risk created by a response                     |
| Mitigate                | Avoid                   | Reduce threat vs. eliminate threat                                |
| Exploit                 | Enhance                 | Ensure opportunity vs. increase its probability or benefit        |
| Push                    | Pull                    | Send information vs. retrieve information                         |
| Expert power            | Legitimate power        | Knowledge vs. formal position                                     |
| Herzberg hygiene        | Herzberg motivator      | Prevent dissatisfaction vs. encourage satisfaction                |
| Theory X                | Theory Y                | Control-oriented vs. self-direction-oriented assumptions          |
| Leader                  | Manager                 | Inspire and guide vs. plan and coordinate                         |

## **3. Memorize the theorists and models**

| Name                         | Associated theory or model                       |
| ---------------------------- | ------------------------------------------------ |
| Ryan and Deci                | Self-Determination Theory                        |
| Abraham Maslow               | Hierarchy of Needs                               |
| Frederick Herzberg           | Motivation-Hygiene Theory                        |
| David McClelland             | Acquired-Needs Theory                            |
| Douglas McGregor             | Theory X and Theory Y                            |
| William Ouchi                | Theory Z                                         |
| Thamhain and Wilemon         | Nine influence bases                             |
| French and Raven             | Five bases of social power                       |
| Stephen Covey                | Seven Habits of Highly Effective People          |
| Kurt Lewin                   | Autocratic, Democratic, Laissez-faire leadership |
| Warren Bennis                | Leader versus manager                            |
| Bruce Tuckman                | Team development stages                          |
| Robert Blake and Jane Mouton | Managerial Grid                                  |
| Fred Brooks                  | Brooks' Law                                      |
| Henry Gantt                  | Gantt chart                                      |

## **4. Which chapter should you review most?**

Based on the quantity and type of material in your uploaded slides, here's how I would prioritize a final review. This is a study recommendation, not a prediction of your professor's question distribution.

**Chapter 5**

Practice first

Most calculation-heavy: PERT, critical path, slack, dependencies, scheduling, and cost.

**Chapter 6**

Practice second

Many documents, risk strategies, RACI, resource leveling, and EMV.

**Chapter 7**

Memorize theories

Large amount of theory memorization, communication, leadership, and team development.

**Chapter 4**

Review definitions

Mostly definitions, scope documents, requirements, WBS, and scope creep.

## **5. Final self-assessment**

Use this to identify what you still need to review.

**Exam readiness checklist**

Check each skill once you can explain it without looking.

## **0/27**

Chapter 4

I can define project scope and distinguish product scope from project scope.

I can explain all five scope deliverables.

I can identify requirement types and collection methods.

I can explain all WBS development approaches.

I understand Agile stories, INVEST, MoSCoW, and Definition of Done.

I can explain causes and prevention of scope creep.

Chapter 5

I can explain the schedule management plan.

I know all four dependency relationships and categories.

I can identify a critical path and calculate slack.

I can calculate PERT estimates without help.

I understand effort, duration, milestones, and Gantt charts.

I can distinguish crashing, fast tracking, and critical chain.

I know cost types, reserves, estimating techniques, and EVM.

Chapter 6

I can explain every stakeholder and resource deliverable.

I can construct and interpret a RACI chart.

I understand resource loading and leveling.

I can distinguish risks from issues and opportunities from threats.

I know every positive and negative risk response strategy.

I can calculate EMV and explain risk utility.

I understand risk registers, risk matrices, and monitoring.

Chapter 7

I can calculate communication channels.

I know how to plan and conduct effective meetings.

I can identify push, pull, and interactive communication.

I know all motivation theories and their authors.

I can identify influence bases and leadership styles.

I know Tuckman's team development stages.

I understand conflict resolution, groupthink, and team dysfunctions.

This guide covers all the learning objectives you provided, the additional Chapter 5 cost objectives, and the major supporting concepts in the four lecture decks. It is extensive, but it cannot guarantee that every possible exam question or detail from a visual slide will appear here.

**The next most useful step is a full practice exam using your professor's material**, especially scenario-based questions where you must distinguish similar terms or select the correct formula.

&#x20; Start the Chapters 4–7 practice exam&#x20;