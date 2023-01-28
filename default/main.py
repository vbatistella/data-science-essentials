import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Name:
    def open(self, path):
        return

    def clean(self, df):
        return
    
    def execute(self, df):
        return
    
    def show(self, df, result):
        return
    
    def save(self, pic):
        return

def main():
    alg = Name()
    df = alg.open("")
    df = alg.clean(df)
    result = alg.execute(df)
    pic = alg.show(df, result)
    alg.save(pic)


if __name__ == "__main__":
    main()