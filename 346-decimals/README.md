# manual testing

## using manual input
- execute the following command:
```sh
./src.py
```
- type your input
- press ^D (ctrl + d) in order to flush it

## using redirected input
```sh
printf "<your input>" | ./src.py
```

# automatic testing (using examples/)
- write a new test by creating two files : *examples/\<name\>.in.txt* containing an input and *examples/\<name\>.out.txt* containing the output to expect
- execute the following command:
```sh
./test.py
```

bonus: refresh test results screen whenever the src content changes
```sh
ls src.py | entr -c -s "./test.py"
```
