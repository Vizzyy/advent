with open('i', 'r') as q: print(sum(sorted([sum(e) for e in [[int(n) for n in t.split('\n')] for t in q.read().strip().split('\n\n')]])[-3:]))
