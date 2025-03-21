#!/bin/bash

suf1=".te1"
suf2=".te2"

cp $1.md $1$suf1

python3 modifica_apersan.py $1

mv $1$suf2 $1$suf1

#python3 modifica_gatos.py 

#mv $1$suf2 $1.rst



