from scipy.stats import shapiro

alfa = 0.05

x = [
    202, 150, 127, 158, 135, 124, 116, 102,118, 110, 113, 142, 102, 90, 89, 88,
    90, 84, 97, 110, 87, 71, 57, 56, 44, 62, 79, 65, 81, 78, 56, 79, 85, 79, 76,
    99, 85, 97, 88, 93, 83, 79, 82, 72, 70, 81, 71, 91, 86, 106, 100, 106, 130,
    82, 89, 91, 75, 71, 72
]

statistic, p_value = shapiro(x)

print(f"Estatística do teste: {statistic}")
print(f"P-value: {p_value}")

if p_value > alfa:
    print("Normal")
else:
    print("Not normal")
