from multiprocessing import Process, Queue

class AJob:
    def __init__(self, feedback_channel: Queue):
        self._feedback_channel = feedback_channel
        pass
    
    def run_job_in_background(self):
        process = Process(target=self._execute)
        process.start()
        process.join()
    
    def _execute(self):
        raise NotImplementedError("Subclasses must implement this method")