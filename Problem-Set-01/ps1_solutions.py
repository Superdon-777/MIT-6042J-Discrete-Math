"""
# Q1:
# a) ∃ x ∈ X (S(x) ∧ A(x))
# b) ∀ x ∈ X ((T(x) ∧ S(x)) → A(x))
# c) ∄ x ∈ X (T(x) ∧ A̅(x))
# d) ∃ x ∃ y ∃ z (T(x) ∧ S̅(x) ∧ T(y) ∧ S̅(y) ∧ T(z) ∧ S̅(z) ∧ E̅(x,y) ∧ E̅)

# Q2 (a)
# Proven the statement: NOT(P OR (Q AND R)) is equivalent to (NOT P) AND (NOT Q OR NOT R)
#
# P   Q   R   |   NOT(P OR (Q AND R))   |   (NOT P) AND (NOT Q OR NOT R)
# ----------------------------------------------------------------------
# T   T   T   |            F            |                F
# T   T   F   |            F            |                F
# T   F   T   |            F            |                F
# F   T   T   |            F            |                F
# F   F   F   |            T            |                T
# T   F   F   |            F            |                F
# F   F   T   |            T            |                T
# F   T   F   |            T            |                T


# Q2 (b)
# Disproven the statement: NOT(P && (Q OR R)) is NOT equivalent to NOT P OR (NOT Q OR NOT R)
# 
# P   Q   R   |   NOT(P && (Q OR R))    |   NOT P OR (NOT Q OR NOT R)
# -------------------------------------------------------------------
# T   T   T   |           F             |               F
# T   T   F   |           F             |               T
# T   F   T   |           F             |               T
# F   T   T   |           T             |               T
# F   F   T   |           T             |               T
# F   T   F   |           T             |               T
# T   F   F   |           T             |               T
# F   F   F   |           T             |               T

# Q3:
# a) 
# i) ¬(A and B)
# ii) (¬A) nand (¬B)
# iii) A nand (¬B)

# b) A nand A

# c) 
# Sentence 1: A nand (A nand A)
# Sentence 2: (A nand (A nand A)) nand (A nand (A nand A))

# Problem 4:
#
# Round 1:
# [Any 6 coins (a)] ---- Balance ---- [Other 6 coins (b)]
# • If b lowers? => weight_b > weight_a
# • Action? Discard coins in b; focus on coins in lot a
#
# Round 2:
# [Any 3 coins (c)] ---- Balance ---- [Other 3 coins (d)]
# • If d lowers? => weight_d > weight_c
# • Action? Discard coins in lot d; focus on coins in lot c
#
# Round 3: [Coins in Lot c]
# [Coin x1] ---- Balance ---- [Coin x2]       (Coin x3 set aside)
#
# Outcomes?
# 1) If x1 weight = x2 weight? => x3 fake
# 2) If x1 weight < x2 weight? => x1 fake
# 3) If x1 weight > x2 weight? => x2 fake
#
# ----------------------------------------------------------------------
#
# Problem 5:
#
# Contrapositive: "If r is rational, then r^(1/5) is rational"
# 
# Proof:
# ⁵√r = a / b  =>  r = a⁵ / b⁵
#
# Since a⁵ and b⁵ are integers, r is rational

# Problem 6: 
# (Statement proven because z² must be a multiple of 4 if even)
#
# w        x        y        | z²                       | Even (where i=j=1)
# --------------------------------------------------------------------------
# 2i       2i       2i       | 12i²                     | ✓
# 2i       2i       2j+1     | 8i² + 4j² + 4j + 1       | X
# 2i       2j+1     2i       | 8i² + 4j² + 4j + 1       | X
# 2j+1     2i       2i       | 8i² + 4j² + 4j + 1       | X
# 2j+1     2j+1     2i       | 4i² + 8j² + 8j + 2       | X
# 2j+1     2i       2j+1     | 4i² + 8j² + 8j + 2       | X
# 2j+1     2j+1     2j+1     | 12j² + 12j + 3           | X
# 2i       2j+1     2j+1     | 4i² + 8j² + 8j + 2       | X
#

"""
