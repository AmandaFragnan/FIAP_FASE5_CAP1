import matplotlib.pyplot as plt
import numpy as np

regions = ["São Paulo (sa-east-1)", "Virgínia do Norte (us-east-1)"]
ec2_costs = [9.782, 6.132]  # Custo da instância EC2 (mensal)
storage_costs = [7.60, 4.00]  # Custo do armazenamento EBS (mensal)

x = np.arange(len(regions))
width = 0.4

fig, ax = plt.subplots(figsize=(8, 5))
rects1 = ax.bar(x - width/2, ec2_costs, width, label="EC2 (Instância)")
rects2 = ax.bar(x + width/2, storage_costs, width, label="EBS (Armazenamento)")

ax.set_xlabel("Região AWS")
ax.set_ylabel("Custo Mensal (USD)")
ax.set_title("Comparação de Custos AWS - EC2 + EBS")
ax.set_xticks(x)
ax.set_xticklabels(regions)
ax.legend()

for rect in rects1 + rects2:
    height = rect.get_height()
    ax.annotate(f"{height:.2f}",
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')
plt.show()