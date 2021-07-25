import numpy as np
import math
import statistics
 

print("Tener un txt con las coordenadas ecuatoriales del Sol y la Luna en el siguiente formato por columnas:")
print("Hora GHAs_grados GHAs_minutos Decs_grado DecS_minutos GHAm_grado GHAm_minutos DecM_grado DecM_minutos SS PS SM PM ")
print("hora: hora en UT")
print("GHAs_grado: ascensión recta del Sol (grados)")
print("GHAs_minutos: ascensión recta del Sol (minutos)")
print("DecS_grado: declinación del Sol (grados)")
print("DecS_minutos: declinación del Sol (minutos)")
print("GHAm_grado: ascensión recta de la Luna (grados)")
print("GHAm_minutos: ascensión recta de la Luna (minutos)")
print("DecM_grado: declinación de la Luna (grados)")
print("DecM_minutos: declinación de la Luna (minutos)")
print("SS: semidiámetro del Sol")
print("PS: paralaje horizontal ecuatorial del Sol")
print("SM: semidiámetro de la Luna")
print("PM: paralaje horizontal ecuatorial de la Luna")

#variables que se leerán de la lista de datos:  
hora=[]#hora en UT
GHAs_grado=[]#ascensión recta del Sol (grados)
GHAs_minutos=[]#ascensión recta del Sol (minutos)
DecS_grado=[]#declinación del Sol (grados)
DecS_minutos=[]#declinación del Sol (minutos)
GHAm_grado=[]#ascensión recta de la Luna (grados)
GHAm_minutos=[]#ascensión recta de la Luna (minutos)
DecM_grado=[]#declinación de la Luna (grados)
DecM_minutos=[]#declinación de la Luna (minutos)
SS=[]#semidiámetro del Sol
PS=[]#paralaje horizontal ecuatorial del Sol
SM=[]#semidiámetro de la Luna
PM=[]#paralaje horizontal ecuatorial de la Luna
ss=0
ps=0
sm=0
pm=0

#poner el nombre del txt:
for line in open('19Nov2021.txt', 'r'):
    values = [float(s) for s in line.split()]
    hora.append(values[0])
    GHAs_grado.append(values[1])
    GHAs_minutos.append(values[2])
    DecS_grado.append(values[3])
    DecS_minutos.append(values[4])
    GHAm_grado.append(values[5])
    GHAm_minutos.append(values[6])
    DecM_grado.append(values[7])
    DecM_minutos.append(values[8])

#condiciones por si los semidiámetros y paralajes no cambian:     
ss=float(input("Si el semidiámetro del Sol no cambia introduzcalo en minutos, sino ingrese cero:"))
if(ss==0):
#poner el nombre del txt:
    for line in open('19Nov2021.txt', 'r'):
        values = [float(s) for s in line.split()]
        SS.append(values[9])
        
else:
    SS=np.zeros(len(hora))
    for a in range(len(hora)):
        SS[a]=ss

ps=float(input("Si el paralaje del Sol no cambia introduzcalo en segundos, sino ingrese cero:"))
if(ps==0):
#poner el nombre del txt:
    for line in open('19Nov2021.txt', 'r'):
        values = [float(s) for s in line.split()]
        PS.append(values[10])
        
else:
    PS=np.zeros(len(hora))
    for b in range(len(hora)):
        PS[b]=ps
        
sm=float(input("Si el semidiámetro de la Luna no cambia introduzcalo en minutos, sino ingrese cero:"))
if(sm==0):
#poner el nombre del txt:
    for line in open('19Nov2021.txt', 'r'):
        values = [float(s) for s in line.split()]
        SM.append(values[11])
        
else:
    SM=np.zeros(len(hora))
    for c in range(len(hora)):
        SM[c]=sm

pm=float(input("Si el paralaje de la Luna no cambia introduzcalo en minutos, sino ingrese cero:"))
if(pm==0):
#poner el nombre del txt:
    for line in open('19Nov2021.txt', 'r'):
        values = [float(s) for s in line.split()]
        PM.append(values[12])
        
else:
    PM=np.zeros(len(hora))
    for d in range(len(hora)):
        PM[d]=pm


#Condición para que el signo en cada lista se mantenga dependiendo del angulo en grados:
for i in range(len(GHAs_grado)):
    if (GHAs_grado[i]<0):
        GHAs_minutos[i]=-GHAs_minutos[i]
        
for j in range(len(GHAm_grado)):
    if (GHAm_grado[j]<0):
        GHAm_minutos[j]=-GHAm_minutos[j]
        
for k in range(len(DecS_grado)):
    if (DecS_grado[k]<0):
        DecS_minutos[k]=-DecS_minutos[k]
        
for l in range(len(DecM_grado)):
    if (DecM_grado[l]<0):
        DecM_minutos[l]=-DecM_minutos[l]
    
