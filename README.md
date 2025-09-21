# bmi_calculator
def main():
    try:
        w = float(input("⚖️  Og'irlik (kg): "))
        h = float(input("📏 Bo'y (m): "))
        if w <= 0 or h <= 0:
            return print("❗ Musbat son kiriting.")
        
        bmi = w / h**2
        status = (
            "Past vazn" if bmi < 18.5 else
            "Normal vazn" if bmi <= 24.9 else
            "Ortiqcha vazn" if bmi <= 29.9 else
            "Semizlik"
        )
        print(f"\n📊 BMI: {bmi:.2f} — {status}")
    except:
        print("❗ Xatolik: Iltimos, to'g'ri son kiriting.")

if __name__ == "__main__":
    main()
