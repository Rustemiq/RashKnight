from configuration.settings import MAP_SIZE
from modules.sprites.tile import Tile


def generate_map(tiles_group, walls_group):
    #пока что пустая карта
    for x in range(MAP_SIZE[0]):
        for y in range(MAP_SIZE[1]):
            Tile('floor', x, y, tiles_group)