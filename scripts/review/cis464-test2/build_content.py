"""Build CIS 464 Exam 2 from the supplied Chapters 4–7 master guide."""
from __future__ import annotations

import html, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
SOURCE=Path(__file__).with_name('study-guide.md')
OUT=ROOT/'dist/cis464-test2-content.json'

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

def first_answer(md,title):
    for p in re.split(r'\n\s*\n',md):
        t=strip_md(p)
        if t and not t.startswith('|') and len(t)>25: return t[:500]
    return f'This topic explains {title.lower()} and how it is applied in project management.'

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
        lessons.append(dict(id=f'464e2-l{number:03}',number=number,section=ch,kind='overview',title=f'Chapter {ch} overview',objective=f'Understand the purpose and exam focus of Chapter {ch}.',summary=overview,html=markdown_html(intro) or f'<p>{html.escape(overview)}</p>',raw=intro)); number+=1
        parts=split_h2(md)
        for title,body in parts:
            if title.startswith(('Objective ','Cost objective ')):
                summary=OBJECTIVE_ANSWERS[title]
                lessons.append(dict(id=f'464e2-l{number:03}',number=number,section=ch,kind='objective',title=title,objective=title.split(':',1)[1].strip(),summary=summary,html=markdown_html(body),raw=body)); number+=1
            elif title.startswith('Part '):
                h3=list(re.finditer(r'^### \*\*(.+?)\*\*\s*$',body,re.M))
                for j,m in enumerate(h3):
                    t=clean_heading(m.group(1)); b=body[m.end():h3[j+1].start() if j+1<len(h3) else len(body)]
                    if len(strip_md(b))<35: continue
                    summary=first_answer(b,t)
                    lessons.append(dict(id=f'464e2-l{number:03}',number=number,section=ch,kind='additional',title=t,objective=f'Explain {t}.',summary=summary,html=markdown_html(b),raw=b)); number+=1
    # Every objective is a separate scored question; additional lessons receive one too.
    questions=[]
    for lesson in lessons:
        pool=[x['summary'] for x in lessons if x['section']==lesson['section'] and x['id']!=lesson['id']]
        questions.append(dict(id='q-'+lesson['id'],number=lesson['number'],section=lesson['section'],source=lesson['number'],title=lesson['title'],q=f"Which answer best explains {lesson['title']}?",correct=lesson['summary'],distractors=choice_set(lesson['summary'],pool),teach=lesson['summary'],answer=lesson['summary'],example=f"Open the {lesson['title']} lesson to see the complete guide explanation, examples, comparisons, and formulas.",kind=lesson['kind']))
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
    data=dict(title='CIS 464 Exam 2',module='Chapters 4–7',sections=[dict(id=ch,chapter=ch,title=t,intro=q) for ch,(t,q) in CHAPTERS.items()],lessons=lessons,questions=questions,vocab=vocab,checks=check_items,cloze=cloze_items,sorts=sort_items,reviewHtml=markdown_html(review),sourceText=text,sourceSummary=dict(objectives=33,chapters=4,sourceLines=len(text.splitlines()),lessons=len(lessons),terms=len(vocab)))
    OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print('Wrote',OUT,data['sourceSummary'],'questions',len(questions),'checks',len(check_items),'blanks',len(cloze_items),'sorts',len(sort_items))

if __name__=='__main__': main()
