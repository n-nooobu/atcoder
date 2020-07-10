import numpy as np
from multiprocessing import Process, Manager

def a(n, result):
    result['evm_scores'][n] = 1


if __name__ == '__main__':
    manager = Manager()
    result = manager.dict({'evm_scores': np.zeros(10, dtype=float)})

    process_list = []
    for i in range(10):
        process = Process(
            target=a,
            kwargs={'n': i, 'result': result})
        process.start()
        process_list.append(process)
    for process in process_list:
        process.join()