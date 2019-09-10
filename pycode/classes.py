senc =[2233, 2323, 3223, 2332, 3232, 3322]
senn =['Advaith.Y', 'Advaith.B', 'Daiwik', 'Tanishq', 'Vidit', 'Amogh']
recc =[4455, 4545, 5445, 4554, 5454, 5544]
recn =['Advaith.Y', 'Advaith.B', 'Daiwik', 'Tanishq', 'Vidit', 'Amogh']
class Trans:
    def __init__(self, tran, sencar, reccar):
        self.trs = tran
        self.a_1 = sencar
        self.a_2 = reccar
        try:
            self.senca = senc.index(sencar)
            self.senna = senn[self.senca]
            self.recca = recc.index(reccar)
            self.recna = recn[self.recca]
        except Exception as ex:
            exit("Sorry, {}".format(ex))
    def transact(self):
        if(self.trs < 1000):
            print("You sent ₹%s to %s" %(self.trs, self.recna))
            print("Your name is %s and account number is ****" %(self.senna))
        else:
            exit("Sorry you're")
acc_1 = int(input("What is your account number           "))
acc_2 = int(input("What's the reciever's account number  "))
acc_3 = int(input("How much money do you want to send    "))
trans_1 = Trans(acc_3, acc_1, acc_2)
trans_1.transact()