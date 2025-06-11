import sys
from logger import logging
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info
    file_name=exc_tb.tb_frame.f_code.co_filename#access the file name
    error_message="Error occured in python script name [{0}] line number[{1}] error_message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))#insert value w.r.t placeholder i.e 0,1,2
    return error_message
    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):#get all the vars u need for the class
        super().__init__(error_message)#inherit the error_message
        self.error_message=error_message_detail(error_message,error_detail=error_detail)#make the error message by caling prev func
    def __str__(self):#new func with all the vars within class
        return self.error_message#finally spit out the error message
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:    
    
        logging.info("divide by zero")
        raise CustomException(e,sys)