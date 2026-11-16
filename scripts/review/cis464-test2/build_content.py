"""Build CIS 464 Exam 2 from the supplied Chapters 4–7 master guide."""
from __future__ import annotations

import html, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
SOURCE=Path(__file__).with_name('study-guide.md')
OUT=ROOT/'dist/cis464-test2-content.json'
OUT_JS=ROOT/'dist/cis464-test2-content.js'

CHAPTERS={
4:('Project Scope Planning','What exactly are we supposed to deliver?'),
5:('Schedule and Budget Planning','How long will it take, and how much will it cost?'),
6:('Stakeholders, Resources, and Risk','Who is involved, what resources do we need, and what could happen?'),
7:('Communications, Leadership, and Motivation','How do we communicate, lead, motivate, and work effectively together?'),
}
CHAPTER_OVERVIEWS={
4:'Chapter 4 defines exactly what the project will deliver, how requirements become an approved scope baseline, and how controlled change prevents scope creep.',
5:'Chapter 5 turns project work into a schedule and budget, then uses dependency, critical-path, PERT, cost, and earned-value calculations to plan and control performance.',
6:'Chapter 6 identifies stakeholders and resources, makes ownership visible, and manages both threats and opportunities through documented risk analysis and responses.',
7:'Chapter 7 explains how teams exchange information, run meetings, lead and motivate people, develop as a group, and handle conflict safely and productively.',
}

OBJECTIVE_ANSWERS={
'Objective 1: Define scope':'Scope is all work and processes required to create the agreed deliverables. It sets the boundary between included work and excluded work.',
'Objective 2: Prepare the five scope management deliverables':'Prepare the scope statement, WBS, scope management plan, requirements management plan, and requirements traceability matrix; each answers a different scope-control question.',
'Objective 3: List methods for collecting and validating requirements':'Collect requirements with interviews, groups, workshops, brainstorming, surveys, observation, prototypes, document analysis, benchmarking, JAD, and use cases; validate that requirements are necessary, clear, feasible, testable, complete, consistent, and traceable.',
'Objective 4: List approaches to building a WBS':'A WBS can be built with top-down decomposition, bottom-up grouping, analogy, mind mapping, or a combination, and should end in manageable work packages.',
'Objective 5: Explain how to control scope creep':'Prevent uncontrolled scope expansion with a clear baseline, traceability, acceptance criteria, stakeholder agreement, impact analysis, and integrated change control.',
'Objective 1: Plan schedule management':'Define the procedures, tools, units, thresholds, roles, reporting rules, and change-control methods used to create and control the schedule.',
'Objective 2: Develop the schedule on a project':'List and describe activities, sequence dependencies, estimate resources and durations, build the network, find the critical path, and produce the approved schedule.',
'Objective 3: Classify dependencies by type and sequence':'Classify why work depends as mandatory, discretionary, internal, or external, and how it connects as finish-to-start, start-to-start, finish-to-finish, or start-to-finish.',
'Objective 4: Identify the critical path':'The critical path is the longest-duration path through the activity network and normally determines the earliest project completion date; its activities usually have zero total slack.',
"Objective 5: Compare Murphy's Law and Parkinson's Law":"Murphy's Law warns that possible problems can occur; Parkinson's Law says work tends to expand to fill the time available.",
'Objective 6: Calculate a PERT estimate':'Use the three-point estimate (optimistic + 4×most likely + pessimistic) ÷ 6, with standard deviation (pessimistic − optimistic) ÷ 6.',
'Objective 7: Prepare the schedule management plan and Gantt chart':'The plan explains how the schedule is managed; the Gantt chart places activities against time to show dates, durations, dependencies, milestones, and progress.',
'Objective 8: Define all specified schedule terms':'Know activities, attributes, milestones, dependencies, leads, lags, networks, critical path, slack, effort, duration, crashing, and fast tracking as separate schedule concepts.',
'Cost objective 1: Plan cost management':'Set the units, precision, control thresholds, reporting, accounting, estimation, budgeting, and change-control rules used to manage project costs.',
'Cost objective 2: Develop the project budget':'Estimate activity and work-package costs, aggregate them through the WBS, add appropriate contingency reserves, and time-phase the approved cost baseline.',
'Cost objective 3: Define cost categories and reserves':'Separate tangible/intangible, direct/indirect, sunk, lifecycle, contingency, and management-reserve concepts so costs are classified and controlled correctly.',
'Cost objective 4: Describe cost estimation techniques':'Use analogous, parametric, bottom-up, three-point, vendor-bid, and reserve-analysis methods according to the detail and uncertainty available.',
'Cost objective 5: Explain why people estimate poorly':'Estimates fail because of incomplete scope, optimism, pressure, uncertainty, ignored risk, weak data, and confusing estimates with commitments; document assumptions and update estimates as knowledge improves.',
'Cost objective 6: Conduct earned value management analysis':'Compare planned value, earned value, and actual cost, then calculate cost and schedule variances and performance indexes to interpret project performance.',
'Cost objective 7: Prepare cost deliverables':'Prepare the cost management plan, detailed cost estimate, and approved time-phased cost baseline.',
'Objective 1: Design the project deliverables':'Create the stakeholder engagement plan, communications plan, organization chart, RAM/RACI, resource histogram, staffing plan, team charter, risk plan, risk register, probability-impact matrix, and EMV analysis.',
'Objective 2: Explain why only one person should be responsible for a deliverable':'One accountable owner prevents ambiguity and makes final ownership clear, while several people may still perform, advise, or receive information about the work.',
'Objective 3: Explain how resource leveling works':'Compare demand with resource capacity and move or delay activities to remove overallocations, accepting that the critical path or finish date may change.',
'Objective 4: Explain how risk utility affects project management':'People value risky outcomes differently, so risk-averse, risk-neutral, and risk-seeking stakeholders can choose different responses to the same probability and impact.',
'Objective 5: Identify good risks versus bad risks':'Threats could harm objectives; opportunities could help them. Both are uncertain risks requiring ownership and an appropriate response, while an issue has already happened.',
'Objective 6: List potential sources of risk and how to address them':'Find technical, people, schedule, cost, supplier, external, organizational, and project-management risks, analyze probability and impact, assign owners, choose responses, and monitor triggers.',
'Objective 1: Calculate the number of communication channels':'For n participants, potential two-person communication channels equal n(n−1)÷2.',
'Objective 2: Plan and conduct an effective meeting':'Clarify purpose and attendees, send an agenda and material, facilitate focused participation and decisions, then distribute minutes, actions, owners, and due dates.',
'Objective 3: Differentiate push, pull, and interactive communication':'Push sends information to recipients, pull lets recipients retrieve it, and interactive communication creates a live two-way exchange.',
'Objective 4: Determine which communication tool works best':'Choose the medium using urgency, complexity, sensitivity, audience, feedback needs, accessibility, documentation, security, and time-zone constraints.',
'Objective 5: List major theories of motivation, influence, power, effectiveness, emotional intelligence, personality, and team building':'Know the named theorists and models, their components, and the behavior each predicts or recommends rather than treating all leadership and motivation ideas as interchangeable.',
'Objective 6: Decide how to motivate and develop people':'Understand individual needs, provide meaningful work and autonomy, set clear expectations, recognize contributions, coach skills, remove obstacles, and adapt leadership to the person and situation.',
'Objective 7: Minimize the negative effects of conflict':'Address disagreements early, separate people from problems, choose an appropriate conflict approach, build psychological safety, and prevent dysfunction, groupthink, and unrealistic death-march conditions.',
}

