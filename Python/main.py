from car import Car
from account import Account

if __name__ == "__main__":
    print("Hola Mundo!")

    car = Car("EO-34K5", Account("EUNICE SANCHEZ", "ESB263"))
    print(vars(car))
    print(vars(car.driver))

    