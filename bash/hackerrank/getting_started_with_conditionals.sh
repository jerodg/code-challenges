read -n 1 char

if [[ $char == 'Y' || $char == 'y' ]]; then
    echo "YES"
elif [[ $char == 'N' || $char == 'n' ]]; then
    echo "NO"
fi