TOPIC_ANSWERS={
'What counts as project scope?':'Project scope includes the work required to create the agreed deliverables, such as configuration, data migration, testing, training, and documentation. Unrelated operations, future projects, past work, and unapproved products remain out of scope.',
'Types of requirements':'Requirement categories include business, stakeholder, user, functional, nonfunctional, technical, operational, feasibility, solution, transition, product, process, quality, implementation, architectural, quality-of-service, and project requirements.',
'Methods of collecting requirements':'Teams can collect requirements through interviews, focus groups, facilitated workshops, brainstorming, surveys, observation, prototypes, document analysis, benchmarking, Joint Application Design workshops, and use cases.',
'Why requirements collection is difficult':'Requirements are difficult to collect because time is limited, stakeholders may disagree or struggle to explain what they need, expectations may be unrealistic, systems may be hard to visualize, and technology or connected functions can change.',
'Scope creep: Causes':'Scope creep commonly comes from vague requirements, unclear boundaries, missing change-control procedures, unreviewed feature requests, weak validation, and poor communication.',
'Methods of control':'Control scope creep by establishing a clear scope baseline, validating requirements and deliverables, recording change requests, analyzing each request’s effects, and approving or rejecting it through integrated change control.',
'Agile scope management':'Agile manages scope in short iterations. Teams refine and prioritize requirements through feedback, deliver usable increments, and treat a sprint as a fixed-length iteration rather than trying to define every detail once at the beginning.',
'MoSCoW prioritization':'MoSCoW ranks requirements as Must have, Should have, Could have, and Won’t have in the current delivery.',
'INVEST rule for user stories':'INVEST means Independent, Negotiable, Valuable, Estimable, Small, and Testable. A useful user story should satisfy all six qualities.',
'Big Visual Charts (BVCs)':'Big Visual Charts, also called information radiators, display current work, progress, and issues where the team can understand project status at a glance.',
'Steps for developing a schedule':'Develop a schedule by identifying activities, sequencing them, estimating resources and durations, creating the activity network, finding the critical path, and approving the resulting schedule baseline.',
'Four categories explaining WHY tasks are dependent':'Mandatory dependencies come from the work itself, discretionary dependencies reflect a preferred sequence, external dependencies involve work outside the project, and internal dependencies remain under the project team’s control.',
'FS':'Finish-to-start means the successor cannot start until the predecessor finishes.',
'SS':'Start-to-start means the successor cannot start until the predecessor starts.',
'FF':'Finish-to-finish means the successor cannot finish until the predecessor finishes.',
'SF':'Start-to-finish means the successor cannot finish until the predecessor starts. It is uncommon.',
'Example: Find the critical path':'Calculate the duration of every complete path through the network. The path with the greatest total duration is the critical path and normally determines the earliest project finish date.',
'Slack formulas':'Total slack equals LS minus ES or LF minus EF. Free slack is the time an activity can slip without delaying the early start of its immediate successor.',
'Forward pass and backward pass':'A forward pass calculates earliest start and finish times: EF = ES + duration, and a successor uses the latest predecessor EF. A backward pass calculates latest finish and start times: LS = LF − duration, and a predecessor uses the earliest successor LS.',
'PERT estimate: Formula':'PERT expected duration equals (optimistic + 4 × most likely + pessimistic) ÷ 6.',
"PERT estimate: Your professor's example":'For optimistic 8, most likely 10, and pessimistic 24 workdays, PERT gives (8 + 4×10 + 24) ÷ 6 = 12 workdays.',
'PERT estimate: Another example':'For optimistic 3, most likely 6, and pessimistic 15, PERT gives (3 + 4×6 + 15) ÷ 6 = 7 work units.',
'Additional PERT formulas':'PERT standard deviation equals (pessimistic − optimistic) ÷ 6. PERT variance is that standard deviation squared. The weighted expected-duration formula remains the main formula emphasized by the lecture.',
'Effort versus duration':'Effort is the total labor required, such as 16 person-hours. Duration is the elapsed calendar time, such as one day when two people each work eight hours.',
'Crashing versus fast tracking':'Crashing shortens the schedule by adding resources or cost to critical-path work. Fast tracking overlaps activities that were planned sequentially, which usually increases rework and risk.',
'Full-Time Equivalent (FTE)':'A Full-Time Equivalent converts labor capacity into the workload of one full-time worker. Two half-time workers equal one FTE.',
'Bottom-up example':'A bottom-up estimate prices detailed components first, then adds them to obtain the total. For example, software, labor, hardware, training, and reserve estimates are calculated separately and summed.',
'Earned value management analysis: Worked example':'With PV=$10,000, EV=$8,000, and AC=$9,000: CV=−$1,000, SV=−$2,000, CPI=0.89, and SPI=0.80. The project is over budget and behind schedule.',
'Cost control tools':'Cost control uses budget and actual-cost reports, variance and trend analysis, earned value management, forecasting, change control, and project-management or accounting software.',
'Controlling AI costs':'Excessive AI spending can come from FOMO, unbounded agents, poor tool selection, repeated uncached work, and weak growth planning. Cost control uses strategy, executive sponsorship, governance, workload-based model routing, task-level cost tracking, and vendor flexibility.',
'Stakeholder engagement levels':'Stakeholder engagement can be unaware, resistant, neutral, supportive, or leading. The team compares current and desired levels and plans how to close important gaps.',
'Risk management plan':'The risk management plan explains how the project will identify, analyze, respond to, monitor, and report risks. It defines the process, roles, categories, timing, budget, and thresholds for risk work.',
'EMV worked example':'For each option, multiply every outcome by its probability and add the results. The project with the best probability-weighted value has the highest EMV, although decision makers may also consider risk preference and strategic fit.',
'Risk versus issue':'A risk is an uncertain future event that may affect objectives. An issue is a problem or event that has already occurred and now requires action.',
'Methods of identifying risks':'Teams identify risks with brainstorming, interviews, checklists, document reviews, assumption analysis, SWOT analysis, cause-and-effect diagrams, Delphi techniques, and lessons learned from earlier projects.',
'Risk monitoring':'Assign every important risk an owner, review triggers and status regularly, carry out approved responses, identify new risks, update the register, and evaluate whether the risk process works.',
'Resource leveling versus resource smoothing':'Resource leveling moves or delays work to resolve resource limits and may change the project finish date. Resource smoothing redistributes work only within available slack so the critical completion date does not change.',
'Communication channels reference table':'Potential channels grow quickly as the team grows: 2 people have 1 channel, 3 have 3, 4 have 6, 5 have 10, and 10 have 45. Use n(n−1)÷2 for any team size.',
'Communication channels: Formula':'For n people, the number of potential two-person communication channels is n(n−1)÷2.',
'Why can adding people cause more delays?':'New people require recruiting, onboarding, training, and coordination. Existing members lose productive time helping them, and the larger team creates more communication channels. This is the reasoning behind Brooks’ Law.',
'Before the meeting':'Before a meeting, confirm that a meeting is necessary, define its purpose, invite only people who contribute or need the result, choose an accessible time and place, and send the agenda and preparation material early.',
'Motivation theories':'The chapter covers Self-Determination Theory, Maslow’s hierarchy, Herzberg’s Motivation-Hygiene Theory, McClelland’s acquired needs, McGregor’s Theory X and Theory Y, and Ouchi’s Theory Z. Each explains motivation from a different angle.',
'Theories of influence and power':'Thamhain and Wilemon describe nine project influence bases, while French and Raven classify social power as legitimate, reward, coercive, expert, and referent power. The models explain where a leader’s influence comes from.',
'Theories of influence and power: Key distinctions':'Legitimate power comes from formal position, reward power from the ability to provide benefits, coercive power from the ability to punish, expert power from knowledge, and referent power from respect or identification.',
'Push, pull, and interactive communication: Key distinction':'Push sends information to recipients, pull stores information for recipients to retrieve, and interactive communication supports a live two-way exchange.',
'Motivation theories: The five levels':'Maslow’s five levels are physiological needs, safety, social belonging, esteem, and self-actualization. Lower needs generally require attention before higher-level growth needs strongly motivate someone.',
'Leadership legacy styles':'The lecture’s leadership legacy styles are ambassador, advocate, people mover, truth seeker, creative builder, and experienced guide. Each describes the type of influence a leader tends to leave behind.',
'Blake-Mouton Managerial Grid':'The Blake-Mouton Managerial Grid compares concern for people with concern for results. It helps describe leadership approaches based on whether each concern is low or high.',
'Can leadership be learned?':'Leadership can be developed through practice, feedback, reflection, education, mentoring, experience, and willingness to change old habits.',
"Team development: Tuckman's Model":'Tuckman’s stages are forming, storming, norming, performing, and adjourning. Teams meet and orient first, work through disagreement, establish norms, perform effectively, and finally close the work.',
'How to prevent these dysfunctions':'Build trust, discuss disagreement constructively, make clear commitments, hold people accountable, and keep attention on shared project results.',
'Five common conflict management approaches':'The five approaches are collaborate or problem-solve, compromise or reconcile, smooth or accommodate, force or direct, and withdraw or avoid. The project manager chooses based on urgency, importance, relationships, and the need for a lasting solution.',
'Communication barriers':'Communication barriers include language or jargon, cultural differences, assumptions, emotion, noise, poor timing, information overload, status differences, inaccessible tools, weak listening, and missing feedback.',
'Microaggressions':'Microaggressions are everyday comments or behaviors that communicate bias toward historically marginalized people. They may be intentional or unintentional, and their impact still matters.',
'RACI definitions':'RACI means Responsible, Accountable, Consulted, and Informed. Responsible performs the work; Accountable owns the final result and approval; Consulted provides input; Informed receives updates.',
'Three risk preferences':'Risk-averse people prefer lower uncertainty, risk-neutral people judge mainly by expected value, and risk-seeking people may accept greater uncertainty for a potentially larger reward.',
"McGregor's Theory X and Theory Y":'Theory X assumes workers dislike work and need close supervision. Theory Y assumes people can be self-directed, responsible, and motivated when the environment supports them.',
"Ouchi's Theory Z":'Theory Z emphasizes trust, quality, collective decision making, cultural values, and long-term relationships and commitment.',
"Effectiveness: Covey's Seven Habits":'Covey’s habits are Be proactive; Begin with the end in mind; Put first things first; Think win-win; Seek first to understand, then to be understood; Synergize; and Sharpen the saw.',
'Communication planning':'A communications plan identifies what information is needed, who needs it, who prepares it, how it will be delivered, when and how often it will be delivered, and how problems will be escalated.',
'Profit formula':'Profit = Revenue − Expenses.',
'Profit margin formula':'Profit margin = (Profit ÷ Revenue) × 100%.',
'EVM formulas':'CV = EV − AC; SV = EV − PV; CPI = EV ÷ AC; SPI = EV ÷ PV.',
'EMV formula':'EMV = the sum of each probability × its monetary outcome.',
}

