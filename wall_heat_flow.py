#Calculating heat (heat energy) flow per square metter (W/m²)

#enter starting temperature, the temperature from where the heat is coming (K)
T1 = int(input('Insert T1(K): '))

#enter final temperature, temperature where the heat is comming in (K)
T2 = int(input('Insert T2(K): '))

#wall thickness (m)
L = float(input('Insert wall thickness(m): '))

#coefient of heat condutivity (W/m.K)
k = float(input('Insert wall condutivity(W/m.k): '))

#Fourier's equation
q = k*(T1-T2)/L

#printing the result
print(q, 'W/m²')