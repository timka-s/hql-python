py.test \
  --cov-report term-missing \
  --cov-config coverage.ini  \
  --cov src/ \
  $@

read -sn1 -p "Press Q to exit or press other key to repeat..." line
if [[ $line != 'Q' ]] && [[ $line != 'q' ]]
then ./test.sh $@
fi
echo ''
