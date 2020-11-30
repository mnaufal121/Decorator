# DECORATOR
def generatord(func):
  def inner(x, y):
    return func(x, y)
  return inner

@generatord
def multi(x, y):
  print(x * y)

# CLOSURES
def generatorc(y):
  def multi(x):
    return x * y
  return multi

# PROSES INPUT
datax = []
datay = []
z = int(input('Masukkan panjang list : '))
for i in range(z):
  x = int(input('Masukkan angka x: '))
  datax.append(x)
  y = int(input('Masukkan angka y: '))
  datay.append(y)

# DECORATOR
for j in range(z):
  multi(datax[j],datay[j])

# CLOSURES
for j in range(z):
  try1 = generatorc(datax[j])
  print(try1(datay[j]))