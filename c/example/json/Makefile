
run: run.o 
	c++ -std=c++11 run.o  -o run
	-rm run.o

run.o: run.cpp json.hpp
	c++ -std=c++11 -c run.cpp