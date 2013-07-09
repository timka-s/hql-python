coverage erase
coverage run --source src --module py.test $@
coverage report --show-missing --omit=*__test*,*__fixture*,*conftest*

read -sn1 -p "Press Q to exit or press other key to repeat..." line
if [[ $line != 'Q' ]] && [[ $line != 'q' ]]
then ./test.sh $@
fi
echo ''
