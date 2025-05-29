def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def main():
    print("Temperature Converter")
    choice = input("Convert from (C)elsius or (F)ahrenheit? ").strip().upper()
    temp = float(input("Enter temperature: "))

    if choice == 'C':
        print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
    elif choice == 'F':
        print(f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()


