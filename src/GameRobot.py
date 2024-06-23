# https://www.crazygames.com/game/hot-dog-bush

import os
from os import path
import keyboard
import pyautogui
import json
import time
from multiprocessing import Process, Queue
from jobs.HotDogBush import HotDogBush
from jobs.KeyboardJob import KeyboardJob

SLEEP_TIME = 0.3

game_objects = [
    {
        "key": "hot-dog-source",
        "name": "hot dog source",
        "position": [0, 0]
    },
    {
        "key": "fried-hot-dog-1",
        "name": "fried hot dog 1",
        "position": [0, 0]
    },
    {
        "key": "fried-hot-dog-2",
        "name": "fried hot dog 2",
        "position": [0, 0]
    },
    {
        "key": "fried-hot-dog-3",
        "name": "fried hot dog 3",
        "position": [0, 0]
    },

    {
        "key": "hot-dog-bun-source",
        "name": "hot dog bun source",
        "position": [0, 0]
    },
    {
        "key": "prepared-hot-dog-bun-1",
        "name": "prepared hot dog bun 1",
        "position": [0, 0]
    },
    {
        "key": "prepared-hot-dog-bun-2",
        "name": "prepared hot dog bun 2",
        "position": [0, 0]
    },
    {
        "key": "prepared-hot-dog-bun-3",
        "name": "prepared hot dog bun 3",
        "position": [0, 0]
    },

    {
        "key": "ketchup",
        "name": "ketchup",
        "position": [0, 0]
    },

    {
        "key": "customer-1",
        "name": "customer 1",
        "position": [0, 0]
    },
    {
        "key": "customer-2",
        "name": "customer 2",
        "position": [0, 0]
    },
    {
        "key": "customer-3",
        "name": "customer 3",
        "position": [0, 0]
    },
    {
        "key": "customer-4",
        "name": "customer 4",
        "position": [0, 0]
    },
    {
        "key": "customer-5",
        "name": "customer 5",
        "position": [0, 0]
    },

    {
        "key": "gold-1",
        "name": "gold 1",
        "position": [0, 0]
    },
    {
        "key": "gold-2",
        "name": "gold 2",
        "position": [0, 0]
    },
    {
        "key": "gold-3",
        "name": "gold 3",
        "position": [0, 0]
    },
    {
        "key": "gold-4",
        "name": "gold 4",
        "position": [0, 0]
    },
    {
        "key": "gold-5",
        "name": "gold 5",
        "position": [0, 0]
    },
]

class DragCommand:
    def __init__(self, source_x, source_y, target_x, target_y, name):
        self.source_x = source_x
        self.source_y = source_y
        self.target_x = target_x
        self.target_y = target_y
        self.Name = name
    def execute(self):
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(self.source_x, self.source_y)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(self.target_x, self.target_y)
        time.sleep(SLEEP_TIME)
        pyautogui.mouseUp()
        pyautogui.FAILSAFE = True

class ClickCommand:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.Name = name
    def execute(self):
        pyautogui.FAILSAFE = False
        pyautogui.click(self.x, self.y)
        pyautogui.FAILSAFE = True

def initialize_game_objects():
    print("Initializing game objects")
    cache_directory = ".\\GameRobot\\cache"
    cache_path = cache_directory + "\\game_object_cache.cache"

    cached_objects = try_load_game_object_from_cache(cache_path)
    if (cached_objects[0] == True):
        return cached_objects[1]
    
    for game_object in game_objects:
        print("Select a position for " + game_object["name"] + " by pressing 'c' button on the game object while the mouse cursor is on the object.")
        is_position_selected = False
        while True:
            if keyboard.is_pressed('c') and is_position_selected == False:
                position = pyautogui.position()
                game_object["position"] = [ position.x, position.y ]
                print("Position saved for " + game_object["name"] + " (" + str(game_object["position"][0]) + ", " + str(game_object["position"][1]) + ")")
                print("Please confirm the selection by pressing 's' or reset it by pressing 'r'")
                is_position_selected = True
            if keyboard.is_pressed('s') and is_position_selected == True:
                print("Selection confirmed")
                break
            if keyboard.is_pressed('r'):
                print("Selection reset successfully. Press 'c' button for a new selection.")
                is_position_selected = False

    if not path.exists(cache_directory):
        os.makedirs(cache_directory)
    with open(cache_path, "w") as cache_file:
        json.dump(game_objects, cache_file)
    
    return game_objects

def try_load_game_object_from_cache(cache_path):
    game_objects = []
    if path.exists(cache_path):
        with open(cache_path, "r") as cache_file:
            game_objects = json.load(cache_file)
            print("GameObjects have been loaded from cache successfully.")
            print(str(game_objects))
            return ( True, game_objects )
    return ( False, game_objects )

def get_game_object_by_key(key, game_objects):
    for game_object in game_objects:
        if game_object["key"] == key:
            return game_object
    raise AttributeError(key + " is not a valid game object key")

def print_game_commands():
    os.system('cls')
    print("h - add a hot dog")
    print("b - a hot dog bun")
    print("f - fill all buns with hot dog")
    print("k - fill hot dob bun with ketchup")
    print("s - serve a customer")
    print("g - collect gold")
    print("r - run commands")
    print("q - quit")

def create_click_on_game_object_command(game_objects, game_object_key, command_name):
    game_object = get_game_object_by_key(game_object_key, game_objects)
    x = game_object["position"][0]
    y = game_object["position"][1]
    
    return ClickCommand(x, y, command_name)

