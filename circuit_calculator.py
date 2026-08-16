"""
Electrical Circuit Calculator
A simple command-line tool to perform common ECE calculations:
- Ohm's Law (Voltage, Current, Resistance)
- Power
- Series and Parallel Resistance

Author: Amaldev P
"""

def ohms_law():
    print("\nOhm's Law: V = I x R")
    print("Which value do you want to find?")
    print("1. Voltage (V)")
    print("2. Current (I)")
    print("3. Resistance (R)")
    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        i = float(input("Enter Current (A): "))
        r = float(input("Enter Resistance (ohms): "))
        v = i * r
        print(f"Voltage = {v} V")

    elif choice == "2":
        v = float(input("Enter Voltage (V): "))
        r = float(input("Enter Resistance (ohms): "))
        i = v / r
        print(f"Current = {i} A")

    elif choice == "3":
        v = float(input("Enter Voltage (V): "))
        i = float(input("Enter Current (A): "))
        r = v / i
        print(f"Resistance = {r} ohms")

    else:
        print("Invalid choice.")


def power_calc():
    print("\nPower: P = V x I")
    v = float(input("Enter Voltage (V): "))
    i = float(input("Enter Current (A): "))
    p = v * i
    print(f"Power = {p} W")


def series_resistance():
    print("\nSeries Resistance: R_total = R1 + R2 + ... + Rn")
    n = int(input("How many resistors? "))
    total = 0
    for x in range(n):
        r = float(input(f"Enter resistance R{x+1} (ohms): "))
        total += r
    print(f"Total Series Resistance = {total} ohms")


def parallel_resistance():
    print("\nParallel Resistance: 1/R_total = 1/R1 + 1/R2 + ... + 1/Rn")
    n = int(input("How many resistors? "))
    total_inverse = 0
    for x in range(n):
        r = float(input(f"Enter resistance R{x+1} (ohms): "))
        total_inverse += 1 / r
    total = 1 / total_inverse
    print(f"Total Parallel Resistance = {total:.2f} ohms")


def main():
    while True:
        print("\n===== Electrical Circuit Calculator =====")
        print("1. Ohm's Law")
        print("2. Power Calculation")
        print("3. Series Resistance")
        print("4. Parallel Resistance")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            ohms_law()
        elif choice == "2":
            power_calc()
        elif choice == "3":
            series_resistance()
        elif choice == "4":
            parallel_resistance()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()