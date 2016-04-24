#!/bin/sh
screen ./latticelm -annealsteps 10 -unkn 10 -burnin 100 -samps 1000 -prefix ./output/ ../corpus/voynich_s.txt
