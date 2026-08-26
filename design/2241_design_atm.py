#Approach: Use an array to keep track of the number of banknotes of each denomination.
#When depositing, simply add the counts to the respective denominations.
#When withdrawing, start from the largest denomination and try to use as many as possible without exceeding the requested amount. 
#If the exact amount cannot be formed, return [-1]. Otherwise, return the counts of banknotes used for each denomination and update the counts in the ATM.

class ATM:

    def __init__(self):
        self.notes = [0] * 5
        self.denoms = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount):
        for i in range(5):
            self.notes[i] += banknotesCount[i]

    def withdraw(self, amount):
        used = [0] * 5

        # Take larger denominations first
        for i in range(4, -1, -1):
            take = min(self.notes[i], amount // self.denoms[i])
            used[i] = take
            amount -= take * self.denoms[i]

        # Cannot form the exact amount
        if amount != 0:
            return [-1]

        # Remove the used notes
        for i in range(5):
            self.notes[i] -= used[i]

        return used
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)