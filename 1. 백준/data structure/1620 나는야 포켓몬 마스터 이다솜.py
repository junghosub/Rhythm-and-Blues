import sys

n, m = map(int, sys.stdin.readline().split())
pokedex = dict()

for i in range(1, n+1):
    pokedex[str(sys.stdin.readline().rstrip())] = i

pokedex_rev = dict(map(reversed, pokedex.items()))

for _ in range(m):
    pokemon = sys.stdin.readline().rstrip()
    if pokemon.isalpha():
        print(pokedex[pokemon])
    else:
        print(pokedex_rev[int(pokemon)])