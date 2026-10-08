musicians = []
while True:
    new_musician = input("Enter a musician: ").strip().lower()
    if new_musician == "done":
        break
    else:
        musicians.append(new_musician)

votes = {}
unique_musicians = list(set(musicians))
unique_musicians.sort()



for m in unique_musicians:
    votes[m] = 0
for b in musicians:
    votes[b] += 1

print("\nVotes\n------------")
for v in votes:
    print(f"- {v.title()}: {votes[v]}")