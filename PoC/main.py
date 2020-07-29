from system import System
import quantumAlgo as QA

print("Deutsch Oracle Negation")
print("Expected: |10>")
QA.DeutschOracleNegation()

print("Deutsch Oracle Identity")
print("Expected: |10>")
QA.DeutschOracleIdentity()

print("Deutsch Oracle Constant 0")
print("Expected: |11>")
QA.DeutschOracleConstant_0()

print("Deutsch Oracle Constant 1")
print("Expected: |11>")
QA.DeutschOracleConstant_1()

print("Super Dense Coding")
print("Expected: {00}")
QA.SuperDenseCoding("00")

print("Super Dense Coding")
print("Expected: {01}")
QA.SuperDenseCoding("01")

print("Super Dense Coding")
print("Expected: {10}")
QA.SuperDenseCoding("10")

print("Super Dense Coding")
print("Expected: {11}")
QA.SuperDenseCoding("11")

print("Quantum Teleportation")
print("Expected: |?1?>")
QA.QTeleportation1()

print("Quantum Teleportation")
print("Expected: |?0?>")
QA.QTeleportation0()