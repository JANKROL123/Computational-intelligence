from simpful import *

FS = FuzzySystem()

TLV = AutoTriangle(3, terms=['poor', 'average', 'good'], universe_of_discourse=[0,10])
FS.add_linguistic_variable("service", TLV)
FS.add_linguistic_variable("quality", TLV)

O1 = TriangleFuzzySet(0,0,10,   term="low")
O2 = TriangleFuzzySet(2,13,22,  term="medium")
O3 = TriangleFuzzySet(14,25,25, term="high")
FS.add_linguistic_variable("tip", LinguisticVariable([O1, O2, O3], universe_of_discourse=[0,25]))

FS.add_rules([
	"IF (quality IS poor) OR (service IS poor) THEN (tip IS low)",
	"IF (service IS average) THEN (tip IS medium)",
	"IF (quality IS good) OR (service IS good) THEN (tip IS high)"
	])

FS.plot_variable("quality")
FS.plot_variable("service")
FS.plot_variable("tip")

FS.set_variable("quality", 10)
FS.set_variable("service", 10)

tip = FS.inference()
print(tip)

FS.set_variable("quality", 5)
FS.set_variable("service", 5)
print(FS.inference())

FS.set_variable("quality", 0)
FS.set_variable("service", 0)
print(FS.inference())



