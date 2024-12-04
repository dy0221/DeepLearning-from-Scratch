import numpy as np

# f(x0,x1) = x0^2 + x1^2
def function_2(x):
    return x[0]**2 + x[1]**2

def  numerical_gradient(f,x):
    h = 1e-4 #0.0001
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]

        # f(x+h)
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # f(x-h)
        x[idx] = tmp_val-h
        fxh2 = f(x)

        grad[idx] = (fxh1-fxh2) / (2*h)
        x[idx] = tmp_val

    return grad


if __name__=='__main__':
    print(numerical_gradient(function_2 ,np.array([3.0,4.0])))
    print(numerical_gradient(function_2 ,np.array([0.0,2.0])))
    print(numerical_gradient(function_2 ,np.array([3.0,0.0])))

