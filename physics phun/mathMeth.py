import numpy as np
import matplotlib.pyplot as plt

def main():
    e_and_b_field(np.array([1., 0., 0.]))

def e_and_b_field(v0: np.ndarray):
    x = np.array([0., 0., 0.])
    e = np.array([0., 0., 1.])
    b = np.array([0., 0., 1.])
    v = v0
    m = 1.
    q = 1.

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    for t_n in np.arange(0, 10, 1000):
        f = q * (np.cross(v, b))
        a = f/m
        x += (v * 10/1000)
        m = (a * 10/1000)
        print(type(m[0]))
        print(type(v[0]))
        v += m
        print(v)

if __name__ == "__main__":
    main()