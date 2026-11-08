from compact_branches_payload import BRANCHES_COMPACT, BANKS_LIST, STATES_LIST, TYPES_LIST

# Let's see what banksLookup, statesLookup, typesLookup are in JS!
print("BANKS_LIST len:", len(BANKS_LIST), "Sample:", BANKS_LIST[:5])
print("STATES_LIST len:", len(STATES_LIST), "Sample:", STATES_LIST[:5])
print("TYPES_LIST len:", len(TYPES_LIST), "Sample:", TYPES_LIST[:5])

# In JS:
# var selBank = 'ALL';
# var selBranch = 'ALL';
# var selState = 'ALL';
# var minDepM = 4700;
# var filtered = branchesCompact.filter(function(b) {
#   var bankName = banksLookup[b[1]] || '';
#   var depM = b[4];
#   var bState = statesLookup[b[5]] || '';
#   var bType = typesLookup[b[6]] || '';
#   if (selBank !== 'ALL' && bankName.indexOf(selBank) === -1) return false;
#   if (selBranch !== 'ALL' && bType.indexOf(selBranch) === -1) return false;
#   if (selState !== 'ALL' && bState !== selState) return false;
#   if (depM < minDepM) return false;
#   return true;
# });

# But wait! How are banksLookup, statesLookup, typesLookup defined in JS?

