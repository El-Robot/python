import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    w = .75
    v_0 = 1
    R = 1.5

    total_d = 2 * R
    t_f = total_d / v_0 

    r_lin = [np.abs(R - v_0 * t) for t in np.linspace(0, t_f, 1000)]
    th_lin = [np.piecewise(t, [R - v_0 * t <= 0, R - v_0 * t > 0], [0, np.pi]) for t in np.linspace(0, t_f, 1000)]

    r_rot = [np.abs(R - v_0 * t) for t in np.linspace(0, t_f, 100000)]
    th_rot = [np.piecewise(t, [R - v_0 * t <= 0, R - v_0 * t > 0], [np.pi + w * t, w* t]) for t in np.linspace(0, t_f, 100000)]

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    
    plt.polar(th_lin, r_lin)
    plt.polar(th_rot, r_rot)

    plt.show()
    