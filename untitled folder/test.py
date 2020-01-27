from math import cos, sin, tan, pi, sqrt

def step(x, y, theta, phi, dt=0.01):

    '''
    Returns a new state (xn, yn, thetan), 
    given an initial state (x, y, theta) and control phi.
    Numerical integration is done at a time step of dt [sec].
    '''

    # state rate
    dx     = cos(theta)
    dy     = sin(theta)
    dtheta = tan(phi)

    # new state (forward Euler integration)
    xn     = x     + dt*dx
    yn     = y     + dt*dy
    thetan = theta + dt*dtheta

    return xn, yn, thetan

if __name__ == "__main__":

    x0 = 0.0
    y0 = 0.0
    theta0 = 0.0

    x = 0.0
    y = 0.0
    theta = 0.0
    phi =  pi / 4.0
    print("x = %f, y = %f, theta = %f" % (x, y, theta))

    step_num = 45

    for i in range(step_num):
        x, y, theta = step(x, y, theta, phi)
    
    distance = sqrt((x - x0)**2 + (y - y0)**2)
    print("x = %f, y = %f, theta = %f" % (x, y, theta))
    print("distance = %f" % distance)

    w = distance / sqrt(2)
    print("grid width = ", w)

    # step = 30 --> chord distance = 0.298878
    # step = 29 --> chord distance = 0.288986
    # grid width = 0.2 --> diagonal length = 0.2828427