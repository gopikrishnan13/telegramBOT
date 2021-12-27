import re

def Math(Str:str):
    result = []
    pattern = re.compile(r"(((\(*[-\+]?\d+\)*)[\+\-\*\%\/]{1}(\(*[-\+]?\d+\)*))([\+\-\*\%\/]{1}\(*[-\+]?\d+\)*)*)")
    matches = pattern.finditer(Str)
    for match in matches:
        result.append(eval(match.group(0)))
    return result
