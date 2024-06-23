from multiprocessing import Queue
import keyboard
from parallelization.Job import AJob
import Waiter

class KeyboardJob(AJob):
    def __init__(self, feedback_channel: Queue):
        self._feedback_channel = feedback_channel
        self._input_puffer = []
        self._waiter = Waiter()
    
    def _execute(self):
        while True:
            key = self._listen_for_key(["h", "k", "l", "esc", "enter"])
            if (key == "esc"):
                self._input_puffer.clear()
                break
            if (key == "enter"):
                order = self._waiter.create_order(self._input_puffer)
                if order == None:
                    # TODO: feedback
                    pass
                else:
                    self._feedback_channel.put(order)
                self._input_puffer.clear()
            else:
                if (not self._is_last_char_equal(self._input_puffer, key)):
                    self._input_puffer.append(key)
      
    def _listen_for_key(self, keys_to_wait_for):
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                key = event.name
                if key in keys_to_wait_for:
                    return key

    def _is_last_char_equal(self, input_string, char_to_compare):
        if input_string and input_string[-1] == char_to_compare:
            return True
        else:
            return False
        
    def _get_character_at_index(self, puffer, index):
        if len(puffer) >= (index - 1):
            return puffer[index]
        return None