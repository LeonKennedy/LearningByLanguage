#include <stdio.h>
//这里描述一个堆栈被占满的情况 
//当栈被塞满也会会出现段错误
int g_i = 0;
void fun()
{
    char tf[1024*1024];
    printf("g_i is %d\n", g_i++);
    fun();
}
int main()
{
    fun();
}
