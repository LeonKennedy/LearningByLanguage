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

void *Test03(void *p)
{
    printf("Cancel point");
    return NULL;
}

void *Test01(void *ptr)
{
    pthread_cleanup_push(Test03,NULL);
    while(1){
        abc++;
        pthread_testcancel(); 
    }
    pthread_cleanup_pop(0);
    return NULL;
}

void *Test02(void *ptr)
{
    while(1){
        sleep(2);
        printf("222cond_wait:abc =0x%08x\n",abc); 
    }
    return NULL;
}

int main(void)
{
    pthread_t tid1,tid2;
    int ret;
    
    printf("Start:\n");
    ret = pthread_create(&tid1, NULL, Test01, NULL);
    ret = pthread_create(&tid2, NULL, Test02, NULL);
    
    sleep(6);
    pthread_cancel(tid1);
    pthread_join(tid1,NULL);
    pthread_join(tid2,NULL);

    return 0;
}
