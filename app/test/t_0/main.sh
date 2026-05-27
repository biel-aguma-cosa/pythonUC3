#main.sh
declare -r DIR=$(dirname "$0")

echo $DIR

rm -f $DIR/temp/pipe
rm -rf $DIR/temp
mkdir -p $DIR/temp
mkfifo $DIR/temp/pipe

python3 $DIR/scripts/graphics.py /temp/pipe &
declare -r PY_PID=$!

declare input=""
while [ "$input" != "q" ];do
    echo "#MAIN.SH \$input - $input"
    case $input in
        "player_x="*) echo "$input" > $DIR/temp/pipe;;
        "player_y="*) echo "$input" > $DIR/temp/pipe;;
    esac
    read input
done

kill $PY_PID
echo "#MAIN.SH - waiting"
wait
echo "#MAIN.SH - end"