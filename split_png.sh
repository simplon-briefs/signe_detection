mkdir ./test
mkdir ./train
mkdir ./dir_tmp
for i in `ls image_kaggle`:
do  
    n=0
    for y in `ls image_kaggle/$i`
    do
        if [ $(( n % 8 )) -eq 0 ]; then
            new_dir="./test/${i}/"
        else
            new_dir="./train/${i}/"
        fi
        mkdir $new_dir
        img="image_kaggle/${i}/${y}"
        python3 code/img_to_csv.py $img
        #python3 code/GenerateTracking.py $img
        mv ./dir_tmp/opencv0.png $new_dir$y
        n=$n+1

        
    done
done
rm -fr dir_tmp