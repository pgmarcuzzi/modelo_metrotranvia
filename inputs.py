import numpy as np
# -------------------------
# GEOMETRÍA VÍA
# -------------------------
L = 100.0                               # Longitud total de vía [m]
sep_dur = 0.5                           # Separación entre durmientes [m]
n_tot = int(L / sep_dur) + 1            # Cantidad total de nodos de la vía
dof_malla = 3                           # Grados de libertad por cada nodo de la vía
g = 9.81                                # Aceleración de la gravedad [m/s²]

# -------------------------
#  PROPIEDADES RIEL
# -------------------------
a_r = np.ones(n_tot - 1) * 7.686e-3     # Área transversal del riel [m²]
gamma_r = np.ones(n_tot - 1) * 7806     # Masa específica del acero [Kg/m³]
m_r = gamma_r * a_r                     # Masa por unidad de longitud del riel [Kg/m]
e_r = np.ones(n_tot - 1) * 2.0e11       # Módulo de Young del acero [Pa]
nu = np.ones(n_tot - 1) * 0.29          # Módulo de Poisson del acero 
i_r = np.ones(n_tot - 1) * 0.03055e-3     # Momento de inercia riel [m⁴]

# -------------------------
#  PROPIEDADES PEDRAPLÉN
# -------------------------
k_b = np.ones(n_tot - 1) * 478353900 #5.3e7        # Balasto vía [N/m²] 53 000 000 478 353 900
c_b = np.ones(n_tot - 1) * 4783539 #1.0e3        # Amortiguamiento vía  [N s/m²] 
q0 = 0.0                                # Magnitud de la carga distribuida sobre vía [Kg/m]

def q(x, q0):
    return np.array([0, -q0, 0, 0, -q0, 0])

# -------------------------
#  NODOS DAÑADOS
# -------------------------

dano_nodal = {
    #45: 0.4,
    #80: 0.6,
    #47: 0.5
}
dano_nodal = None


gdl_restringidos = [0, 1, 2, (n_tot-1)*3, (n_tot-1)*3 + 1, (n_tot-1)*3 + 2]


tren_params = dict(
    n_vagones=1,                        # Cantidad de vagones
    n_ejes=6,                           # Número de ejes por vagón
    m1=4050.0,                          # Masa 1/8 vagón [Kg]
    m2=500.0,                           # Masa 1/4 bogie [Kg]
    k1=7.5e10,                          # Rigidez resorte entre vagón y bogie (susp. secundaria) [N/m]
    k2=1e11,                            # Rigidez resorte bogie y vía (susp. primaria) [N/m]
    c1=0.01,                            # Amortiguamiento entre vagón y bogie (susp. secundaria) [Ns/m]
    c2=0.01,                            # Amortiguamiento entre bogie y vía (susp. primaria) [Ns/m]
    d1=1.8,                             # Distancia entre ejes de bogie [m]
    d2=7.72,                            # Distancia entre ejes de diferentes vagones
    d3=0.0
)

t_sim = 1                               # Tiempo de simulación [s]
dt = 0.001                              # Dt de la salida
t_eval = np.arange(0, t_sim, dt)


vx_0 = 4.5                              # velocidad inicial [m/s]
vx_1 = 5.0                             # velocidad final   [m/s]
x0 = 20.0                               # posición inicial  [m]

# =========================
# CINEMÁTICA DE LA CARGA
# =========================
cinematica_params = dict(
    tipo="lineal",          # constante, lineal, trapezoidal, senoidal
    v0=vx_0,
    v1=vx_1,
    t_total=t_sim,
    x0=x0
)

# =========================
# PARÁMETROS DE SIMULACIÓN
# =========================
sim_params = dict(
    T_rampa=0.0
)


# =========================
# CONFIGURACIÓN DE LA VÍA
# =========================
dof_malla = 3
usar_amortiguamiento_rayleigh = True


# =========================
# CARGA MÓVIL – CONFIGURACIÓN
# =========================
carga_params = dict(
    x0=x0,
    Le=sep_dur
)