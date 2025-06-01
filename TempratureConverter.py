def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature():
    print("🌡️ Hey there! Welcome to your friendly temperature converter.")
    print("I can help you convert between Celsius (C), Fahrenheit (F), and Kelvin (K). Let's get started!")

    while True:
        from_unit = input("\n🔁 What unit are you converting *from*? (C, F, or K): ").strip().upper()
        to_unit = input("➡️ What unit are you converting *to*? (C, F, or K): ").strip().upper()

        if from_unit not in ['C', 'F', 'K'] or to_unit not in ['C', 'F', 'K']:
            print("🤔 Hmm, that doesn't seem right. Please use 'C', 'F', or 'K'.")
            continue

        try:
            temp = float(input(f"📥 Alright! Now enter the temperature in {from_unit}: "))
        except ValueError:
            print("⚠️ That doesn't look like a valid number. Mind trying again?")
            continue

        if from_unit == to_unit:
            converted = temp
        elif from_unit == 'C' and to_unit == 'F':
            converted = celsius_to_fahrenheit(temp)
        elif from_unit == 'C' and to_unit == 'K':
            converted = celsius_to_kelvin(temp)
        elif from_unit == 'F' and to_unit == 'C':
            converted = fahrenheit_to_celsius(temp)
        elif from_unit == 'F' and to_unit == 'K':
            converted = fahrenheit_to_kelvin(temp)
        elif from_unit == 'K' and to_unit == 'C':
            converted = kelvin_to_celsius(temp)
        elif from_unit == 'K' and to_unit == 'F':
            converted = kelvin_to_fahrenheit(temp)

        print(f"\n✅ Got it! {temp}°{from_unit} is about {converted:.2f}°{to_unit}.")

        again = input("\n🔄 Want to convert another one? (yes/no): ").strip().lower()
        if again != 'yes':
            print("\n👋 Alright, take care! Stay cozy, whether it's chilly or toasty out there!")
            break

if __name__ == "__main__":
    convert_temperature()