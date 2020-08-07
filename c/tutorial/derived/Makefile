

obj = WebtownClub.o run.o
cc = clang++
run: $(obj)
	c++ $(obj) -o $@
	-rm $(obj)
# all: WebtownClub.o run.o
# 	c++ WebtownClub.o run.o -o all

.PHONY: clean
clean: 
	-rm $(obj)