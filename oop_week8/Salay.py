class test:
    def ___init___(self,test_name,test_work,test_money):
        self.name = test_name
        self.work = test_work
        self.money = test_money
    def test(self):
        o = self.money*12
        return o
    
mytest1 = test('โซเฟีย','ครู',12000)
mytest2 = test('ปีเตอร์','หมอ',45000)
mytest3 = test('บ็อบ','โปรแกรมเมอร์',40000)

print(f"{mytest1.name}ประกอบอาชีพ {mytest1.work}มีเงินเดือนทั้งปี = {mytest1.test()}")
print(f"{mytest2.name}ประกอบอาชีพ {mytest2.work}มีเงินเดือนทั้งปี = {mytest2.test()}")
print(f"{mytest3.name}ประกอบอาชีพ {mytest3.work}มีเงินเดือนทั้งปี = {mytest3.test()}")