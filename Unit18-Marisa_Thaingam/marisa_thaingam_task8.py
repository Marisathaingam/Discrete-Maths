print("Marisa Thaingam")
print("Task 8: Checking whether (Z9*, multiplication mod 9) is a group")

Z = [1, 2, 4, 5, 7, 8]
print("Z9* =", Z)

def mult_mod9(a, b):
    return (a * b) % 9

def check_binary():
    for a in Z:
        for b in Z:
            if mult_mod9(a, b) not in Z:
                return False
    return True

def check_associative():
    for a in Z:
        for b in Z:
            for c in Z:
                if mult_mod9(mult_mod9(a, b), c) != mult_mod9(a, mult_mod9(b, c)):
                    return False
    return True

def check_unit():
    for e in Z:
        works = True
        for a in Z:
            if mult_mod9(e, a) != a or mult_mod9(a, e) != a:
                works = False
                break
        if works:
            return e
    return False

def check_inverse(unit):
    inverses = {}
    for a in Z:
        found = False
        for b in Z:
            if mult_mod9(a, b) == unit and mult_mod9(b, a) == unit:
                inverses[a] = b
                found = True
                break
        if not found:
            return False, {}
    return True, inverses

binary_result = check_binary()
associative_result = check_associative()
unit_result = check_unit()

if unit_result is not False:
    inverse_result, inverse_map = check_inverse(unit_result)
else:
    inverse_result, inverse_map = False, {}

print("Binary operation:", binary_result)
print("Associative:", associative_result)
print("Identity element:", unit_result)
print("Every element has an inverse:", inverse_result)
print("Inverses:", inverse_map)

is_group = binary_result and associative_result and (unit_result is not False) and inverse_result
print("Conclusion: (Z9*, multiplication mod 9) is a group =", is_group)