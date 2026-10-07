votes = {"Alice": 12, "Bob": 20, "Cara": 15}

winner = None
max_value = 0

for candidate, count in votes.items():
    if count > max_value:
        max_value = count
        winner = candidate

print(f"Winner: {winner} with {max_value} votes")