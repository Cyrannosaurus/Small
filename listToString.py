import time, random as rand


def evaluate(fn):
    """ A wrapper class for evaluating the performace of a simple function """
    runs = 1000
    def speed_evaluation(*args) -> str:
        t_start = time.time()
        for _ in range(runs):
            fn(*args)
        t_end = time.time()
        return f'The average runtime for {fn.__name__} was {(t_end-t_start)/runs}'
    return speed_evaluation
    

@evaluate
def listToString1(*args) -> str:
    """ Profs shown method of list -> string """
    return ''.join([str(x) for x in args])

@evaluate
def listToString2(*args) -> str:
    """ The method I fell in love with for list -> string """
    return ''.join(map(str, args))

if __name__ == "__main__":
    print(listToString1([1]*100000))
    print(listToString2([1]*100000))
