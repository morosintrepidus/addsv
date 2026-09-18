import matplotlib.pyplot as plt

nam = int(input("Nhap so sinh vien nam: "))
nu = int(input("Nhap so sinh vien nu: "))

plt.bar(["Nam", "Nu"], [nam, nu])

plt.title("So luong sinh vien nam va nu")
plt.xlabel("Gioi tinh")
plt.ylabel("So luong")

plt.savefig("bieudo.png")

print("Da tao bieu do")