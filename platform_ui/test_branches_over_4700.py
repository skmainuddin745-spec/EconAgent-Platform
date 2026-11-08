from compact_branches_payload import BRANCHES_COMPACT

over_4700 = [b for b in BRANCHES_COMPACT if b[4] >= 4700]
print(f'Branches with deposit >= 4700: {len(over_4700)}')
for b in over_4700:
    print(b)

