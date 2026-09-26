import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];p=ROOT/'dist/cis464-content.json';d=json.loads(p.read_text())
def v(source,term,answer,wrong,exp=''):
 q=d['questions'][source-1];d['vocab'].append(dict(id=f'464-v{len(d["vocab"])+1:03}',source=source,section=q['section'],term=term,exp=exp,q=f'What does {term} mean in project management?',answer=answer,correct=answer,distractors=wrong.split('|'),teach=q['teach']))
v(2,'Project','A temporary effort creating a unique result','A continuing routine with no planned endpoint|A permanent functional department|A recurring business operation')
v(7,'Operations','Ongoing work that sustains a business or service','A temporary effort producing one unique result|A portfolio selection committee|A one-time project authorization')
v(3,'Progressive elaboration','Refining detail as knowledge improves','Adding unlimited work without approval|Fixing every detail before any learning|Replacing planning with improvisation')
v(5,'Scope','The work and results included in a project','The timing of project activities|The funding available for the work|The uncertainty affecting objectives')
v(5,'Schedule','When activities and milestones are planned to occur','The total work included in the project|The people affected by its result|The approved financial justification')
v(5,'Constraint','A limit or restriction affecting choices','An uncertain event that might occur|A benefit already realized|An optional suggestion with no effect')
v(42,'Assumption','Something treated as true for planning and needing validation','A confirmed limit imposed on the project|A completed requirement acceptance test|A change already approved by the sponsor')
v(9,'Stakeholder','Someone who affects or is affected by the project, including perceived effects','Only the people performing project tasks|Only the manager approving funding|Only supportive customers')
v(9,'Sponsor','A person or group supporting and authorizing project resources','The person who performs every technical task|Any user who submits feedback|The keeper of a Sprint task board only')
v(9,'Champion','An advocate who promotes support for the project','The sole author of every technical specification|Any external contractor regardless of advocacy|Only the person performing financial audits')
v(9,'Steering committee','A group providing project direction and oversight','A list of daily implementation tasks|A team that performs every product test|A database of customer requirements')
v(10,'Ambiguity','Unclear meaning or multiple possible interpretations','A known budget limit|A precisely defined requirement|A completed project phase')
v(11,'Team norm','An agreed expectation for how team members work together','A technical product specification only|A financial return ratio|A list of software licenses')
v(11,'SMART','Specific, Measurable, Achievable, Relevant, Time-bound','Simple, Managed, Approved, Recorded, Tested|Scope, Money, Activities, Resources, Time|Specific, Monitored, Agile, Reliable, Technical','Specific Measurable Achievable Relevant Time-bound')
v(13,'Storming','The team stage when differences and conflict surface','The stage when members first meet politely|The stage of consistently effective teamwork|The stage when the team wraps up')
v(13,'Norming','The team stage of developing shared working agreements','The initial discovery of who is on the team|The final disbanding of a team|A period defined only by unresolved conflict')
v(14,'Program','Related projects and activities coordinated for joint benefits','Any set of unrelated work ranked for strategy|A single routine performed indefinitely|Only a list of approved purchases')
v(14,'Portfolio','A collection of work managed to achieve strategic objectives','Only projects that must share one direct dependency|Only one product’s coding tasks|Only a department’s recurring operational checklist')
v(14,'Megaproject','An exceptionally large, complex, often multi-year project','A routine task repeated many times|Every project with more than one manager|Any program regardless of scale')
v(14,'CIO','The executive overseeing an organization’s information technology','The person managing only one Sprint backlog|The committee approving scope changes|An external certification examiner','Chief Information Officer')
v(7,'DevOps','Practices and collaboration connecting development with operations','A replacement for every business strategy|A rule forbidding frequent deployment|Only the team that writes new code','Development and Operations')
v(6,'MORE','Manage perceptions, Own success, Relentlessly reassess, Expand perspective','Measure outputs, Organize resources, Record expenses, Execute|Manage objectives, Own resources, Restrict changes, End work|Monitor operations, Organize records, Reassess expenses, Expand scope','Manage perceptions Own success Relentlessly reassess Expand perspective')
v(16,'Governance','Decision rights, accountability, and oversight for work','Only the order of coding tasks|Only the final quality inspection|A team’s informal meeting notes')
v(17,'Predictive approach','An approach emphasizing early planning for relatively stable requirements','An approach requiring no initial planning|A rule that requirements must change every day|A method defined only by short feedback cycles')
v(17,'Adaptive approach','An approach using learning and feedback to respond to evolving requirements','An approach that prohibits stakeholder feedback|An approach that freezes every feature at the start|An approach that removes all planning discipline')
v(18,'Iteration','A repeated cycle that refines a solution','A newly delivered piece of capability only|A final authorization signature|A fixed organizational department')
v(18,'Increment','An added usable piece of the product or result','Any unfinished task regardless of usability|A change to an employee’s reporting line|A prediction of future project cost')
v(18,'Tailoring','Deliberately adapting practices to project needs','Skipping controls whenever inconvenient|Using one identical method for every situation|Adding features without evaluating impact')
v(20,'Sprint','A fixed-length Scrum event in which value is created','An unlimited period ending whenever all ideas are complete|A final project authorization meeting|A financial ranking method')
v(20,'Product Owner','The Scrum accountability focused on product value and effective backlog management','The person assigning every Developer’s daily task|The person responsible only for team payroll|A committee that replaces all stakeholder input')
v(20,'Scrum Master','The accountability supporting Scrum and Scrum Team effectiveness','The owner of all product prioritization decisions|The manager assigning every coding task|The customer who accepts every contract')
v(21,'Product Backlog','An ordered evolving list of work needed to improve a product','A frozen list of every detail known before the project|Only the work already completed|Only the project’s financial transactions')
v(21,'Definition of Done','An agreed description of the quality state required for an Increment','A person’s claim that coding has stopped|The same thing as the Product Goal|A promise that testing can happen after release','Definition of Done')
v(22,'PMI','The professional organization associated with PM standards and certifications','A company’s software task board|A project’s funding approval document|A product’s final testing checklist','Project Management Institute')
v(22,'CAPM','A PMI credential demonstrating foundational project-management knowledge','A senior-only program-director license|A project scheduling software package|An AI model evaluation metric','Certified Associate in Project Management')
v(22,'PMP','A PMI credential recognizing project-management experience and competence','An entry-level software product|A document approving one project|A technique for ranking vendors','Project Management Professional')
v(28,'SWOT','Strengths, Weaknesses, Opportunities, Threats','Scope, Work, Objectives, Time|Strengths, Workflows, Outputs, Tasks|Strategy, Weaknesses, Operations, Technology','Strengths Weaknesses Opportunities Threats')
v(29,'Balanced scorecard','A way to connect strategy to measures across multiple perspectives','Only a weighted ranking of individual vendors|Only a comparison of budget totals|A method requiring equal scores for every project')
v(30,'Weight','The relative importance assigned to a scoring criterion','The rating earned by an option on that criterion|The total cost of the chosen option|The number of team members scoring it')
v(31,'Discount rate','The rate used to translate future cash flows into present value','A guaranteed reduction in every vendor’s price|The count of years in the project|The total net benefit of an investment')
v(31,'PV','A future cash flow expressed as a value at the present time','The total percentage return on investment|The time needed to recover costs|The sum of all future benefits without discounting','Present Value')
v(32,'NPV','Discounted benefits minus discounted costs summed across periods','The gross benefit divided by investment cost|The time until cumulative cash flow reaches zero|The rate at which all future cash flows disappear','Net Present Value')
v(33,'ROI','Net return divided by investment cost, often expressed as a percentage','The total benefits before subtracting costs|The sum of all project years|The discount rate making NPV zero','Return on Investment')
v(34,'IRR','The discount rate at which NPV equals zero','The time needed to recover initial costs|The raw total of benefits minus costs|The current yearly inflation rate by definition','Internal Rate of Return')
v(34,'Payback period','The time required for cumulative net cash flows to recover investment costs','The percentage return earned over all years|The largest single annual benefit|The total amount invested in staff')
v(36,'Sunk cost','A cost already incurred that cannot be recovered by the decision now being made','A future cost that can still be avoided|A new project benefit expected next year|A planned contingency reserve not yet spent')
v(36,'Gate review','An authorized checkpoint to continue, redirect, pause, or stop work','A daily conversation with no decision role|An automatic instruction to cancel the project|Only a final product demonstration')
v(38,'Outsourcing','Obtaining work or services from an external provider','Transferring all organizational accountability automatically|Moving every employee into one office|Completing all work with internal staff only')
v(39,'Cadence','The rhythm or frequency of work or delivery','The size of a project budget|The scope of a stakeholder’s authority|The number of product requirements')
v(40,'PMO','An organizational entity supporting project-management goals and practices','A single project’s initial permission document|Only the project’s customer representative|A method for calculating net present value','Project Management Office')
v(41,'Baseline','An approved reference plan for comparison with actual performance','The latest informal guess with no approval history|Only the actual results recorded after work|A forecast that automatically replaces previous commitments')
v(41,'Variance','A difference between a reference value and actual performance','A formal permission to start work|A future benefit that is guaranteed|An outside stakeholder’s identity')
v(42,'Business case','A justification explaining the need, options, value, and feasibility of investment','The formal authorization alone|The detailed daily work assignments only|The final product configuration record')
v(43,'Charter','The document that formally authorizes a project','The list of potential project ideas only|The complete detailed management plan|The final lessons-learned report')
v(44,'Project management plan','The integrated guide for executing, monitoring, controlling, and closing the project','Only the initial investment justification|Only the signature granting project authority|Only the list of external stakeholders')
v(46,'Stakeholder register','A structured list and assessment of stakeholders','The plan for all product versions|Only a list of approved scope changes|A table of financial discount factors')
v(47,'Engagement','Meaningful involvement and interaction with stakeholders','Only sending a one-way announcement|Only holding a formal job title|Only approving the final budget')
v(48,'Power','A stakeholder’s capacity to influence decisions or outcomes','How strongly they agree with the project|How frequently they use the software alone|Their level of personal friendliness')
v(48,'Interest','A stakeholder’s degree of concern or attention toward the project','Their formal authority over project decisions|Their salary band|Their support for the project in every case')
v(52,'CCB','An authorized group deciding proposed project changes','The team that approves only staff vacations|A list of all product requirements|The tool that automatically implements every request','Change Control Board')
v(53,'Configuration management','Control of product characteristics, versions, status, and conformance','Only approval of the business investment|Only the ranking of stakeholder interest|Only the calculation of financial return')
v(56,'ML','Methods that learn patterns from data for tasks such as prediction','A fixed rule manually written for every possible case|Only software that stores files|Only a system that generates pictures','Machine Learning')
v(56,'Deep learning','Machine learning using multi-layer neural networks','A category containing every kind of machine learning|Only a human studying data carefully|A database with many tables')
v(56,'NLP','Computational methods for processing human language','Only the physical networking of computers|The project’s net present value|A rule prohibiting language generation','Natural Language Processing')
v(57,'LLM','A large model trained on language-related data for processing or generating text','A guarantee that generated facts are verified|Any program using a fixed spreadsheet formula|Only an autonomous agent with tool permissions','Large Language Model')
v(57,'Generative AI','AI that produces content based on learned patterns and input','Only a system assigning fixed labels to data|Any system guaranteed to act autonomously|A method that cannot generate text or images','Generative Artificial Intelligence')
v(58,'Agentic AI','AI oriented toward goals and choosing or executing actions within permissions','Only a system producing one passive draft|Any tool that has unlimited authority|A guarantee that no human oversight is needed','Agentic Artificial Intelligence')
v(58,'Autonomy','The degree of independent action a system can take','The accuracy of every answer by definition|The size of the training dataset|The number of words generated')
v(66,'Hallucination','Generated content that is unsupported or wrong despite sounding plausible','An authorized user request to change a goal|Only a malicious instruction in retrieved text|Any disagreement between two real stakeholders')
v(66,'Prompt injection','Untrusted content attempting to redirect an AI system’s instructions or actions','Any ordinary user asking an allowed question|Only an accidental calculation error|A model’s correct summary of a source')
v(69,'Bias','A systematic tendency that can produce skewed or unfair outcomes','Any random error with no pattern|A guarantee that all groups benefit equally|An explanation of the system’s limitations')
v(69,'Accountability','Owning decisions, actions, and their consequences','Passing all responsibility to software|Keeping decisions hidden from affected people|Counting only the number of completed tasks')
v(69,'Transparency','Making relevant use, limits, and decision processes understandable','Releasing all private data publicly|Guaranteeing that every prediction is correct|Removing humans from all decisions')
v(64,'Inference','Using a trained model to produce an output','The earlier process of training the model only|A guarantee that output is true|The physical building housing servers')
v(71,'PMI-CPMAI','A credential focused on managing AI projects','A tool for writing project code automatically|A project-specific charter|A certification that replaces all data evaluation','PMI Certified Professional in Managing AI')
# Authored expansion alternatives stay within similar wording; no borrowing random answers.
expwrong={
'SMART':'Specific Measurable Approved Relevant Timeless|Simple Managed Achievable Recorded Time-bound|Specific Measurable Agile Reliable Technical',
'CIO':'Chief Infrastructure Operator|Corporate Information Officer|Chief Integration Organizer',
'DevOps':'Development and Optimization|Device Operations|Delivery and Oversight',
'MORE':'Manage objectives Own resources Restrict change Expand scope|Measure outputs Organize resources Record expenses Execute|Monitor operations Own requirements Reassess estimates Expand effort',
'Definition of Done':'Description of Delivery|Definition of Development|Decision on Delivery',
'PMI':'Project Management Initiative|Program Management Institute|Project Measurement Institute',
'CAPM':'Certified Analyst in Project Management|Certified Associate in Program Management|Certified Agile Project Manager',
'PMP':'Project Management Practitioner|Program Management Professional|Project Measurement Professional',
'SWOT':'Strengths Workflows Outputs Tasks|Scope Weaknesses Opportunities Time|Strategy Work Operations Threats',
'PV':'Projected Value|Planned Variance|Portfolio Value',
'NPV':'Net Project Value|Nominal Present Value|Net Planned Variance',
'ROI':'Return on Integration|Rate of Investment|Return on Implementation',
'IRR':'Internal Revenue Ratio|Investment Return Ratio|Initial Rate of Return',
'PMO':'Project Management Organization|Program Monitoring Office|Project Measurement Office',
'CCB':'Change Coordination Board|Configuration Control Baseline|Change Compliance Bureau',
'ML':'Model Logic|Machine Language|Managed Learning',
'NLP':'Natural Learning Process|Neural Language Prediction|Network Language Processing',
'LLM':'Large Learning Machine|Layered Language Method|Logical Language Model',
'Generative AI':'General Artificial Intelligence|Generated Automated Information|Generative Adaptive Integration',
'Agentic AI':'Automatic Artificial Intelligence|Agentic Automated Information|Adaptive Agent Integration',
'PMI-CPMAI':'PMI Certified Practitioner in Modeling AI|PMI Certified Professional in Monitoring AI|PMI Certified Program Manager for AI'}
d['abbreviationDistractors']={k:v.split('|') for k,v in expwrong.items()}
def check(n,q,a,wrong,why):
 d['checks'].append(dict(id=f'464-c{len(d["checks"])+1:03}',source=n,section=d['questions'][n-1]['section'],q=q,correct=a,answer=a,distractors=wrong.split('|'),teach=why))
