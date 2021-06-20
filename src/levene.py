from scipy.stats import levene

alfa = 0.05

x1 = [202, 150, 127, 158, 135, 124, 116, 102, 118, 110, 113]  # está faltando um valor

add = 0
for x in x1:
    add += x
x1.append(add / len(x1))

x2 = [142, 102, 90, 89, 88, 90, 84, 97, 110, 87, 71, 57]

x3 = [56, 44, 62, 79, 65, 81, 78, 56, 79, 85, 79, 76]

x4 = [99, 85, 97, 88, 93, 83, 79, 82, 72, 70, 81, 71]

x5 = [91, 86, 106, 100, 106, 130, 82, 89, 91, 75, 71, 72]

n = 12
n_groups = 5

levene_test, p_value = levene(
    x1, x2, x3, x4, x5, center="mean"
)  # 'trimmed' or 'median'

print(f"Estatística de teste: {levene_test}")
print(f"P-valor: {p_value}")

if p_value > alfa:
    print("Igualdade das variâncias")
else:
    print("Não igualdade das variâncias")
