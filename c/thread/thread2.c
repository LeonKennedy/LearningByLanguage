#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
/*
 * 功能：主要使用线程互斥
 * 相关：prthread_mutex_t pthread_cond_t
 * 作者：coffee
 */ 


pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;
void* thr1(void *arg)
{
    pthread_mutex_lock(&mutex);
    printf("in thread 0 tag 1\n");
    sleep(5);
    /*这个小例子中理解这个函数最为重要：
     * 它有两个特点:
     *       1.调用时会释放锁 
     *       2.等待时会设置enable_asynccancel,被唤醒后会设置disable_asynccancel。 
     *       3.等待是被取消，会调用清理程序，取回锁，如此将会形成死锁.
     */
    pthread_cond_wait(&cond, &mutex);
    printf("in thread 0 tag 2\n");
    pthread_mutex_unlock(&mutex);
    printf("in thread 0 tag 3\n");
    pthread_exit(NULL);
}

void* thr2(void *arg)
{
    sleep(2);
    printf("in thread 1 tag 1\n");
    pthread_mutex_lock(&mutex);
    printf("in thread 1 tag 2\n");
    pthread_cond_broadcast(&cond);
    pthread_mutex_unlock(&mutex);
    printf("in thread 1 tag 3\n");
    pthread_exit(NULL);
}

int main()
{
    pthread_t tid[2];
    if (pthread_create(&tid[0], NULL, thr1, NULL) != 0) {
        exit(1);
    }
    if (pthread_create(&tid[1], NULL, thr2, NULL) != 0) {
        exit(1);
    }
    sleep(6);
    printf("in main thread tag 1\n");
    //pthread_cancel(tid[0]);

    pthread_join(tid[0], NULL);
    pthread_join(tid[1], NULL);

    pthread_mutex_destroy(&mutex);
    pthread_cond_destroy(&cond);
    return 0;
}

    

