from pyboy import WindowEvent

# Orden explícito del espacio de acción.
ACTIONS = [
    "UP", # 0
    "DOWN", # 1
    "LEFT", # 2
    "RIGHT", # 3
    "A", # 4
    "B", # 5
    "START", # 6
    "SELECT", # 7
]

# Mapeo de acción a evento de PyBoy
ACTION_TO_EVENT = {
    "UP": WindowEvent.PRESS_ARROW_UP,
    "DOWN": WindowEvent.PRESS_ARROW_DOWN,
    "LEFT": WindowEvent.PRESS_ARROW_LEFT,
    "RIGHT": WindowEvent.PRESS_ARROW_RIGHT,
    "A": WindowEvent.PRESS_BUTTON_A,
    "B": WindowEvent.PRESS_BUTTON_B,
    "START": WindowEvent.PRESS_BUTTON_START,
    "SELECT": WindowEvent.PRESS_BUTTON_SELECT,
}

# Devuelve el evento de PyBoy correspondiente al índice de acción.
def get_event_by_index(index):
    if 0 <= index < len(ACTIONS):
        action = ACTIONS[index]
        return ACTION_TO_EVENT[action]
    raise ValueError(f"Índice de acción fuera de rango: {index}")

# Devuelve el nombre de la acción correspondiente al índice.
def get_action_name(index):
    if 0 <= index < len(ACTIONS):
        return ACTIONS[index]
    raise ValueError(f"Índice de acción fuera de rango: {index}")

# Devuelve el evento de PyBoy correspondiente al nombre de la acción.
def get_event_by_name(action_name):
    try:
        return ACTION_TO_EVENT[action_name]
    except KeyError:
        raise ValueError(f"Acción desconocida: {action_name}")

# Devuelve el número total de acciones disponibles.
def num_actions():
    return len(ACTIONS)

# Devuelve una lista de todos los nombres de acciones.
def all_action_names():
    return ACTIONS.copy()

# Devuelve una lista de todos los eventos de PyBoy en el mismo orden que ACTIONS.
def all_events():
    return [ACTION_TO_EVENT[action] for action in ACTIONS]
