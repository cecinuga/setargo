import sys

def SetNArg(_narg):
    global narg;
    narg = _narg

def SetArgo( argomenti ):#Aggiungi i tuoi argomenti
    for arg in argomenti:
        if arg == '--help':
            print("--url Ganache Url")
            print("--addr Other Account")
            exit()
        elif arg == '--url':
            ganache_url = sys.argv[i+1]
        elif arg == '--gasPrice':
            gasPrice = sys.argv[i+1]
        elif arg == '--addr':
            address = sys.argv[i+1]
        i += 1;