#lista de ascenciones rectas y declinaciones en radianes:
GHAs = ((np.array(GHAs_minutos)/60) + np.array(GHAs_grado))*(np.pi/180)
GHAm = ((np.array(GHAm_minutos)/60) + np.array(GHAm_grado))*(np.pi/180)
DecS = ((np.array(DecS_minutos)/60) + np.array(DecS_grado))*(np.pi/180)
DecM = ((np.array(DecM_minutos)/60) + np.array(DecM_grado))*(np.pi/180)

#semidiámetros y paralaje horizontal ecuatorial de la Luna convertido en segundos:
SS=(np.array(SS)*60)
SM=(np.array(SM)*60)
PM=(np.array(PM)*60)


#funciones para calcular el "x" y el "y" en segundos de arco:
def x_pos(GHAsol,GHAluna,delt_s):
    x=206264.800507*np.sin(GHAluna-GHAsol+np.pi)*np.cos(delt_s)
    return x

def y_pos(epsilon,delt_s,delt_l):
    y=206264.800507*((np.sin(delt_s+delt_l))-epsilon)
    return y
#epsilon en radianes:
eps=2*np.cos(DecM)*np.sin(DecS)*((np.sin((np.pi-GHAs+GHAm)/2))**2)


#calculo de "x" y "y":
x= x_pos(GHAs, GHAm, DecM)
y= y_pos(eps,DecS, DecM)
#imprimir "x" y "y":
print("\n")
print("hora\t\t\tx\t\t\t\t\t\tepsilon\t\t\t\t\t\t\ty")
print("-----------------------------------------------------------------------------------")
for z in range(len(x)):
    print(hora[z],"\t",x[z],"\t\t",eps[z],"\t\t",y[z])
 
#calculos de "x'" y "y'" ("velocidades"):
dx=[]
for m in range(len(x)-1):
    dx.append((x[m+1]-x[m]))
    
dy=[]
for f in range(len(y)-1):
    dy.append((y[f+1]-y[f]))
#imprimir "x'" y "y'" ("velocidades"):
print("\n")
print("hora\t\t\tx'\t\t\t\t\t\ty'")
print("----------------------------------------------------------------------------------------")
for w in range(len(dx)):
    print(hora[w],"\t",dx[w],"\t",dy[w])

#promedios de "x'" y "y'" (velocidades promedio):
dxprom= statistics.mean(dx)
dyprom= statistics.mean(dy)

#imprimir promedios:
print("----------------------------------------------------------------------------------------")
print("x' promedio:",dxprom)
print("y' promedio:",dyprom)
    
#calculo de "n" y "n al cuadrado":
n2=(dxprom**2)+(dyprom**2)
n=n2**(0.5)

#calculo del tiempo medio:
print("----------------------------------------------------------------------------------------")
T0=int(input("Seleccione el tiempo más próximo a la Luna LLena:"))
indice=0
for o in range(len(hora)):
    if(T0==hora[o]):
        indice=o
    

#parametro de tiempo transcurrido desde la hora T0:
t=((x[indice]*dxprom)+(y[indice]*dyprom))/(n2)*(-1)

#tiempo medio:
T=t+T0

#convertir en hora local, Perú:
print("----------------------------------------------------------------------------------------")
h=int(input("Seleccione la zona horaria:"))
print("----------------------------------------------------------------------------------------")
T=T+(24+h)

#condición para que no se pase de 00 a 23 horas:
if(T>24):
    T=T-24
if(T<0):
    T=T+24
    

#convertir horas en horas, minutos y segundos:
Th=int(T)

Tm=(T-Th)*60
TM=int(Tm)

Ts=(Tm-TM)*60
Ts=round(Ts,2)

#pasar a min y seg
if (Th==0):
    print('Tiempo medio o máximo del eclipse: 00 h',TM,"m",Ts,"s")
    print("----------------------------------------------------------------------------------------")
else:
    print('Tiempo medio o máximo del eclipse:',Th,"h",TM,"m",Ts,"s")
    print("----------------------------------------------------------------------------------------")


#radios "eta" para cada tiempo de contacto:
eta=(51/50)*((PS[indice])+(PM[indice])+(SS[indice]))+(SM[indice])#penumbra
eta1=(51/50)*((PS[indice])+(PM[indice])-(SS[indice]))+(SM[indice])#1 y 4
eta2=(51/50)*((PS[indice])+(PM[indice])-(SS[indice]))-(SM[indice])#2 y 3

#calculo de "seno de psi":
senpsi=((x[indice]*dyprom)-(y[indice]*dxprom))/(n*eta)
senpsi1=((x[indice]*dyprom)-(y[indice]*dxprom))/(n*eta1)
senpsi2=((x[indice]*dyprom)-(y[indice]*dxprom))/(n*eta2)

if(senpsi2>1) or (senpsi2<1):
    print("Es un eclipse parcial\n")
else:
    print("Es un eclipse total\n")

#calculo de "psi":
psi=np.arcsin(senpsi)
psi1=np.arcsin(senpsi1)
psi2=np.arcsin(senpsi2)

#calculo del "coseno de psi":
cospsi=math.cos(psi)
cospsi1=math.cos(psi1)
cospsi2=math.cos(psi2)

