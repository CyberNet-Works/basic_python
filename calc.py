class Calc:
    def __init__(self, *args):
        self.add = sum(args)
        self.avg = sum(args) / len(args) if args else 0
        self.red = args[0] - sum(args[1:]) if args else 0
        self.mode = None
        self.med = None
        self.prd = args[0] * (lambda p=1: [p := p * x for x in args[1:]][-1])()
        self.div = None
        self.exp = None
        self.sqrt = None
        self.primechk = None


numbers = Calc(1,2,3,4,5,6)

print(f"sum: {numbers.add}")
print(f"avg: {numbers.avg}")
print(f"red: {numbers.red}")
print(f"mode: {numbers.mode}")
print(f"product: {numbers.prd}")

'''
factorial

n = int(input())
total = 1
i = 1

while i <= n:
    total = i * total
    i += 1

print(total)
'''