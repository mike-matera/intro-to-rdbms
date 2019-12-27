SOURCE = $(shell ls notebooks/*/*.py)
NOTEBOOKS = $(SOURCE:.py=.ipynb)
GENERATOR = $(abspath ./tools/gen_questions.py)

all: $(NOTEBOOKS)

%.ipynb: %.py $(GENERATOR)
	cd $(dir $*); python3 $(GENERATOR) $(notdir $*)

clean: 
	rm $(NOTEBOOKS)

.PYONY: clean
