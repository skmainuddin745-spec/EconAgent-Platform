from compact_branches_payload import BRANCHES_COMPACT, BANKS_LIST, STATES_LIST, TYPES_LIST

def test_filter(sel_bank, sel_branch, sel_state, min_dep_m):
    count = 0
    for b in BRANCHES_COMPACT:
        bank_name = BANKS_LIST[b[1]] if b[1] < len(BANKS_LIST) else ''
        dep_m = b[4]
        b_state = STATES_LIST[b[5]] if b[5] < len(STATES_LIST) else ''
        b_type = TYPES_LIST[b[6]] if b[6] < len(TYPES_LIST) else ''

        if sel_bank != 'ALL' and sel_bank not in bank_name:
            continue
        if sel_branch != 'ALL' and sel_branch not in b_type:
            continue
        if sel_state != 'ALL' and b_state != sel_state:
            continue
        if dep_m < min_dep_m:
            continue
        count += 1
    return count

print("0:", test_filter('ALL', 'ALL', 'ALL', 0))
print("500:", test_filter('ALL', 'ALL', 'ALL', 500))
print("1000:", test_filter('ALL', 'ALL', 'ALL', 1000))
print("4700:", test_filter('ALL', 'ALL', 'ALL', 4700))

