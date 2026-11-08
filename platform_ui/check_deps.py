from compact_branches_payload import BRANCHES_COMPACT, BANKS_LIST, STATES_LIST, TYPES_LIST

print(f"Total branches: {len(BRANCHES_COMPACT)}")
print("Sample branch:", BRANCHES_COMPACT[0])
# Let's inspect max and min of b[4]
deps = [b[4] for b in BRANCHES_COMPACT]
print(f"Max b[4]: {max(deps)}, Min b[4]: {min(deps)}")
# How many branches have b[4] >= 4700?
print("Branches with dep >= 4700:", sum(1 for d in deps if d >= 4700))
print("Branches with dep >= 1000:", sum(1 for d in deps if d >= 1000))
print("Branches with dep >= 500:", sum(1 for d in deps if d >= 500))
print("Branches with dep >= 100:", sum(1 for d in deps if d >= 100))
print("Branches with dep >= 10:", sum(1 for d in deps if d >= 10))
print("Branches with dep >= 0:", sum(1 for d in deps if d >= 0))
print("Sample first 10 b[4] values:", deps[:10])

