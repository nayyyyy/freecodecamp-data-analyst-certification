import numpy as np

def calculate(list_data):
    if not len(list_data) == 9:
        raise ValueError("List must contain nine numbers.")
    
    data = np.array(list_data).reshape(3,3)
    output = {}
    
    output['mean'] = [calculate_mean(data, 0), calculate_mean(data, 1), calculate_mean(data)]
    output['variance'] = [calculate_variance(data, 0), calculate_variance(data, 1), calculate_variance(data)]
    output['standard deviation'] = [calculate_stddev(data, 0), calculate_stddev(data, 1), calculate_stddev(data)]
    output['max'] = [calculate_max(data, 0), calculate_max(data, 1), calculate_max(data)]
    output['min'] = [calculate_min(data, 0), calculate_min(data, 1), calculate_min(data)]
    output['sum'] = [calculate_total(data, 0), calculate_total(data, 1), calculate_total(data)]

    return output

def calculate_mean(data, axis = None):
    if axis is None:
        return np.mean(data) 
    else:
        return np.mean(data, axis=axis)
    
def calculate_variance(data, axis = None):
    if axis is None:
        return np.var(data)
    else:
        return np.var(data, axis=axis)
    
def calculate_stddev(data, axis = None):
    if axis is None:
        return np.std(data)
    else:
        return np.std(data, axis=axis)
    
def calculate_max(data, axis = None):
    if axis is None:
        return np.max(data)
    else:
        return np.max(data, axis=axis)
    
def calculate_min(data, axis = None):
    if axis is None:
        return np.min(data)
    else:
        return np.min(data, axis=axis)
    
def calculate_total(data, axis = None):
    if axis is None:
        return np.sum(data)
    else:
        return np.sum(data, axis=axis)