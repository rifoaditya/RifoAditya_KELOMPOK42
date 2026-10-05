# Sistem Evaluasi Nilai UTBK - Watermark: Kelompok 42
def info_sistem():
    """Function Non-return type tanpa parameter"""
    print("=" * 55)
    print(" SISTEM EVALUASI NILAI UTBK - KELOMPOK 42 ")
    print("=" * 55)

def hitung_skor_akhir(pm, bi, bing):
    """Function Return type berparameter"""
    return (pm * 0.4) + (bi * 0.3) + (bing * 0.3)

class PesertaUTBK:
    def __init__(self, nama):
        self.nama = nama
        self.skor = 0

    def set_skor(self, skor_baru):
        """Method Non-return type berparameter"""
        self.skor = skor_baru
        print(f"> Skor untuk {self.nama} berhasil diupdate menjadi {self.skor:.2f}")

    def get_status_kelulusan(self):
        """Method Return type tanpa parameter"""
        if self.skor >= 700:
            return "Lulus (Sangat Memuaskan)"
        elif self.skor >= 600:
            return "Lulus (Memuaskan)"
            
        return "Tidak Lulus"

def main():
    info_sistem()
    peserta_list = []
    
    while True:
        try:
            jumlah = int(input("Masukkan jumlah peserta (minimal 1): "))
            if jumlah > 0:
                break
            print("[!] Jumlah peserta tidak valid.")
        except ValueError:
            print("[!] Masukkan input berupa angka bulat.")
            
    for i in range(jumlah):
        print(f"\n--- Data Peserta {i+1} ---")
        nama = input("Nama peserta: ")
        peserta = PesertaUTBK(nama)
        
        pm = float(input("Nilai Penalaran Matematika (PM): "))
        bi = float(input("Nilai Bahasa Indonesia: "))
        bing = float(input("Nilai Bahasa Inggris: "))
        
        skor_akhir = hitung_skor_akhir(pm, bi, bing)
        peserta.set_skor(skor_akhir)
        peserta_list.append(peserta)
        
    print("\n" + "=" * 55)
    print(" HASIL EVALUASI AKHIR ".center(55))
    print("=" * 55)
    
    for p in peserta_list:
        status = p.get_status_kelulusan()
        print(f"Peserta: {p.nama} | Skor: {p.skor:.2f} | Status: {status}")

if __name__ == "__main__":
    main()