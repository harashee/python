

def extract_log(log_file):

    """
    Extract the statistics of type of logs (ERROR, WARN, INFO, DEBUG) and its occurrence

    Args:
        log_file (String): Log file which is to be used to extract the statistics

    Returns:
        [Dict]: [This will have log type and its msg repetition count]
    """     
        
    with open( log_file,'r') as f:
        content = f.readlines()
    msg = {}
    for line in content:
        # line = line.replace("  "," ")
        if len(line) <= 3:
            continue
        a = line.split("  ")
        if a[1] not in msg:
            msg[a[1]] = [1, a[2]]#,' '.join(a[4:])]
        else:
            msg[a[1]][0] +=1    
    return msg

if __name__ == "__main__":
    print(extract_log("config/test_fileOp.log"))