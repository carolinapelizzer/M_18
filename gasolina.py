
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('gasolina.csv')

# Criar o gráfico
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='dia', y='venda', marker='o')
plt.title('Preço da Gasolina em SP nos 10 primeiros dias de Julho de 2021')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.savefig('gasolina.png')
