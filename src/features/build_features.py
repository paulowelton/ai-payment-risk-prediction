import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def categorize_score(score):
    if score < 300:
        return 'baixo'
    elif score < 700:
        return 'medio'
    else:
        return 'alto'
    
def value_range(value):
    if value < 500:
        return 'baixo'
    elif value < 2000:
        return 'medio'
    else:
        return 'alto'
    
def create_customer_features(df: pd.DataFrame) -> pd.DataFrame:
    df['media_atraso_real'] = df.groupby('cliente_id')['dias_atraso'].transform('mean')
    df['total_pagamentos'] = df.groupby('cliente_id')['valor'].transform('count')
    df['ticket_medio'] = df.groupby('cliente_id')['valor'].transform('mean')
    df['taxa_pagamento_dia'] = df.groupby('cliente_id')['pagou_em_dia'].transform('mean')
    df["score_categoria"] = df["score_credito"].apply(categorize_score)
    df["faixa_valor"] = df["valor"].apply(value_range)
    
    return df

def save_data(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)
    
def build_features(input_path: str, output_path: str):
    df = load_data(input_path)
    
    df = create_customer_features(df)
    
    save_data(df, output_path)
    
    print('Features criadas com sucesso!')
    
if __name__ == '__main__':
    build_features(
        'data/processed/pagamentos_processados.csv',
        'data/processed/pagamentos_features.csv'
    )