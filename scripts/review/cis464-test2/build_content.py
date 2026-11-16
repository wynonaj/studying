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
'Additional AI cost-management discussion':'The slides connect excessive AI spending to FOMO, unbounded agents, poor tool selection, repeated uncached work, and weak growth planning. High performers use strategy, executive sponsorship, governance, workload-based model routing, task-level cost tracking, and vendor flexibility.',
'Stakeholder engagement levels':'Stakeholder engagement can be unaware, resistant, neutral, supportive, or leading. The team compares current and desired levels and plans how to close important gaps.',
'Risk management plan':'The risk management plan explains how the project will identify, analyze, respond to, monitor, and report risks. It defines the process, roles, categories, timing, budget, and thresholds for risk work.',
"Your professor's EMV example":'For each option, multiply every outcome by its probability and add the results. The project with the best probability-weighted value has the highest EMV, although decision makers may also consider risk preference and strategic fit.',
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
'Can leadership be learned?':'The slides treat leadership as a learnable skill developed through practice, feedback, reflection, education, mentoring, experience, and willingness to change old habits.',
"Team development: Tuckman's Model":'Tuckman’s stages are forming, storming, norming, performing, and adjourning. Teams meet and orient first, work through disagreement, establish norms, perform effectively, and finally close the work.',
'How to prevent these dysfunctions':'Build trust, discuss disagreement constructively, make clear commitments, hold people accountable, and keep attention on shared project results.',
'Five common conflict management approaches':'The five approaches are collaborate or problem-solve, compromise or reconcile, smooth or accommodate, force or direct, and withdraw or avoid. The project manager chooses based on urgency, importance, relationships, and the need for a lasting solution.',
'Communication barriers':'Communication barriers include language or jargon, cultural differences, assumptions, emotion, noise, poor timing, information overload, status differences, inaccessible tools, weak listening, and missing feedback.',
'Microaggressions':'Microaggressions are everyday comments or behaviors that communicate bias toward historically marginalized people. They may be intentional or unintentional, and their impact still matters.',
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
}

def clean_heading(s): return re.sub(r'\*\*','',s).strip().strip('#').strip()
def strip_md(s):
    s=re.sub(r'!\[[^]]*\]\([^)]*\)','',s); s=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',s)
    s=re.sub(r'[`*_>#]','',s); s=re.sub(r'\s+',' ',s)
    return s.strip()
def inline(s):
    s=html.escape(s.strip())
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
    title=re.sub(r'^[A-G]\.\s*','',title)
    if title in generic and parent:
        parent=re.sub(r'^(?:Objective|Cost objective) \d+:\s*','',parent)
        parent=re.sub(r'^[A-G]\.\s*','',parent)
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
    if low.startswith(('methods of ','ways to ','types of ','steps ','five ','four ','three ','major ','potential sources','common causes','factors to consider')):
        return f'Which answer correctly describes {title.lower()}?'
    if any(word in low for word in ('formula','calculation','estimate')):
        return f'How is {title.lower()} calculated or used?'
    if low.endswith((' plan',' matrix',' chart',' register',' statement',' structure',' analysis',' theory',' model',' method',' grid',' law',' baseline',' histogram',' list',' attributes',' criteria',' card',' cards',' management',' communication',' communications')):
        return f'What is the purpose of {title}?'
    return f'What does {title} mean in project management?'

def rows_from_tables(md,ch):
    rows=[]; lines=md.splitlines(); i=0
    while i<len(lines)-2:
        if lines[i].lstrip().startswith('|') and re.match(r'^\s*\|?\s*:?-+',lines[i+1]):
            head=[strip_md(c) for c in lines[i].strip().strip('|').split('|')]; data=[]; i+=2
            while i<len(lines) and lines[i].lstrip().startswith('|'):
                data.append([strip_md(c) for c in lines[i].strip().strip('|').split('|')]); i+=1
            if len(head)>=2 and head[0].lower() not in {'id','year','activity','path','team size','n','criterion'}:
                for r in data:
                    if len(r)>=2 and r[0] and r[1] and len(r[0])<=90 and len(r[1])<=600: rows.append((ch,r[0],r[1]))
            continue
        i+=1
    return rows

