from pulp import LpVariable, LpProblem, LpMaximize, value

#  -------- INPUT -------------
# Definisikan variabel
# x1 maupun x2 tidak boleh bernilai negatif
x1 = LpVariable('x1', lowBound=0, cat='Integer')
x2 = LpVariable('x2', lowBound=0, cat='Integer')

# Definisikan mode maksimum
prob = LpProblem('myProblem', LpMaximize)

# Definisikan constrain
prob += (2*x1) + x2 <= 400
prob += (2*x1) + (5*x2) <= 800

# Definisikan solusi
prob += (300*x1) + (500*x2)
# --------------------------

status = prob.solve()
hasil_x1 = int(value(x1))
hasil_x2 = int(value(x2))
maksimal = int(300*hasil_x1 + 500*hasil_x2)

# Pencetakan
print('Kue dadar yang dibuat sebaiknya berjumlah', hasil_x1)
print('Kue apem yang dibuat sebaiknya berjumlah', hasil_x2)
print('Dengan keuntungan maksimum yang didapat Rp.{}' .format(maksimal))
