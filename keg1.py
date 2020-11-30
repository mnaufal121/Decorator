number = [input('Masukkan angka: ') for _ in range(int(input('Jumlah no: ')))]

def compose(f):
  def phone(number):
    f(["+628"+c[-10:] for c in number])
  return phone

@compose
def sort(number):
  print(*sorted(number), sep='\n')

sort(number)