for n,q,a,w,why in [
(2,'A team replaces the university’s LMS over nine months. Project or operations?','Project','Operations|Portfolio governance only|A permanent functional department','This is a temporary effort creating a particular replacement, even though the new platform will later be operated continuously.'),
(5,'A sponsor adds features but keeps the same deadline. What should happen first?','Assess impacts and discuss trade-offs through change control','Promise unchanged cost and quality automatically|Silently skip testing|Add the work without updating any plan','More scope can require time or resources. Understand the connected effects before committing.'),
(9,'A person opposes a project because it changes their job. Are they a stakeholder?','Yes','No, because they oppose it|Only if they fund it|Only if they join the project team','Being affected is enough; resistance does not remove someone from consideration.'),
(14,'Several related projects share benefits that require coordination. What structure fits?','Program','Single routine operation|Independent task|A financial baseline','Joint benefits and related work distinguish a program from an arbitrary list of projects.'),
(15,'The team compares actual progress to the schedule and acts on a delay. Which focus area?','Monitoring and Controlling','Initiating|Closing|Executing only','The action combines measuring a difference and responding to it.'),
(16,'Who may approve major changes is most directly a question of which domain?','Governance','Schedule|Scope|Resources','Governance establishes decision authority and accountability.'),
(18,'A release adds a usable reporting feature. Which idea does this most directly illustrate?','Incremental delivery','Only iteration of the same feature|Project cancellation|Formal authorization','A new usable piece of capability is an increment; improving an existing solution through repetition is iteration.'),
(20,'Which Scrum event inspects how the team worked and identifies improvements?','Sprint Retrospective','Sprint Review|Sprint Planning|Daily Scrum only','The Retrospective focuses on team effectiveness. The Review inspects the product outcome with stakeholders.'),
(20,'Who is accountable for maximizing product value and effective Product Backlog management?','Product Owner','Scrum Master|Steering committee by definition|Any individual Developer by definition','The Product Owner orders and manages the product work in pursuit of value; the Scrum Master has a different accountability.'),
(24,'Informal coalitions compete for a scarce budget. Which organizational frame is most relevant?','Political','Structural only|Human resources only|Symbolic only','The political frame examines interests, influence, resource conflict, and coalitions.'),
(25,'A developer reports to an engineering manager and a project manager. Which structure fits?','Matrix','Purely projectized only|Purely functional with no cross-project authority|A portfolio baseline','Matrix structures share authority between functional and project lines.'),
(28,'A new competitor enters the market. Which SWOT category fits?','Threat','Strength|Weakness|Opportunity in every case','The competitor is an external condition with potential negative impact, so it is a threat in this scenario.'),
(30,'Weights 0.10, 0.60, 0.30 with ratings 1, 10, 5 give what total?','7.6','16|5.33|6.1','Multiply pairs: 0.1 + 6 + 1.5 = 7.6. Do not use the unweighted sum or average.'),
(32,'You must select one project using NPV: A = $10K, B = $20K, C = $30K. Which should you choose?','Project C','Project A|Project B|Cannot decide without recalculating the discount rates','This reproduces the slide 30 selection scenario. The NPVs are already calculated; C has the highest value under the stated criterion.'),
(33,'PV benefits are $150,000 and PV costs are $100,000. What is discounted ROI?','50%','150%|33.33%|−50%','Subtract cost to find $50,000 net return, then divide by $100,000 cost and multiply by 100.'),
(34,'Cumulative net cash flow is still negative at the last stated year. What can you say?','Payback has not occurred within the stated horizon','Payback occurred in the first profitable year|ROI must be exactly zero|Future payback is guaranteed next year','One profitable year does not necessarily recover earlier costs. Do not invent later cash flows.'),
(36,'The team has already spent heavily, but remaining benefits are lower than remaining costs. What matters for continuation?','Future incremental value and risks, not sunk costs alone','Money already spent guarantees continuation|The original forecast must be treated as certain|Every project must continue until its budget is exhausted','Prior spending cannot be undone by continuing. Reassess what the next decision will cost and achieve.'),
(42,'Which document compares alternatives and explains why an investment is worthwhile?','Business case','Charter|Stakeholder register|Configuration status report','Justification precedes authorization. A business case provides the value argument.'),
(43,'Which document formally recognizes the project and authorizes it?','Project charter','Business case alone|Meeting minutes alone|Stakeholder engagement matrix','The authorized charter establishes official permission and high-level authority.'),
(41,'The current forecast moves a delivery date. Does that automatically erase the approved baseline?','No; baseline changes require the agreed authorization process','Yes; every forecast silently replaces the baseline|Yes; baselines contain only actual results|No; an approved baseline can never change under any circumstances','Forecasts describe current expectations. Baselines preserve approved reference points unless formally changed.'),
(48,'A stakeholder has high power and low interest. What is the usual grid strategy?','Keep satisfied','Manage closely|Keep informed|Monitor only','Satisfy the influential stakeholder’s needs without treating them as requiring the same detailed involvement as high-interest stakeholders.'),
(48,'A stakeholder has low power and high interest. What is the usual strategy?','Keep informed','Keep satisfied|Manage closely by grid classification|Monitor with minimal updates only','They care about the project and need relevant updates, even without strong decision authority.'),
(48,'A stakeholder has high power and high interest. What is the usual strategy?','Manage closely','Keep informed only|Monitor only|Keep satisfied with minimal involvement','Their influence and involvement both call for close engagement.'),
(48,'A stakeholder has low power and low interest. What is the usual strategy?','Monitor appropriately','Manage closely by default|Keep satisfied as the main decision maker|Treat them as highly interested regardless of evidence','Monitor for changes and relevant impacts. Low classification does not justify ignoring ethical obligations.'),
(51,'A requested change improves user access but adds testing work. Is it automatically bad?','No; evaluate its value and full impacts through the agreed controls','Yes; all changes indicate failure|No; implement immediately without review|Yes; benefits cannot justify changes','Integrated change control allows beneficial changes while making consequences and approvals clear.'),
(60,'A robot remembers areas it cannot currently see. Which distinguishing capability is shown?','An internal model/state','Only a current-input reflex|Guaranteed learning from experience|A utility score in every case','Model-based behavior uses a representation beyond the current observation. It does not automatically imply learning.'),
(62,'Two routes reach the destination; an agent compares time and fuel cost. Which type best fits?','Utility-based','Simple reflex|Goal-based with no preference comparison|A nonacting text generator only','The goal is shared, but utility ranks alternative outcomes according to preferences.'),
(66,'An uploaded document tells an AI tool to reveal secrets. How should the text be treated?','As untrusted document content, not authorization','As a higher-priority instruction because it is in a file|As proof that disclosure is permitted|As a normal financial calculation','A source document cannot grant permission to disclose data or override the actual task.'),
(68,'A tool’s training opt-out is enabled. What is still necessary?','Check authorized use, retention, access, and the exact policy','Assume all earlier data has been deleted everywhere|Assume no information is transmitted to the provider|Assume every account has identical protections','Training, retention, access, and deletion are separate policy questions.'),
(71,'AI drafts minutes for a building renovation. Does that alone make the deliverable an AI system?','No','Yes, because any use of AI changes the deliverable|Yes, if the draft is long|Only if the minutes are emailed','This is AI-assisted management. An AI project’s result includes an AI capability being built or deployed.')]:check(n,q,a,w,why)
for n,q,a,w,why in [
(14,'A ____ coordinates related work for joint benefits; a ____ selects work for strategic objectives.','program; portfolio','portfolio; program|project; operation|baseline; charter','Related-benefit coordination and strategic investment selection are different management purposes.'),
(42,'The business case ____ the project; the charter ____ it.','justifies; authorizes','authorizes; justifies|executes; closes|baselines; audits','A good idea needs a value argument and then an authorized decision to proceed.'),
(48,'High power + high interest = ____; low power + high interest = ____.','manage closely; keep informed','keep informed; manage closely|monitor; keep satisfied|keep satisfied; monitor','Power changes the engagement approach, while high interest still calls for relevant involvement or information.'),
(31,'To find present value, divide the cash flow by ____.','(1 + r)^t','r × t|(1 − r) × t|cash flow × r','Compounding is reversed by dividing by the growth factor for the number of periods.'),
(33,'NPV is a ____ amount; ROI is a ____ relative to cost.','money; ratio','time; money|ratio; time|count; schedule','NPV expresses net present money. ROI compares net return to the investment denominator.'),
(56,'Deep learning is a subset of ____; NLP concerns ____.','machine learning; human language','human language; project finance|generative AI only; hardware|project management; neural hardware','These terms describe different aspects of AI capabilities and can overlap.'),
(66,'An invented citation is a ____; hostile instructions in retrieved text can be ____.','hallucination; prompt injection','prompt injection; a baseline|forecast; authorization|utility score; a charter','A factual fabrication and an attempt to redirect instructions are different failures.')]:
 qbase=d['questions'][n-1];d['cloze'].append(dict(id=f'464-blank{len(d["cloze"])+1}',source=n,section=qbase['section'],q=q,correct=a,answer=a,distractors=w.split('|'),teach=why))
