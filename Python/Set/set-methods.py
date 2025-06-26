# s1 = {1, 2, 3}

# s2 = {3, 4, 5}


# 1️⃣ s1.union(s2)
# ✔ Combines all unique elements from both sets
# ✔ Original s1 stays unchanged

# Result:
# {1, 2, 3, 4, 5}


# 2️⃣ s1.intersection(s2)
# ✔ Finds common elements in both sets
# ✔ Original s1 unchanged

# Result:
# {3}


# 3️⃣ s1.difference(s2)
# ✔ Elements in s1 but not in s2
# ✔ Original s1 unchanged

# Result:
# {1, 2}


# 4️⃣ s1.issubset(s2)
# ✔ Checks if all elements of s1 exist in s2

# Result:
# False — Because 1 and 2 not in s2


# 5️⃣ s1.isdisjoint(s2)
# ✔ Checks if sets have no common elements

# Result:
# False — Because 3 is common


# 6️⃣ s1.issuperset(s2)
# ✔ Checks if s1 contains all elements of s2

# Result:
# False — s2 has 4, 5 which s1 doesn't


# 7️⃣ s1.intersection_update(s2)
# ✔ Modifies s1 to keep only common elements

# Before: s1 = {1, 2, 3}
# After: s1 = {3}


# 8️⃣ s1.difference_update(s2)
# ✔ Removes elements from s1 found in s2

# Before: s1 = {3}
# After: s1 = set() — because 3 removed


# 9️⃣ s1.symmetric_difference(s2)
# ✔ Elements in either set, but not both
# ✔ Original s1 stays unchanged

# Before Reset s1 to {1, 2, 3}
# Result: {1, 2, 4, 5}


# 🔟 s1.symmetric_difference_update(s2)
# ✔ Modifies s1 to hold symmetric difference

# Before: s1 = {1, 2, 3}
# After: s1 = {1, 2, 4, 5}

# 🧩 Summary Table
# |---------------------------------|-------------------------------------|----------------------------|
# | Method                          | What it Did                         | s1 After Operation         |
# |---------------------------------|-------------------------------------|----------------------------|
# | union(s2)                       | Combined all unique elements        | {1, 2, 3} (unchanged)      |
# | intersection(s2)                | Common elements                     | {1, 2, 3} (unchanged)      |
# | difference(s2)                  | s1 elements not in s2               | {1, 2, 3} (unchanged)      |
# | issubset(s2)                    | Checked if s1 inside s2             | False                      |
# | isdisjoint(s2)                  | Checked if no common elements       | False                      |
# | issuperset(s2)                  | Checked if s1 contains all s2       | False                      |
# | intersection_update(s2)         | s1 became only common elements      | {3}                        |
# | difference_update(s2)           | Removed s2 elements from s1         | set()                      |
# | symmetric_difference(s2)        | Elements in either, not both        | {1, 2, 4, 5}               |
# | symmetric_difference_update(s2) | s1 modified to symmetric difference | {1, 2, 4, 5}               |
# |---------------------------------|-------------------------------------|----------------------------|