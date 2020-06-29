import sys
import pandas as pd
import re


def find_longest_tandem_repeats(seq, tandem):
    
# define
    tandem_length = len(tandem)
    nors = []

# find all occurrences    
    lotr = re.findall(f"{tandem}(?:{tandem})*", seq)

# if no tandem are found return 0    
    if not lotr:
        temp = 0
        return(temp)

# go through the list of tantem repeats and calculate the number of repeats        
    for tr in lotr:
        nors.append(len(tr)/tandem_length)

# returns the longest number of repeats    
    return(int(max(nors)))    

def compare_number_of_repeats(lols, df):
#    print(df[0:len(df.columns)])
#    print(lols)

# create a data frame with bolean values based on the repeat counts    
    df2 = df.isin(lols)

# loop through the data frame, every row becomes a Series and if all the values are True
# the function returns the row(index)name for that row. 
    for i in range(len(df.index)):
        if (df2.iloc[i].all()):
            return(df2.index.values[i])
    
def main():
    lols = []
    if len(sys.argv) != 3:
        raise ValueError("Invalid argument number")

# Open fasta file        
    with open(sys.argv[2], "r") as sequence:
        seq = sequence.read()
        
# Open database using panda         
    with open(sys.argv[1], "r") as database:  
        df = pd.read_csv(database, index_col=0)
   
# Create a list with the tandems
    tandems = list(df)[0:]
#    print(tandems[0])
#    print(seq)

# for each of the tandem call fuction that returns the longest repeat, append them in a list list of lenghts   
    for tandem in tandems:
        lols.append(find_longest_tandem_repeats(seq, tandem))

# compare lols with the csv table
    match = compare_number_of_repeats(lols, df)
    
    if not match:
        print("No match")
    else:
        print(match)    

main()    
