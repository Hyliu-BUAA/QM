#!/bin/sh
#SBATCH --partition=cpu
#SBATCH --job-name=cu1646_vv12
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --threads-per-core=1

##SBATCH --gres=gpu:4
##SBATCH --gpus-per-task=1


module load intel/2020
conda activate psi4

psi4 input.dat output.dat