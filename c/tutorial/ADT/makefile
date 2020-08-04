# edit: main.o kbd.o command.o display.o insert.o search.o files.o utils.o
# cc -o main.o kbd.o command.o display.o insert.o search.o files.o utils.o

# main.o: main.c defs.h
# cc -c main.c
# kbd.o: kbd.c defs.h command.h
# cc -c command.c
# display.o: display.c defs.h buffer.h
# cc -c display.c 
# search.o: search.c defs.h buffer.h
# cc -c search.c 
# files.o: files.c defs.c buffer.c command.h
# cc -c files.c
# utils.o: utils.c defs.h
# cc -c utils.c 
# clean:
# rm edit main.o kbd.o command.o display.o insert.o search.o files.o utils.o

CC=clang++
edit: run.o stack.o vector.o
	c++ run.o stack.o vector.o -o edit

other: %.o
	@echo $<
	c++ $< -o other


# run.o: stack.hpp
# stack.o: stack.hpp

.PHONY: clean
clean:
	-rm edit run.o stack.o

