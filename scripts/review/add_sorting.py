import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def extend(course,rows):
 if globals().get("only_course",course)!=course:return
 p=ROOT/f'dist/cis{course}-content.json';d=json.loads(p.read_text());ids={x['id'] for x in d['sorts']}
 for ident,n,title,items,why in rows:
  if ident in ids:continue
  q=next(q for q in d['questions'] if q['number']==n)
  d['sorts'].append(dict(id=ident,source=n,section=q['section'],q=title,items=items,teach=why))
 p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
if __name__=='__main__':
 extend('304',[
 ('304-s7',29,'Build the enterprise architecture view: business purpose down to technical support',['Business architecture','Data architecture','Application architecture','Technology architecture'],'Start with what the business needs to do. Describe its data, the applications that use that data, and the technology supporting them. This is the course study view, not a universal chronological implementation order; the domains influence one another.'),
 ('304-s8',36,'Build the direction-to-implementation relationship',['Strategy','Architecture','Infrastructure'],'Strategy sets the goals and direction. Architecture turns them into an organized design. Infrastructure supplies the concrete technology. Feedback can lead to revisions; this is the intended direction of design decisions.'),
 ('304-s9',19,'Production: build the simplified flow',['Plan the work','Transform inputs or perform the service','Check the result’s quality','Provide the finished output'],'Know what to produce before doing the work. Check that the result meets requirements. Real processes may also check quality during production and repeat steps when corrections are needed.'),
 ('304-s10',19,'Accounting: build the simplified information flow',['Record financial events','Classify the records','Reconcile and check','Summarize and report'],'First capture what happened, then organize records by category, check that they agree with supporting evidence, and report useful financial information. This is a simplified teaching flow, not every accounting procedure.'),
 ('304-s11',11,'Build DSRP in the order of its letters',['Distinctions','Systems','Relationships','Perspectives'],'D identifies what something is and is not. S considers parts and wholes. R considers connections. P considers viewpoints. This is acronym order, not a rule that thinking must always happen in four fixed steps.')])
 extend('464',[
 ('464-s9',14,'Build this nested example: broadest collection to individual work effort',['Portfolio containing a program','Program coordinating related projects','One project within that program'],'In this example the portfolio selects a strategic mix, the program coordinates related benefits, and the project delivers a particular result. Portfolios can also contain projects directly, and not every project belongs to a program.'),
 ('464-s10',43,'Follow the course’s project-document progression',['Business case: justify the investment','Project charter: authorize the project','Project management plan: guide how it will be managed'],'First explain why the project is worthwhile, then obtain formal authorization, then develop the integrated management plan. Early planning can help the case and charter; the documents can later be revisited. A business plan is not an interchangeable name for any of these.'),
 ('464-s11',47,'Turn stakeholder knowledge into an engagement approach',['Identify relevant stakeholders','Record and assess them in the stakeholder register','Plan how to engage them','Carry out engagement and review feedback'],'First learn who matters and how they are affected. Use that knowledge to plan involvement and communication, then listen to feedback. This repeats as stakeholders or project conditions change.')])
