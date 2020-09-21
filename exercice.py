#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    nb=float(input('veuillez entrez un nombre: '))
    if nb<0:
        nb=-1*nb
    return nb


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
 for lettre in prefixes:
     nom =lettre + suffixes
     resultat.append(nom)
     
    return resultat


def prime_integer_summation() -> int:
    n=0
    c=0
    i=0
    somme=0
    
    while c<0:
     estpremier=True   
        for i in range(1,11)
          if(n%i==0 and i!=1 and i!= n)
           estpremier=False
           break
     if estpremier   
         c+=1
         n+=1
         somme+=n
    return somme


def factorial(number: int) -> int:
    return 0


def use_continue() -> None:
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
