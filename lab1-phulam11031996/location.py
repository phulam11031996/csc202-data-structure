class Location:
    """Represents a location on Earth

    Attributes:
        name: The name of this location.
        latitude: The latitude in degrees, between -90 and 90
        longitude: The longitude in degrees, between -180 and 180
    """
    def __init__(self, name: str, latitude: float, longitude: float):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    # TODO: Add __eq__ and __repr__ here
    def __repr__(self) -> str:
        return 'Location(%r, %r, %r)' % (
            self.name,
            self.latitude,
            self.longitude
        )

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, Location) and
            self.name == other.name and
            self.longitude == other.longitude and
            self.latitude == other.latitude
        )


def main() -> None:
    loc1 = Location('SLO', 35.3, -120.7)
    loc2 = Location('Paris', 348.9, 2.4)
    loc3 = Location('SLO', 35.3, -120.7)
    loc4 = loc1

    print('Location 1:', loc1)
    print('Location 2:', loc2)
    print('Location 3:', loc3)
    print('Location 4:', loc4)

    print()

    print('Location 1 equals Location 2:', loc1 == loc2)
    print('Location 1 equals Location 3:', loc1 == loc3)
    print('Location 1 equals Location 4:', loc1 == loc4)

    print()

    locations = [loc1, loc2]
    print(loc1 in locations)
    print(loc2 in locations)
    print(loc3 in locations)
    print(loc4 in locations)


if __name__ == '__main__':
    main()