for n,title,items,why in [
(13,'Build Tuckman’s team-development sequence',['Forming','Storming','Norming','Performing','Adjourning'],'This is the usual teaching sequence. Real teams can return to earlier stages.'),
(15,'Arrange the five focus areas in their conventional listing',['Initiating','Planning','Executing','Monitoring and Controlling','Closing'],'This orders the course list, not five strictly separated phases. Monitoring and Controlling overlaps with other work.'),
(27,'Strategy to selected projects',['Develop strategic plan','Analyze departmental needs','Propose projects','Authorize resource allocation'],'Choose useful work based on goals and needs before committing resources.'),
(30,'Build a weighted-scoring evaluation',['Apply eligibility requirements','Choose criteria and weights','Rate each option consistently','Multiply each rating by its weight','Sum and compare weighted scores'],'Eligibility comes first. A high score does not excuse failing a mandatory requirement.'),
(52,'Process a proposed change',['Record the request','Analyze connected impacts','Obtain authorized decision','Update approved documents if accepted','Communicate and implement the decision'],'A request is not an approval. Use the organization’s actual control procedure; this is a simplified teaching flow.'),
(31,'Discount a cash flow',['Identify cash flow and time','Convert rate to a decimal','Calculate (1 + r)^t','Divide cash flow by the factor'],'Time zero uses a factor of one. Keep period lengths consistent.'),
(33,'Calculate discounted ROI',['Calculate PV of benefits','Calculate PV of costs','Subtract PV costs from PV benefits','Divide net present return by PV costs','Multiply by 100 for percent'],'The first two computations can be done in either order; this activity asks for this worked-example order. Net return must be computed before the ratio.')]:
 d['sorts'].append(dict(id=f'464-s{len(d["sorts"])+1}',source=n,section=d['questions'][n-1]['section'],q=title,items=items,teach=why))
d['references']=[
{'title':'PMI · Project management framework (edition check)','url':'https://www.pmi.org/standards/pmbok','questions':[15,16]},
{'title':'The Scrum Guide','url':'https://scrumguides.org/scrum-guide.html','questions':[20,21]},
{'title':'Agile Manifesto','url':'https://agilemanifesto.org/','questions':[19]},
{'title':'PMI · Code of Ethics and Professional Conduct','url':'https://www.pmi.org/-/media/pmi/documents/public/pdf/ethics/pmi-code-of-ethics.pdf','questions':[55,69]},
{'title':'IBM · Types of AI agents','url':'https://www.ibm.com/think/topics/ai-agent-types','questions':[59,60,61,62,63]},
{'title':'PMI · CAPM','url':'https://www.pmi.org/certifications/certified-associate-capm','questions':[22]},
{'title':'PMI · PMP','url':'https://www.pmi.org/certifications/project-management-pmp','questions':[22]},
{'title':'PMI · Managing AI projects credential','url':'https://www.pmi.org/certifications/ai-project-management-cpmai','questions':[71]}]
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n');print({k:len(d[k]) for k in ['questions','vocab','checks','cloze','sorts']})