QUESTION_OVERRIDES={
'Important definitions':'How do project scope, product scope, deliverables, in-scope work, and out-of-scope work differ?',
'Memorize the differences':'How do the scope statement, WBS, scope management plan, requirements management plan, and RTM differ?',
'Types of requirements':'Which categories can project requirements fall into?',
'Methods of collecting requirements':'Which methods can a project team use to collect requirements?',
'Why requirements collection is difficult':'Why is collecting requirements difficult?',
'Methods of control':'How can a project manager control scope creep?',
'Agile scope management':'How does Agile manage project scope?',
'Value Breakdown Structure (VBS)':'How does a Value Breakdown Structure differ from a WBS?',
'MoSCoW prioritization':'What do the four MoSCoW priority categories mean?',
'INVEST rule for user stories':'What does each letter in INVEST require from a user story?',
'Big Visual Charts (BVCs)':'What are Big Visual Charts, and why does a project team use them?',
'Steps for developing a schedule':'What are the steps for developing a project schedule?',
'Four categories explaining WHY tasks are dependent':'What are the four reasons that project activities may depend on one another?',
'FS':'What does a finish-to-start dependency require?',
'SS':'What does a start-to-start dependency require?',
'FF':'What does a finish-to-finish dependency require?',
'SF':'What does a start-to-finish dependency require?',
'Example: Find the critical path':'How do you identify the critical path in an activity network?',
'Slack formulas':'How do you calculate total slack?',
'Scope creep: Causes':'What causes uncontrolled project scope growth?',
'PERT estimate: Formula':'What is the PERT expected-duration formula?',
"PERT estimate: Your professor's example":'Using the lecture values O=8, M=10, and P=24, what PERT duration should you obtain?',
'PERT estimate: Another example':'Using O=3, M=6, and P=15, what PERT duration should you obtain?',
'Earned value management analysis: Worked example':'What do CV, SV, CPI, and SPI show when PV=$10,000, EV=$8,000, and AC=$9,000?',
'Communication channels: Formula':'What formula calculates the number of potential communication channels among n people?',
'Push, pull, and interactive communication: Key distinction':'How do push, pull, and interactive communication differ?',
'Motivation theories: The five levels':'What are Maslow’s five levels of need, from lowest to highest?',
'Theories of influence and power: Key distinctions':'How do legitimate, reward, coercive, expert, and referent power differ?',
'Effort versus duration':'What is the difference between effort and duration?',
'Crashing versus fast tracking':'How do crashing and fast tracking shorten a schedule differently?',
'Full-Time Equivalent (FTE)':'What does Full-Time Equivalent measure?',
'Risk versus issue':'What is the difference between a risk and an issue?',
'Before the meeting':'What should the project manager do before a meeting?',
'Why can adding people cause more delays?':'Why can adding people to a late project make it later?',
'Microaggressions':'What is a microaggression, and why does impact matter?',
'Work Breakdown Structure (WBS)':'What is a Work Breakdown Structure, and how does it organize project work?',
'Requirements Traceability Matrix (RTM)':'What does an RTM track throughout a project?',
'Definition of Done':'What conditions does a Definition of Done establish?',
'Questions a project manager should ask':'Which questions should a project manager answer before building the schedule?',
'Methods for estimating schedules':'Which methods can a team use to estimate activity durations?',
'Forward pass and backward pass':'What does a forward pass calculate, and what does a backward pass calculate?',
'SMART milestones':'What does each letter in SMART require from a milestone?',
'Bottom-up example':'How does bottom-up cost estimating work?',
'Ways to improve estimates':'How can a project team improve the accuracy of estimates?',
'Three core EVM values':'What do PV, EV, and AC measure?',
'Cost control tools':'Which tools help a project manager monitor and control costs?',
'Controlling AI costs':'Which behaviors can make organizational AI spending unnecessarily high?',
'Stakeholder engagement levels':'What are the five stakeholder engagement levels?',
'Responsibility Assignment Matrix (RAM)':'What does a Responsibility Assignment Matrix show?',
'RACI definitions':'What does each letter in RACI mean?',
'Team charter or team contract':'What rules should a team charter establish?',
'EMV worked example':'How is EMV used to compare risky project options?',
'Resource loading':'What does resource loading measure?',
'Resource leveling':'How does resource leveling correct an overallocation?',
'Resource Breakdown Structure (RBS)':'How does an RBS organize project resources?',
'Three risk preferences':'How do risk-averse, risk-neutral, and risk-seeking decision makers differ?',
'Negative risks: threats':'What makes a project risk a threat?',
'Positive risks: opportunities':'What makes a project risk an opportunity?',
'Issue log':'What information does an issue log track?',
'Potential sources of project risk':'Which categories can produce project risk?',
'Methods of identifying risks':'Which methods can a team use to discover project risks?',
'Contingency reserve':'When is contingency reserve used, and is it inside the cost baseline?',
'Management reserve':'When is management reserve used, and is it inside the cost baseline?',
'Five response strategies for negative risks':'What are the five response strategies for threats?',
'Five response strategies for positive risks':'What are the five response strategies for opportunities?',
'Residual risk':'What remains after a risk response is implemented?',
'Secondary risk':'What is a secondary risk?',
'Inherent risk':'What does inherent risk measure?',
'Risk monitoring':'What should happen while project risks are being monitored?',
'Top Ten Risk Item Tracking':'Why does a team maintain a Top Ten Risk Item list?',
'Practical risk management':'Which day-to-day behaviors make project risk management effective?',
'Example: 5 people':'How many communication channels exist among five people?',
'Example: 10 people':'How many communication channels exist among ten people?',
'During the meeting':'What should happen during an effective project meeting?',
'After the meeting':'What should happen after an effective project meeting?',
'Factors to consider':'Which factors determine the best communication medium?',
'Communication tool selection':'Which communication tools fit routine, complex, urgent, sensitive, and reference information?',
'Email etiquette':'Which practices make project email clear and reliable?',
'Effective listening':'Which behaviors demonstrate effective listening?',
'Self-Determination Theory: Ryan and Deci':'How does Self-Determination Theory distinguish intrinsic and extrinsic motivation?',
"Maslow's Hierarchy of Needs":'How does Maslow organize human needs?',
"McGregor's Theory X and Theory Y":'How do Theory X and Theory Y make different assumptions about workers?',
"Ouchi's Theory Z":'What workplace assumptions define Theory Z?',
"Thamhain and Wilemon's nine influence bases":'What are Thamhain and Wilemon’s nine ways a project manager can influence people?',
"French and Raven's five bases of social power":'What are French and Raven’s five sources of social power?',
"Effectiveness: Covey's Seven Habits":'What are Covey’s Seven Habits of Highly Effective People?',
"Kurt Lewin's leadership styles":'How do autocratic, democratic, and laissez-faire leadership differ?',
'Six emotional leadership styles':'What are the six emotional leadership styles and their general purposes?',
'Leadership legacy styles':'What leadership legacies can a leader leave behind?',
'Emotional intelligence (EQ)':'What is emotional intelligence, and why does a project manager need it?',
'Important EQ-related abilities':'Which abilities make up emotional intelligence?',
'Personality and team development':'Why should a project manager adapt to different personalities?',
'Ways to develop a team':'Which actions help a project team develop?',
'Applying the theories':'How can a project manager match motivation theories to individual needs?',
'Common causes of project conflict':'What commonly causes conflict on projects?',
'Five common conflict management approaches':'What are the five approaches for handling project conflict?',
'Five team dysfunctions':'What are the five team dysfunctions, and how do they build on one another?',
'Communication and project success':'How can poor communication damage project performance?',
'Communication planning':'Which questions must a communications plan answer?',
'Communication barriers':'Which barriers can prevent a project message from being understood?',
'Profit formula':'How do you calculate profit?',
'Profit margin formula':'How do you calculate profit margin?',
'EVM formulas':'Which formulas calculate EVM cost and schedule performance?',
'EMV formula':'How do you calculate Expected Monetary Value?',
}

