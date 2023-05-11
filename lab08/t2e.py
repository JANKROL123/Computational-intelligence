import text2emotion as te
pos = open("positive.txt","rt").read()
neg = open("negative.txt","rt").read()
score_pos = te.get_emotion(pos)
score_neg = te.get_emotion(neg)
print(score_pos)
print(score_neg)