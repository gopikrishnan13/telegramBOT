# a = "([\+\-]?\d+\.?\d*[\+\-\*\/]?)"
# 1  = ((\(*[\-\+]?\d+\)*)*[\+\-\*\/\%](\(*[\-\+]?\d+\)*)*)?
#final = '"(((\(*[-\+]?\d+\)*)[\+\-\*\%\/]{1}(\(*[-\+]?\d+\)*))([\+\-\*\%\/]{1}\(*[-\+]?\d+\)*)*)"gm'

import re
txt = "/math 9834+2"
pattern = re.compile(r"(((\(*[-\+]?\d+\)*)[\+\-\*\%\/]{1}(\(*[-\+]?\d+\)*))([\+\-\*\%\/]{1}\(*[-\+]?\d+\)*)*)")
matches = pattern.finditer(txt)
print(matches)
