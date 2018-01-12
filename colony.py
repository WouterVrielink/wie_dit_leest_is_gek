from mesa.time import RandomActivation
from ant import Ant
from mesa import Agent
import numpy as np
import matplotlib.patches as patches
import itertools


class Colony(Agent):
    """ A Colony which contains a number of ants."""
    def __init__(self, environment, pheromone_id, pos, N, radius=1):
        # TODO init the actual agent? (super init)
        self.environment = environment
        self.pheromone_id = pheromone_id
        self.pos = pos
        self.num_agents = N
        self.ant_list = RandomActivation(environment)
        self._radius = radius

        # Create agents
        self.add_ants(N)

        # Register self
        self.environment.grid.place_agent(self, self.pos)

        # Animation attributes
        self._patches = []

    def on_colony(self, pos):
        """
        Checks whether the pos is on top of its own colony.
        :param pos: tuple (x, y) coordinates
        :return: True if on colony, False otherwise
        """
        return np.sum(np.subtract(pos, self.pos) ** 2) ** 0.5 <= self.radius

    def step(self):
        '''
        Advance each ant in this colony by one time-step.
        '''
        self.ant_list.step()

    def add_ants(self, N):
        """
        Adds N ants to this colony.
        :param N: integer value which specifies the nr of ants to add
        """
        for i in range(N):
            a = Ant(i, self)
            self.ant_list.add(a)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        """
        Make sure the animation is update accordingly to the new radius.
        :param new_radius: the new radius
        """
        assert new_radius >= 0, "the radius has to be a positive number"
        if self.radius != new_radius:
            raise NotImplementedError

    def update_vis(self):
        """

        :return:
        """
        if len(self._patches) == 0:
            for x, y in itertools.product(np.arange(-self.radius, self.radius + 1),
                                          np.arange(-self.radius, self.radius + 1)):
                pos = np.add(self.pos, (x, y))
                if self.on_colony(pos):
                    patch = patches.Rectangle(self.environment.grid_to_array(pos), 1, 1, linewidth=1, edgecolor='r',
                                                  facecolor='r', fill=True)
                    self._patches.append(patch)
                    self.environment.ax.add_patch(patch)

        return self._patches

    def __exit__(self):
        """
        Make sure the animation is update accordingly to the removed colony
        """
        raise NotImplementedError
