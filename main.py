with open('dobasok.txt', "r", encoding="utf-8") as f:
    dices = f.readline().strip().split(" ")
    dices = [int(i) for i in dices]

with open('osvenyek.txt', "r", encoding="utf-8") as f:
    lines = [i.strip() for i in f.readlines()]

print("2. feladat")
print(f"A dobások száma: {len(dices)}")
print(f"Az ösvények száma: {len(lines)}")

print("3. feladat")
longest_line_index = 0
longest_line_len = len(max(lines,key=len))
for i in range(len(lines)):
    if len(lines[i]) == longest_line_len:
        longest_line_index = i+1
        break
print(f"Az egyik leghosszabb a(z) {longest_line_index}. ösvény, hossza: {longest_line_len}")

print("4. feladat")
line_index = int(input("Adja meg egy ösvény sorszámát! "))
number_of_players = int(input("Adja meg a játékosok számát! "))

print("5. feladat")
fields = {
    "M": 0,
    "V": 0,
    "E": 0
}
for line in lines[line_index-1]:
    if line == "M":
        fields["M"] += 1
    elif line == "V":
        fields["V"] += 1
    else:
        fields["E"] += 1

[print(f"{key}: {value} darab") for key, value in fields.items()]

special_fields = "EV"
with open("kulonleges.txt", "w", encoding="utf-8") as f:
    for i in range(len(lines[line_index-1])):
        if lines[line_index-1][i] in special_fields:
            f.write(f"{i+1}\t{lines[line_index-1][i]}\n")

print("7. feladat")
player_dices = {}
winners = []
for i in range(number_of_players):
    player_dices[i+1] = 0

chosen_line = lines[line_index-1]

current_player = 0
for i in range(len(dices)):
    current_player += 1
    player_dices[current_player] += dices[i]
    if player_dices[current_player] >= len(chosen_line):
        winners.append(current_player)

    if len(winners) > 0 and (i+1) % number_of_players == 0:
        print(f"A játék a(z) {(i+1)//number_of_players}. körben fejeződött be. A legtávolabb jutó(k) sorszáma: ", end="")
        [print(i, sep=" ") for i in winners]
        break

    if current_player % number_of_players == 0:
        current_player = 0

print("8. feladat")
for i in range(number_of_players):
    player_dices[i + 1] = 0

current_player = 0
winners = []

for i in range(len(dices)):

    current_player += 1
    player_dices[current_player] += dices[i]

    if player_dices[current_player] <= len(chosen_line):
        if chosen_line[player_dices[current_player] - 1] == "E":
            player_dices[current_player] += dices[i]
        elif chosen_line[player_dices[current_player] - 1] == "V":
            player_dices[current_player] -= dices[i]

    if player_dices[current_player] >= len(chosen_line):
        winners.append(current_player)
        player_dices.pop(current_player)

    if len(winners) > 0 and (i + 1) % number_of_players == 0:
        print("Nyertes(ek):", end=" ")
        print(*winners)
        print("A többiek pozíciója:")
        for key, value in player_dices.items():
            if key not in winners:
                print(f"{key}. játékos, {value}. mező")
        break

    if current_player % number_of_players == 0:
        current_player = 0