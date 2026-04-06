import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)

NUM_CLIENTES = 200
NUM_REGISTROS = 3000

clientes = [f"C{i}" for i in range(NUM_CLIENTES)]

dados = []

for _ in range(NUM_REGISTROS):
    cliente = random.choice(clientes)
    
    valor = np.random.randint(100, 5000)
    
    atraso = np.random.choice(
        [0,1,2,5,10,15,30],
        p=[0.5,0.1,0.1,0.1,0.1,0.05,0.05]
    )
    
    data_pagamento = datetime.now() - timedelta(days=np.random.randint(0,180))
    
    forma_pagamento = random.choice(["boleto", "pix", "cartao"])
    
    qtd_pagamentos_anteriores = np.random.randint(0, 50)
    
    media_atraso_cliente = np.random.uniform(0, 15)
    
    cliente_novo = 1 if qtd_pagamentos_anteriores < 5 else 0
    
    pagou_em_dia = 1 if atraso == 0 else 0
    
    regiao = random.choice(["norte", "nordeste", "sul", "sudeste", "centro oeste"])
    
    score_credito = np.random.randint(0, 1000)
    
    tipo_empresa = random.choice(["MEI", "EI", "SLU", "LTDA", "S/A", "S/S"])
    
    dados.append([
        cliente,
        data_pagamento,
        valor,
        atraso,
        forma_pagamento,
        qtd_pagamentos_anteriores,
        media_atraso_cliente,
        cliente_novo,
        pagou_em_dia,
        regiao,
        score_credito,
        tipo_empresa
    ])
    
df = pd.DataFrame(dados, columns=[
    "cliente_id",
    "data_pagamento",
    "valor",
    "dias_atraso",
    "forma_pagamento",
    "qtd_pagamentos_anteriores",
    "media_atraso_cliente",
    "cliente_novo",
    "pagou_em_dia",
    "regiao",
    "score_credito",
    "tipo_empresa"
])

df.to_csv("data/raw/pagamentos.csv", index=False, sep=';')

print('Dataset gerado com sucesso')