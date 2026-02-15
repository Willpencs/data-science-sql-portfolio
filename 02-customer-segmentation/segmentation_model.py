import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1. Calculando a Inércia (WCSS) para diferentes valores de K
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(df_scaled) # df_scaled é o seu dado normalizado
    wcss.append(kmeans.inertia_)

# 2. Gerando o Gráfico do Cotovelo (Elbow Method)
plt.figure(figsize=(10, 5))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('Método do Cotovelo - Definindo o Número Ideal de Clusters')
plt.xlabel('Número de Clusters (K)')
plt.ylabel('WCSS (Inércia)')
plt.grid(True)
plt.show()
