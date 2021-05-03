import os

def creator(filename: str) -> IO:
    if os.path.isfile(filename):
        if(os.stat(filename).st_size == 0):
            return 'old'
        else: 
            raise ValueError('File exist and already has content')
    else:
        f = open(filename, "w")
        f.close()   
        return f


def writer (opened: IO, data: Union[str, List[str]]) -> int:
    f = open(opened,"w+");
    f.truncate()
    if(isinstance(data, list)):
        f.writelines(data)
    else:
        f.write(data)
    length = f.read()
    f.close()
    return length


def closer( opened: IO) -> IO:
    f = open(opened,"r");
    f.close()
    if not f.closed:
        raise RuntimeError("Closer failed")
    else:
        return opened


# corection

# cwd = os.getcwd()
# if(path.exists(cwd+"/"+filename)
# if(os.stat(filename).st_size)
# try catch -> si existe ou pas 

# opened.seek(0)
# instruction  
# opened.truncate(0)





    


        

