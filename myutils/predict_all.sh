# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/dengyangshen/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/dengyangshen/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/dengyangshen/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/dengyangshen/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

conda activate fossil;

for i in `ls data/imgs`
do 
python predict.py -i data/imgs/$i -o data/predict/$i --model ./checkpoints/CP_epoch5.pth
done;

for j in `ls data/imgs_dim2`
do
python predict.py -i data/imgs_dim2/$j -o data/predict_dim2/$j --model ./checkpoints/CP_epoch5.pth
done;

for k in `ls data/imgs_dim3`
do
python predict.py -i data/imgs_dim3/$k -o data/predict_dim3/$k --model ./checkpoints/CP_epoch5.pth
done;
