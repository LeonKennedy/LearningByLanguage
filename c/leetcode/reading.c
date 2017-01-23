#include<stdio.h>
#include<math.h>


/*
 *  458. Poor Pigs
 *
 *  If there are n buckets and a pig drinking poison will die 
 *  within m minutes, how many pigs (x) you need to figure out
 *  the "poison" bucket within p minutes? There is exact one 
 *  bucket with poison.
 */ 

int poorPigs(int buckets, int minutesToDie, int minutesToTest){
    int times = minutesToTest / minutesToDie;

    int pigs = 1;
    while(pow(times + 1, pigs) < buckets){
        pigs++;
    }
    return pigs;
}

main(){
    int ansersw = poorPigs(25,15,60);
    printf("%d\n", ansersw);


}
