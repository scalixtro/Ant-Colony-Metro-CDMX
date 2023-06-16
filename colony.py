import numpy as np
import pandas as pd
from ant import Ant

class Colony:
    ants: list[Ant]
    n_ants: int
    epochs: int
    df_adjacent: pd.DataFrame
    df_pheromones: pd.DataFrame
    df_distances: pd.DataFrame

    def __init__(self,
        start: str,
        end: str,
        n_ants: int,
        df_adjacent: pd.DataFrame,
        df_pheromones: pd.DataFrame,
        df_distances: pd.DataFrame
        ) -> None:
        self.n_ants = n_ants
        self.df_adjacent = df_adjacent
        self.df_pheromones = df_pheromones
        self.df_distances = df_distances
        # Inicializar Hormigas
        self.ants = [Ant(start, end) for _ in range(n_ants)]


    def ant_search(self) -> None:
        all_finished = False
        for ant in self.ants:
            ant.reset()

        while not all_finished:
            for ant in self.ants:
                ant.search_path(self.df_pheromones, self.df_distances)

            all_finished = all([ant.finished for ant in self.ants])

        return


    def get_pairs(self, visited: list[str]):
        """Gets pair of stations, equivalent of getting the
        paths taken by an ant
        visited: List of visited stations"""
        pairs = []
        for i in range(len(visited) - 1):
            current_pair = [visited[i], visited[i+1]]
            if not current_pair in pairs:
                pairs.append(current_pair)
        return pairs


    def update_pheromones(self, rho: float, Q: float) -> None:
        """Pheromone update
        rho: Evaporation ratio
        Q: Learning rate"""
        self.df_pheromones * (1 - rho)

        for ant in self.ants:
            L = ant.path_distance

            visited_pairs = self.get_pairs(ant.visited)

            for x1,x2 in visited_pairs:
                self.df_pheromones.loc[x1,x2] += Q / L

    
    def train(self, epochs, rho, Q) -> None:
        """For each epoch get ants to find a path from start to end, then
        update the pheromones matrix"""
        for i in range(epochs):
            self.ant_search()
            self.update_pheromones(rho, Q)

    
    def get_best(self) -> None:
        """Returns the best ant which has the least traveled distance"""
        best_ant = self.ants[0]
        for ant in self.ants:
            if ant.path_distance < best_ant.path_distance:
                best_ant = ant
        
        return best_ant