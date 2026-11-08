const { spawn } = require('child_process');

// Let's test the bank filtering logic directly
const fs = require('fs');

// Read compact_branches_payload.py to extract arrays
const pyContent = fs.readFileSync('platform_ui/compact_branches_payload.py', 'utf8');

const banksMatch = pyContent.match(/BANKS_LIST = (\[.*?\])/s);
const statesMatch = pyContent.match(/STATES_LIST = (\[.*?\])/s);
const typesMatch = pyContent.match(/TYPES_LIST = (\[.*?\])/s);
const branchesMatch = pyContent.match(/BRANCHES_COMPACT = (\[.*?\]\n)/s);

const banksLookup = JSON.parse(banksMatch[1]);
const statesLookup = JSON.parse(statesMatch[1]);
const typesLookup = JSON.parse(typesMatch[1]);
const branchesCompact = JSON.parse(branchesMatch[1].trim());

console.log('Total branches loaded:', branchesCompact.length);

function testFilter(selBank, selBranch, selState, minDepM) {
  const filtered = branchesCompact.filter(function(b) {
    var bankName = banksLookup[b[1]] || '';
    var depM = b[4]; // Corrected index for deposit in Millions!
    var bState = statesLookup[b[5]] || '';
    var bType = typesLookup[b[6]] || '';

    if (selBank !== 'ALL' && bankName.indexOf(selBank) === -1) return false;
    if (selBranch !== 'ALL' && bType.indexOf(selBranch) === -1) return false;
    if (selState !== 'ALL' && bState !== selState) return false;
    if (depM < minDepM) return false;
    return true;
  });
  return filtered.length;
}

console.log('ALL, ALL, ALL, 0:', testFilter('ALL', 'ALL', 'ALL', 0));
console.log('ALL, ALL, ALL, 500:', testFilter('ALL', 'ALL', 'ALL', 500));
console.log('ALL, ALL, ALL, 1000:', testFilter('ALL', 'ALL', 'ALL', 1000));
console.log('ALL, ALL, ALL, 4700:', testFilter('ALL', 'ALL', 'ALL', 4700));

// Wait! What if minDepM is compared differently or what if in the OLD bmap_js_template b[4] was NOT deposit?

