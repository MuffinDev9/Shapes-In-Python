# Asks You What Shape You Want
def Shape():
  print("What Shape Do You Want? ")
  shapes = input("Square, Triangle, Circle ")
  if shapes == "Square":
    Square()
  elif shapes == "Triangle":
    Triangle()
  elif shapes == "Circle":
    Circle()


# Prints A Triangle
def Triangle():
  print("    /\\")
  print("   /  \\")
  print("  /    \\")
  print(" /      \\")
  print("/________\\")


# Prints A Square
def Square():
  print(" ______ ")
  print("|      |")
  print("|      |")
  print("|______|")


# Prints The Letter O, Bevause  I Can't Make A Big Circle
def Circle():
  print("O")


Shape()
