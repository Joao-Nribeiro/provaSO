import time
from connectdb import *
import random

print('='*10,'INÍCIO DAS MEDIÇÕES','='*10)
print('-'*10,'Ctrl+C para parar','-'*10,'\n')

try:
    
    vetTrans = []

    while True:

        transferencia = random.randint(100,1000)

        vetTrans.append(int(transferencia))
            
        data_hora = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        print(f'Valor Transferência: R${transferencia} | Data: {data_hora}')
        print("===============================================")
        time.sleep(2)
            
        insert_db(transferencia)
    
    
except KeyboardInterrupt:
    pass

