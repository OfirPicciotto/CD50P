def main():
    get_change()



def get_change():
        accepted_coins = [25, 10, 5]
        coke = 50
        sum = 0
        while sum < coke:
            user_input = int(input("Insert a coin: "))
            if user_input in accepted_coins:
                sum += user_input
                if sum - coke > 0:
                    print(f"Change owed: {abs(sum-coke)}")
                    break
                else:
                    print(f"Amount due: {abs(sum-coke)}")
            else:
               print(f"Amount due: {abs(sum-coke)}")
main()