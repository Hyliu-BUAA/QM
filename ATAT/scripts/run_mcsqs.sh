#PBS -N sqs_ReNbSSe
#PBS -l nodes=1:ppn=24
#PBS -l walltime=1445:00:00
#PBS -q batch
#PBS -S /bin/bash
#PBS -V

source /opt/intel2015/composer_xe_2015/bin/compilervars.sh intel64
source /opt/intel2015/mkl/bin/intel64/mklvars_intel64.sh
source /opt/intel2015/impi/5.0.2.044/bin64/mpivars.sh


NP=`cat $PBS_NODEFILE | wc -l`
NN=`cat $PBS_NODEFILE | sort | uniq | tee /tmp/nodes.$$ | wc -l`
EXEC=/opt/software/vasp_ifort/vasp.5.4.4/bin/vasp_std

cat $PBS_NODEFILE > /tmp/nodefile.$$
cd $PBS_O_WORKDIR
ulimit -s unlimited


### 以上部分，根据集群不同儿不同

# 1. 提取团簇信息
mcsqs -2=5 -3=3

# 2. 搜索结构
mcsqs -n=108 -2d