from datetime import datetime

def write_log_to_file(message: str):
    with open("log.txt", mode="a") as log_file:
        now = datetime.now()
        df_string = now.strftime("%d/%m/%Y %H:%M:%S")
        log_msg = df_string + " get title Id: \t" + message + "\n"
        log_file.write(log_msg)
    