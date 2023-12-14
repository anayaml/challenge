orbital_periods_per_planet = {
    "mercury": 0.2408467,
    "venus": 0.615,
    "earth": 1.0,
    "mars": 1.8808158,
    "jupiter": 11.862615,
    "saturn": 29.447498,
    "uranus": 84.016846,
    "neptune": 164.79132
}

def calculate_celestial_age(seconds, planet):
    earth_years = seconds / (365.25 * 24 * 60 * 60) # 365.25 days in a year
    try:
        return round(earth_years / orbital_periods_per_planet[planet.islower() and planet or planet.lower()],2)
    except Exception as e:
        raise Exception(f"Invalid planet: {planet}") from e