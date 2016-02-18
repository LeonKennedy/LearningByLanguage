#include<pthread.h>
#include<stdio.h>
#include<stdbool.h>

//int pthead_create(pthread_t* restrict tidp, const pthread_attr_t* restrict attr, void *(*start_rtn)(void), void *restrict arg);

typedef struct _block{
    int aa;
} Block;
bool GetBlockFromNet(Block * out_block);
bool WriteBlockToDisk(Block * in_block);

pthread_key_t key;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;
unsigned long abc = 0;
