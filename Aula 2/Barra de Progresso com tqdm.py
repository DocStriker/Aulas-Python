# Como fazer uma barra de progresso com o tqdm para acompanhar seu código:
from tqdm import tqdm
import time

for i in tqdm(range(10)):
    time.sleep(1)

with tqdm(total=100) as barra_de_progresso:
    for i in range(10):
        time.sleep(1)
        barra_de_progresso.update(10)