def create_drag_game_object_command(game_objects, source_game_object_key, target_game_object_key, command_name):
    source_game_object = get_game_object_by_key(source_game_object_key, game_objects)
    target_game_object = get_game_object_by_key(target_game_object_key, game_objects)

    source_x = source_game_object["position"][0]
    source_y = source_game_object["position"][1]
    target_x = target_game_object["position"][0]
    target_y = target_game_object["position"][1]

    return DragCommand(source_x, source_y, target_x, target_y, command_name)

def print_command_names(commands):
    command_list = ""
    for command in commands:
        command_list = command_list + " -> " + command.Name
    print(command_list)

def get_index(upper_limit):
    while True:
        for i in range(upper_limit):
            if keyboard.is_pressed(str(i + 1)):
                return i + 1

def execute_commands(commands):
    for command in commands:
        command.execute()
    commands.clear()

def run_command(game_objects):
    print_game_commands()
    command_list = []
    print("Select a command and hit enter or type 'c' to cancel:")
    while True:
        if keyboard.is_pressed('h'):
            command = create_click_on_game_object_command(game_objects, "hot-dog-source", "ADD HOT DOG")
            command_list.append(command)
            command_list.append(command)
            command_list.append(command)

            execute_commands(command_list)

            print_game_commands()
            print_command_names(command_list)
            time.sleep(SLEEP_TIME)
        if keyboard.is_pressed('b'):
            command = create_click_on_game_object_command(game_objects, "hot-dog-bun-source", "ADD HOT DOG BUN")
            command_list.append(command)
            command_list.append(command)
            command_list.append(command)

            execute_commands(command_list)

            print_game_commands()
            print_command_names(command_list)
            time.sleep(SLEEP_TIME)
        if keyboard.is_pressed('f'):
            command1 = create_drag_game_object_command(game_objects, "fried-hot-dog-1", "prepared-hot-dog-bun-1", "PLACE HOT DOG 1 TO BUN 1")
            command2 = create_drag_game_object_command(game_objects, "fried-hot-dog-2", "prepared-hot-dog-bun-2", "PLACE HOT DOG 2 TO BUN 2")
            command3 = create_drag_game_object_command(game_objects, "fried-hot-dog-3", "prepared-hot-dog-bun-3", "PLACE HOT DOG 3 TO BUN 3")
            command_list.append(command1)
            command_list.append(command2)
            command_list.append(command3)

            execute_commands(command_list)

            print_game_commands()
            print_command_names(command_list)
            time.sleep(SLEEP_TIME)
        if keyboard.is_pressed('k'):
            print("Bun index (1, 2, 3):")
            target_bun = get_index(3)
            
            command = create_drag_game_object_command(game_objects, "ketchup", "prepared-hot-dog-bun-" + str(target_bun), "FILL HOT DOG BUN " + str(target_bun) + " WITH KETCHUP")
            command_list.append(command)

            execute_commands(command_list)

            print_game_commands()
            print_command_names(command_list)
            time.sleep(SLEEP_TIME)
        if keyboard.is_pressed('s'):
            print("Serve hot dog (1, 2, 3):")
            hotdog_index = get_index(3)
            time.sleep(SLEEP_TIME)
            print("To customer (1, 2, 3, 4, 5):")
            customer_index = get_index(5)
            
            command = create_drag_game_object_command(game_objects, "prepared-hot-dog-bun-" + str(hotdog_index), "customer-" + str(customer_index), "SERVE CUSTOMER " + str(customer_index) + " WITH HOT DOG " + str(hotdog_index))
            command_list.append(command)

            execute_commands(command_list)

            print_game_commands()
            print_command_names(command_list)
            time.sleep(SLEEP_TIME)
        if keyboard.is_pressed('g'):
            for i in range(5):
                command = create_click_on_game_object_command(game_objects, "gold-" + str(i + 1), "COLLECT GOLD " + str(i + 1))
                command_list.append(command)
            
            execute_commands(command_list)

            print_game_commands()
            print_command_names(command_list)
            time.sleep(SLEEP_TIME)
        if keyboard.is_pressed('q'):
            return False
    return True

def print_main_commands():
    os.system('cls')
    print("Waiting for input:")
    print("Press 'q' to quit")
    print("Press 'e' to execute a command")



##############################
#####        MAIN        #####
##############################
def start_background_job(command_channel, game_objects):
    robot_job = Process(target=background_cursor_job, args=(command_channel, game_objects))
    robot_job.start()
    return robot_job

def background_cursor_job(command_channel: Queue, game_objects: []):
    while True:
        # TODO: do paramless jobs like add hot dog and others
        if (not command_channel.empty()):
            command = command_channel.get()
            print(command)
            if (command == 'q'):
                return
        
def start_listener(command_channel: Queue):
    while True:
        if keyboard.is_pressed('a'):
            send_command_to_channel(command_channel, "QUEUE COMMAND")
        if keyboard.is_pressed('q'):
            send_command_to_channel(command_channel, "q")
            break

def send_command_to_channel(command_channel: Queue, command: str):
    command_channel.put_nowait(command)
    time.sleep(SLEEP_TIME)

def alma(s):
    print(s)

def main():
    #job_handler = JobHandler()
    #game_objects = initialize_game_objects()
    
    feedback_channel = Queue()
    keyboard_handler = KeyboardJob(feedback_channel)
    keyboard_handler.run_job_in_background()
    # hot_dog_bush = HotDogBush(feedback_channel)
    # hot_dog_bush.run_job_in_background()

    #job_handler.run_job(alma, ("hello world",))
    # if __name__ == '__main__':
    #     game_objects = initialize_game_objects()
    #     command_channel = Queue()
    #     robot_job = start_background_job(command_channel, game_objects)
    #     start_listener(command_channel)
    #     robot_job.join()

    while True:
        pass

if __name__ == "__main__":
    main()