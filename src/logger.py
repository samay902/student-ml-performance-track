import logging#for tracking the error
import os
from datetime import datetime
LOG_FILE=f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"#log file name in datetime naming
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)#current working directory-->logs-->log files 
os.makedirs(logs_path,exist_ok=True)#make directory
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s-%(message)s",
    level=logging.INFO
)
if __name__=="__main__":
    logging.info("logging has started")

