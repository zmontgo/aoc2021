depths = """INPUT""".splitlines()

# PART ONE

prior = None
greater = 0

for row in depths:
  num = int(row)

  if (prior and num > prior):
    greater += 1

  prior = num

print("Part one: " + greater)

# PART TWO

prior = None
greater = 0
window = 2

while (window < len(depths)):
  sum = int(depths[window]) + int(depths[window - 1]) + int(depths[window - 2])

  if (prior and sum > prior):
    greater += 1

  prior = sum
  window += 1

print("Part two: " + greater)