QUESTION_CONFIGS={
'Profit formula':{
 'distractors':['Profit = Revenue + Expenses','Profit = Expenses − Revenue','Profit = Revenue ÷ Expenses'],
 'teach':'Revenue is all income earned before costs are removed. Expenses are the costs paid to produce that income. Subtracting expenses shows the amount left over, which is profit.',
 'example':'If a project-related service earns $100,000 and costs $75,000, the profit is $100,000 − $75,000 = $25,000.'},
'Profit margin formula':{
 'distractors':['Profit margin = Profit − Revenue','Profit margin = Revenue ÷ Profit × 100%','Profit margin = Expenses ÷ Revenue × 100%'],
 'teach':'Profit margin changes the dollar profit into a percentage of revenue. Dividing by revenue answers: “Of every dollar earned, what portion remained as profit?” Multiplying by 100 converts the decimal to a percentage.',
 'example':'A $25,000 profit on $100,000 of revenue gives $25,000 ÷ $100,000 = 0.25, or a 25% profit margin.'},
'PERT estimate: Formula':{
 'distractors':['(Optimistic + Most likely + Pessimistic) ÷ 3','(Optimistic + Most likely + 4 × Pessimistic) ÷ 6','(4 × Optimistic + Most likely + Pessimistic) ÷ 6'],
 'teach':'PERT gives the most-likely estimate four times the weight of either extreme because the middle estimate represents the outcome the team expects most often. The six in the denominator is the total weight: 1 + 4 + 1.',
 'example':'For O=4, M=7, and P=16: (4 + 4×7 + 16) ÷ 6 = 48 ÷ 6 = 8 days.'},
'Slack formulas':{
 'distractors':['Total slack = ES − LS or EF − LF','Total slack = EF − ES','Total slack = LF + EF'],
 'teach':'Early dates show when work can occur as soon as possible. Late dates show the last time it can occur without delaying the project. The gap between the matching late and early dates is the available scheduling flexibility.',
 'example':'If ES=2 and LS=5, total slack is 5 − 2 = 3 days. The activity can start three days later without moving the project finish date.'},
'Communication channels: Formula':{
 'distractors':['n × (n − 1)','n² ÷ 2','n + (n − 1)'],
 'teach':'Each person could communicate with every other person, producing n(n−1) directional pairings. A relationship between Alex and Jordan is the same pair as Jordan and Alex, so dividing by two removes the duplicate count.',
 'example':'With 5 people: 5×4÷2 = 10 possible two-person communication channels.'},
'EMV formula':{
 'distractors':['EMV = Monetary outcome ÷ Probability','EMV = Probability + Monetary outcome','EMV = Highest possible outcome only'],
 'teach':'EMV weights each possible financial result by how likely it is. Multiplying probability by outcome gives that outcome’s probability-adjusted contribution; adding all contributions gives the average value expected across many similar decisions.',
 'example':'A 30% chance of losing $50,000 contributes 0.30×−$50,000 = −$15,000 to EMV.'},
'EVM formulas':{
 'distractors':['CV = AC − EV; SV = PV − EV; CPI = AC ÷ EV; SPI = PV ÷ EV','CV = EV − PV; SV = EV − AC; CPI = EV ÷ PV; SPI = EV ÷ AC','CV = EV + AC; SV = EV + PV; CPI = AC ÷ PV; SPI = PV ÷ AC'],
 'teach':'Cost measures compare earned work with what it actually cost, so CV and CPI use EV and AC. Schedule measures compare earned work with what should have been completed, so SV and SPI use EV and PV. Positive variances and indexes above 1 are favorable.',
 'example':'If EV=$80,000, AC=$100,000, and PV=$100,000, then CV=−$20,000, CPI=0.80, SV=−$20,000, and SPI=0.80: over budget and behind schedule.'},
'Four categories explaining WHY tasks are dependent':{
 'distractors':['Mandatory, discretionary, finish-to-start, and finish-to-finish','Internal, external, start-to-start, and start-to-finish','Optimistic, pessimistic, mandatory, and discretionary'],
 'teach':'The four categories answer why the relationship exists. Mandatory comes from the work itself, discretionary comes from a team preference, external crosses the project boundary, and internal stays within the team’s control. FS, SS, FF, and SF answer a different question: how the start and finish points connect.',
 'example':'Testing after coding is usually mandatory. Waiting for a government permit is external. Writing one report before another by preference is discretionary. A team-controlled review before its own release is internal.'},
'RACI definitions':{
 'distractors':['Responsible approves the final result; Accountable performs the work; Consulted receives updates; Informed gives expert input','Responsible and Accountable both only receive updates; Consulted performs the work; Informed approves it','Responsible provides optional advice; Accountable receives status reports; Consulted owns the result; Informed performs the work'],
 'teach':'RACI separates four different relationships to one task. Responsible identifies who does the work. Accountable identifies the single person who answers for the finished result. Consulted people participate through two-way input. Informed people receive one-way updates.',
 'example':'For a project report, an analyst may be Responsible, the project manager Accountable, a security specialist Consulted, and the sponsor Informed.'},
}

CHECK_CONFIGS={
'Product scope versus project scope':(['Product scope describes the work; project scope describes product features','Product scope and project scope both describe only the schedule','Product scope describes the budget; project scope describes only quality'], 'Product scope answers what the product must do. Project scope answers what work the team must perform to create that product. Keeping them separate prevents a feature list from being mistaken for the full implementation effort.', 'A registration dashboard is product scope. Designing, coding, testing, documenting, and training people to use it are project scope.'),
'Five scope documents':(['Work Breakdown Structure (WBS)','Scope statement','Requirements management plan'], 'The RTM creates a row for each requirement and follows it through its source, implementation, testing, and status. That trace lets the team prove that no approved requirement disappeared or remained unverified.', 'If requirement R-17 calls for confirmation email, its RTM row can link the stakeholder request to the feature, test case, owner, and acceptance result.'),
'WBS wording':(['WBS deliverable: Prepare training materials; activity: Training materials','WBS deliverable: Conduct testing; activity: Testing','WBS deliverable: Create documentation; activity: Documentation'], 'A WBS names the outputs the project must produce, so its labels normally use nouns. A schedule names the actions that produce those outputs, so activities normally begin with verbs.', '“Training materials” names an output. “Prepare training materials” names the work performed to create it.'),
'Scope creep':(['Add the feature immediately because a stakeholder requested it','Reject every change without recording it','Ask the team to fit it in without changing schedule or cost'], 'A request becomes scope creep only when it enters the project without controlled evaluation and approval. Change control makes the tradeoffs visible before anyone commits the team.', 'A two-week feature may also require testing, documentation, training, and support. The decision maker needs those effects before approving it.'),
'Dependency type':(['Start-to-start (SS)','Finish-to-finish (FF)','Start-to-finish (SF)'], 'Finish-to-start connects a predecessor’s finish to a successor’s start. Coding is the predecessor, and testing is the successor, so testing waits for coding to finish.', 'Washing a car must finish before drying can start.'),
'Critical path':(['Only that activity becomes late; the project finish never changes','The project automatically gains two days of slack','All noncritical activities must also slip two days'], 'A zero-slack activity has no unused schedule flexibility. A delay therefore passes directly to the project finish unless the team shortens later critical work or changes the network.', 'If the critical path finishes Friday and one critical task slips to Monday, the project also moves to Monday unless time is recovered.'),
'PERT':(['7 days','9 days','10 days'], 'PERT weights the most-likely value four times: (4 + 4×7 + 16) ÷ 6 = 48 ÷ 6 = 8. A simple average would ignore the intended weighting.', 'The weights are 1, 4, and 1, so the denominator is six.'),
'Effort and duration':(['8 hours of effort and 2 days of duration','16 hours of effort and 2 days of duration','8 hours of effort and 1 day of duration'], 'Effort adds every person’s labor hours. Duration measures elapsed calendar time. Two people working simultaneously contribute 8+8=16 labor hours while only one day passes.', 'Parallel work can reduce duration without reducing total effort.'),
'Profit margin':(['$25,000 profit and 33.3% profit margin','$75,000 profit and 25% profit margin','$25,000 profit and 75% profit margin'], 'Profit is revenue minus cost: $100,000−$75,000=$25,000. Margin divides that profit by revenue: $25,000÷$100,000=0.25=25%.', 'Margin always uses revenue as the denominator, not expenses.'),
'EVM cost':(['CV = $20,000 and CPI = 1.25','CV = −$20,000 and CPI = 1.25','CV = $20,000 and CPI = 0.80'], 'Cost variance compares earned value with actual cost: 80,000−100,000=−20,000. CPI uses the same two values as a ratio: 80,000÷100,000=0.80. Both results show cost inefficiency.', 'A negative CV and CPI below 1 mean the project paid more than the value of work it earned.'),
'EVM schedule':(['SV = $20,000 and SPI = 1.25','SV = −$20,000 and SPI = 1.25','SV = $20,000 and SPI = 0.80'], 'Schedule variance compares earned value with planned value: 80,000−100,000=−20,000. SPI is 80,000÷100,000=0.80. The team completed only 80% of the value planned by this point.', 'A negative SV and SPI below 1 indicate that the project is behind schedule.'),
'RACI accountability':(['Several people should be Accountable so ownership is shared','No one should be Accountable until the deliverable is complete','The Responsible worker must always be the only Accountable person'], 'RACI separates doing the work from answering for its final result. Several people can be Responsible for tasks, but one Accountable owner prevents conflicting approvals and uncertainty about who makes the final decision.', 'Two analysts may prepare a report, while one project sponsor is Accountable for accepting it.'),
'Resource leveling':(['Adds more work to fill every unused hour','Removes the activity from the project scope','Keeps every date fixed even when capacity is insufficient'], 'Leveling compares assigned work with actual capacity. When demand exceeds capacity, the schedule moves work, changes sequencing, or assigns another available resource. The finish date can change because resource limits are real constraints.', 'A person with 16 hours assigned in an 8-hour day needs work moved, split, or reassigned.'),
'Risk versus issue':(['An issue, because a supplier is involved','A completed response, because the event is known','A positive opportunity, because delivery has not occurred'], '“Might miss” describes uncertainty, so the event is still a risk. It becomes an issue only after the supplier actually misses the delivery date.', 'Risks receive planned responses and triggers. Issues require immediate resolution and tracking in an issue log.'),
'EMV':(['$15,000','−$50,000','−$150,000'], 'A threat uses a negative monetary outcome. Multiply 0.30 by −$50,000 to get −$15,000. EMV expresses the probability-weighted financial effect, not the worst-case loss itself.', 'Across many similar decisions, a 30% chance of losing $50,000 averages to an expected loss of $15,000 per decision.'),
'Threat responses':(['Mitigate','Transfer','Accept'], 'Avoidance changes the plan so the threat cannot occur or cannot affect the objective. Mitigation only lowers probability or impact, transfer shifts ownership, and acceptance leaves the risk in place.', 'Choosing a proven technology instead of an unstable experimental one may remove a technical threat entirely.'),
'Opportunity responses':(['Enhance','Share','Accept'], 'Exploit takes action to make an opportunity happen, rather than merely increasing its probability. Enhance improves the chance or benefit, share involves another party, and accept waits without proactive action.', 'Assigning the best available specialist to guarantee an early-completion opportunity is exploitation.'),
'Communication channels':(['40','50','90'], 'The formula counts unique pairs: 10×9÷2=45. Multiplying by nine counts every person’s relationships, and dividing by two removes duplicate pairs.', 'Alex-to-Jordan and Jordan-to-Alex represent one relationship, not two separate channels.'),
'Push/pull/interactive':(['Push communication','Pull communication','Broadcast-only communication'], 'A live meeting allows participants to send, receive, question, and clarify in real time, so it is interactive. Push sends information one way, while pull requires recipients to retrieve stored information.', 'Email is normally push; a knowledge base is pull; a video conversation is interactive.'),
'Herzberg':(['Hygiene factors create lasting motivation; motivators only prevent dissatisfaction','All employee needs belong to one identical category','Pay is the only factor capable of changing satisfaction'], 'Herzberg separates the conditions that prevent dissatisfaction from the factors that make work satisfying. Fixing poor pay or unsafe conditions removes complaints, while achievement, recognition, responsibility, and growth create motivation.', 'A fair policy may stop frustration; meaningful responsibility can make the work motivating.'),
'Power':(['Legitimate power','Reward power','Referent power'], 'Expert power comes from trusted knowledge or skill. Legitimate power comes from position, reward power from control of benefits, and referent power from admiration or identification.', 'A security architect may influence a decision because the team trusts her technical expertise even when she is not the manager.'),
'Tuckman':(['Forming','Norming','Performing'], 'Storming occurs when team members challenge roles, priorities, authority, or working methods. The disagreement can be productive if the team resolves it and moves into shared norms.', 'A newly assembled team is forming; a team debating who decides and how work should happen is storming.'),
'Conflict':(['Forcing or directing','Withdrawing or avoiding','Smoothing or accommodating'], 'Collaborating investigates the needs beneath each position and searches for a solution that satisfies both sides. It takes more effort than forcing or avoiding but is best suited to an important conflict requiring a durable outcome.', 'Two teams needing the same specialist can redesign timing and responsibilities so both critical needs are met.'),
}

