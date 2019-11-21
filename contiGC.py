import csv
import os
from pathlib import Path
import argparse
import plotly
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='path to a fasta file containing contigs or scaffolds')
args = parser.parse_args()

if args.input:
    input_path = Path(args.input)
    input_filename = os.path.basename(input_path)
else:
    print('No input file provided')
    #input_path = Path('test.fasta')
    raise SystemExit

gccontent ={}
frequencies = []
contigs = 0

with open(input_path) as file:
    input = file.read().splitlines()
    for line in input:
        if not line.strip(): continue
        if line[0] == '>':
            contigs += 1
            gc = 0
            at = 0
            name = line[1:]
            gccontent[name] = ''
        else:
            for base in line:
                if base.lower() == 'a':
                    at += 1
                if base.lower() == 't':
                    at += 1
                if base.lower() == 'c':
                    gc += 1
                if base.lower() == 'g':
                    gc += 1
            total = gc + at

            gccontent[name] = 100/total*gc

for key, value in sorted(gccontent.items(), key=lambda item: item[1]):
    #print("%s: %s" % (key, value))
    frequencies.append(value)
   
print(frequencies[:10])
print('...')
print(frequencies[-10:])

gcdf = pd.DataFrame(list(gccontent.items()))
print(gcdf)

fig = px.histogram(gcdf, x=1, nbins=100)
fig.update_layout(
    title=input_filename,
    xaxis_title='GC content',
    yaxis_title='number of contigs'
)
fig.update_xaxes(range=[0,100])

plotly.io.write_html(fig, file=input_filename+'.html', auto_open=False)