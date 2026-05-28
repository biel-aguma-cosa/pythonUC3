#$DIR/scripts/sleep_test.sh
SECONDS=0

declare -A array



for i in {0..10000};do
    array[i]=$((i*i*i*i*i*i*i*i*i*i*i))
done
echo "FINISHED AT $SECONDS"