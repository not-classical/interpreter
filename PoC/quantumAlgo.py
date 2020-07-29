from system import System

def DeutschOracleNegation():
  sys = System(2)
  sys.singleGate("X", 0)
  sys.singleGate("X", 1)
  sys.singleGate("H", 0)
  sys.singleGate("H", 1)

  sys.multiGate("CNOT", 1, 0)
  sys.singleGate("X", 1)

  sys.singleGate("H", 0)
  sys.singleGate("H", 1)

  sys.collapse()

def DeutschOracleIdentity():
  sys = System(2)
  sys.singleGate("X", 0)
  sys.singleGate("X", 1)
  sys.singleGate("H", 0)
  sys.singleGate("H", 1)

  sys.multiGate("CNOT", 1, 0)

  sys.singleGate("H", 0)
  sys.singleGate("H", 1)

  sys.collapse()

def DeutschOracleConstant_0():
  sys = System(2)
  sys.singleGate("X", 0)
  sys.singleGate("X", 1)
  sys.singleGate("H", 0)
  sys.singleGate("H", 1)

  # NOP

  sys.singleGate("H", 0)
  sys.singleGate("H", 1)

  sys.collapse()

def DeutschOracleConstant_1():
  sys = System(2)
  sys.singleGate("X", 0)
  sys.singleGate("X", 1)
  sys.singleGate("H", 0)
  sys.singleGate("H", 1)

  sys.singleGate("X", 1)

  sys.singleGate("H", 0)
  sys.singleGate("H", 1)

  sys.collapse()

def SuperDenseCoding(message):
  sys = System(2)
  sys.singleGate("H", 0)
  sys.multiGate("CNOT", 0, 1)

  if message == "00":
    sys.singleGate("I", 0)
  elif message == "01":
    sys.singleGate("X", 0)
  elif message == "10":
    sys.singleGate("Z", 0)
  else:
    sys.singleGate("X", 0)
    sys.singleGate("Z", 0)

  sys.multiGate("CNOT", 0, 1)
  sys.singleGate("H", 0)
  
  sys.collapse()

def QTeleportation1():
  sys = System(3)
  sys.singleGate("X", 2)

  sys.singleGate("H", 0)
  sys.multiGate("CNOT", 0, 1)

  sys.multiGate("CNOT", 2, 0)
  sys.singleGate("H", 2)

  q0 = sys.measure(0)
  q2 = sys.measure(2)

  if q0 == 1:
    sys.singleGate("X", 1)
  if q2 == 1:
    sys.singleGate("Z", 1)
  
  sys.collapse()

def QTeleportation0():
  sys = System(3)

  sys.singleGate("H", 0)
  sys.multiGate("CNOT", 0, 1)

  sys.multiGate("CNOT", 2, 0)
  sys.singleGate("H", 2)

  q0 = sys.measure(0)
  q2 = sys.measure(2)

  if q0 == 1:
    sys.singleGate("X", 1)
  if q2 == 1:
    sys.singleGate("Z", 1)
  
  sys.collapse()



  
