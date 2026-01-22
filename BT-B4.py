import numpy as np
import matplotlib.pyplot as plt

#De bai
toc_do_hoc = 0.01        # alpha
sai_so_cho_phep = 1e-3   # epsilon
chay_toi_da = 1000       # so vong lap trong 1 lan chay
so_lan_thu = 20          # so lan chay
so_bien = 3              # 3 bien la x1, x2, x3 trong de ghi
vung_gia_tri = [-5.12, 5.12] 

# Cai ham de bai cho (ham nay nhap x se cho ra f(x))
def tinh_ham_so(x):
    return 30 + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))

# Dao ham cua f(x)
def tinh_dao_ham(x):
    return 2 * x + 20 * np.pi * np.sin(2 * np.pi * x)

# Mang chua gia tri cuoi cung
danh_sach_kq = []

# Them 2 bien nay de luu du lieu ve bieu do (phuc vu cau 4)
lich_su_tot_nhat = []
kq_tot_nhat = float('inf') # Gan tam la vo cung

print(f"Dang thuc hien {so_lan_thu} lan chay thu nghiem...")

for lan in range(so_lan_thu):
    # Random diem bat dau
    x = np.random.uniform(vung_gia_tri[0], vung_gia_tri[1], so_bien)
    
    # List tam de luu duong di cua lan chay hien tai
    lich_su_hien_tai = []
    
    # Chay gradient
    for vong in range(chay_toi_da):
        # Tinh gia tri ham so de luu vao lich su
        val = tinh_ham_so(x)
        lich_su_hien_tai.append(val)
        
        grad = tinh_dao_ham(x)
        x_moi = x - toc_do_hoc * grad
        
        if np.linalg.norm(grad) < sai_so_cho_phep:
            x = x_moi
            break
        x = x_moi
    
    # Lay gia tri cuoi cung
    kq_cuoi = tinh_ham_so(x)
    danh_sach_kq.append(kq_cuoi)
    
    # Kiem tra xem lan nay co tot nhat khong de luu lai ve hinh
    if kq_cuoi < kq_tot_nhat:
        kq_tot_nhat = kq_cuoi
        lich_su_tot_nhat = lich_su_hien_tai

    print(f"Lan {lan+1}: {kq_cuoi:.4f}")

# Ve hinh
plt.figure(figsize=(10, 6))
plt.plot(lich_su_tot_nhat, color='blue', linewidth=2)
plt.title('Qua trinh hoi tu')
plt.xlabel('So vong lap')
plt.ylabel('Gia tri f(x)')
plt.grid(True)
plt.savefig('bieudo.png')
plt.show()