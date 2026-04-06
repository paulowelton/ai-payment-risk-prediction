import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def prepare_data(df: pd.DataFrame):
    df = df.copy()
    
    df = df.drop(columns=['cliente_id', 'data_pagamento', 'dias_atraso', 'media_atraso_real', 'taxa_pagamento_dia'], errors='ignore')
    
    X = df.drop('pagou_em_dia', axis=1)
    y = df['pagou_em_dia']
    
    X = pd.get_dummies(X)
    
    return X, y

def split_data(X, y):
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    
def save_model(model, path: str):
    joblib.dump(model, path)
    
def main():
    df = load_data('data/processed/pagamentos_features.csv')
    
    X, y = prepare_data(df)
    
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    model = train_model(X_train, y_train)
    
    evaluate_model(model, X_test, y_test)
    
    joblib.dump(X.columns, 'models/columns.pkl')
    save_model(model, 'models/model.pkl')
    
    print('Modelo treinado e salvo com sucesso!')
    
if __name__ == '__main__':
    main()