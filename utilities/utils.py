import softest
import logging
import inspect


class Utils(softest.TestCase):
    
    def assertErrorMessageText(self, popup_message, value):
        print("Error message is " + popup_message.text)
        self.soft_assert(self.assertEqual, popup_message.text, value)
        if popup_message.text == value:
            print("Test Passed")
        else :
            print("Test Failed")
            
    def custom_logger(loglevel=logging.DEBUG):
        #Set class/method name from wehere its called
        logger_name = inspect.stack()[1][3]
        #Create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)
        #Create console handler or file handler and set the log level
        fh = logging.FileHandler("automation.log", mode="a")
        #Create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        #Add formatter to console or file handler
        fh.setFormatter(formatter)
        #Add console handler to logger
        logger.addHandler(fh)
        return logger