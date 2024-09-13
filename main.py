"""c"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """f"""

    # votre code ici
    pre=True
    if p==1:
        return False
    for d in range (2,int(sqrt(p)+1)):
        if p%d==0:
            pre = False
    return pre

#### Fonction principale


def main():
    """h"""

    # vos appels à la fonction secondaire ici

    for n in range(0, 100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
