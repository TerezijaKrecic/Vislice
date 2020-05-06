for n in range(2, 201):
    for d in range(2, n):
        if n % d == 0:
            break
    else: # se izpolni, če zanka ni bila predčasno prekinjena (ni blo breaka)
        print(n)
