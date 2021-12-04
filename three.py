bits = """INPUT"""

# PART ONE

line_len = len(bits.splitlines()[0].strip())

# Make the input a single string
pretty = "".join(bits.splitlines())

# If half of the column's bits added together are ones, they should equal or surpass this value
half = int(len(bits.splitlines())/2)

i = 0

gamma = []
epsilon = []

# Loop through each column
while i < line_len:
  add = 0

  for j in pretty[i::line_len]:
    add += int(j)
    
  if (half >= add):
    gamma.append("0")
    epsilon.append("1")
  else:
    gamma.append("1")
    epsilon.append("0")

  i += 1

print("Part one:", int("".join(gamma), 2) * (int("".join(epsilon), 2)))

# PART TWO
oxy_list = bits.splitlines()
col = 0

def match(inp, col, filter):
  reply = []

  for row in inp:
    if row[col] == filter:
      reply.append(row)

  return reply

while col < len(bits.splitlines()[0]):
  pretty = "".join(oxy_list)
  filt = []

  add = 0
  zeros = 0
  ones = 0

  for j in pretty[col::line_len]:
    if (j == "0"):
      zeros += 1
    else:
      ones += 1

  if (ones >= zeros):
    filt.append("1")
  else:
    filt.append("0")

  oxy_list = match(oxy_list, col, "".join(filt))

  if (len(oxy_list) == 1):
    break
  
  col += 1

cot_list = bits.splitlines()
col = 0

while col < len(bits.splitlines()[0]):
  pretty = "".join(cot_list)
  filt = []

  add = 0
  zeros = 0
  ones = 0

  for j in pretty[col::line_len]:
    if (j == "0"):
      zeros += 1
    else:
      ones += 1

  if (zeros <= ones):
    filt.append("0")
  else:
    filt.append("1")

  cot_list = match(cot_list, col, "".join(filt))

  if (len(cot_list) == 1):
    break
  
  col += 1

print("Part two:", int(cot_list[0], 2) * int(oxy_list[0], 2))