import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.lower().str.strip()
    return df

def convert_types(df: pd.DataFrame) -> pd.DataFrame:
    df['data_pagamento'] = pd.to_datetime(df['data_pagamento'])
    df['valor'] = df['valor'].astype(float)
    return df

def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()
    
def enconde_categorical(df: pd.DataFrame) -> pd.DataFrame:
    df = pd.get_dummies(df, columns=['forma_pagamento', 'regiao', 'tipo_empresa'])
    return df

def process_data(input_path: str, output_path: str):
    df = load_data(input_path)
    df = clean_column_names(df)
    df = convert_types(df)
    df = handle_missing(df)
    df = enconde_categorical(df)
    
    df.to_csv(output_path, index=False)
    
    print('Dados processados com sucesso!')
    
if __name__ == '__main__':
    process_data(
        'data/raw/pagamentos.csv',
        'data/processed/pagamentos_processados.csv'
    )