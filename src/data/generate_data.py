import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_data():
    np.random.seed(42)

    NUM_CLIENTES = 200
    NUM_REGISTROS = 3000

    clientes = [f'C{i}' for i in range(NUM_CLIENTES)]

    dados = []

    for _ in range(NUM_REGISTROS):
        cliente = random.choice(clientes)
        
        valor = np.random.randint(100, 5000)
        
        atraso = np.random.choice(
            [0,1,2,5,10,15,30],
            p=[0.5,0.1,0.1,0.1,0.1,0.05,0.05]
        )
        
        data_pagamento = datetime.now() - timedelta(days=np.random.randint(0,180))
        
        forma_pagamento = random.choice(['boleto', 'pix', 'cartao'])
        
        qtd_pagamentos_anteriores = np.random.randint(0, 50)
        
        media_atraso_cliente = np.random.uniform(0, 15)
        
        cliente_novo = 1 if qtd_pagamentos_anteriores < 5 else 0

        regiao = random.choice(['norte', 'nordeste', 'sul', 'sudeste', 'centro oeste'])
        
        score_credito = np.random.randint(0, 1000)
        
        tipo_empresa = random.choice(['MEI', 'EI', 'SLU', 'LTDA', 'S/A', 'S/S'])

        prob_pagamento = (
            0.3
            + (score_credito / 1000) * 0.4
            + (1 - cliente_novo) * 0.2
            - (media_atraso_cliente / 30) * 0.3
        )

        prob_pagamento = max(0, min(1, prob_pagamento))
        
        pagou_em_dia = np.random.choice([1, 0], p=[prob_pagamento, 1 - prob_pagamento])
        
        dados.append([
            cliente,
            data_pagamento,
            valor,
            atraso,
            forma_pagamento,
            qtd_pagamentos_anteriores,
            media_atraso_cliente,
            cliente_novo,
            regiao,
            score_credito,
            tipo_empresa,
            prob_pagamento,
            pagou_em_dia
        ])
        
    df = pd.DataFrame(dados, columns=[
        'cliente_id',
        'data_pagamento',
        'valor',
        'dias_atraso',
        'forma_pagamento',
        'qtd_pagamentos_anteriores',
        'media_atraso_cliente',
        'cliente_novo',
        'regiao',
        'score_credito',
        'tipo_empresa',
        'probabilidade_pagamento',
        'pagou_em_dia'
    ])

    df.to_csv('data/raw/pagamentos.csv', index=False)

    print('Dataset gerado com sucesso')
    
if __name__ == '__main__':
    generate_data()