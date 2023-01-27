from slotmachine import SlotMachine

#add the quantity of columns and the multiplier of win

slot1 = SlotMachine(3, {"777": 300, "888": 300, "999": 300})

slot2 = SlotMachine(4, {
    '7': 1,
    '77': 50,
    '777': 500,
    '7777': 5000,

    '1': 1,
    '11': 10,
    '111': 100,
    '1111': 1000,

    '2': 1,
    '22': 10,
    '222': 100,
    '2222': 1000,

    '3': 1,
    '33': 10,
    '333': 100,
    '3333': 1000,

    '4': 1,
    '44': 10,
    '444': 100,
    '4444': 1000,

    '5': 1,
    '55': 10,
    '555': 100,
    '5555': 1000,

    '6': 1,
    '66': 10,
    '666': 100,
    '6666': 1000,

    '8': 1,
    '88': 10,
    '888': 100,
    '8888': 1000,

    '9': 1,
    '99': 10,
    '999': 100,
    '9999': 1000
})


#print(slot1.reels)
#print(slot1.wins)

#1st - quatity of simulations, 2nd - pot Amount, 3rd - bet Amount

#print(slot1.simulation(10000, 20000, 2))
print(slot2.simulation(1000, 2000, 2))