#calculo de los tiempos de contacto:
#t0
t0=t+T0-(eta*cospsi/n)#entrada a la penumbra
#Convertir t0 en horas, minutos y segundos:
t0=t0+(24+h)

#condición para que no se pase de 00 a 23 horas:
if(t0>24):
    t0=t0-24
if(t0<0):
    t0=t0+24

#convertir en horas, minutos y segundos:
t0h=int(t0)

t0m=(t0-t0h)*60
t0M=int(t0m)

t0s=(t0m-t0M)*60
t0s=round(t0s,2)

#pasar a min y seg
if (t0h==0):
    print('Entrada al cono penumbral: 00 h',t0M,"m",t0s,"s\n")
else:
    print('Entrada al cono penumbral:',t0h,"h",t0M,"m",t0s,"s\n")

#t1
t1=t+T0-(eta1*cospsi1/n)#1ero
#Convertir t1 en horas, minutos y segundos:
t1=t1+(24+h)

#condición para que no se pase de 00 a 23 horas:
if(t1>24):
    t1=t1-24
if(t1<0):
    t1=t1+24

#convertir en horas, minutos y segundos:
t1h=int(t1)

t1m=(t1-t1h)*60
t1M=int(t1m)

t1s=(t1m-t1M)*60
t1s=round(t1s,2)

#pasar a min y seg
if (t1h==0):
    print('1er tiempo de contacto: 00 h',t1M,"m",t1s,"s\n")
else:
    print('1er tiempo de contacto:',t1h,"h",t1M,"m",t1s,"s\n")

#para 2do y 3ro
if(senpsi2>1) or (senpsi2<1):
    print("Es un eclipse parcial y no tendrá 2do y 3er tiempo de contacto\n")
else:
    #t2
    t2=t+T0-(eta2*cospsi2/n)#2do
    #Convertir t2 en horas, minutos y segundos:
    t2=t2+(24+h)
    
    #condición para que no se pase de 00 a 23 horas:
    if(t2>24):
        t2=t2-24
    if(t2<0):
        t2=t2+24
    
    #convertir en horas, minutos y segundos:
    t2h=int(t2)
    
    t2m=(t2-t2h)*60
    t2M=int(t2m)
    
    t2s=(t2m-t2M)*60
    t2s=round(t2s,2)
    
    #pasar a min y seg
    if (t2h==0):
        print('2do tiempo de contacto: 00 h',t2M,"m",t2s,"s\n")
    else:
        print('2do tiempo de contacto:',t2h,"h",t2M,"m",t2s,"s\n")


    #t3
    t3=t+T0+(eta2*cospsi2/n)#3ero
    #Convertir t3 en horas, minutos y segundos:
    t3=t3+(24+h)
    
    #condición para que no se pase de 00 a 23 horas:
    if(t3>24):
        t3=t3-24
    if(t3<0):
        t3=t3+24
    
    #convertir en horas, minutos y segundos:
    t3h=int(t3)
    
    t3m=(t3-t3h)*60
    t3M=int(t3m)
    
    t3s=(t3m-t3M)*60
    t3s=round(t3s,2)
    
    #pasar a min y seg
    if (t3h==0):
        print('2do tiempo de contacto: 00 h',t3M,"m",t3s,"s\n")
    else:
        print('2do tiempo de contacto:',t3h,"h",t3M,"m",t3s,"s\n")


#t4
t4=t+T0+(eta1*cospsi1/n)#4to    
#Convertir t4 en horas, minutos y segundos:
t4=t4+(24+h)

#condición para que no se pase de 00 a 23 horas:
if(t4>24):
    t4=t4-24
if(t4<0):
    t4=t4+24

#convertir en horas, minutos y segundos:
t4h=int(t4)

t4m=(t4-t4h)*60
t4M=int(t4m)

t4s=(t4m-t4M)*60
t4s=round(t4s,2)

#pasar a min y seg
if (t4h==0):
    print('4to tiempo de contacto: 00 h',t4M,"m",t4s,"s\n")
else:
    print('4to tiempo de contacto:',t4h,"h",t4M,"m",t4s,"s\n")
    

#t5
t5=t+T0+(eta*cospsi/n)#salida de la penumbra 
#Convertir t5 en horas, minutos y segundos:
t5=t5+(24+h)

#condición para que no se pase de 00 a 23 horas:
if(t5>24):
    t5=t5-24
if(t5<0):
    t5=t5+24

#convertir en horas, minutos y segundos:
t5h=int(t5)

t5m=(t5-t5h)*60
t5M=int(t5m)

t5s=(t5m-t5M)*60
t5s=round(t5s,2)

#pasar a min y seg
if (t5h==0):
    print('Salida del cono penumbral: 00 h',t5M,"m",t5s,"s\n")
    print("----------------------------------------------------------------------------------------")
else:
    print('Salida del cono penumbral:',t5h,"h",t5M,"m",t5s,"s\n")
    print("----------------------------------------------------------------------------------------")
