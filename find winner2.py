votes = {}

while True:
    name = input().strip()
    if name == "END":
        break
    votes[name] = votes.get(name, 0) + 1

if not votes:
    print("No votes cast")
else:
    for candidate, count in votes.items():
        print(f"{candidate}: {count}")

    winner = None
    max_value = 0
    for candidate, count in votes.items():
        if count > max_value:
            max_value = count
            winner = candidate

    print(f"Winner: {winner}")