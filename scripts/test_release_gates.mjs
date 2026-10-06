#!/usr/bin/env node
/**
 * Release-boundary tests for src/worker.js's RELEASE_GATES.
 * Verifies every gated path is a 404-equivalent (gated=true) one second
 * before its release instant, and freely served (gated=false) exactly at
 * and one second after it. Run: node scripts/test_release_gates.mjs
 */
import { isGated, RELEASE_GATES, filterSitemap } from '../src/worker.js';
import { readFileSync } from 'fs';

let failures = 0;
let checks = 0;

function assert(condition, label) {
  checks++;
  if (!condition) {
    failures++;
    console.log(`  FAIL: ${label}`);
  }
}

const paths = Object.keys(RELEASE_GATES);
console.log(`Testing ${paths.length} release-gated paths...\n`);

for (const path of paths) {
  const releaseAt = new Date(RELEASE_GATES[path]);
  const oneSecBefore = new Date(releaseAt.getTime() - 1000);
  const atRelease = new Date(releaseAt.getTime());
  const oneSecAfter = new Date(releaseAt.getTime() + 1000);
  const wellBefore = new Date('2026-10-04T11:00:00Z');
  const wellAfter = new Date('2026-10-12T00:00:00Z');

  assert(isGated(path, wellBefore) === true, `${path}: gated well before release`);
  assert(isGated(path, oneSecBefore) === true, `${path}: gated 1s before release instant`);
  assert(isGated(path, atRelease) === false, `${path}: NOT gated exactly at release instant`);
  assert(isGated(path, oneSecAfter) === false, `${path}: NOT gated 1s after release instant`);
  assert(isGated(path, wellAfter) === false, `${path}: NOT gated well after release`);
}

// Non-gated paths must never be gated, at any time.
const controlPaths = ['/', '/about', '/services/water-heater-repair-nampa-id', '/nonexistent-page'];
for (const path of controlPaths) {
  assert(isGated(path, new Date('2026-10-04T11:00:00Z')) === false, `${path}: control path never gated (before)`);
  assert(isGated(path, new Date('2026-10-12T00:00:00Z')) === false, `${path}: control path never gated (after)`);
}

// All 7 approved Oct 5 batch paths must be present with that batch's release instant.
// (Revised down from 10: the 6 brand pages + /brands hub were dropped —
// their technical claims could not be verified beyond search-snippet level
// in this environment, and stripping them left thin, duplicative content.)
const oct5Paths = [
  '/repair-vs-replace-nampa-id',
  '/common-issues/water-heater-rotten-egg-smell-nampa-id',
  '/water-heater-lifespan-nampa-id',
  '/gas-vs-electric-water-heater-nampa-id',
  '/tankless-vs-tank-water-heater-nampa-id',
  '/water-heater-sizing-guide-nampa-id',
  '/water-heater-maintenance-checklist-nampa-id',
];
assert(oct5Paths.length === 7, 'exactly 7 approved Oct 5 paths expected');
for (const p of oct5Paths) {
  assert(RELEASE_GATES[p] === '2026-10-05T01:00:00Z', `${p}: present with correct release instant (01:00 UTC Oct 5 = 06:00 PKT)`);
}

// The single approved Oct 6 page (the only Oct 6 candidate ever brought to
// review status — short-cycling was rejected and never replaced) must be
// present with its own release instant.
const oct6Paths = ['/water-heater-dip-tube-failure-nampa-id'];
for (const p of oct6Paths) {
  assert(RELEASE_GATES[p] === '2026-10-06T00:00:00Z', `${p}: present with correct release instant (00:00 UTC Oct 6)`);
}

const expectedPaths = [...oct5Paths, ...oct6Paths];
assert(Object.keys(RELEASE_GATES).length === 8, 'RELEASE_GATES has exactly 8 entries, no extras');

// The 6 dropped brand pages and /brands must NOT be gated entries — they
// don't exist as files at all now, so a request 404s unconditionally,
// but confirm they were also fully removed from the gate config itself.
const droppedPaths = [
  '/brands',
  '/brands/rheem-water-heater-repair-nampa-id',
  '/brands/ao-smith-water-heater-repair-nampa-id',
  '/brands/bradford-white-water-heater-repair-nampa-id',
  '/brands/navien-water-heater-repair-nampa-id',
  '/brands/rinnai-water-heater-repair-nampa-id',
  '/brands/noritz-water-heater-repair-nampa-id',
];
for (const p of droppedPaths) {
  assert(!(p in RELEASE_GATES), `${p}: correctly absent from RELEASE_GATES (dropped from release)`);
}

// sitemap.xml must not leak any gated URL before its own release instant,
// and must include it once that instant passes — checked independently per
// batch, since Oct 5 and Oct 6 pages release at different instants.
console.log('\nTesting sitemap.xml filtering...\n');
const sitemapXml = readFileSync(new URL('../sitemap.xml', import.meta.url), 'utf-8');

const beforeAnyRelease = new Date('2026-10-04T11:00:00Z');
const filteredBeforeAny = filterSitemap(sitemapXml, beforeAnyRelease);
for (const p of expectedPaths) {
  assert(!filteredBeforeAny.includes(`https://nampawaterheater.com${p}</loc>`), `sitemap before any release: ${p} absent`);
}
// The 31 pre-existing pages must still be present pre-release.
assert(filteredBeforeAny.includes('https://nampawaterheater.com/</loc>'), 'sitemap pre-release: homepage still present');
assert(filteredBeforeAny.includes('https://nampawaterheater.com/about</loc>'), 'sitemap pre-release: /about still present');

const afterOct5OnlyRelease = new Date('2026-10-05T01:00:01Z');
const filteredAfterOct5Only = filterSitemap(sitemapXml, afterOct5OnlyRelease);
for (const p of oct5Paths) {
  assert(filteredAfterOct5Only.includes(`https://nampawaterheater.com${p}</loc>`), `sitemap after Oct 5 release only: ${p} present`);
}
for (const p of oct6Paths) {
  assert(!filteredAfterOct5Only.includes(`https://nampawaterheater.com${p}</loc>`), `sitemap after Oct 5 release only: ${p} still absent (Oct 6 not yet released)`);
}

const afterBothReleases = new Date('2026-10-06T00:00:01Z');
const filteredAfterBoth = filterSitemap(sitemapXml, afterBothReleases);
for (const p of expectedPaths) {
  assert(filteredAfterBoth.includes(`https://nampawaterheater.com${p}</loc>`), `sitemap after both releases: ${p} present`);
}

// Dropped brand paths must never appear in the raw sitemap at all, at any time.
for (const p of droppedPaths) {
  assert(!sitemapXml.includes(`https://nampawaterheater.com${p}</loc>`), `sitemap: dropped path ${p} not present in raw sitemap.xml at all`);
}

console.log(`\n${checks - failures}/${checks} checks passed.`);
if (failures > 0) {
  console.log(`${failures} FAILURE(S)`);
  process.exit(1);
} else {
  console.log('All release-boundary tests passed.');
}
