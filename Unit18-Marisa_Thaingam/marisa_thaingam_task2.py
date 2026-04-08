from itertools import product

print("Marisa Thaingam")
print("Task 2(c): Validation of the Boolean expression")

def implication(a, b):
    return (not a) or b

# Assumption:
# ((p -> q) and (r -> s) and (not s)) -> (not p)
def original_expression(p, q, r, s):
    left_part = implication(p, q) and implication(r, s) and (not s)
    return implication(left_part, not p)

def simplified_expression(p, q, r, s):
    return (not p) or (not q) or r or s

print(f"{'p':^5}{'q':^5}{'r':^5}{'s':^5}{'original':^12}{'simplified':^12}{'same':^8}")
print("-" * 59)

all_same = True

for p, q, r, s in product([False, True], repeat=4):
    orig = original_expression(p, q, r, s)
    simp = simplified_expression(p, q, r, s)
    same = (orig == simp)
    all_same = all_same and same

    print(f"{int(p):^5}{int(q):^5}{int(r):^5}{int(s):^5}{str(orig):^12}{str(simp):^12}{str(same):^8}")

print("\nEquivalent in all cases:", all_same)