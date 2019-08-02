import src.main.python.com.revature.controller.controller
import src.main.python.com.revature.io.file_handler
import src.main.python.com.revature.error.business_errors
class business:
    def __init__(self):
        self.io = src.file_handler()
        self.controller = src.controller()

    def run(self):
        self.io.load()
        self.controller.initalize(other=self)
        self.controller.run()

