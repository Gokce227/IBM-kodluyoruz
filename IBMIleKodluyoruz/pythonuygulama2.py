import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# 2D uzaydaki noktaları içeren liste
points = [(1, 2), (4, 6), (7, 8), (2, 3), (9, 1)]

# Mesafeleri saklamak için boş liste
distances = []

# Her nokta çifti arasındaki mesafeyi hesaplayan döngü
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum mesafeyi bulma
min_distance = min(distances)

# Sonuçları yazdırma
print("Tüm mesafeler:", distances)
print("Minimum mesafe:", min_distance)
