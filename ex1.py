import re 
exemple = '''
P1 est un produit compose de P2 et P3
P2 est un produit elementaire
P5 est un produit compose de P1 et P4
P4 est un produit elementaire
P9 est un produit compose de P1 et P6 et P4
P10 est un produit compose de P3 et P5
P11 est un produit compose de P5 et P3
'''
prodElem = re.findall(r'P\d+ est un produit elementaire',exemple)
print("-les Produits elementaires :")
print(prodElem)


CompOf3 = re.findall(r'P\d+ est un produit compose de P\d+ et P\d+ et P\d+',exemple)
print("-Les produits composes de trois produits: ")
print(CompOf3)


P3_P5 = re.findall(r'P\d+ est un produit compose de P3 et P5|P\d+ est un produit compose de P5 et P3',exemple)
print("-les produit compose de P3 et P5 sont: ")
print(P3_P5)


compOfP9 = re.findall(r'P\d+ est un produit compose de (P\d+) et (P\d+) et (P\d+)',exemple)
print("-P9 est compose de 3 produit sont :")
print(compOfP9)


butP2 = re.findall(r"(P\d+ est un produit composed+) de P[^2]", exemple)
print("-les produit qui compose pas P2 sont :")
print(butP2)





