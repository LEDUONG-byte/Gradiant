import numpy as np

# De bai
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

for lan in range(so_lan_thu):
    # Random diem bat dau (-5.12, 5.12)
    x = np.random.uniform(vung_gia_tri[0], vung_gia_tri[1], so_bien)
    
    # Chay gradient 1000 lan lap
    for vong in range(chay_toi_da):
        grad = tinh_dao_ham(x)
        
        # Cap nhat x 
        x_moi = x - toc_do_hoc * grad
        
        # So sanh dieu kien
        if np.linalg.norm(grad) < sai_so_cho_phep:
            x = x_moi
            break
            
        x = x_moi
    
    # Luu gia tri cuoi cua tung lan chay 
    kq_cuoi = tinh_ham_so(x)
    danh_sach_kq.append(kq_cuoi)
    print(f"Lan {lan+1}: {kq_cuoi:.4f}")

# Tinh toan thong ke 
mang_so = np.array(danh_sach_kq)

print(f"Nho nhat (Min): {np.min(mang_so):.4f}")
print(f"Lon nhat (Max): {np.max(mang_so):.4f}")
print(f"Trung binh (Mean): {np.mean(mang_so):.4f}")
print(f"Do lech (Std): {np.std(mang_so):.4f}")