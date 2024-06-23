#TODO: remove this: just create objects by order in KEyboardJob
import IOrder

class Waiter:
    def create_order(self, raw_order):
        order_str = self._concatenate_char_array(raw_order)

        next_index = 0
        if order_str.startswith("hko"):
            next_index = 3
            raise NotImplementedError()
        if order_str.startswith("hk"):
            next_index = 2
            raise NotImplementedError()
        if order_str.startswith("h"):
            next_index = 1
            raise NotImplementedError()
        
        order_part = self._get_character_by_index(next_index)
        if order_part == None:
            # TODO: return order
            raise NotImplementedError()
        
        if order_part == "l":
            raise NotImplementedError()


        return None
    
    def _concatenate_char_array(self, char_array):
        concatenated_string = ''.join(char_array)
        return concatenated_string    
    
    def _get_character_by_index(self, array, index):
        if (len(array) >= (index - 1)):
            return array[index]
        return None
