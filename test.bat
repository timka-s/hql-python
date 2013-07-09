coverage erase
coverage run --source src --module py.test %*
coverage report --show-missing --omit=*__test*,*__fixture*,*conftest*
