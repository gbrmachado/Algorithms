W = 6

Mochila = [ #(Valor, peso)
            (10, 4),
            (6,3),
            (7,2),
            (3,1),
        ]

nItem = len(Mochila)
M = [[0 for x in range(W+1)] for x in range(nItem+1)]
for i in range(1, nItem + 1):
    for j in range(1, W+1):
        valor = Mochila[i-1][0]
        peso = Mochila[i-1][1]
        difM = j - peso
        if difM >= 0:
            M[i][j] = max(M[i-1][difM] + valor, M[i-1][j])

for m in M:
    print m


