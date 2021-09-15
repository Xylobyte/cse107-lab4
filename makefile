COURSE = cse107
GROUP_NAME = donovan_griego
ASSIGNMENT = lab4
TARGETS = navigate2.py nested.py statistics107.py
zip: $(TARGETS)
	zip $(COURSE)_$(GROUP_NAME)_$(ASSIGNMENT).zip $(TARGETS)