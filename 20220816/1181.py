n = int(input())
spell = []
for i in range(n):
    spell.append(input())
spell = set(spell)
spell = list(spell)
spell.sort()
for i in range(1,51):
    for j in range(len(spell)):
        if len(spell[j]) == i :
            print(spell[j])
