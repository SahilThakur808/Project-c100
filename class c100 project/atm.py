class atm (object) :
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
    def cashWithdrawl(self):
        print("Cash Withdrawled")
    def balanceEnquiry(self):
        print("Balance enquiried")
sahil=atm(123456,12345)
print(sahil.cardNumber)
print(sahil.pinNumber)

