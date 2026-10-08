input_phrase = input("Classified phrase: ")
target_words = ["james", "london", "mi6", "classified", "paris", "midnight", "nuclear", "asset"]
phrase = input_phrase.strip().replace(".","").split()
new_phrase = ""
for w in phrase:
	unchanged = True
	for c in target_words:
		if w.lower() == c:
			unchanged = False
			break
	
	if unchanged:
		new_phrase = new_phrase + f"{w} "
	else:
		new_phrase = new_phrase + "[REDACTED] "

print(new_phrase)