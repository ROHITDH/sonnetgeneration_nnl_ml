import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
#!/usr/bin/env python
#sonnet generator
#ada_lovelase_day_celebration
#19/09/2020

#import req. lib/package
from keras.models import load_model
import numpy as np
import warnings
warnings.filterwarnings("ignore")





def load_data(max_length_seq=25, step=3):
    with open(os.path.join(os.getcwd(),os.path.join('dataset.txt')), 'r', encoding = 'utf8') as f:
        data = f.read().lower()

    sentences = []
    targets = []
    for i in range(0, len(data) - max_length_seq, step):
        sentences.append(data[i:i + max_length_seq])
        targets.append(data[max_length_seq + i])
    #all unique characters
    uniques = sorted(list(set(data)))
    #unique --->  integer indices
    unique_indices = dict((unique, uniques.index(unique)) for unique in uniques)
    return data, unique_indices, uniques

#Reweight predicted
def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

#model loading and construction through prediction
#for sonnet lines
def generate_sonnet(new_sonnet):
    new_sonnet=new_sonnet.lower()[:40]
    max_length_seq = len(new_sonnet)
    step = 3
   # new_gen = ""
    data, unique_indices, uniques = load_data(max_length_seq, step)

    model = load_model('sonnet_gen_model.h5')
   # start_idx = np.random.randint(0, len(data) - max_length_seq - 1)
   # new_sonnet = data[start_idx:start_idx + max_length_seq]
    new_gen = new_sonnet
    for i in range(625):

        sampled = np.zeros((1, max_length_seq, len(uniques)))
        for j, unique in enumerate(new_sonnet):
            sampled[0, j, unique_indices[unique]] = 1.


        preds = model.predict(sampled, verbose=0)[0]
        pred_idx = sample(preds, temperature=0.5)
        next_unique = uniques[pred_idx]

        # Append unique and ready for next unique
        new_sonnet += next_unique
        new_sonnet = new_sonnet[1:]

        new_gen += next_unique
    return new_gen


#model loading and construction through prediction
#generate sonnet full
def generate_sonnet_f():
    max_length_seq = 40
    step = 3
    new_gen = ""
    data, unique_indices, uniques = load_data(max_length_seq, step)

    model = load_model('sonnet_gen_model.h5')
    start_idx = np.random.randint(0, len(data) - max_length_seq - 1)
    new_sonnet = data[start_idx:start_idx + max_length_seq]
    new_gen += new_sonnet
    for i in range(625):

        sampled = np.zeros((1, max_length_seq, len(uniques)))
        for j, unique in enumerate(new_sonnet):
            sampled[0, j, unique_indices[unique]] = 1.


        preds = model.predict(sampled, verbose=0)[0]
        pred_idx = sample(preds, temperature=0.5)
        next_unique = uniques[pred_idx]

        # Append unique and ready for next unique
        new_sonnet += next_unique
        new_sonnet = new_sonnet[1:]

        new_gen += next_unique
        
    print("\n\n")
    return new_gen



def generate_sonnet_lines(inp):
    if len(inp)<40:
        inp=inp+(40-len(inp))*" "

    d=generate_sonnet(inp).replace("\n\n","\n").split("\n")[0:14]
    
    for i in(d):
        print("\t\t" , i.strip())

        
def generate_sonnet_full():
    d=generate_sonnet_f().replace("\n\n","\n").split("\n")[1:15]
    d1=d.pop(0).split(" ")

    if(d1[0]=="'" or d1[0]=='"'or d1[0]==':'or d1[0]==';'or d1[0]==','or d1[0]=='.'):
        d1[0]=""
        if(d1[1].lower()=='and' or d1[1].lower()=='but' or d1[1].lower()=='And' or d1[1].lower()=='But'):
            d1[1]="As"
    elif(d1[0].lower()=='and' or d1[0].lower()=='but' or d1[0].lower()=='And' or d1[0].lower()=='But'):
        d1[0]="As"

    d2 = d.pop().split(" ")
    if(d2[-1].lower()=='and' or d2[-1].lower()=='but' or d2[-1].lower()=='And' or d2[-1].lower()=='But'):
        d2[-1]="."

    d = [" ".join(d1).strip().capitalize()]+d+[" ".join(d2).strip()]
    k=0
    for i in d:
        d[k]=i.strip()
        k+=1
    for line in d:
        print("\t\t",line)
   

def run():    
    inp = input("\n\t<< ENTER a line of Sonnet / Leave blank to generate Random >> \n\n >> : ")
    if len(inp) <=25 and len(inp)>0:
        print("\tYour input sequence is too short, \n\t So generating whole sonnet:\n")
        generate_sonnet_full()

    elif len(inp) >= 90:
        print("\tYour input sequence is too large, \n\t So generating whole sonnet:\n")
        generate_sonnet_full()
    else:
        print("\n\t..Generating a sonnet for you..\n\n")
        generate_sonnet_lines(inp)
    
    
##########  attributions  ##############
## loosely based on theory on machinelearningmastery.com by Jason Brownlee