def feet2meter(v):
    feet_str = v.replace("ft", "")
    feet = float(feet_str)
    meters = feet * 0.3048
    return meters

def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

main()
