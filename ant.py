import numpy as np
import pandas as pd

class Ant:
    finished: bool
    path_distance: int
    start: str
    end: str
    visited: list[str]

    def __init__(
        self,
        start: str,
        end: str
    ) -> None:
        """Constructor for an ant, it only knows the first and last stations
        start: Start station
        end: Final station
        """
        self.start = start
        self.end = end
        self.finished = False
        self.path_distance = 0
        self.visited = [start]


    def get_probabilities(
        self,
        pheromones: pd.Series, 
        distances: pd.Series, 
        previous_station=''
    ) -> pd.Series:
        """Get the probabilities of each path that an ant can take ignoring the
        previous station visited
        pheromones: Pheromone matrix
        distances: Distance matrix
        previous station: Previous station visited by an ant"""
        visibility = (1 / distances)
        samples = (pheromones * visibility).dropna().drop(previous_station, errors='ignore')
        total_sum = samples.sum()
        return samples / total_sum


    def select_next_station(self, df_pheromones, df_distances) -> str:
        """Select the next station based on probability. A station
        is more likely to get chosen if the pheromone level in that path is higher"""
        actual_station = self.visited[-1]
        previous_station = self.visited[-2] if len(self.visited)>=2 else ''
        # np.random.seed(1)
        rand = np.random.random()

        possible_next = self.get_probabilities(df_pheromones.loc[actual_station],
                                               df_distances.loc[actual_station],
                                               previous_station)
        possible_sorted = possible_next[possible_next > 0].sort_values().cumsum()
        next_station = possible_sorted[possible_sorted >= rand].index[0]

        return next_station

    
    def search_path(self, df_pheromones, df_distances) -> None:
        """Search a path adding new stations to the visited list,
        if the ant has arrived to destination, then does nothing"""
        if self.visited[-1] == self.end:
            self.finished = True

        if not self.finished:
            next_station = self.select_next_station(df_pheromones, df_distances)
            self.path_distance += df_distances.loc[self.visited[-1], next_station]
            self.visited.append(next_station)

    
    def reset(self) -> None:
        """Reset ant state by setting finished to False, visited to an empty list
        and path distance to 0"""
        self.finished = False
        self.visited = [self.start]
        self.path_distance = 0