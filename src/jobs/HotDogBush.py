from multiprocessing import Queue
from parallelization.Job import AJob

CONSTANST = {
    "ADD_ORDER": "o",
    "QUIT_COMMAND": "q"
}

# TODO: replace this class to corresponding module
class HotDogBush(AJob):
    def __init__(self, feedback_channel: Queue):
        super.__init__(self, feedback_channel)
        self._input = ""
        self._orders = []

    def _execute(self):
        while True:
            self._cook()
            self._serve_customers()
            # self._do_subjobs()
            # if (not self._feedback_channel.empty()):
            #     order = self._feedback_channel.get()
            #     self._queue_order(order)
    
    # def _do_subjobs(self):
    #     self._cook()
    #     self._serve_customers()
    #     pass

    def _cook(self):
        self._fill_buffet_car_with_buns()
        if (True): # TODO: parameters & implement
            self._place_a_raw_hotdog_to_grill()
        if (True): # TODO: parameters & implement
            self._fill_hotdog_bun_with_fried_hot_dog()
        if (True): # TODO: parameters & implement
            self._fill_hot_dog_bun_with_ketchup()
        pass

    def _fill_buffet_car_with_buns(self):
        pass

    def _place_a_raw_hotdog_to_grill(self):
        pass

    def _fill_hotdog_bun_with_fried_hot_dog(self):
        pass

    def _fill_hot_dog_bun_with_ketchup(self):
        pass

    def _serve_customers(self):
        if (True): # TODO: parameters & implement (# TODO: check if any order is ready)
            orders = self._orders
            self._serve_customer()
        self._collect_coins()
    
    def _queue_order(self, order):
        if order == CONSTANST["ADD_ORDER"]:
            if (True): # TODO: validate order
                # TODO: create command and queue order
                pass
            self._input = ""
        if order == CONSTANST["QUIT_COMMAND"]:
            return
        else:
            self._input = self._input + order
            print(self._input) # TODO: outsource to UI feedback

    def _serve_customer(self):
        
        pass

    def _collect_coins():
        pass