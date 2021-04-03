from collections import defaultdict
d = defaultdict(dict)
d = dict(d)

#nombre de nœuds du graphe
keys = 7
#nom de chaque sommet
sommets = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#nombre de lieux de rendez-vous
rdv = 3
#nom de chaque sommet étant un lieu de rendez-vous
spot_rdv = ['b', 'g', 'd']
#deux noms des sommets initiaux
Initials=['e','d']
#liste de triplets (SommetInitial, SommetTerminal, Durée), rep
d[('e', 'a')] = 1
d[('a', 'e')] = 3
d[('a', 'b')] = 5
d[('b', 'a')] = 1
d[('b', 'c')] = 8

d[('c', 'b')] = 1
d[('c', 'd')] = 3
d[('d', 'c')] = 5
d[('d', 'g')] = 10
d[('g', 'd')] = 5
d[('g', 'f')] = 2

d[('f', 'g')] = 3
d[('f', 'c')] = 5
d[('c', 'f')] = 9
d[('f', 'e')] = 11
d[('e', 'f')] = 2
