import pandas as pd 
import sys
import soundex
from pyphonetics import Soundex
sound=Soundex()

       
df1=list(pd.read_csv("train.csv").tweets.values)
df2=list(pd.read_csv("dev.csv").tweets.values)
df3=list(pd.read_csv("test.csv").tweets.values)


all_tw_se=[]
all_tweets= df1+df2+df3
for tweet in all_tweets:
    ex_wrds=tweet.split()
    sound_enc=[]
    for wrd in ex_wrds:
        try:
            enc=sound.phonetics(wrd.strip())
            # sound_enc.append(wrd)
            sound_enc.append(enc)
        except:
            # sound_enc.append(wrd)
            sound_enc.append("0000")
    sound_vector=" ".join(sound_enc)
    all_tw_se.append(tweet.strip()+" [SEP] "+sound_vector)

from sklearn.model_selection import train_test_split 

x_train, x_test, y_train, y_test=train_test_split(all_tw_se, all_tw_se, test_size=0.2)
print(len(x_train), len(x_test))

with open("train.txt", "w") as f:
	for i in range(len(x_train)):
		f.write(x_train[i])
		f.write("\n")
pass
with open("dev.txt", "w") as f:
	for i in range(len(x_test)):
		f.write(x_test[i])
		f.write("\n")
pass