TEACH_OVERRIDES={
'Chapter 4 overview':'Scope planning gives the team a shared boundary. Without that boundary, different people can expect different deliverables, making schedule and cost estimates unreliable and allowing unapproved work to enter the project.',
'Schedule management plan':'The plan sets the rules for building and controlling the schedule. The Gantt chart is the schedule display itself. One governs the process; the other shows activities across time.',
'Learning curve theory':'Repeated work often becomes faster because people improve their method, remember prior solutions, and make fewer mistakes. Estimates for later units can therefore be lower than estimates for the first unit.',
'Cradle-to-grave analysis':'A purchase can create costs long after acquisition. Counting operation, maintenance, support, retirement, and disposal prevents a cheap initial option from appearing less expensive than it truly is.',
'Cost management plan':'This plan defines how the team will estimate, measure, report, and control money. It creates consistent rules before the team begins comparing planned and actual costs.',
'Cost estimate':'An estimate predicts how much resources or work will cost using the information currently available. It includes assumptions and uncertainty and can change as the project becomes clearer.',
'Cost baseline':'The baseline spreads the approved budget across time. That time-phased plan lets the manager compare how much the project planned to spend by a date with how much value and cost actually occurred.',
'Black swan event':'A black swan is difficult to predict yet produces extreme consequences. Ordinary contingency planning may not name the event, so resilient projects also preserve management flexibility and reserves for unexpected disruption.',
'11. Expected Monetary Value (EMV) analysis':'EMV does not promise that an outcome will equal the calculated number. It provides a probability-weighted average that helps compare risky options on a consistent financial basis.',
'Risk management plan':'This plan defines the project’s risk process before individual risks are handled. A risk register stores the individual risks; the plan explains how the team will find, score, respond to, and monitor them.',
'Contingency reserve':'Contingency reserve covers identified uncertainty that the team can partly anticipate. Because it supports known risks in planned work, it belongs inside the cost baseline.',
'Management reserve':'Management reserve protects against unforeseen work that cannot be tied to a known risk. It sits outside the cost baseline so using it requires management control rather than routine activity spending.',
'Inherent risk':'Inherent risk measures exposure before a response. Comparing it with residual risk after controls shows how much the response reduced the original threat or opportunity.',
'Top Ten Risk Item Tracking':'Focusing regular reviews on the most important risks keeps limited management attention on exposures that could affect the project most. The list changes as probability, impact, and triggers change.',
'Risk-related project management advice':'Risk management works only when it changes decisions and actions. Assigning owners, monitoring triggers, funding responses, and updating the register turns a list of worries into active control.',
'Example: 10 people':'Team size creates relationships faster than it creates people. Ten people have 45 unique pairs, which explains why adding staff increases coordination work rather than adding only productive capacity.',
"Brooks' Law":'New staff initially consume experienced staff time for onboarding and create more communication paths. On a late software project, that short-term coordination cost can exceed the new people’s immediate contribution.',
'During the meeting':'The facilitator keeps discussion tied to the agenda, confirms decisions, and records actions with owners and dates. This turns conversation into accountable project work.',
'Factors to consider':'A communication medium must fit the message. Sensitive or complicated issues need quick feedback and richer interaction, while routine information may need a durable written record that people can retrieve later.',
'Project management application':'Motivation theories are useful only when connected to a person’s situation. A manager first identifies the unmet need or work condition, then chooses an action such as autonomy, recognition, clearer expectations, or skill development.',
"Ouchi's Theory Z":'Theory Z assumes that trust, long-term relationships, shared responsibility, and collective decisions can strengthen commitment. It contrasts with managing mainly through close control or individual rewards.',
'Controlling AI costs':'AI spending becomes wasteful when teams choose expensive models by habit, let automated agents run without limits, repeat uncached work, or fail to match the tool to the task. Monitoring cost per completed task exposes whether spending creates useful output.',
'Emotional intelligence (EQ)':'A project manager regularly works through disagreement, pressure, and uncertainty. Recognizing emotions and regulating reactions helps the manager listen accurately, respond deliberately, and preserve working relationships.',
'Personality and team development':'People differ in communication, decision making, pace, and response to conflict. Discussing those differences helps the team design working agreements instead of treating every difference as poor performance.',
'Ways to develop a team':'Training improves capability, while coaching, team-building, clear norms, and prompt conflict resolution improve how people use those capabilities together. Development addresses both skill and collaboration.',
'Common causes of project conflict':'Projects combine limited resources, interdependent work, deadlines, and people with different priorities. Conflict becomes easier to solve when the team identifies the underlying cause instead of arguing only about positions.',
'Five team dysfunctions':'The dysfunctions build on one another. Low trust discourages honest disagreement, weak discussion reduces commitment, weak commitment undermines accountability, and poor accountability shifts attention away from team results.',
}

VOCAB_TEACH_OVERRIDES={
'Decomposition':'A project manager begins with a large deliverable and divides it until each work package is small enough to estimate, assign, monitor, and control. The point is to make large scope manageable without losing its relationship to the whole project.',
"Murphy's Law":'The law reminds managers to plan for uncertainty instead of assuming ideal conditions. Risk reviews, buffers, backups, and contingency plans reduce the damage when foreseeable problems occur.',
'Top-down / analogous':'This method starts with the cost or duration of a similar past project and adjusts for differences. It is fast when little detail exists, but it is usually less precise than estimating every component.',
'Effort vs. duration':'Effort adds all labor hours, while duration measures calendar time. Two people can complete 16 hours of effort in one eight-hour day when they work in parallel.',
'Avoid':'Avoidance changes the plan so a threat can no longer affect the project. Mitigation leaves the threat in place but reduces its probability or impact.',
'Exploit':'Exploitation commits resources to make a beneficial uncertain event occur. Enhancement only increases the chance or value of the opportunity without guaranteeing it.',
'1. Be proactive':'Being proactive means acting on factors you can influence before circumstances force a response. In a project, that includes raising a risk early and preparing a response instead of waiting for failure.',
}

def clean_heading(s): return re.sub(r'\*\*','',s).strip().strip('#').strip()
def plain_math(s):
    s=s.replace('\\\\[',' ').replace('\\\\]',' ').replace('\\[',' ').replace('\\]',' ')
    s=re.sub(r'\\boxed\{([^{}]*)\}',r'\1',s)
    s=re.sub(r'\\text\{([^{}]*)\}',r'\1',s)
    # The supplied guide uses simple fractions; repeat so inner text replacements settle first.
    for _ in range(3): s=re.sub(r'\\frac\{([^{}]*)\}\{([^{}]*)\}',r'(\1) ÷ (\2)',s)
    s=s.replace('\\times','×').replace('\\sum','Σ').replace('\\sigma','σ').replace('\\qquad','; ').replace('boxed','')
    s=s.replace('\\(','').replace('\\)','')
    s=s.replace('\\,',' ').replace('\\','')
    s=s.replace('{','').replace('}','')
    s=re.sub(r'\s*=\s*',' = ',s)
    return re.sub(r'\s+',' ',s).strip()
def strip_md(s):
    s=plain_math(s)
    s=re.sub(r'!\[[^]]*\]\([^)]*\)','',s); s=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',s)
    s=re.sub(r'[`*_>#]','',s); s=re.sub(r'\s+',' ',s)
    return s.strip()
def inline(s):
    s=html.escape(plain_math(s.strip()))
    s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
    s=re.sub(r'\*([^*]+)\*',r'<em>\1</em>',s)
    return s
