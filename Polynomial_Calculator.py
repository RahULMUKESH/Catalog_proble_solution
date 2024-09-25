import json  
import sys  

def decode_value(base, value):  
    """  
    Decode a given value represented in a specific base to decimal.  
    """  
    return int(value, int(base))  

def lagrange_interpolation(x_values, y_values):  
    """  
    Calculate the interpolated value at x=0 to find the constant term (c).  
    """  
    total = 0  
    n = len(x_values)  
    
    for i in range(n):  
        xi, yi = x_values[i], y_values[i]  
        li = 1  
        
        for j in range(n):  
            if i != j:  
                xj = x_values[j]  
                li *= (0 - xj) / (xi - xj)  

        total += li * yi  

    return total  

def main(input_json):  
    # Load JSON input  
    data = json.loads(input_json)  
    
    n = data["keys"]["n"]  
    k = data["keys"]["k"]  
    
    # Prepare lists for x (keys) and y (decoded values)  
    x_values = []  
    y_values = []  

    # Iterate through the JSON data, decode the y values  
    for key in range(1, n + 1):  
        base = data[str(key)]["base"]  
        value = data[str(key)]["value"]  
        x = key  # the key is the x-coordinate  
        y = decode_value(base, value)  # decode y value  
        
        x_values.append(x)  
        y_values.append(y)  
    
    # Perform Lagrange interpolation to find c  
    c = lagrange_interpolation(x_values[:k], y_values[:k])  # use only the first k pairs  

    print(int(c))  

if __name__ == "__main__":  
    # Test with the given second testcase  
    input_json = '''{  
        "keys": {  
            "n": 9,  
            "k": 6  
        },  
        "1": {  
            "base": "10",  
            "value": "28735619723837"  
        },  
        "2": {  
            "base": "16",  
            "value": "1A228867F0CA"  
        },  
        "3": {  
            "base": "12",  
            "value": "32811A4AA0B7B"  
        },  
        "4": {  
            "base": "11",  
            "value": "917978721331A"  
        },  
        "5": {  
            "base": "16",  
            "value": "1A22886782E1"  
        },  
        "6": {  
            "base": "10",  
            "value": "28735619654702"  
        },  
        "7": {  
            "base": "14",  
            "value": "71AB5070CC4B"  
        },  
        "8": {  
            "base": "9",  
            "value": "122662581541670"  
        },  
        "9": {  
            "base": "8",  
            "value": "642121030037605"  
        }  
    }'''  
    
    main(input_json)