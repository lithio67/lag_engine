import multiprocessing
import time

def heavy_computation(process_id):
  while True:
    # Intensive calculations
    for i in range(1000000):
      for j in range(1000000):
        x = i * j * i*i*j
    print(f"Process {process_id} finished iteration")
    time.sleep(0.1)

if __name__ == '__main__':
  processes = []
  for i in range(multiprocessing.cpu_count()):
    p = multiprocessing.Process(target=heavy_computation, args=(i,))
    processes.append(p)
    p.start()

  for p in processes:
    p.join()





