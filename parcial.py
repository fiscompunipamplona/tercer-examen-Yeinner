from numpy import array, linspace
from math import sin, cos, pi
from pylab import plot, xlabel, ylabel, show
from scipy.integrate import odeint

from vpython import sphere, scene, vector, color, arrow, text, sleep

arrow_size = 0.1

arrow_x = arrow(pos=vector(0,0,0), axis=vector(arrow_size,0,0), color=color.red)
arrow_y = arrow(pos=vector(0,0,0), axis=vector(0,arrow_size,0), color=color.green)
arrow_z = arrow(pos=vector(0,0,0), axis=vector(0,0,arrow_size))

R = 0.02

def func (conds, t, q, B, m ): # funcion definida para los valores de theta y omega (Reducimos el grado de la ecuación)
    dvx=((q*B)/m)*conds[1]
    dvy=-((q*B)/m)*conds[0]
    dvz=0*conds[2]
    return array([dvx, dvy, dvz], float)


#Condiciones iniciales-----------------------------------------------------------------
B=1
q=1
m=1
vx=10.
vy=6.
vz=2.
t0=0.2

initcond = array([vx,vy,vz], float)#arreglos de las condiciones iniciales

n_steps = 1000 #numero de pasos
t_start = 0. #tiempo inicial
t_final = 4.#tiempo final
t_delta = (t_final - t_start) / n_steps #diferencial de tiempo
t = linspace(t_start, t_final, n_steps)#arreglo de diferencial de tiempo

solu, outodeint = odeint( func, initcond, t, args = (q,B,m), full_output=True) #solucion de la ecuacion diferencial (parametros acordes a los definidos en la funcion)


Vx, Vy, Vz = solu.T # solucion para cada paso de theta y omega

scene.range = 0.6 # tamaño de la ventana de fondo


vpx = (1/(q*B/m))*vx*sin((q*B/m)*t0)+vy*cos((q*B/m)*t0) 
vpy = (1/(q*B/m))*vx*(cos((q*B/m)*t0)-1)+vy*sin((q*B/m)*t0)
vpz = vz*t0

sleeptime = 0.0001 # tiempon con el que se utiliza la posicion de la particula

prtcl = sphere(pos=vector(vpx,vpy,vpz), radius=R, color=color.yellow) #Definimos la esfera

time_i = 0 #es un contador que se mueve ene el espacio temporal en donde se resolvio la ecuacion deferencial
t_run = 0 #tiempo en el q se ejecuta la animacion

while t_run < t_final: #animacion 
    sleep(sleeptime)
    prtcl.pos = vector( Vx[time_i]*cos((q*B/m))+Vy[time_i]*sin((q*B/m)),-Vx[time_i]*sin((q*B/m))+Vy[time_i]*cos((q*B/m)), Vz[time_i])

    t_run += t_delta
    time_i += 1