def choice_set(correct,pool):
    vals=[]
    for v in pool:
        if v!=correct and v not in vals: vals.append(v)
    while len(vals)<3: vals.append(f'An unrelated project concept {len(vals)+1}')
    return vals[:3]

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
        siblings=[x['summary'] for x in lessons if x['section']==lesson['section'] and x['parent']==lesson['parent'] and x['id']!=lesson['id']]
        chapter_pool=[x['summary'] for x in lessons if x['section']==lesson['section'] and x['id']!=lesson['id']]
        pool=siblings+chapter_pool
        questions.append(dict(id='q-'+lesson['id'],number=lesson['number'],section=lesson['section'],source=lesson['number'],title=lesson['title'],q=lesson_question(lesson),correct=lesson['summary'],distractors=choice_set(lesson['summary'],pool),teach=f"{lesson['summary']} This directly answers the question about {lesson['title']}.",answer=lesson['summary'],example=f"The complete {lesson['title']} lesson includes the source explanation, examples, comparisons, or formulas.",kind=lesson['kind']))
    # Table rows become term/comparison cards; deduplicate exact labels within a chapter.
    seen=set(); vocab=[]
    for ch in CHAPTERS:
        for _,term,definition in rows_from_tables(chapter_sources[ch],ch):
            key=(ch,term.lower())
            if key in seen: continue
            seen.add(key); peers=[d for c,t,d in rows_from_tables(chapter_sources[ch],ch) if d!=definition]
            vocab.append(dict(id=f'464e2-v{len(vocab)+1:03}',section=ch,source=next((l['number'] for l in lessons if l['section']==ch and term.lower() in l['raw'].lower()),lessons[0]['number']),title=term,term=term,q=f'Which description correctly matches {term}?',correct=definition,distractors=choice_set(definition,peers),teach=f'{term} means: {definition}',answer=definition,example=f'Keep {term} separate from nearby concepts by identifying its specific purpose.'))
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
    all_answers=[x[3] for x in checks]
    for i,(ch,title,q,correct) in enumerate(checks,1):
        check_items.append(dict(id=f'464e2-c{i:02}',section=ch,source=next(l['number'] for l in lessons if l['section']==ch),title=title,q=q,correct=correct,distractors=choice_set(correct,all_answers),teach=correct,answer=correct,example='Apply the definition or formula step by step before choosing.'))
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
    cloze_items=[]
    for i,(ch,q,ans) in enumerate(cloze,1): cloze_items.append(dict(id=f'464e2-b{i:02}',section=ch,source=next(l['number'] for l in lessons if l['section']==ch),title='Build the relationship',q=q,correct='; '.join(ans),distractors=['schedule','cost','manager'],teach='Read the completed sentence as one relationship.',answer='; '.join(ans),example='The surrounding words identify the role of each blank.',kind='cloze'))
    sorts=[
      (4,'Scope management flow',['Collect and validate requirements','Write the detailed scope statement','Create the WBS and scope baseline','Validate completed deliverables','Control requested scope changes']),
      (5,'Schedule development',['Define activities','Sequence activities','Estimate resources and durations','Build the network and find the critical path','Develop and baseline the schedule']),
      (5,'Forward-pass logic',['Start at time zero','Calculate earliest start','Add duration for earliest finish','Use the largest predecessor finish at a merge','Continue to project completion']),
      (6,'Risk process',['Plan risk management','Identify risks','Analyze probability and impact','Plan and assign responses','Implement and monitor responses']),
      (7,'Tuckman team development',['Forming','Storming','Norming','Performing','Adjourning']),
      (7,'Effective meeting',['Define purpose and needed participants','Send agenda and prework','Facilitate discussion and decisions','Assign actions, owners, and due dates','Distribute minutes and follow up']),
    ]
    sort_items=[]
    for i,(ch,title,items) in enumerate(sorts,1): sort_items.append(dict(id=f'464e2-s{i:02}',section=ch,source=next(l['number'] for l in lessons if l['section']==ch),title=title,q=f'Put {title.lower()} in order.',items=items,correct=' → '.join(items),distractors=[],teach=f'{title} follows this sequence so each later step uses the result of the earlier one.',answer=' → '.join(items),example='Follow the work from preparation through completion.',kind='sort'))
    review=text[re.search(r'^# \*\*Final Exam Review',text,re.M).start():]
    data=dict(title='CIS 464 Exam 2',module='Chapters 4–7',sections=[dict(id=ch,chapter=ch,title=t,intro=q) for ch,(t,q) in CHAPTERS.items()],lessons=lessons,questions=questions,vocab=vocab,checks=check_items,cloze=cloze_items,sorts=sort_items,reviewHtml=markdown_html(review),sourceText=text,sourceSummary=dict(objectives=33,chapters=4,sourceLines=len(text.splitlines()),lectureSlides=238,lessons=len(lessons),terms=len(vocab)))
    OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    OUT_JS.write_text('window.CIS464_EXAM2_CONTENT='+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n')
    print('Wrote',OUT,data['sourceSummary'],'questions',len(questions),'checks',len(check_items),'blanks',len(cloze_items),'sorts',len(sort_items))

if __name__=='__main__': main()
