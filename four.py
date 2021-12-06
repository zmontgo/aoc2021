raw = """INPUT""".split("\n\n")

instructions = raw[0].split(",")
boards = []

for i in raw[1:]:
  board = {}
  for j in i.splitlines():
    for k in j.split():
      board[k.strip()] = False

  boards.extend([board])

def check(board):
  l = list(board.values())
  
  if (
    all(l[0:5]) or
    all(l[5:10]) or
    all(l[10:15]) or
    all(l[15:20]) or
    all(l[20:25]) or
    all(l[0::5]) or
    all(l[1::5]) or
    all(l[2::5]) or
    all(l[3::5]) or
    all(l[4::5])
  ):
    return True

  return False

def calc(board, num):
  sum = 0

  for i in board:
    if not board[i]:
      sum += int(i)

  return sum * int(num)

# PART ONE

def play():
  for round in instructions:
    for board in boards:
      if (round in board):
        board[round] = True 

      if (check(board)):
        return calc(board, round)

# PART TWO

def play_two():
  for round in instructions:
    for board in boards[:]:
      if (round in board):
        board[round] = True 

      if (check(board)):
        if len(boards) > 1:
          boards.remove(board)
        else:
          return calc(board, round)

if __name__ == "__main__":
  print("Part one", play())
  print("Part two:", play_two())