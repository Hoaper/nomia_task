class ATM():
    def __init__(self):
        self.banknotes = [10, 50, 100, 200, 500]
        self.bank = [0, 0, 0, 0, 0]
        print("ATM created")

    def deposit(self, banknotesCount: list[int]) -> None:
        for i in range(5):
            self.bank[i] += banknotesCount[i]
        print("Deposit successful. Banknotes: ", self.bank)

    def withdraw(self, amount: int) -> list[int]:
        out_banknotes = [0, 0, 0, 0, 0]
        for i in range(4, -1, -1):
            out_banknotes[i] = min(self.bank[i], amount // self.banknotes[i])
            amount -= out_banknotes[i] * self.banknotes[i]

        if amount == 0:
            for i in range(5):
                self.bank[i] -= out_banknotes[i]
            print("Withdraw successful. Banknotes: ", self.bank)
            return out_banknotes
        else:
            print("Withdraw failed")
            return [-1]            


if __name__ == '__main__':
    obj = ATM()

    obj.deposit([0,0,1,2,1])
    print(obj.withdraw(600))

    obj.deposit([0,1,0,1,1])
    print(obj.withdraw(600))
    print(obj.withdraw(550))
