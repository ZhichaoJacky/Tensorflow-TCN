import numpy as np


def data_generator(t, mem_length, b_size):
    """
    Generate data for the copying memory task
    :param t: The total blank time length
    :param mem_length: The length of the memory to be recalled
    :param b_size: The batch size
    :return: Input and target data tensor
    """
    seq = np.array(np.random.randint(1, 9, size=(b_size, mem_length)), dtype=float)
    zeros = np.zeros((b_size, t))
    marker = 9 * np.ones((b_size, mem_length + 1))
    placeholders = np.zeros((b_size, mem_length))

    x = np.array(np.concatenate((seq, zeros[:, :-1], marker), 1), dtype=float)
    y = np.array(np.concatenate((placeholders, zeros, seq), 1), dtype=int)
    return np.expand_dims(x, axis=2), y


if __name__ == '__main__':
    # print(data_generator(t=601, mem_length=10, b_size=1)[0].flatten())
    # x, y = data_generator(t=601, mem_length=10, b_size=2)
    # print(x.shape, y.shape)  
    # print(x[0, :20])
    # print(y[0, -20:])
    x_train, y_train = data_generator(601, 10, 30000)
    print(y_train[0, :, 0])
    print(x_train.shape)   # (30000, 621, 1)


