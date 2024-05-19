from ATM import ATM


def test_atm():
    obj = ATM()
    
    obj.deposit([0,0,1,2,1])
    assert obj.withdraw(600) == [0,0,1,0,1]
    obj.deposit([0,1,0,1,1])
    assert obj.withdraw(600) == [-1]
    assert obj.withdraw(550) == [0,1,0,0,1]