objs=run.o report.o
CPP_FLAGS=-std=c++11
run: $(objs)
	c++ $(objs) -o $@
	-rm $< 

lambda: lambda.o
	c++ ${CPP_FLAGS} lambda.o -o lambda

lambda.o: lambda.cpp
	c++ ${CPP_FLAGS} -c lambda.cpp

.PHONY: clean
clean: 
	-rm lambda.o lambda report.o run



