

obj = WebtownClub.o run.o Students.o Worker.o
cc = clang++
run: $(obj)
	c++ $(obj) -o $@
	
# all: WebtownClub.o run.o
# 	c++ WebtownClub.o run.o -o all


.PHONY: clean
clean: 
	-rm $(obj)