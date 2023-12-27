# SELECT world.name, world.population, world.area FROM world WHERE world.population >= 25000000 OR world.area >= 3000000;
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[(world['population'] >= 25000000) | (world['area'] >= 3000000)][['name','population','area']]