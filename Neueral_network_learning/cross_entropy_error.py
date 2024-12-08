import numpy as np

def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        
    # 훈련 데이터가 원-핫 벡터라면 정답 레이블의 인덱스로 반환
    if t.size == y.size:
        t = t.argmax(axis=1)

    # if t.dtype != int:  # 정수형으로 변환
    #     t = t.astype(int)
             
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size # t가 float64여서 에러 발생 << int 형으로

if __name__=='__main__':
    t = [0, 0 , 1, 0 , 0, 0, 0, 0, 0, 0]

    y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]

    print(cross_entropy_error(np.array(y), np.array(t)))

    y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]

    print(cross_entropy_error(np.array(y), np.array(t)))