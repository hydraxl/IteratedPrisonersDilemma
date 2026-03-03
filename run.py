import dilemma
import strategies

p1 = dilemma.Player(strategies.always_cooperate)
p2 = dilemma.Player(strategies.always_cheat)

h = dilemma.History()

dilemma.iterate_dilemma(p1, p2)

print(p1.score, p2.score)