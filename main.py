import pandas as pd
import numpy as np
from flask import Flask, render_template, request, redirect
from ant import Ant
from colony import Colony

def get_distance(X1, X2):
    """Get distance between two given points
    X1: 1D numpy array
    X2: 1D numpy array"""
    return np.sqrt(np.sum((X1 - X2) ** 2))

df_adjacent_stations = pd.read_excel('./Data.xlsx', sheet_name=0, header=0, index_col=0)
df_positions = pd.read_excel('./Data.xlsx', sheet_name=1, header=0, index_col=0)
app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        return getRoute()
    return render_template('index.html')

@app.route('/getRoute', methods=["POST", "GET"])
def getRoute():
    if request.method == "POST":
        start = request.form.get('start')
        end = request.form.get('end')
    
    df_distances = df_adjacent_stations.copy()
    df_pheromones = df_adjacent_stations.copy()
    
    # Matriz de distancia
    for station_name,station_neighbors in df_distances.iterrows():
        for neighbor, is_adjacent in station_neighbors.items():
            if is_adjacent:
                station1 = df_positions.loc[station_name]
                station2 = df_positions.loc[neighbor]
                d = get_distance(station1.to_numpy(), station2.to_numpy())
                df_distances.loc[station_name, neighbor] = d
    
    # Matriz de feromonas
    df_pheromones = df_pheromones.applymap(lambda x: x * 0.1);
    model = Colony(start, end, 20, df_adjacent_stations, df_pheromones, df_distances)
    model.train(epochs=15, rho=0.5, Q=0.99)
    best = model.get_best()

    return render_template('ruta.html', stations=best.visited)



if __name__ == '__main__':
    app.run(debug=True)