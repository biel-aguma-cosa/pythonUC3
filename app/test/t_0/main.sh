#main.sh
declare -r DIR=$(dirname "$0")

echo $DIR

rm -f $DIR/tmp/pipe
rm -rf $DIR/tmp
mkdir -p $DIR/tmp
mkfifo $DIR/tmp/pipe

python3 $DIR/scripts/graphics.py /tmp/pipe &
declare -r PY_PID=$!

declare input=""
while [ "$input" != "q" ];do
    echo "#MAIN.SH \$input - $input"
    case $input in
        "player_x="*) echo "$input" > $DIR/tmp/pipe;;
        "player_y="*) echo "$input" > $DIR/tmp/pipe;;
    esac
    read input
done

kill $PY_PID
echo "#MAIN.SH - waiting"
wait
echo "#MAIN.SH - end"