s = [ [0, 1, 0, 0, 7, 8, 0, 0, 0],
      [0, 8, 0, 0, 4, 0, 9, 0, 0],
      [0, 0, 5, 6, 0, 0, 0, 1, 0],
      [1, 0, 0, 0, 6, 0, 0, 0, 5],
      [0, 4, 0, 9, 1, 5, 0, 7, 2],
      [0, 6, 7, 0, 8, 0, 4, 0, 0],
      [0, 0, 0, 3, 0, 0, 1, 0, 0],
      [0, 7, 0, 8, 9, 0, 0, 2, 3],
      [0, 0, 0, 0, 0, 4, 0, 0, 0] ]

def ligne (s, i):
    return [s[i][j] for j in range(9) if s[i][j] != 0]

def colonne (s, j):
    return [s[i][j] for i in range(9) if s[i][j] != 0]

def bloc(s, i, j): #1 instruction, 1 ligne
    return [s[ligne][colonne] for ligne in range ((i//3)*3, (i//3)*3+3) for colonne in range((j//3)*3, (j//3)*3+3) if s[ligne][colonne] != 0]

def possible(s, i, j): #1 instruction, 1 ligne
    return [chiffre for chiffre in range(1, 10) if chiffre not in bloc(s, i, j) and chiffre not in ligne(s, i) and chiffre not in colonne(s, j)]

def suivante(i, j):
    if j < 8:
        return (i, j + 1)
    elif j == 8:
        return (i + 1, 0)

profondeur = [0]
compteur = [0]

def solve(s, i, j, p = 0):
    compteur [0] += 1
    profondeur [0] = max(profondeur[0], p)
    if i == 9:
        return True
    elif s[i][j] > 0:
        i, j = suivante(i, j)
        return solve(s, i, j, p + 1)
    for k in possible(s, i, j):
        s[i][j] = k
        a, b = suivante(i, j)
        if solve(s, a, b, p + 1):
            return True
    s[i][j] = 0
    return False

solve(s, 0, 0)
print(s)