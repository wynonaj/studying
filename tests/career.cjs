const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');

const root = path.resolve(__dirname, '..');
const read = file => fs.readFileSync(path.join(root, file), 'utf8');
const data = JSON.parse(read('dist/career-content.json'));

assert.equal(data.audience, 'U.S. entry-level / May 2027 graduate');
assert.equal(data.tracks.length, 7);
assert.equal(data.modules.length, 9);
assert.equal(data.lessons.length, 34);
assert.equal(data.interviews.length, data.lessons.length);
assert.ok(data.questions.length >= 60);
assert.ok(data.sources.length >= 15);

const requiredRoles = [
  'Technology Analyst', 'IT Analyst', 'Systems Analyst',
  'Business Systems Analyst', 'Technical Business Analyst',
  'Technology Consultant', 'IT Consultant', 'Associate Technology Consultant',
  'Solutions Consultant', 'Implementation Consultant', 'Technical Consultant',
  'Technology Risk Analyst', 'IT Risk Analyst', 'IT Auditor',
  'Technology Rotational Program / Technology Development Program'
];
const mappedRoles = data.tracks.flatMap(track => track.roles);
assert.deepEqual(new Set(mappedRoles), new Set(requiredRoles));

const lessonIds = new Set(data.lessons.map(lesson => lesson.id));
const sourceIds = new Set(data.sources.map(source => source.id));
assert.equal(lessonIds.size, data.lessons.length);
assert.ok(data.modules.every(module => data.lessons.some(lesson => lesson.module === module.id)));

for (const lesson of data.lessons) {
  assert.ok(lesson.title.length > 8, lesson.id);
  assert.ok(lesson.teach.length >= 3, lesson.id);
  assert.ok(lesson.terms.length >= 2, lesson.id);
  assert.ok(lesson.example.length > 50, lesson.id);
  assert.ok(lesson.sources.every(id => sourceIds.has(id)), lesson.id);
  assert.ok(data.questions.some(question => question.lesson === lesson.id), lesson.id);
  assert.ok(data.interviews.some(question => question.lesson === lesson.id), lesson.id);
}

for (const question of data.questions) {
  assert.ok(lessonIds.has(question.lesson), question.id);
  assert.ok(question.why.length > 45, question.id);
  if (question.kind === 'mc') {
    assert.equal(question.options.length, 4, question.id);
    assert.equal(new Set(question.options).size, 4, question.id);
    assert.ok(question.options.includes(question.answer), question.id);
    assert.notEqual(question.why.trim(), question.answer.trim(), question.id);
  } else {
    assert.ok(['blank', 'sort'].includes(question.kind), question.id);
    assert.ok(Array.isArray(question.answer) && question.answer.length >= 2, question.id);
    assert.ok(question.answer.every(item => question.bank.includes(item)), question.id);
  }
}

for (const interview of data.interviews) {
  assert.equal(interview.kind, 'Original practice prompt');
  assert.equal(interview.outline.length, 3, interview.id);
  assert.ok(interview.prompt.length > 25, interview.id);
}

const career = read('dist/career.html');
const classes = read('dist/classes.html');
for (const page of ['dist/index.html', 'dist/cis304.html', 'dist/cis464.html']) {
  const html = read(page);
  assert.match(html, /href="classes\.html"/);
  assert.match(html, /href="career\.html"/);
}
assert.match(career, /MAY 2027 GRADUATE/);
assert.match(career, /id="career-track"/);
assert.match(classes, /CIS 320/);
assert.match(classes, /CIS 304/);
assert.match(classes, /CIS 464/);

for (const page of ['dist/index.html', 'dist/cis304.html', 'dist/cis464.html', 'dist/classes.html', 'dist/career.html']) {
  for (const match of read(page).matchAll(/(?:src|href)="([\w.-]+\.(?:js|css))\?v=([a-f0-9]+)"/g)) {
    const expected = crypto.createHash('sha256').update(read(`dist/${match[1]}`)).digest('hex').slice(0, 12);
    assert.equal(match[2], expected, `${page}: ${match[1]} cache hash`);
  }
}

const js = read('dist/career.js');
assert.match(js, /const CAREER_KEY='recall-career-v1'/);
assert.ok(!js.includes("setItem('cis320"));
assert.ok(!js.includes("setItem('cis304"));
assert.ok(!js.includes("setItem('cis464"));
assert.match(js, /You will try this again later in this round/);
assert.match(js, /No typing required/);
assert.match(js, /Nothing is recorded/);
assert.match(js, /not a leaked question bank/);

console.log(`PASS Career: ${data.lessons.length} entry-level lessons, ${data.questions.length} tap-based checks, ${data.interviews.length} spoken prompts, all requested roles mapped, isolated progress, source boundaries, and Classes/Career navigation.`);