def markdown_html(md):
    lines=md.splitlines(); out=[]; i=0; para=[]
    def flush():
        if para: out.append('<p>'+inline(' '.join(x.strip() for x in para))+'</p>'); para.clear()
    while i<len(lines):
        line=lines[i]
        if not line.strip(): flush(); i+=1; continue
        if re.match(r'^\s*\\\\?\[',line):
            flush(); out.append('<div class="formula">'+html.escape(plain_math(line))+'</div>'); i+=1; continue
        if line.startswith('|') and i+1<len(lines) and re.match(r'^\s*\|?\s*:?-+',lines[i+1]):
            flush(); rows=[]
            while i<len(lines) and lines[i].lstrip().startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')]); i+=1
            if len(rows)>1:
                out.append('<div class="note-table"><table><thead><tr>'+''.join('<th>'+inline(c)+'</th>' for c in rows[0])+'</tr></thead><tbody>')
                for row in rows[2:]: out.append('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in row)+'</tr>')
                out.append('</tbody></table></div>')
            continue
        m=re.match(r'^(#{2,5})\s+(.*)',line)
        if m: flush(); level=min(4,len(m.group(1))); out.append(f'<h{level}>{inline(clean_heading(m.group(2)))}</h{level}>'); i+=1; continue
        if re.match(r'^[-*]\s+',line):
            flush(); out.append('<ul>')
            while i<len(lines) and re.match(r'^[-*]\s+',lines[i]): out.append('<li>'+inline(re.sub(r'^[-*]\s+','',lines[i]))+'</li>'); i+=1
            out.append('</ul>'); continue
        if re.match(r'^\d+[.)]\s+',line):
            flush(); out.append('<ol>')
            while i<len(lines) and re.match(r'^\d+[.)]\s+',lines[i]): out.append('<li>'+inline(re.sub(r'^\d+[.)]\s+','',lines[i]))+'</li>'); i+=1
            out.append('</ol>'); continue
        para.append(line); i+=1
    flush(); return ''.join(out)

def chapter_text(all_text,ch):
    start=re.search(rf'^# \*\*Chapter {ch}:.*$',all_text,re.M).end()
    nxt=re.search(rf'^# \*\*Chapter {ch+1}:.*$',all_text[start:],re.M) if ch<7 else re.search(r'^# \*\*Final Exam Review',all_text[start:],re.M)
    return all_text[start:start+(nxt.start() if nxt else len(all_text))]

def split_h2(md):
    matches=list(re.finditer(r'^## \*\*(.+?)\*\*\s*$',md,re.M)); out=[]
    for j,m in enumerate(matches): out.append((clean_heading(m.group(1)),md[m.end():matches[j+1].start() if j+1<len(matches) else len(md)]))
    return out

def heading_blocks(md):
    """Return every meaningful H2-H4 block while retaining its parent objective/topic."""
    matches=list(re.finditer(r'^(#{2,4})\s+\*\*(.+?)\*\*\s*$',md,re.M)); out=[]; stack={}
    for i,m in enumerate(matches):
        level=len(m.group(1)); title=clean_heading(m.group(2))
        end=len(md)
        for nxt in matches[i+1:]:
            if len(nxt.group(1))<=level:
                end=nxt.start(); break
        for old in list(stack):
            if old>=level: del stack[old]
        parent=stack.get(level-1) or stack.get(2)
        stack[level]=title
        if title.startswith('Part ') or title=='Practice calculator' or re.fullmatch(r'[\d/]+',title): continue
        if title in {'Chapter 6: Vocabulary summary','Chapter 7: Complete vocabulary summary'}: continue
        out.append(dict(level=level,title=title,parent=parent,body=md[m.end():end]))
    return out

def table_summary(md):
    lines=md.splitlines(); result=[]; i=0
    while i<len(lines)-2:
        if lines[i].lstrip().startswith('|') and re.match(r'^\s*\|?\s*:?-+',lines[i+1]):
            i+=2
            while i<len(lines) and lines[i].lstrip().startswith('|') and len(result)<3:
                cells=[strip_md(c) for c in lines[i].strip().strip('|').split('|')]
                if len(cells)>=2 and cells[0] and cells[1]: result.append(f'{cells[0]}: {cells[1]}')
                i+=1
            if result: return '; '.join(result)
        i+=1
    return ''

def first_answer(md,title):
    """Build a concrete answer from the source instead of a generic placeholder."""
    if title in TOPIC_ANSWERS: return TOPIC_ANSWERS[title]
    candidates=[]
    for p in re.split(r'\n\s*\n',md):
        t=strip_md(p)
        if t and not t.startswith('|') and len(t)>15:
            t=re.sub(r'^[-*]\s*','',t)
            candidates.append(t)
    answer=next((x for x in candidates if len(x)>=40 and not re.match(r'^(example|exam tip|remember|your professor|imagine|the following|these categories|this distinction|the slides|your slides)',x,re.I)),None)
    answer=answer or table_summary(md) or (candidates[0] if candidates else '')
    if not answer:
        raise ValueError(f'No answerable source content for lesson: {title}')
    if len(answer)>520:
        answer=answer[:517].rsplit(' ',1)[0]+'…'
    return answer

def display_title(title,parent):
    generic={'Formula','Example','Examples','Causes','Methods','Types','The five levels','Key distinction','Key distinctions','Worked example','Your professor\'s example','Another example','Practice calculator'}
    title=re.sub(r'^(?:\d+\.|[A-G]\.)\s*','',title)
    title={'Your professor\'s EMV example':'EMV worked example','Additional AI cost-management discussion':'Controlling AI costs','Email etiquette from your slides':'Email etiquette','Risk-related project management advice':'Practical risk management'}.get(title,title)
    if title in generic and parent:
        parent=re.sub(r'^(?:Objective|Cost objective) \d+:\s*','',parent)
        parent=re.sub(r'^(?:\d+\.|[A-G]\.)\s*','',parent)
        parent=re.sub(r'^(?:Explain how to|List methods for|Calculate (?:a|the)|Conduct|Differentiate|Prepare|Identify|Compare)\s+','',parent,flags=re.I)
        if 'scope creep' in parent.lower(): parent='Scope creep'
        if 'communication channels' in parent.lower(): parent='Communication channels'
        parent=parent[:1].upper()+parent[1:]
        return f'{parent}: {title}'
    return title

def lesson_question(lesson):
    title=lesson['title']; low=title.lower()
    if title in QUESTION_OVERRIDES: return QUESTION_OVERRIDES[title]
    if lesson['kind']=='overview': return f'What is the main focus of Chapter {lesson["section"]}?'
    if lesson['kind']=='objective': return f'What must you know for {title.lower()}?'
    if re.match(r'^(what|why|how|when|which)\b',title,re.I): return title.rstrip('?')+'?'
    if ' versus ' in low or ' vs. ' in low or ' vs ' in low:
        pair=re.sub(r'\s+(?:versus|vs\.)\s+',' and ',title,flags=re.I)
        return f'What is the difference between {pair}?'
    if low.startswith(('methods of ','ways to ','types of ','steps ','major ')):
        return f'Which items belong to {title.lower()}?'
    if any(word in low for word in ('formula','calculation','estimate')):
        return f'How is {title.lower()} calculated or used?'
    if low.endswith((' plan',' matrix',' chart',' register',' statement',' structure',' analysis',' theory',' model',' method',' grid',' law',' baseline',' histogram',' list',' attributes',' criteria',' card',' cards',' management',' communication',' communications')):
        return f'What is the purpose of {title}?'
    if low.endswith('s') and not low.endswith(('analysis','process')): return f'What are {title}?'
    return f'What is {title}?'

def is_practice_lesson(lesson):
    if lesson['kind'] in {'overview','objective'}: return False
    low=lesson['title'].lower()
    grouped=('terms to know','vocabulary','critical distinctions','memorize the differences','basic financial vocabulary','meeting vocabulary','examples','raci example','project management application')
    aggregators={'motivation theories','theories of influence and power','leadership styles','general leadership styles','motivation theory comparison','emotional intelligence and personality','communication channels reference table'}
    return not any(label in low for label in grouped) and low not in aggregators

def prose_terms(md):
    found=[]
    skip={'example','exam distinction','exam tip','important distinction','answer','remember','important','relationship to the project charter'}
    for line in md.splitlines():
        line=line.strip()
        patterns=[
          r'^\*\*([^*]{2,100}?):\*\*\s*(.+)$',
          r'^\*\*([^*]{2,80}?)\*\*\s+(?:is|are|means|refers to)\s+(.+)$',
          r'^\*\*([^*]{2,80}?)\s+(?:is|are|means)\s+([^*]+?)\.?\*\*\s*$',
        ]
        match=next((re.match(pattern,line,re.I) for pattern in patterns if re.match(pattern,line,re.I)),None)
        if not match: continue
        term=strip_md(match.group(1)).rstrip(':').strip(); definition=strip_md(match.group(2)).strip().rstrip('.')
        if term.lower() in skip or len(term)<2 or len(definition)<5: continue
        found.append((term,definition))
    return found

def is_vocab_title(title):
    low=title.lower()
    blocked=('objective ','chapter ','overview','example','questions ','methods ','ways ','steps ','factors ','common causes','potential sources','how ','why ','what ','memorize','terms to know','vocabulary','critical distinctions','worked example','formula')
    return not any(low.startswith(x) for x in blocked) and ':' not in title[:3]

def source_facts(md):
    facts=[]
    for block in re.split(r'\n\s*\n',md):
        value=strip_md(block)
        if not value or value.startswith('|') or len(value)<25: continue
        if re.match(r'^(your professor|your slides|the slides|this chapter|this section|exam tip|remember)',value,re.I): continue
        facts.append(value)
    # Table rows often contain the clearest contrast or application.
    lines=md.splitlines(); i=0
    while i<len(lines)-2:
        if lines[i].lstrip().startswith('|') and re.match(r'^\s*\|?\s*:?-+',lines[i+1]):
            i+=2
            while i<len(lines) and lines[i].lstrip().startswith('|'):
                cells=[strip_md(c) for c in lines[i].strip().strip('|').split('|')]
                if len(cells)>=2 and cells[0] and cells[1]: facts.append(f'{cells[0]} means {cells[1]}.')
                i+=1
            continue
        i+=1
    result=[]
    for fact in facts:
        if fact not in result: result.append(fact)
    return result

def lesson_explanation(lesson,lessons):
    config=QUESTION_CONFIGS.get(lesson['title'])
    if config: return config['teach']
    if lesson['title'] in TEACH_OVERRIDES: return TEACH_OVERRIDES[lesson['title']]
    answer=re.sub(r'\W+',' ',lesson['summary'].lower()).strip()
    candidates=[]
    for fact in source_facts(lesson['raw']):
        normalized=re.sub(r'\W+',' ',fact.lower()).strip()
        if normalized==answer or normalized in answer or answer in normalized: continue
        if fact.startswith(('\\[','Profit =','Profit margin =')): continue
        candidates.append(fact)
    if candidates:
        preferred=next((x for x in candidates if re.search(r'\b(because|so that|helps|allows|ensures|instead|while|without|when|example|means)\b',x,re.I)),candidates[0])
        return preferred[:700]
    siblings=[x for x in lessons if x['section']==lesson['section'] and x['parent']==lesson['parent'] and x['id']!=lesson['id']]
    if siblings:
        other=siblings[0]
        return f'Use this concept within {lesson["parent"]}. Keep it separate from {other["title"]}: {other["summary"]}'[:700]
    return f'This concept supports the chapter goal of {CHAPTERS[lesson["section"]][1].lower()} Use it to identify the specific decision, document, calculation, or behavior named in the question.'

def lesson_example(lesson):
    config=QUESTION_CONFIGS.get(lesson['title'])
    if config: return config['example']
    raw=lesson['raw']
    match=re.search(r'(?m)^(?:\*\*)?(?:Example|For example)(?:\*\*)?:?\s*(.+?)(?=\n\s*\n|\n#{2,4}|$)',raw,re.I|re.S)
    if match:
        value=strip_md(match.group(1))
        if value: return value[:500]
    return ''

def rows_from_tables(md,ch):
    rows=[]; lines=md.splitlines(); i=0; group=0
    allowed={'term','document','type','method','approach','letter','component','category','abbreviation','law','symbol','reserve','technique','metric',"don't confuse",'level','preference','strategy','need','theory','influence base','power','habit','style','term a','name'}
    definition_priority=['definition','meaning','explanation','main concept','key difference','associated theory or model','general focus','role','purpose','formula','estimate']
    while i<len(lines)-2:
        if lines[i].lstrip().startswith('|') and re.match(r'^\s*\|?\s*:?-+',lines[i+1]):
            group+=1
            head=[strip_md(c) for c in lines[i].strip().strip('|').split('|')]; lower=[x.lower() for x in head]; data=[]; i+=2
            while i<len(lines) and lines[i].lstrip().startswith('|'):
                data.append([strip_md(c) for c in lines[i].strip().strip('|').split('|')]); i+=1
            if len(head)>=2 and lower[0] in allowed:
                for r in data:
                    if not r or not r[0]: continue
                    if lower[0]=='term a' and len(r)>=3:
                        term=f'{r[0]} versus {r[1]}'; definition=r[2]
                    else:
                        idx=next((lower.index(label) for label in definition_priority if label in lower),1)
                        if idx>=len(r): continue
                        term=r[0]; definition=r[idx]
                        if lower[0]=='metric' and 'interpretation' in lower and lower.index('interpretation')<len(r): definition+=f'; {r[lower.index("interpretation")]}'
                        elif lower[0] in {'letter','symbol','theory','need'} and len(r)>idx+1 and r[idx+1]: definition+=f' — {r[idx+1]}'
                    if term and definition and len(term)<=120 and 2<len(definition)<=700: rows.append((ch,group,term,definition))
            continue
        i+=1
    return rows

def choice_set(correct,pool):
    vals=[]
    for v in pool:
        if v!=correct and v not in vals: vals.append(v)
    while len(vals)<3: vals.append(f'An unrelated project concept {len(vals)+1}')
    return vals[:3]

def title_tokens(title):
    stop={'what','is','a','the','of','and','or','to','for','how','why','objective','cost','project','management','formula','example'}
    return {w for w in re.findall(r'[a-z0-9]+',title.lower()) if w not in stop and len(w)>2}

def lesson_distractors(lesson,lessons):
    config=QUESTION_CONFIGS.get(lesson['title'])
    if config: return config['distractors']
    wanted=title_tokens(lesson['title'])
    candidates=[]
    for other in lessons:
        if other['id']==lesson['id'] or other['section']!=lesson['section'] or other['summary']==lesson['summary']: continue
        shared=len(wanted & title_tokens(other['title']))
        distance=abs(other['number']-lesson['number'])
        score=(12 if other['parent']==lesson['parent'] else 0)+(3 if other['kind']==lesson['kind'] else 0)+(5*shared)+max(0,8-distance/2)
        score-=abs(len(other['summary'])-len(lesson['summary']))/150
        candidates.append((score,other['number'],other['summary']))
    candidates.sort(key=lambda x:(-x[0],x[1]))
    return choice_set(lesson['summary'],[x[2] for x in candidates])

def main():
    text=SOURCE.read_text(); lessons=[]; number=1; chapter_sources={}
    for ch in CHAPTERS:
        md=chapter_text(text,ch); chapter_sources[ch]=md
        intro=md[:re.search(r'^## ',md,re.M).start()]
        overview=CHAPTER_OVERVIEWS[ch]
        lessons.append(dict(id=f'464e2-l{number:03}',number=number,section=ch,kind='overview',title=f'Chapter {ch} overview',objective=f'Understand the purpose and exam focus of Chapter {ch}.',summary=overview,html=markdown_html(intro) or f'<p>{html.escape(overview)}</p>',raw=intro,parent=f'Chapter {ch}')); number+=1
        for block in heading_blocks(md):
            original=block['title']; body=block['body']
            is_objective=original.startswith(('Objective ','Cost objective '))
            # A heading with no explanatory source text is only a visual divider, not a lesson.
            if not is_objective and len(strip_md(body))<15 and not table_summary(body): continue
            title=display_title(original,block['parent'])
            summary=OBJECTIVE_ANSWERS[original] if is_objective else first_answer(body,title)
            objective=original.split(':',1)[1].strip() if is_objective else f'Explain {title} clearly and distinguish it from related concepts.'
            lessons.append(dict(id=f'464e2-l{number:03}',number=number,section=ch,kind='objective' if is_objective else 'topic',title=title,objective=objective,summary=summary,html=markdown_html(body),raw=body,parent=block['parent'] or f'Chapter {ch}')); number+=1
    # Every objective and granular topic receives a direct, answerable question.
    questions=[]
    for lesson in lessons:
        questions.append(dict(id='q-'+lesson['id'],number=lesson['number'],section=lesson['section'],source=lesson['number'],title=lesson['title'],q=lesson_question(lesson),correct=lesson['summary'],distractors=lesson_distractors(lesson,lessons),teach=lesson_explanation(lesson,lessons),answer=lesson['summary'],example=lesson_example(lesson),kind=lesson['kind'],practice=is_practice_lesson(lesson)))
    # Build the glossary from definition tables, bold prose definitions, and concrete lesson topics.
    # Worked examples and numeric tables remain practice material rather than pretending to be vocabulary.
    candidates=[]
    for ch in CHAPTERS:
        chapter_lessons=[l for l in lessons if l['section']==ch]
        for _,group,term,definition in rows_from_tables(chapter_sources[ch],ch):
            source=next((l for l in chapter_lessons if term.lower() in l['raw'].lower()),chapter_lessons[0])
            candidates.append(dict(section=ch,group=f'table-{group}',term=term,definition=definition,source=source))
        for term,definition in prose_terms(chapter_sources[ch]):
            source=next((l for l in chapter_lessons if term.lower() in l['raw'].lower()),chapter_lessons[0])
            candidates.append(dict(section=ch,group=f'lesson-{source["number"]}',term=term,definition=definition,source=source))
        for lesson in chapter_lessons:
            if lesson['kind']=='topic' and is_vocab_title(lesson['title']):
                candidates.append(dict(section=ch,group=f'parent-{lesson["parent"]}',term=lesson['title'],definition=lesson['summary'],source=lesson))
    seen=set(); unique=[]
    for item in candidates:
        key=(item['section'],item['term'].lower())
        if key in seen: continue
        seen.add(key); unique.append(item)
    vocab=[]
    for item in unique:
        ch,term,definition,source=item['section'],item['term'],item['definition'],item['source']
        peers=[x['definition'] for x in unique if x['section']==ch and x['group']==item['group'] and x['definition']!=definition]
        if len(peers)<3:
            nearby=sorted((x for x in unique if x['section']==ch and x['definition']!=definition),key=lambda x:abs(x['source']['number']-source['number']))
            peers.extend(x['definition'] for x in nearby if x['definition'] not in peers)
        teach=VOCAB_TEACH_OVERRIDES.get(term,lesson_explanation(source,lessons))
        vocab.append(dict(id=f'464e2-v{len(vocab)+1:03}',section=ch,source=source['number'],title=term,term=term,q=f'What does {term} mean?',correct=definition,distractors=choice_set(definition,peers),teach=teach,answer=definition,example=lesson_example(source)))
    checks=[
      (4,'Product scope versus project scope','Which statement correctly separates product scope from project scope?','Product scope describes product features; project scope describes the work required to create them'),
      (4,'Five scope documents','Which document checks whether every requirement is addressed from need through validation?','Requirements Traceability Matrix (RTM)'),
      (4,'WBS wording','Which pair follows the guide’s WBS-versus-activity naming rule?','WBS deliverable: Training materials; activity: Prepare training materials'),
      (4,'Scope creep','A stakeholder asks for an unplanned feature. What should happen first?','Document it and analyze scope, schedule, cost, resource, quality, and risk impacts through change control'),
      (5,'Dependency type','Testing can start only after coding finishes. Which relationship is this?','Finish-to-start (FS)'),
      (5,'Critical path','What normally happens if an activity on a zero-slack critical path slips by two days?','The project finish date slips unless another change recovers the time'),
      (5,'PERT','For O=4, M=7, and P=16, what is the PERT expected duration?','8 days'),
      (5,'Effort and duration','Two people each work 8 hours during one calendar day. What are effort and duration?','16 hours of effort and 1 day of duration'),
      (5,'Profit margin','Revenue is $100,000 and costs are $75,000. What are profit and profit margin?','$25,000 profit and 25% profit margin'),
      (5,'EVM cost','EV is $80,000 and AC is $100,000. What are CV and CPI?','CV = −$20,000 and CPI = 0.80'),
      (5,'EVM schedule','EV is $80,000 and PV is $100,000. What are SV and SPI?','SV = −$20,000 and SPI = 0.80'),
      (6,'RACI accountability','Why should only one person be Accountable for a deliverable?','One final owner prevents ambiguity about who answers for completion and approval'),
      (6,'Resource leveling','A specialist is assigned 16 hours of work on the same day. What does leveling do?','Moves or delays work to fit capacity, possibly changing the critical path or finish date'),
      (6,'Risk versus issue','A supplier might miss a future delivery date. What is this now?','A risk, because the uncertain event has not happened yet'),
      (6,'EMV','A 30% threat would cost $50,000. What is its EMV?','−$15,000'),
      (6,'Threat responses','Which response removes the cause of a threat or changes the plan so it cannot affect the project?','Avoid'),
      (6,'Opportunity responses','Which response acts to ensure a positive risk occurs?','Exploit'),
      (7,'Communication channels','How many potential communication channels exist among 10 people?','45'),
      (7,'Push/pull/interactive','A live video meeting with immediate questions and answers uses which method?','Interactive communication'),
      (7,'Herzberg','Which statement matches Herzberg’s theory?','Hygiene factors prevent dissatisfaction; motivators create satisfaction and growth'),
      (7,'Power','Influence based on specialized knowledge is which French and Raven power base?','Expert power'),
      (7,'Tuckman','A team is openly disagreeing about roles and methods. Which stage is this?','Storming'),
      (7,'Conflict','Which conflict approach seeks a win-win solution by addressing underlying needs?','Collaborating or problem solving'),
    ]
    check_items=[]
    for i,(ch,title,q,correct) in enumerate(checks,1):
        distractors,teach,example=CHECK_CONFIGS[title]
        check_items.append(dict(id=f'464e2-c{i:02}',section=ch,source=next(l['number'] for l in lessons if l['section']==ch),title=title,q=q,correct=correct,distractors=distractors,teach=teach,answer=correct,example=example))
    cloze=[
      (4,'Product ____ describes features; project ____ describes the work required to create them.',['scope','scope']),
      (4,'A WBS uses ____ for deliverables; schedule activities normally use ____.',['nouns','verbs']),
      (5,'PERT expected time = (____ + 4×____ + ____) ÷ 6.',['optimistic','most likely','pessimistic']),
      (5,'Cost variance = ____ − AC; schedule variance = EV − ____.',['EV','PV']),
      (6,'RACI means ____, Accountable, Consulted, and Informed.',['Responsible']),
      (6,'A future uncertain event is a ____; a problem that has happened is an ____.',['risk','issue']),
      (7,'Communication channels for n people = n(n−1) ÷ ____.',['2']),
      (7,'Tuckman: Forming → ____ → Norming → Performing → Adjourning.',['Storming']),
    ]
    cloze_teach=[
      ('Product scope names the product’s features. Project scope names the labor and processes needed to create those features.','A dashboard can be product scope; designing, coding, and testing it are project scope.'),
      ('A WBS describes outputs, so nouns keep attention on what must exist. A schedule describes actions, so verbs show what the team must do.','“Test report” is a WBS deliverable; “prepare test report” is an activity.'),
      ('PERT uses one optimistic estimate, four copies of the most-likely estimate, and one pessimistic estimate. The denominator six equals the total weighting.','For 4, 7, and 16 days: (4+28+16)÷6=8 days.'),
      ('Cost performance compares earned value with actual cost, while schedule performance compares earned value with planned value. That is why AC appears in CV and PV appears in SV.','EV=80, AC=100 gives a negative cost variance; EV=80, PV=100 gives a negative schedule variance.'),
      ('Responsible identifies who performs the work. Accountable identifies the one person who gives final approval and answers for the result. Consulted people provide input, and Informed people receive updates.','Several developers may be Responsible, but one product owner can remain Accountable.'),
      ('Uncertainty separates a risk from an issue. A risk may happen, so the team prepares a response; an issue has happened, so the team must resolve it.','“The server might fail” is a risk. “The server failed” is an issue.'),
      ('The formula begins with every person’s possible relationships, then divides by two because each pair would otherwise be counted twice.','Five people create 5×4÷2=10 channels.'),
      ('Teams often disagree while establishing roles and methods. Resolving that storming stage allows shared norms to form before the team performs effectively.','A team arguing over decision authority is storming, not yet norming.'),
    ]
    cloze_items=[]
    for i,(ch,q,ans) in enumerate(cloze,1):
        teach,example=cloze_teach[i-1]
        cloze_items.append(dict(id=f'464e2-b{i:02}',section=ch,source=next(l['number'] for l in lessons if l['section']==ch),title='Build the relationship',q=q,correct='; '.join(ans),distractors=['schedule','cost','manager'],teach=teach,answer='; '.join(ans),example=example,kind='cloze'))
    sorts=[
      (4,'Scope management flow',['Collect and validate requirements','Write the detailed scope statement','Create the WBS and scope baseline','Validate completed deliverables','Control requested scope changes']),
      (5,'Schedule development',['Define activities','Sequence activities','Estimate resources and durations','Build the network and find the critical path','Develop and baseline the schedule']),
      (5,'Forward-pass logic',['Start at time zero','Calculate earliest start','Add duration for earliest finish','Use the largest predecessor finish at a merge','Continue to project completion']),
      (6,'Risk process',['Plan risk management','Identify risks','Analyze probability and impact','Plan and assign responses','Implement and monitor responses']),
      (7,'Tuckman team development',['Forming','Storming','Norming','Performing','Adjourning']),
      (7,'Effective meeting',['Define purpose and needed participants','Send agenda and prework','Facilitate discussion and decisions','Assign actions, owners, and due dates','Distribute minutes and follow up']),
    ]
    sort_teach=[
      'Requirements establish the need. The scope statement defines the boundary, the WBS organizes deliverables, validation checks the finished work, and change control protects the approved baseline.',
      'Each scheduling step needs information produced by the previous step: activities must exist before sequencing, and sequence plus duration estimates are required before finding the critical path.',
      'A forward pass moves from the beginning toward completion. At a merge, the successor must wait for every predecessor, so it uses the largest predecessor finish.',
      'Risk work is cyclical: the team defines the process, finds uncertainty, prioritizes it, prepares responses, and continues monitoring because risks change throughout the project.',
      'Tuckman describes how team relationships mature: orientation, disagreement, shared norms, effective performance, and closure.',
      'A useful meeting starts with a reason and preparation, produces decisions and assigned actions, then preserves accountability through minutes and follow-up.',
    ]
    sort_items=[]
    for i,(ch,title,items) in enumerate(sorts,1): sort_items.append(dict(id=f'464e2-s{i:02}',section=ch,source=next(l['number'] for l in lessons if l['section']==ch),title=title,q=f'Put {title.lower()} in order.',items=items,correct=' → '.join(items),distractors=[],teach=sort_teach[i-1],answer=' → '.join(items),example=f'The first step is “{items[0]}” because it supplies the starting information for the remaining sequence.',kind='sort'))
    review=text[re.search(r'^# \*\*Final Exam Review',text,re.M).start():]
    data=dict(title='CIS 464 Exam 2',module='Chapters 4–7',sections=[dict(id=ch,chapter=ch,title=t,intro=q) for ch,(t,q) in CHAPTERS.items()],lessons=lessons,questions=questions,vocab=vocab,checks=check_items,cloze=cloze_items,sorts=sort_items,reviewHtml=markdown_html(review),sourceText=text,sourceSummary=dict(objectives=33,chapters=4,sourceLines=len(text.splitlines()),lectureSlides=238,lessons=len(lessons),terms=len(vocab)))
    OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    OUT_JS.write_text('window.CIS464_EXAM2_CONTENT='+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n')
    print('Wrote',OUT,data['sourceSummary'],'questions',len(questions),'checks',len(check_items),'blanks',len(cloze_items),'sorts',len(sort_items))

if __name__=='__main__': main()
