number = [input() for _ in range(int(input()))]


def compose(f):
    def phone(number):
        f(["+62 "+c[-10:-5]+" "+c[-5:] for c in number])
    return phone


@compose
def sort(number):
    print(*sorted(number), sep='\n')


sort(number)
