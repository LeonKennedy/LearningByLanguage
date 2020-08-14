objs = run.o oper.o iter.o algo.o
CPP_FLAGS=-std=c++11
run: $(objs)
	c++ -std=c++11 $(objs) -o $@ 
	-rm $<

run.o : run.cpp oper.hpp iter.hpp algo.hpp
	c++ ${CPP_FLAGS} -c run.cpp

oper.o: oper.cpp oper.hpp
	c++ ${CPP_FLAGS} -c oper.cpp

iter.o: iter.cpp iter.hpp
	c++ ${CPP_FLAGS} -c iter.cpp

algo.o: algo.cpp algo.hpp
	c++ ${CPP_FLAGS} -c algo.cpp

.PHONY: clean
clean: 
	-rm ${objs}