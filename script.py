import random
import time

planets = []
with open("planets.txt", "r") as f:
    raw = f.read()

start_time = time.time();

planets = raw.split("\n")
total_syllables = 0

syllables = []

for p in planets:
    lex = p.split("-")
    total_syllables += len(lex)
    for l in lex:
        if l not in syllables:
            syllables.append(l)
print("syllables : " + str(len(syllables)))

div_index = len(syllables) / total_syllables
div_index_str = str(div_index)[:4]
print("Diversity index : " + div_index_str)

size = len(syllables) + 1
freq = [[0] * size for i in range(size)]

for p in planets:
    lex = p.split("-")
    i = 0
    while i < len(lex) - 1:
        freq[syllables.index(lex[i])][syllables.index(lex[i+1])] += 1
        i += 1
    freq[syllables.index(lex[len(lex) - 1])][size-1] += 1
print('frequency analysis : done!\n')

num_names = 0
planet_name = ""
suffixes = ["prime", "",
            "B", "",
            "alpha", "",
            'proxima', "",
            "IV", "",
            "V", "",
            "C", "",
            "VI", "",
            "VII", "",
            "VIII", "",
            "X", "",
            "IX", "",
            "D", "",
            "", ""]
while num_names < 20:
    length = random.randint(2, 3)
    initial = random.randint(0, size - 2)
    while length > 0:
        while 1 not in freq[initial]:
            initial = random.randint(0, size - 2)
        planet_name += syllables[initial]
        initial = freq[initial].index(1)
        length -= 1
    suffix_index = random.randint(0, len(suffixes) - 1)
    planet_name += " "
    planet_name += suffixes[suffix_index]
    print(planet_name)
    planet_name = ""
    num_names += 1

end_time = time.time()
print("Completed in : " + str(end_time - start_time)[:6] + "s")
