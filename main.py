import requests
# CodTECH Task 4 - Weather App CLI
# INTERNID: CITS1188
# Name: GUDIVAKA DINEESHA
def get_weather(city):
    # Free API - No key needed for demo
    api_url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            print(f"\n🌤️  Weather Report: {response.text}")
        else:
            print("❌ City not found. Check spelling.")
    except Exception as e:
        print("❌ Error fetching weather. Check internet connection.")
def main():
    print("=" * 40)
    print("   CODTECH WEATHER APP (CLI)")
    print("   INTERNID: CITS1188")
    print("=" * 40)
    while True:
        city = input("\nEnter city name OR 'exit' to quit: ")
        if city.lower() == 'exit':
            print("Thank you! Stay updated with weather 🌦️")
            break
        elif city == "":
            print("Please enter a city name.")
        else:
            get_weather(city)
if __name__ == "__main__":
    main()
