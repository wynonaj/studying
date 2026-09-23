import { mkdir, readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';
import path from 'node:path';

const root = fileURLToPath(new URL('../', import.meta.url));
const manifest = JSON.parse(await readFile(path.join(root, '.openai/hosting.json'), 'utf8'));
if (manifest.static?.directory !== 'dist') throw new Error('Expected dist as the static site directory.');
await mkdir(path.join(root, 'artifacts'), { recursive: true });
const output = path.join(root, 'artifacts', 'cis320-recall-lab.tar.gz');
const result = spawnSync('tar', ['-czf', output, '-C', root, 'dist', '.openai/hosting.json'], { stdio: 'inherit' });
if (result.error) throw result.error;
if (result.status !== 0) process.exit(result.status || 1);
console.log(output);
