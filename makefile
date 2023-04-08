#here is the makefile
PYTHON = python3

# set the default target
all: run

# compile and run the program
run: animal.py dog.py cat.py main.py
	$(PYTHON) main.py

# remove all compiled files
clean:
	rm -f *.pyc


#bootylicious
=======
>>>>>>> f8f32444ea1b16e9e8f5ccf215d7dc5646ed3dd6
