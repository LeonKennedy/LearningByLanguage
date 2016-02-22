#include <stdio.h>
#include <pthread.h>
//线程取消的使用方法
//取消点的设置   例如第三方库的调用 就算取消点之一

void *thr (void* arg)
{
    //pthread_setcancelstate(PTHREAD_CANCEL_DISABLE,NULL);
    pthread_setcancelstate(PTHREAD_CANCEL_ENABLE,NULL);
    //pthread_setcanceltype(PTHREAD_CANCEL_ASYNCHRONOUS,NULL); 
    pthread_setcanceltype(PTHREAD_CANCEL_DEFERRED,NULL); 
    int i=0;
    while(1){
        //pthread_testcancel();
    }
    printf("bb\n");;
    sleep(2);
}

int main()
{
    pthread_t th1;
    pthread_create(&th1, NULL, thr, NULL);
    sleep(1);
    pthread_cancel(th1);       //在PTHREAD_CANCEL_ENABLE   PTHREAD_CANCEL_DEFERRED的情况下才可以使用
    pthread_join(th1, NULL);
    printf("The Main thread is exit!");
    return 0;
}
