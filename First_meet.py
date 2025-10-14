def chit_chat():
    names = ["fizza","tooba","muteeba","khadeeja","fatima","mehak","shamsa","faiza","salma","ishrat","sonia","noor","areeba"]

    name = input("What's your name? \n").lower()

    if name in names:
        print(f"Oh! Hi {name}. It's Beautiful name.")
    else:
        print(f"Hi {name}. Nice to meet you.")

    
