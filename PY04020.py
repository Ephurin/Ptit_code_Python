class Bill:
    def __init__(self, GID, name, numbers, price, ck):
        self.GID = GID
        self.name = name
        self.numbers = numbers
        self.price = price
        self.ck = ck

    def sum_price(self):
        ans = self.price * self.numbers - self.ck
        return ans
    
    def __str__(self) -> str:
        return '{} {} {} {} {} {}'.format(self.GID, self.name, self.numbers, self.price, self.ck, self.sum_price())

def cmp(a):
    return -a.sum_price()

if __name__=='__main__':
    a = []
    for t in range(int(input())):
        data = []
        for i in range(5):
            if i < 2: data.append(input())
            else: data.append(int(input()))
        a.append(Bill(data[0], data[1], data[2], data[3], data[4]))
    a.sort(key = cmp)
    for i in a:
        print(i)