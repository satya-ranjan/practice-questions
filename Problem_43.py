def card_flip(card):
    num = 0
    list1 = []
    for i in range(len(card)-1,0,-1):
        while card[i] < 0:
            num = (card[i]*2)-card[i]
            print(num)
            list1.append(num)
    print(list1)




num_friends=int(input("Enter how many friend you want to input : "))
card = list(map(int, input("Enter the card numbers : ").strip().split(",")))[:num_friends]
card_flip(card)