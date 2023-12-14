import pytest
import app.planets as planets

@pytest.mark.parametrize("seconds, planet, expected_age", [
    (2500000000, "Venus", 128.77),
    (1000000000, "Earth", 31.69),
    (500000000, "Mercury", 3.28),
    (2500000000, "Venus", 128.77),
    (1000000000, "Earth", 31.69),
    (500000000, "Mercury", 3.28),
    (3600000000, "Mars", 3.83),
    (20000000000, "Jupiter", 1.68),
    (4000000000, "Saturn", 4.06),
    (10000000000, "Uranus", 1.19),
    (50000000000, "Neptune", 1.36),
    (1234567890, "Venus", 64.08),
    (9876543210, "Earth", 253.33),
    (1111111111, "Mercury", 15.36),
    (2222222222, "Mars", 2.98),
    (3333333333, "Jupiter", 0.46),
    (4444444444, "Saturn", 1.51),
    (5555555555, "Uranus", 0.66),
    (6666666666, "Neptune", 0.34),
    (7777777777, "Venus", 128.24),
    (8888888888, "Earth", 351.53),
    (9999999999, "Mercury", 41.27),
    (10000000000, "Mars", 5.32),
    (1234567890, "Jupiter", 0.10),
    (2345678901, "Saturn", 0.24),
    (3456789012, "Uranus", 0.11),
    (4567890123, "Neptune", 0.06),
])
def test_calculate_age(seconds, planet, expected_age):
    actual_age = planets.calculate_celestial_age(seconds, planet)
    assert actual_age == expected_age