import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

if __name__=='__main__':
    t = [0, 0 , 1, 0 , 0, 0, 0, 0, 0, 0]

    y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]

    print(mean_squared_error(np.array(y), np.array(t)))

    y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]

    print(mean_squared_error(np.array(y), np.array(t)))