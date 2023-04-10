vFirstPlanet = 1.43128e15 #км^3
vSecondPlanet = 6.254e13 #км^3
pEarth = 5.5153e12 #кг/км^3

mFirstPlanet = float(input('Масса первой планеты: '))
mSecondPlanet = float(input('Масса второй планеты: '))

pFirstPlanet = mFirstPlanet / vFirstPlanet
pSecondPlanet = mSecondPlanet / vSecondPlanet
print('Плотность первой планеты:', pFirstPlanet)
print('Плотность второй планеты:', pSecondPlanet)

if abs(pEarth - pFirstPlanet) < abs(pEarth - pSecondPlanet):
    print('Плотность первой планеты ближе к плотности земли')
else:
    print('Плотность второй планеты ближе к плотности земли')