import time
import pandas as pd
import numpy as np

def generate_stream():

    while True:

        data = {
            "temperature": np.random.normal(25,3),
            "battery": np.random.normal(85,5),
            "signal_strength": np.random.normal(90,4),
            "cpu_load": np.random.normal(40,10)
        }

        df = pd.DataFrame([data])

        yield df

        time.sleep(1)