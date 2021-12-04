directions = """INPUT""".splitlines()

# PART ONE

hor = 0
ver = 0

for line in directions:
  direction = line.split(" ")

  if (direction[0] == "forward"):
    hor += int(direction[1])
  elif (direction[0] == "up"):
    ver -= int(direction[1])
  else:
    ver += int(direction[1])

print("Part one: " + hor * ver)

# PART TWO

hor = 0
ver = 0
aim = 0

for line in directions:
  direction = line.split(" ")

  if (direction[0] == "forward"):
    hor += int(direction[1])
    ver += (aim * int(direction[1]))
  elif (direction[0] == "up"):
    aim -= int(direction[1])
  else:
    aim += int(direction[1])

print("Part two: " + hor * ver)