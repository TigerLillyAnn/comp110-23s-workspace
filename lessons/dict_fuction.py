"""CQ4 - Dictionary Function writing!"""
__author__ = "730477496"

from typing import List, Dict

def zip(keys: List[str], values: List[int]) -> Dict[str, int]:
    if len(keys) != len(values):
        return 
    
    output = []
    for i in range(len(keys)):
        output[keys[i]] = values[i]
    return output