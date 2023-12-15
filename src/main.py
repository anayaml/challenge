import app.planets as planets
import utils.util as formatting_input

if __name__ == "__main__":
    user_input = input()
    seconds, planet = formatting_input.extract_values(user_input)
    age = planets.calculate_celestial_age(seconds, planet)
    print(f"{age} {planet}-Years-Old.")