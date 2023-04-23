# %%

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('airbnb_europe.csv')


# para melhor tratamento, mudando colunas do tipo bool para int:
df['Shared Room'] = df['Shared Room'].astype(int)
df['Private Room'] = df['Private Room'].astype(int)
df['Superhost'] = df['Superhost'].astype(int)

# para encontrar e excluir possíveis outliers:


col_can_have_outliers = ['Price', 'City Center (km)', 'Metro Distance (km)', 
               'Attraction Index', 'Normalised Attraction Index', 
               'Restraunt Index', 'Normalised Restraunt Index'] 

# removendo os outliers (IQR - Distancia entre quartil superior e inferior da distribuição)
for col in col_can_have_outliers:
    Q_inferior = df[col].quantile(0.25)
    Q_superior = df[col].quantile(0.75)
    
    IQR = Q_superior - Q_inferior
    limit_low = Q_inferior - IQR * 1.7
    limit_high = Q_superior + IQR * 1.7
    
    df = df[(df[col] >= limit_low) & (df[col] <= limit_high)]



# VIS 1 - preço por cidade

plt.figure(figsize = (10, 7))
sns.histplot(data = df, x = 'Price', hue = 'City', bins = 20, multiple = 'stack', kde = True)

plt.title('Preço por cidade')
plt.xlabel('Preço')
plt.ylabel('Count')

## Amsterdã tem os preços mais altos do dataset em média
## Vienna tem os menores, em média




# %%
plt.figure(figsize = (10, 7))
sns.lineplot(x = 'Cleanliness Rating', y = 'Price', data=df)
plt.title('Variação de Preço por Taxa de Limpeza')
plt.ylabel('Preço')
plt.xlabel('Taxa de Limpeza')
## Quartos com menor taxa de limpeza ( < 5) possuem maior variação no preço 
# do que quartos com maior taxa de limpeza ( > 5)

# %%
plt.figure(figsize = (10, 7))
sns.lineplot(x = 'Guest Satisfaction', y = 'Price', data = df, color = 'green')
plt.title('Preço por Satisfação do Cliente')
plt.ylabel('Preço')
plt.xlabel('Satisfação do Cliente')
plt.show()



# %%
grouped = df.groupby(['City','Room Type'], as_index=True).agg(average_price = ('Price', 'mean'))
grouped.to_csv('average_price_by_city_by_room.csv', encoding='utf-8')

# foi criado um csv para facilitar o uso do sns
price_city_room = pd.read_csv('average_price_by_city_by_room.csv')
plt.figure(figsize=(10, 7))
sns.set_style('darkgrid')
sns.barplot(data = price_city_room, x = 'Room Type', y='average_price', hue = 'City')
plt.title('Variação de Preço por Tipo de Quarto em cada cidade')
plt.xlabel('Tipo de Quarto')
plt.ylabel('Preço Médio')

# %%
df_distance_center_satisfaction = df.groupby(['City','Guest Satisfaction'], as_index=True).agg(average_distance_center = ('City Center (km)', 'mean'))
df_distance_metro_satisfaction = df.groupby(['City','Guest Satisfaction'], as_index=True).agg(average_distance_metro = ('Metro Distance (km)', 'mean'))
df_distance_center_satisfaction.to_csv('dist_center_satisfaction.csv', encoding='utf-8')
df_distance_metro_satisfaction.to_csv('dist_metro_satisfaction.csv', encoding='utf-8')

#Criado um csv com o groupby para facilitar o manejo com o sns

df_center_guest_satisfaction = pd.read_csv('dist_center_satisfaction.csv')
plt.figure(figsize=(10, 7))
sns.scatterplot(x = 'average_distance_center', y='Guest Satisfaction', data = df_center_guest_satisfaction
                , color = 'blue', s = 20, alpha = 0.8)
plt.title('Satisfação do Cliente por Distancia do Centro')
plt.ylabel('Satisfação do Cliente')
plt.xlabel('Distancia para o centro (km)')


df_metro_guest_satisfaction = pd.read_csv('dist_metro_satisfaction.csv')
plt.figure(figsize=(10, 7))
sns.scatterplot(x = 'average_distance_metro', y='Guest Satisfaction', data = df_metro_guest_satisfaction
                , color = 'green', s = 20, alpha = 0.8)

plt.title('Satisfação do Cliente por Distancia do Metro')
plt.ylabel('Satisfação do Cliente')
plt.xlabel('Distancia para o metro (km)')



# %%
# analise de preço 

plt.figure(figsize=(10, 7))
sns.scatterplot(x='City Center (km)', y = 'Price', data = df, color = 'blue', s = 10, alpha = 0.8)
plt.title('Preço por Distancia do centro')
plt.ylabel('Preço')
plt.xlabel('Distancia do centro (km)')


plt.figure(figsize=(10, 7))
sns.scatterplot(x='Metro Distance (km)', y = 'Price', data = df, color = 'purple', s = 10, alpha = 0.8)
plt.title('Preço por Distancia do Metro')
plt.ylabel('Preço')
plt.xlabel('Distancia do metro (km)')

plt.figure(figsize=(10, 7))
sns.scatterplot(x='Normalised Attraction Index', y = 'Price', data = df, color = 'green', s = 10, alpha = 0.8)
plt.title('Preço por Indice de Atrações')
plt.ylabel('Preço')
plt.xlabel('Indice de atração')

plt.figure(figsize=(10, 7))
sns.scatterplot(x='Normalised Restraunt Index', y = 'Price', data = df, color = 'gray', s = 10, alpha = 0.8)
plt.title('Preço por Indice de restaurantes')
plt.ylabel('Preço')
plt.xlabel('Indice de restaurante')


