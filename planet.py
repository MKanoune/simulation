import numpy as np
import matplotlib.pyplot as plt
from math import hypot

GRAVITY = 6.673e-11

all_planets = []


class Planet:
    def __init__(self, distance, v, m):
        self.m = m
        self.pos = np.array([distance, 0])
        self.v = np.array([0, v])
        self.time = 0
        self.a = 0
        self.pos_x = []
        self.pos_y = []

    def update(self, new_time):
        """
        :param new_time:
        :return:
        """
        self.plot_pos()
        self.update_velocity(new_time)
        self.calc_position(sun, new_time)
        self.time = new_time

    def plot_pos(self):
        self.pos_x.append(self.pos[0])
        self.pos_y.append(self.pos[1])

    def calc_position(self, planet, time):
        """
        Methode zum aktualisieren der Gravitationskraft, der Beschleunigung und der daraus entstehenden neuen Position
        :param planet:
        :param time:
        """
        r = self.calc_distance(planet)
        force_gravity = (GRAVITY * self.m * planet.m / r ** 3) * (planet.pos - self.pos)

        self.a = force_gravity / self.m
        dt = self.get_delta_time(time)

        self.pos = (self.pos + dt * self.v + 0.5 * dt ** 2 * self.a)

    def calc_distance(self, planet):
        """
        Methode welche die Distanz zwischen beiden Himmelskörpern gibt
        :param planet:
        :return: int
        """
        return np.linalg.norm(self.pos - planet.pos)

    def update_velocity(self, time):
        """
        Methode zum anpassen der Geschwindigkeit zum neuen Zeitpunkt
        :param time:
        """
        print(self.v)
        self.v = self.a * self.get_delta_time(time) + self.v

    def get_delta_time(self, new_time):
        """
        Methode gibt das Delta eines Zeitintervalls an
        :param new_time:
        :return: int
        """
        return new_time - self.time


def main():
    for time in range(0, int(3600 * 24 * 365.25), 12 * 60 * 60):
        earth.update(time)
    plt.plot(earth.pos_x, earth.pos_y)
    plt.show()


if __name__ == '__main__':
    sun = Planet(0, 0, 1.989e30)
    earth = Planet(1.496e11, 29870, 5.974e24)
    all_planets.append(earth)
    main()
