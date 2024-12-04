import time
from threading import Thread

#a
def create_file_with_delay(file_name):
    time.sleep(1) 
    with open(file_name, 'w') as file:
        file.write("File created!")  

#b,в
def mnogopotoch():
    start_time = time.time()  
    threads = []  
    for i in range(100):
        thread = Thread(target=create_file_with_delay, args=(f"file_{i}.txt",))
        threads.append(thread)  
        thread.start()  

    for thread in threads:
        thread.join()  
    end_time = time.time()  
    razniza_time = end_time - start_time  
    print(f"Vse zanyalo vremeni {razniza_time} v secundax")

if __name__ == "__main__":
    mnogopotoch()
