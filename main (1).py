def Shape():
  print("What Shape Do You Want? ")
  shapes = input("Square, Triangle, Circle ")
  if shapes == "Square":
    Square()
  elif shapes == "Triangle":
    Triangle()
  elif shapes == "Circle":
    Circle()


def Triangle():
  print("    /\\")
  print("   /  \\")
  print("  /    \\")
  print(" /      \\")
  print("/________\\")


def Square():
  print(" ______ ")
  print("|      |")
  print("|      |")
  print("|______|")


def Circle():
  print("O")


Shape()