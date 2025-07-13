from pyboy import PyBoy
pyboy = PyBoy('assets/pokemon_rojo.gb')
while pyboy.tick():
    pass
pyboy.stop()