"""Authored CIS 304 guide answers. Original prompts are kept separately for coverage checks."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
prompts=json.loads((Path(__file__).parent/'guide-prompts.json').read_text())
rows=[]
def add(title,answer,teach,example,correct,wrong,slides):
 n=len(rows)+1
 rows.append(dict(id=f'304-q{n:02}',number=n,section=1 if n<=10 else 2 if n<=26 else 3 if n<=37 else 4,q=prompts[n-1],title=title,answer=answer,teach=teach,example=example,correct=correct,distractors=wrong.split('|'),slides=slides))
add('Data → information → knowledge → wisdom',
'Data are individual facts. Information is data organized or processed into meaning. Knowledge is the ability to understand and apply information. Wisdom is sound judgment about what to do in a situation. DIKW stands for Data, Information, Knowledge, Wisdom, in that order.',
'A fact alone may tell you very little. Add context, recognize what it means, and then decide what to do. Each step uses the earlier step; simply collecting more facts does not automatically create good judgment.',
'A shop records 12, 18, and 30 sales. A report shows sales rising over three days: information. The manager knows weekends create extra demand: knowledge. She balances demand and waste before ordering extra stock: wisdom.',
'Data → Information → Knowledge → Wisdom',
'Information → Data → Knowledge → Wisdom|Data → Knowledge → Information → Wisdom|Data → Information → Wisdom → Knowledge',[5])
add('An information system',
'An information system (IS) is an organized combination of people, processes, data, hardware, and software that collects, processes, stores, and shares information to support work and decisions.',
'A system means parts working together. Here the job is handling information. A computer program is only one part: someone must enter or use the data, and there must be a procedure for doing the work.',
'At checkout, the cashier scans a product, software finds its price, the system records the sale, and the cashier gives a receipt. The person, scanner, program, product data, and checkout steps form the information system.',
'People and technology working through processes to handle information',
'Only the programs installed on a computer|Only the cables and computers used by a company|Only a collection of facts without people or procedures',[6])
add('The five IS components',
'The five components are hardware, software, data, people, and processes (also called procedures). Hardware is physical equipment. Software is instructions for computers. Data are facts the system handles. People operate and use it. Processes describe how work is performed.',
'Do not count the Internet as a sixth component. Network equipment fits within hardware, and network programs fit within software. The five categories describe the whole working system.',
'Checkout: scanner = hardware; checkout app = software; price = data; cashier = people; scan, total, and pay = process.',
'Hardware, software, data, people, processes',
'Hardware, software, data, networks, electricity|Hardware, software, customers, profits, buildings|Hardware, memory, storage, processors, networks',[6])
add('Computer hardware',
'Essential hardware components include the CPU/processor, main memory (RAM), persistent storage, input devices, output devices, and communication/networking devices. The CPU executes instructions; RAM holds active work; storage keeps files; input brings information in; output presents results; networking exchanges data.',
'Hardware is equipment you can physically touch. Memory and storage are different: RAM is temporary working space; an SSD keeps files when power is off.',
'You type with a keyboard (input). The CPU runs a spreadsheet using RAM. You save to an SSD (storage), see the chart on a monitor (output), and send it using a network adapter.',
'CPU, memory, storage, input, output, and communication devices',
'Operating system, apps, utilities, and procedures|CPU, applications, people, and business goals|Storage and monitors only; processing is software',[6])
add('Computer software',
'System software, especially the operating system, manages hardware and provides services for programs. Application software performs user tasks. Utilities/support software maintain, protect, or configure the computer; utilities are commonly a category of system software.',
'Software is a set of instructions, not a physical object. The operating system coordinates the computer. An app helps a person do a particular job. A utility supports the computer itself.',
'Windows manages files and memory; a spreadsheet calculates a budget; a backup utility copies files so they can be recovered.',
'Operating/system software, application software, and supporting utilities',
'CPU, memory, storage, and input devices|Applications only; operating systems are hardware|People, procedures, data, and network cables',[6])
add('Business organizations',
'A business organization is people and resources coordinated to achieve shared business goals, usually by providing goods or services. Goods are tangible products; services are work performed for someone.',
'An organization is not just a building. It is people working together with agreed responsibilities. A goal is a result they want to achieve.',
'A bakery has bakers, sales staff, ingredients, ovens, and routines. Together they make and sell bread; each person does part of the shared work.',
'People and resources coordinated around shared business goals',
'Any building containing computers|A temporary task with no continuing business activity|A collection of departments with no shared purpose',[])
add('Business strategy',
'Business strategy is the broad, long-term plan for reaching goals and competing successfully. The slides emphasize cost leadership (competing through lower costs) and differentiation (offering something customers value as distinct).',
'Competitive advantage means giving customers a reason to choose you over alternatives. Strategy decides the direction. It does not list every computer or every daily task.',
'One bakery competes by producing affordable bread efficiently. Another competes with unusual recipes and custom cakes. Their technology choices should support their different strategies.',
'A long-term approach to goals and competitive advantage',
'A list of hardware purchases without business goals|The daily sequence for processing one order|A record of last month’s sales only',[7,8,9])
add('A business’s primary objective',
'A business aims to create value and achieve its goals. For a for-profit business, delivering things customers want while earning sustainable profits supports survival and continued operation. The exact goals depend on the organization.',
'Value means a useful benefit someone cares about. Revenue is money coming in from sales. Profit is what remains after costs. High sales alone do not prove a business is successful if costs exceed revenue.',
'A bakery that sells bread customers enjoy must also cover ingredients, wages, and rent so it can keep operating.',
'Create value and achieve goals with sustainable returns in a for-profit business',
'Maximize sales regardless of costs or customer value|Buy the newest technology regardless of usefulness|Optimize each department even if the whole business suffers',[7,9,10])
add('Business models and examples',
'A business model describes how an organization creates, delivers, and captures value: what it offers, to whom, and how it earns money. Examples from the guide include retail (Walmart), subscription (Netflix), freemium (Spotify), marketplace (eBay), and advertising (Google). Slides also give bricks and clicks (physical and online stores), direct sales/cutting out the middleman (Dell), franchise (McDonald’s), and value-added reseller (a seller bundles a product with setup/support).',
'A strategy explains how the business plans to compete. A business model explains how the business works and earns revenue. A company can use more than one model.',
'A subscription charges repeatedly for ongoing access. A marketplace connects buyers and sellers and can charge transaction fees. A franchisee pays to use an established brand and business approach.',
'How a business creates, delivers, and captures value',
'Only the reporting relationships between employees|Only the hardware used to store customer data|Only a plan to lower costs with no explanation of revenue',[10,11])
add('Two ways IS creates an advantage',
'Information systems can improve existing business processes—making work faster, less costly, or better—and enable new or differentiated products, services, and business models. These support cost leadership and differentiation.',
'The first route improves how existing work is done. The second changes what the business can offer. Installing technology without either benefit is not automatically an advantage.',
'An inventory system reduces wasted ingredients. An online custom-cake service creates a new way to order. Both use IS, but they improve the business in different ways.',
'Improve existing processes and enable new offerings or business models',
'Replace all people and eliminate all procedures|Buy hardware and ignore changes to business work|Increase data volume and increase paperwork',[9,10])
add('Systems thinking and DSRP',
'Systems thinking examines parts, their connections, and the whole they form. DSRP means Distinctions (what something is and is not), Systems (parts and wholes), Relationships (interactions), and Perspectives (different viewpoints).',
'A decision that helps one part can harm another. DSRP gives you four questions: What are we talking about? What contains it and what is inside it? What does it affect? Who sees it differently?',
'A bakery cuts purchasing costs by buying huge amounts. Purchasing benefits, but storage fills up and ingredients spoil. Systems thinking asks about the effect on the whole bakery, not only the purchasing bill.',
'Distinctions, Systems, Relationships, Perspectives',
'Data, Systems, Resources, Processes|Distinctions, Strategy, Requirements, Productivity|Decisions, Software, Relationships, Projects',[13,14])
add('Processes and business processes',
'A process is related activities that use inputs to produce outputs. A business process performs work toward a business goal for a customer or recipient. Its parts include actors, inputs, activities/subprocesses, decisions, and outputs. Actors can be people or information systems.',
'Input means what goes into the work. Output means what comes out. An actor is whoever or whatever performs an action. A decision chooses a path, such as whether payment was approved.',
'Input: an order for bread. Activities: check stock, collect payment, pack bread. Actors: cashier and checkout system. Decision: is enough stock available? Output: a fulfilled order.',
'Related activities transform inputs into outputs serving a business goal',
'A list of departments with no activities or outputs|A single goal with no work needed to reach it|A collection of hardware unrelated to customer outcomes',[15,16,18])
add('Process models',
'A process model represents how work is performed: activities, sequence, decisions, participants, responsibilities, and information flows. It supports shared understanding, finding problems, and designing improvements. An as-is model shows current work; a to-be model shows proposed work. High-level models show major subprocesses; low-level models show detailed actions. UML activity diagrams are one modeling method.',
'A model is a simplified picture, not the real work itself. It lets people see missing steps, repeated work, and handoffs. A handoff is when responsibility moves from one person or team to another.',
'A diagram shows an order waiting for two identical approvals. Staff can see the duplicate check and propose a to-be flow with one appropriate approval.',
'A representation of activities and decisions used to understand and improve work',
'A financial report that only lists total revenue|A replacement for carrying out any actual work|A hardware inventory with no activities or participants',[17,18])
add('Projects versus repeated processes',
'A project is a temporary effort undertaken to create a unique product, service, or result. It has a beginning and an end. A business process is a repeatable way of performing work; an individual process instance ends, but the process can run again.',
'Temporary describes the effort, not how long its result lasts. Building a new ordering website is a project. Taking customer orders through it every day is ongoing business work.',
'Opening one new bakery location is a project. Buying ingredients and selling bread at that location are recurring processes.',
'A temporary effort that creates a unique product, service, or result',
'A repeatable routine that must continue forever|Any task performed by a project manager, with no required result|A permanent department that handles all operations',[])
add('Efficiency: planned input ÷ actual input',
'For this course, efficiency = PI / AI. PI is initial planned input; AI is actual input. Inputs are resources such as hours or dollars. Using less input than planned gives a ratio above 1; using more gives a ratio below 1. Multiply by 100 to express the ratio as a percentage. Compare like units and comparable work.',
'Ask: Did we use more or fewer resources than expected? Keep planned input on top. This ratio describes resource use; it does not by itself show whether enough useful output was produced.',
'Plan 10 labor hours; actually use 8. Efficiency = 10 / 8 = 1.25 = 125%. If you actually use 12.5 hours, 10 / 12.5 = 0.80 = 80%.','PI / AI',
'AI / PI|AO / PO|AO / AI',[19,20])
add('Effectiveness: actual output ÷ planned output',
'For this course, effectiveness = AO / PO. AO is actual output; PO is initial planned output. Output is the result produced. A ratio of 1 meets the output target; below 1 falls short; above 1 exceeds it. Multiply by 100 for a percentage. The output measure should represent the intended goal, including quality.',
'Ask: Did we achieve the result we planned? Actual output goes on top because you are comparing the result achieved with the target.',
'Plan 100 acceptable orders; complete 90. Effectiveness = 90 / 100 = 0.90 = 90%. Counting defective orders as acceptable would give a misleading result.',
'AO / PO','PO / AO|PI / AI|AO / AI',[19,20])
add('Productivity: actual output ÷ actual input',
'For this course, productivity = AO / AI. It measures actual output per unit of actual input, such as orders per labor hour. Calculate it for each time period to compare performance. Percentage change = (new productivity − old productivity) / old productivity × 100, provided the old value is not zero.',
'Ask: How much useful work came out for each resource unit used? Productivity has units. It is not automatically a percentage, and it uses actual values on both sides.',
'80 orders / 10 hours = 8 orders per hour. Later, 100 / 10 = 10 per hour. The increase is (10 − 8) / 8 × 100 = 25%.',
'AO / AI','PI / AI|AO / PO|AI / AO',[20])
add('The four essential processes',
'The course identifies procurement, production, fulfillment, and accounting as four interrelated processes common to businesses. Procurement obtains resources. Production makes goods or provides services. Fulfillment supplies the customer and receives payment. Accounting records and reports financial activity.',
'Think: get what you need, produce value, deliver it, and track the money. In a service organization, production means doing the service, not necessarily manufacturing a physical object.',
'A hair salon buys shampoo (procurement), performs haircuts (production/service delivery), handles bookings and payment (fulfillment), and records income and expenses (accounting).',
'Procurement, production, fulfillment, accounting',
'Marketing, human resources, sales, information technology|Planning, organizing, leading, controlling|Procurement, advertising, recruitment, storage',[21])
add('Purpose, flow, input, and output of all four processes',
'Procurement: obtain needed resources. Inputs: a need, requirements, and funds. Flow: identify need → request approval if required → select vendor/create purchase order → receive and inspect → pay. Outputs: accepted resources and purchase/payment records.\nProduction: create goods or deliver a service. Inputs: materials or information, labor, and equipment. Flow: plan → transform/perform work → check quality. Outputs: finished goods or a completed service.\nFulfillment: satisfy a customer order and receive payment. Inputs: customer order and available goods/service capacity. Flow: record sales order → prepare/pick and pack → deliver → bill/collect payment. Outputs: delivered goods/service, satisfied order, and payment records. Payment timing varies.\nAccounting: track financial events. Inputs: sales, purchases, payroll, and payment records. Flow: record → classify → reconcile/check → summarize/report. Outputs: financial statements and reliable financial records.',
'The same transaction appears from different sides. Your bakery buying flour is procurement for the bakery and fulfillment for the flour supplier. Production uses that flour; accounting records its cost and the eventual sale.',
'A purchase requisition is an internal request. A purchase order goes to the chosen vendor. A sales order records the seller’s handling of a customer order. A sales invoice requests customer payment; the buyer receives it as a vendor invoice.',
'Procurement obtains; production transforms; fulfillment delivers; accounting records finances',
'Procurement sells; production records finances; fulfillment buys; accounting manufactures|Procurement obtains; production ships only; fulfillment audits; accounting takes all orders|Procurement records finances; production buys; fulfillment transforms; accounting delivers',[21,22,23,24,25,26,27])
add('Showing whether a process works well',
'Define its goal, choose relevant measures, establish a planned target or baseline, measure actual performance, and compare under comparable conditions. Indicators include efficiency (PI/AI), effectiveness (AO/PO), productivity (AO/AI), cost, cycle time, error/defect rate, on-time delivery, and customer satisfaction. Efficacy here means how well the process achieves useful results.',
'A claim such as “the process is better” needs evidence. Cycle time means elapsed time from start to finish. A defect is an unacceptable result. Faster work is not an improvement if it creates many more errors.',
'Before: orders take 3 days and 5% are wrong. After: 2 days and 1% wrong, at comparable volume and cost. These measures make the improvement visible.',
'Compare goal-related actual results with targets or a comparable baseline',
'Count new software features without measuring work outcomes|Use only employee opinions and ignore actual performance|Assume a faster process is better regardless of quality',[19,20,28])
add('Business Process Management',
'Business Process Management (BPM) is the ongoing discipline of designing/building, executing, monitoring, evaluating, and improving business processes. It keeps work aligned with organizational goals.',
'Management here means actively looking after how work gets done over time. BPM includes measuring results and changing the process when needed; it is broader than buying a workflow app.',
'A manager maps ordering, puts it into use, measures delays, removes a bottleneck, and continues checking performance. A bottleneck is a step that slows the whole flow.',
'An ongoing cycle of designing, running, measuring, and improving processes',
'A one-time purchase of business software|Only radical replacement of every existing process|Only recording financial transactions after work ends',[28])
add('Business Process Improvement',
'Business Process Improvement (BPI) makes incremental improvements to an existing process. Incremental means smaller changes made in steps. It aims to improve outcomes, quality, cost, or speed while retaining much of the current process.',
'You start with how work happens now, find a problem, and improve that part. Smaller changes tend to be easier for people to adopt and less disruptive.',
'A purchasing team keeps its current approval process but removes duplicate data entry and clarifies who approves each request.',
'Incremental improvements to the existing process',
'Radical redesign starting from fundamental assumptions|Keeping all steps unchanged while measuring results|Replacing an organization’s goals with department goals',[30])
add('Business Process Re-engineering',
'Business Process Re-engineering (BPR) fundamentally rethinks and radically redesigns a process to seek major gains in cost, quality, service, or speed. Information technology can enable the new way of working.',
'Radical means a large change to the design, not just a small repair. BPR asks whether the old steps are needed at all. It changes work and responsibilities, not only the software screen.',
'Instead of routing paper orders through five departments, a company redesigns fulfillment around one shared order record and coordinated teams.',
'Fundamental rethinking and radical redesign for major performance gains',
'Small continuous adjustments that preserve the existing design|Replacing only the computer hardware while keeping every task|Measuring a process without ever changing it',[29,30])
add('How BPM, BPI, and BPR are similar',
'All focus on business processes and better organizational outcomes. They involve understanding work, considering customer value, and evaluating results. BPI and BPR are ways to change processes within the broader discipline of BPM.',
'Do not memorize these as three unrelated software products. BPM is the continuing management effort. Improvement and re-engineering are approaches that effort can use.',
'A company can manage fulfillment with BPM, make small BPI changes this month, and later choose BPR if the current design cannot meet its goals.',
'All focus on improving processes and organizational outcomes',
'All require radical redesign from scratch|All are names for the same software product|All avoid measuring results after a change',[28,29,30])
add('How BPM, BPI, and BPR differ',
'BPM is ongoing process management. BPI improves the existing process through smaller changes. BPR fundamentally redesigns it for larger change. BPI usually begins with the current process; BPR challenges its assumptions and may replace much of it.',
'Think about scope: managing the cycle, adjusting the current design, or replacing the design. The choice depends on the problem and the level of improvement required.',
'Shortening one approval step = BPI. Replacing the entire approval arrangement = BPR. Continuing to run, measure, and revise approvals = BPM.',
'BPM manages continuously; BPI adjusts; BPR fundamentally redesigns',
'BPM buys software; BPI replaces everything; BPR makes small tweaks|BPM and BPI are temporary projects; BPR never ends|All three differ only in the department that uses them',[28,29,30])
add('The BPI–BPR trade-off',
'BPI tends to offer smaller gains with less disruption, risk, and resistance. BPR can offer larger gains but often requires greater investment, organizational change, and implementation risk. Large gains are possible, not guaranteed.',
'Disruption means normal work is disturbed during the change. Resistance means people may struggle with or oppose unfamiliar work. Choose an approach based on the size of the problem, not just a fashionable label.',
'A small delay may need a BPI fix. A process unable to support the business’s new strategy may need BPR, even though retraining and rollout are harder.',
'Smaller, lower-disruption gains versus potentially larger gains with greater change risk',
'BPI always costs more and is riskier than BPR|BPR guarantees gains with no need to retrain people|Both have identical scope, cost, and disruption',[30])
add('Enterprise architecture and its framework',
'An enterprise is an organization or group of organizations with shared goals. Enterprise architecture (EA) is the overall design/blueprint connecting business, data, applications, and technology to those goals. An EA framework provides a structured way to describe, organize, and develop that architecture, using common views, concepts, or methods.',
'Architecture is the actual design for this organization. A framework is guidance for organizing that design. Neither is just a drawing of a building or just a list of computers.',
'A bakery chain’s EA connects its goal of fast service to ordering work, customer/order data, ordering apps, and the technology running them. A framework tells the designers which views to document.',
'EA is the enterprise blueprint; a framework structures how it is described and developed',
'EA is physical equipment; a framework is the building that houses it|EA is only software code; a framework is only customer data|EA and its framework are both the company’s day-to-day sales records',[32,33,34])
add('Key properties of enterprise architecture',
'The slides emphasize an enterprise-wide blueprint, alignment with business goals, support for organizational design/redesign, standardization, and integration. Enterprise-wide means considering the whole organization. Alignment means choices support the strategy. Standardization means agreed consistent ways of working. Integration means parts share information and work together. These help prevent tangled, unplanned “hairball” connections. The guide does not supply a separate fixed list of named properties; this answer synthesizes slides 33–36.',
'A design should help the organization work as a whole. Buying a different disconnected app for every problem can create duplicate records and complicated connections.',
'If all branches use an agreed customer ID and connected ordering records, staff can understand each other’s records and complete work across branches.',
'An enterprise-wide, strategy-aligned blueprint supporting standardization and integration',
'A hardware-only inventory with unrelated department plans|A rule requiring every organization to use one identical product|A design that deliberately prevents information sharing',[33,34,35,36])
add('Four architecture layers',
'Business architecture covers strategy, governance, organization, and processes. Data architecture covers the structure and management of data assets. Application architecture covers software applications, their interactions, and support for processes. Technology architecture covers the hardware, supporting software, networks, and technical capabilities needed to run them.',
'These are views of an enterprise, not the OSI networking layers from CIS 320. Governance means who makes decisions and what rules guide them. Data assets are useful collections of information the organization maintains.',
'Online ordering: business = how orders are fulfilled; data = customers, products, orders; application = ordering and inventory apps; technology = servers, operating systems, and networks.',
'Business, Data, Application, Technology',
'Application, Transport, Network, Physical|Strategy, Profit, Revenue, Cost|Hardware, People, Buildings, Customers',[34])
add('Centralized IT architecture',
'In the slides’ centralized/mainframe model, a central computer system runs applications and stores company data, usually managed by a central IT department. Users access it through a network. Central control can make management and standardization easier; dependence on the center must be managed.',
'Centralized describes where control and computing are concentrated. Users can still be in many buildings. It does not mean only one person can use the system.',
'All branches use the company’s central order system rather than maintaining separate branch systems and databases.',
'Computing and data are concentrated in a centrally managed system',
'Each department independently manages separate systems and data|Software functions are defined only as reusable services|Every workstation operates without any network connection',[38])
add('Decentralized IT architecture',
'Decentralized IT spreads computing, data, and management across multiple systems or locations. The slides call this server-based architecture. It can support local needs, but coordinating management, security, and standards can become harder and more costly.',
'A server is a computer/program providing services to other devices. A client requests those services. Having multiple systems makes their connections important; it does not automatically make them independent of networks.',
'One department manages a library system while another manages learning systems. They need coordination if the same student records must work across both.',
'Computing and management are spread across multiple systems or locations',
'All company work runs on one centrally controlled computer|All software must come from one cloud vendor|Users cannot access systems over a network',[39])
add('Service-oriented architecture',
'Service-oriented architecture (SOA) organizes software into reusable services that can be connected to support business processes. A service performs a defined function through an agreed interface. Slide 40 associates SOA with cloud-based architecture; technically SOA can run on premises or in the cloud, and not every cloud application is SOA.',
'Reusable means multiple applications can call the same function instead of building it repeatedly. An interface is the agreed way to request the function and receive its result.',
'An online shop and a mobile app both use the same payment-checking service. A larger ordering process combines that service with stock-checking and delivery services.',
'Reusable software services are connected to perform business work',
'All applications must run on one mainframe|Every department must keep its data isolated|Any software hosted online is automatically SOA',[40])
add('IT infrastructure',
'IT infrastructure is the actual hardware, software, networking resources, facilities, and supporting services used to operate and manage IT. Architecture describes the required design; infrastructure implements and runs it.',
'A blueprint says what must fit together. Infrastructure is the equipment and services you actually use. Cloud infrastructure still uses real equipment; it is operated remotely by a provider.',
'The design calls for reliable shared ordering. Its infrastructure includes chosen servers or cloud services, database software, networks, and support arrangements.',
'The actual technology resources and services that run IT',
'Only the business’s long-term competitive goals|Only a conceptual diagram with no installed resources|Only customer-facing application screens',[41,42])
add('Infrastructure components',
'Components include hardware such as servers, storage, and user devices; software such as operating systems, databases, and middleware; networks and communications; facilities such as power/cooling and data centers; and IT services such as operation, support, and management. Data storage/management resources support the organization’s data.',
'Middleware is software helping other programs communicate or work together. A data center is a facility that houses computing equipment. These are supporting parts of the working environment.',
'An ordering app needs a place to run, software to manage its data, a network for users to reach it, electricity, and people/services keeping it operating.',
'Hardware, software, networks, facilities, and supporting IT services',
'Only CPUs and keyboards; software is never infrastructure|Only strategic goals and customer promises|Only accounting records and marketing plans',[41,42])
add('IT platforms',
'An IT/computing platform is a hardware/software environment on which applications or services run. It provides capabilities and interfaces that those applications depend on. A platform is part of the infrastructure; it is not the entire enterprise architecture.',
'An app needs a compatible environment to run, just as a kitchen appliance needs a suitable power supply and fittings. The platform supplies the base rather than the business goal.',
'A PC with Windows is a platform for compatible desktop apps. A phone’s operating system is a platform for mobile apps. A cloud application platform provides a place and tools to run hosted apps.',
'A hardware/software environment on which applications or services run',
'A list of strategic objectives with no computing environment|A single customer’s transaction record|A diagram showing only department reporting lines',[41])
add('Strategy → architecture → infrastructure',
'Strategy sets the business direction and goals. Architecture translates those goals into a coordinated design and requirements. Infrastructure is the concrete technology selected and operated to implement that design. The intended direction is strategy drives architecture, which drives infrastructure.',
'Start with why the business needs a capability, then decide how the parts should work, and then choose what will run it. Choosing technology first can produce a system that does not solve the business problem.',
'Goal: faster pickup orders. Design: branches share live stock and order information. Infrastructure: chosen ordering software, databases, devices, and network services.',
'Strategy drives architecture, which drives infrastructure',
'Infrastructure determines goals before strategy exists|Architecture is only a synonym for purchased hardware|Strategy, architecture, and infrastructure are unrelated',[35,36,41,43])
add('Translating strategy into architecture',
'Extract goals from strategy → align goals with business requirements → derive architectural requirements → organize those requirements into the enterprise design. Then functional specifications and component specifications guide infrastructure choices. A requirement states something the solution must do or satisfy.',
'A broad goal is too vague to buy equipment from. Make the needed business behavior explicit, then work out what data, applications, and technology capabilities must support it.',
'Strategy: compete on fast delivery. Goal: fulfill orders promptly. Business requirement: staff see stock before promising delivery. Architecture requirement: ordering and inventory systems share current stock information.',
'Strategic goals → business requirements → architectural requirements',
'Hardware purchase → random features → business goals|Department preferences → isolated tools → no shared design|Architectural requirements → discard strategy → choose goals',[36,41])
add('Functional organization',
'A functional structure groups people by specialized work, such as marketing, finance, operations, or HR. People in a function develop expertise and typically report through that function’s management.',
'A function is a type of work, not a software button. Functional structure can be useful. The problem arises when departments protect their own goals while ignoring how work must move between them.',
'A marketing team knows how to reach customers. An accounting team knows financial records. Both are needed to complete profitable customer sales.',
'Grouping people by specialized business work or departments',
'Grouping every employee by which customer order arrived first|A structure that removes all specialization|A list of reusable software services only',[45,47])
add('Typical departments',
'Typical functions include marketing, sales, operations/production, procurement/purchasing, logistics/warehousing, accounting/finance, human resources (HR), and information technology (IT). Organizations vary in size and naming; one team can cover several functions.',
'HR handles people-related work such as hiring and training. Finance manages funding and financial planning; accounting records financial activity. Departments are organizational groups; a process can cross several of them.',
'Sales takes an order, operations prepares it, warehouse staff ship it, and accounting records payment. One fulfillment process crosses multiple functions.',
'Marketing/sales, operations, purchasing, finance/accounting, HR, and IT',
'CPU, memory, storage, input, and output|Efficiency, effectiveness, productivity, and quality|Business, data, application, and technology layers only',[45,46,47])
add('Silo effect',
'The silo effect occurs when departments or teams operate in isolation and prioritize local goals over the organization’s goals. It can cause duplicate work, inconsistent data, delays, poor communication, and conflicting decisions. Remedies include shared goals and measures, cross-functional teams/process owners, better communication, and integrated systems/data.',
'A silo stores something separately. Here it is a metaphor for people or information being cut off from the rest of the business. Specialization alone is not the problem; lack of coordination is.',
'Sales promises next-day delivery without checking warehouse capacity. Sales looks successful, but customers receive late orders. Shared capacity information and delivery goals help both teams make realistic promises.',
'Isolated teams prioritize their own goals, harming whole-business coordination',
'Departments build expertise while also sharing data and goals|All teams use one agreed customer record|A company removes duplicate work through integrated processes',[45,46,47])
add('Business-process perspective',
'A business-process perspective follows work from start to finish across functions, focusing on the outcome and value delivered. It helps remedy silos through shared goals, responsibility for handoffs, cross-functional coordination, and supporting shared information systems.',
'End-to-end here means from the start of business work to its final result. It is not the networking meaning from CIS 320. Instead of asking only “Did my department finish?”, ask “Did the customer get the right result?”',
'Track an order from sales through production, shipping, and payment. A process owner can address the delay between departments instead of letting each team blame another.',
'Follow work across departments toward the complete customer/business outcome',
'Maximize one department’s results without tracking later steps|Replace all specialists with identical jobs|Measure only the number of computers each department owns',[46,47])
add('Standardization',
'Standardization means using agreed, consistent procedures, definitions, or formats. Process standardization requires clearly defined, documented, and maintained ways of performing work. It supports consistency, quality control, compliance, and efficiency.',
'Consistent means people follow the same agreed approach where appropriate. It does not mean every customer or every business must be identical. Compliance means meeting applicable rules.',
'All branches use the same required fields and steps when entering orders. Employees no longer invent a different order form at each branch.',
'Using agreed, consistent procedures, definitions, or formats',
'Connecting systems without agreeing on how work is performed|Giving each department unrelated definitions for the same data|Radically redesigning every process whenever an order arrives',[48])
add('Integration',
'Integration connects data, applications, people, or processes so they work together across the enterprise. It supports information sharing and cross-functional work. Standardization makes approaches consistent; integration makes the parts work together.',
'Two departments can use identical forms yet still keep separate copies they never share: standardized but not integrated. Sharing a connected order record lets the next team act without retyping it.',
'When a sale is recorded, inventory is updated and accounting receives the transaction. Those connected actions demonstrate integration.',
'Connecting parts so information and work flow between them',
'Using the same form while keeping every record isolated|Separating all departments so they cannot share information|Documenting a procedure without connecting any work',[49])
add('Functional Area Information Systems',
'A Functional Area Information System (FAIS) supports work within a particular business function, such as payroll within HR or an accounting system within accounting. Its scope is the functional area; integration across the enterprise is not its defining feature.',
'Scope means the range of work covered. A system can be useful within one department yet leave other departments needing separate copies or manual handoffs.',
'A payroll system calculates wages for HR. If it is separate from other systems, staff may need to transfer payroll totals into financial records.',
'An information system focused on one business function',
'A system defined by integrating all enterprise functions|A hardware platform with no business software|A service used only between unrelated companies',[50,51])
add('Enterprise Information Systems',
'An Enterprise Information System (EIS) supports enterprise-wide information sharing and cross-functional processes by integrating functional work. In this course EIS means Enterprise Information System, not Executive Information System. ERP is one type of EIS.',
'Enterprise-wide means across the organization. Cross-functional means the work involves more than one department. Staff use connected information instead of disconnected department records.',
'Sales, inventory, and accounting can all act on a connected customer order, even though they perform different tasks.',
'A system integrating information and work across enterprise functions',
'A system restricted to one isolated function by definition|Only a dashboard for executives, as EIS is used in this course|Only the physical network connecting computers',[50,51,52])
add('FAIS versus EIS',
'FAIS focuses on one functional area. EIS connects functions to support enterprise-wide processes and information sharing. The difference is the scope and integration of business work, not simply the number of users or computers.',
'A large payroll system can still be functional. A smaller system connecting sales, inventory, and accounting can be enterprise-oriented. Count the connected business activities, not the machines.',
'An isolated sales application is FAIS. A shared order flowing through sales, warehouse, and accounting illustrates EIS.',
'FAIS supports a function; EIS integrates work across functions',
'FAIS always has fewer than ten users; EIS always has more|FAIS is hardware; EIS is a business strategy|FAIS integrates the whole enterprise; EIS isolates departments',[51])
add('Enterprise Resource Planning',
'Enterprise Resource Planning (ERP) is an integrated enterprise system supporting core cross-functional business processes through connected modules and shared data, commonly a common database. A module supports an area such as finance, procurement, or production. An organization chooses the modules it needs.',
'A database is an organized collection of stored data. Shared data lets departments refer to the same order rather than maintain conflicting versions. “Single version of the truth” means consistent records, not that bad data becomes correct automatically.',
'A sales order can reserve inventory, inform production, and create financial records through connected ERP modules.',
'Integrated modules and shared data support core cross-functional processes',
'A planning spreadsheet kept only by the production manager|Separate department apps designed never to share records|A network cable standard used to connect servers',[52])
add('How ERP helps',
'ERP coordinates work across functions, reduces duplicate data entry, improves access to consistent information, supports standardized processes, and gives a company-wide view for decisions. These benefits depend on good configuration, data quality, and people using the system properly.',
'Duplicate entry means typing the same facts into several systems. Each new copy is a chance for a typo or an outdated value. A shared record can reduce that problem.',
'Sales enters an order once. Warehouse staff see what to ship, and accounting sees what to bill. Teams spend less time reconciling separate lists.',
'Coordinates cross-functional work using consistent shared information',
'Automatically fixes every incorrect record without human effort|Guarantees profit as soon as software is purchased|Eliminates the need to design processes or train staff',[52])
add('ERP costs, benefits, and risks',
'Costs: software/subscriptions, implementation/configuration, data migration, integration, training, support, and ongoing maintenance. Benefits: coordinated processes, less duplicate entry, better visibility, and more consistent data. Risks: cost/schedule overruns, business disruption, poor data migration, process mismatch, resistance to change, security/access failures, and dependence on a vendor or shared system.',
'Data migration means moving existing records into the new system. Configuration means setting up rules and options. Implementation means getting the system working in the organization. A shared system spreads benefits, but a shared mistake or outage can affect many teams.',
'If product codes are copied incorrectly, purchasing, inventory, and sales can all be affected. Testing, training, clean data, and a planned rollout reduce that risk.',
'Integration benefits must be weighed against implementation costs and change/data risks',
'ERP has software costs but no training or migration costs|A common database removes all security and data-quality risks|ERP always pays for itself immediately regardless of fit',[52])
add('ERP examples',
'Examples include SAP S/4HANA, Oracle Fusion Cloud ERP, and Microsoft Dynamics 365 Finance/Supply Chain Management. These are product families that support enterprise business processes. An organization selects appropriate modules rather than necessarily buying every capability.',
'ERP is a category; SAP and Oracle are vendors offering products in that category. A word processor or standalone browser is not ERP merely because employees use it.',
'Finance and supply-chain modules can be part of an ERP solution; Microsoft Word is an individual productivity application, not an ERP suite.',
'SAP S/4HANA, Oracle Fusion Cloud ERP, Microsoft Dynamics 365 Finance',
'Microsoft Word, Google Chrome, Adobe Acrobat|Windows, Linux, macOS|TCP, IP, Ethernet',[])
add('ERP II',
'In the slides, ERP II extends ERP I with real-time access, web-based applications, and support for interorganizational processes. Interorganizational means work crossing organization boundaries, such as coordination with customers and suppliers. ERP I emphasizes internal integration; ERP II extends that reach outward.',
'The Roman numeral II means two. It describes the expanded concept in this course, not simply version 2 of a specific vendor’s software. Intraorganizational = within one organization; interorganizational = between organizations.',
'A supplier can interact with a company’s purchasing process through a web portal, using up-to-date information rather than waiting for separate emailed spreadsheets.',
'ERP extended through web access, real-time information, and interorganizational processes',
'ERP restricted to a single department with no web access|A second copy of the same database kept disconnected|A system that replaces all supplier communication with paper',[50,52])
assert len(rows)==51
out=dict(title='CIS 304 · Enterprise Architecture',module='Module I',sections=[dict(id=1,title='Foundations',reading='COB 204 / COB 300 refresher',intro='Start with information systems and the business goals they support.'),dict(id=2,title='Business Processes',reading='Reading Set 1',intro='Understand how work flows, how to measure it, and how to improve it.'),dict(id=3,title='Architecture & Infrastructure',reading='Reading Set 2',intro='Connect business strategy to the design and technology that support it.'),dict(id=4,title='Enterprise Systems',reading='Reading Set 3',intro='See how departments, processes, shared data, and ERP fit together.')],questions=rows)
(ROOT/'dist/cis304-content.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print('Wrote',len(rows),'complete guide answers')
