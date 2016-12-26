
rm log
for i in {1..20};
    do python2 grade.py $RANDOM $RANDOM;
done
python2 summary.py
