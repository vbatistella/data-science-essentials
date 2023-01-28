import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    def open(self, path):
        df = pd.read_csv(path, low_memory=False)
        return df

    def clean(self, df):
        df = df[df.Source == "GISTEMP"]
        # df = df[df.Date >= "1950-01-01"]
        df = df.sort_values("Date")
        df = df["Mean"]
        return df
    
    def execute(self, df):
        y = np.array(df.values.tolist())
        n = len(y)
        x = np.array([*range(n)])

        sumx = np.sum(x)
        sumy = np.sum(y)
        sumxy = sum([i * j for i, j in zip(x, y)])
        sumxsqrd = sum([i ** 2 for i in x])
        sumysqrd = sum([i ** 2 for i in y])

        b = (sumxy - ((sumx*sumy)/n)) / (sumxsqrd - ((sumx ** 2)/n))
        a = np.average(y) - b*np.average(x)

        return [a, b]
    
    def show(self, df, result):
        df = df.values.tolist()
        coef = 2.576
        plt.plot(range(len(df)), df, ".", c="black")
        plt.plot([1, len(df)], [result[0]+1*result[1], result[0]+len(df)*result[1]])
        plt.show()
        plt.savefig("out/out.png")

def main():
    alg = LinearRegression()
    df = alg.open("in/monthly_csv.csv")
    df = alg.clean(df)
    result = alg.execute(df)
    alg.show(df, result)


if __name__ == "__main__":
    main()