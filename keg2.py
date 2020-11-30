dataorg = [{'dpn': 'Afwun', 'bkg': 'Shiddiq', 'usia': 20, 'jk': 'Laki Laki'},
           {'dpn': 'Rosalia', 'bkg': 'Benarti', 'usia': 21, 'jk': 'Perempuan'},
           {'dpn': 'Ahmad', 'bkg': 'Sentosa', 'usia': 20, 'jk': 'Laki Laki'},
           {'dpn': 'Mary', 'bkg': 'Jane', 'usia': 19, 'jk': 'Perempuan'},
           {'dpn': 'Muhammad', 'bkg': 'Jito', 'usia': 27, 'jk': 'Laki Laki'},
           {'dpn': 'Bunga', 'bkg': 'Rosalia', 'usia': 26, 'jk': 'Perempuan'}]

def renamed(jk):
  if jk == 'Laki Laki':
    return 'Mr. '
  else:
    return 'Ms. '
 
def generator(func):
    def inner(data):
      return func(data)
    return inner

@generator
def view(data):
  data.sort(key= lambda i : i['usia'])
  for orang in data:
    print(renamed(orang['jk']) + orang['dpn'] + " " + orang['bkg'])

view(dataorg)