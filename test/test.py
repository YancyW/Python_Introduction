
#import tensorflow as tf
#import numpy as np


import re
rule = "cat"
replace = "dog"
target = "I like a cat"
print(re.sub(rule,replace,target))
