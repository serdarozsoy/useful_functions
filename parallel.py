import numpy as np
import pandas as pd
from joblib import Parallel, delayed
import multiprocessing
from multiprocessing import cpu_count
from multiprocessing.pool import Pool
 
cores = cpu_count() #Number of CPU cores on your system
partitions = cores #Define as many partitions as you want

def parallelize(data, func):
    data_split = np.array_split(data, partitions)
    pool = Pool(cores)
    data = pd.concat(pool.map(func, data_split))
    pool.close()
    pool.join()
    return data
    
#Example usage 1 
def work1(ht):
    return ht[ht['authorized_flag']=="Y"].groupby(["card_id","purchase_month_str"]).agg(aggs)

tt20 = parallelize(ht, work)

#Example usage 2 
def work2(tt20):
    return tt20.groupby('card_id').apply(lambda x : x.set_index('purchase_month_str')
                                            .resample('M')
                                            .first()
                                            .fillna(0)).reset_index(level=0, drop=True).reset_index()

tt40 = parallelize(tt20, work)