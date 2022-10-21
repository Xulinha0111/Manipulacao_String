"""
Formatação e Manipulação de string.
"""

# -*- coding: utf8 -*-
frase = 'Batatinha quando nasce, é colhida e vira purê.'

#-- (.upper) : Passa tudo pra maiúsculo--#
print(frase.upper())


#-- (.lower) : Passa tudo pra minúsculo--#
print(frase.lower())


#-- (.capitalize) : Passa a primeira letra pra maiúsculo--#
print(frase.capitalize())



frase2 = 'E ela morreu!!!'

#-- (.split) : Separa palavra por palavra (só o que ele entende por palavra) --#
print(frase2.split())

#-- (.replace) : Divide caracter por caracter --#
print(frase2.replace('',' '))