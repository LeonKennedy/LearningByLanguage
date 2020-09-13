#include <arpa/inet.h>
#include <sys/socket.h>
// #include <netinet/in.h>
#include <iostream>
#include <netdb.h>
#include <fcntl.h>
// #include <errno.h>
#include <thread>

#define BUFLEN 1000
#define QLEN 10
#define HOST_NAME_MAX 256

void method()
{
    // h 表示主机字节序 n 表示网络字节序
    // l 表示长整数 4字节    s表示短整数 4字节

    // uint32_t htonl(uint32_t hostint32);  //返回以网络字节序表示的32位整数
    // uint16_t htons(uint16_t hostint16);  //返回以网络字节序表示的16位整数
    // uint32_t ntohl(uint32_t hostint32);  //返回以主机字节序表示的32位整数
    // uint16_t htohs(uint16_t hostint16);  //返回以主机字节序表示的16位整数
}
void showhostent()
{
    // 查询网络地址
    hostent *phe = gethostent();
    std::cout << "gethostent: " << std::endl;
    std::cout << "\th_addr_list: " << phe->h_addr_list << std::endl;
    std::cout << "\th_addrtype: " << phe->h_addrtype << std::endl;
    std::cout << "\th_aliases: " << phe->h_aliases << std::endl;
    std::cout << "\th_length: " << phe->h_length << std::endl;
    std::cout << "\th_name: " << phe->h_name << std::endl;

}

int initserver(int type, const struct sockaddr *addr, socklen_t alen, int qlen)
{
    int fd;
    int err = 0;
    if ((fd = socket(addr->sa_family, type, IPPROTO_TCP)) < 0)
        return -1;
    if (bind(fd, addr, alen) < 0) {
        err = errno;
        shutdown(fd, SHUT_RDWR);
        errno = err;
        return -1;
    }
    if (listen(fd, qlen) < 0) {
        shutdown(fd, SHUT_RDWR);
        return -1;
    }
    std::cout << "fd: " << fd << std::endl; 
    return fd;
}

int InitSocketServer()
{
    int fd;
    struct sockaddr_in serv_addr; 
    std::string host = "127.0.0.1";
    int port = 9492;
    memset(&serv_addr, 0, sizeof(serv_addr));  //每个字节都用0填充
    serv_addr.sin_family = AF_INET;  //使用IPv4地址
    serv_addr.sin_addr.s_addr = inet_addr(host.c_str());  //具体的IP地址
    serv_addr.sin_port = htons(9492);  //端口
    if ((fd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0)
        throw std::runtime_error("cant create socket fd");
    if (bind(fd, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) < 0) 
        throw std::runtime_error("cant bind socket fd");
    if (listen(fd, 20) < 0)
        throw std::runtime_error("cant listen socket fd");
    std::cout << "start listen " << host <<":"<< port <<std::endl;
    return fd;
}

int set_cloexec(int fd)
{
    int val;
    if ((val = fcntl(fd, F_GETFD, 0)) < 0)
        return -1;
    val |= FD_CLOEXEC;
    return (fcntl(fd, F_SETFD, val));
}

void serve(int sockfd)
{
    int clfd;
    FILE *fp;
    char buf[BUFLEN];

    set_cloexec(sockfd);
    for (;;) {
        if ((clfd = accept(sockfd, NULL, NULL)) < 0) {
            std::clog << "ruptimed: accept error: " << strerror(errno);
            exit(1);
        }
        set_cloexec(clfd);
        send(clfd, buf, strlen(buf), 0);
        shutdown(clfd, SHUT_RDWR);
    }
}

int main(){
    struct addrinfo *alilist, *aip;
    int serv_sock = InitSocketServer();
    // std::cout << "start" << std::endl;
    // sockaddr * sa = (struct sockaddr*)&serv_addr;
    // std::cout << "sockaddr_in:" << serv_addr.sin_family << " binary s_addr " << serv_addr.sin_addr.s_addr << " " << inet_ntoa(serv_addr.sin_addr) << std::endl; 
    // std::cout << "scokeaddr:" << sa->sa_family << " " << sa->sa_len << std::endl;
    showhostent();
    //接收客户端请求
    
    while (1) {
        struct sockaddr_in clnt_addr;
        socklen_t clnt_addr_size = sizeof(clnt_addr);
        int clnt_sock = accept(serv_sock, (struct sockaddr*)&clnt_addr, &clnt_addr_size);
        //向客户端发送数据
        std::cout << inet_ntoa(clnt_addr.sin_addr) << ":" << clnt_addr.sin_port <<  std::endl;
        float buf[BUFLEN];
        char str[] = "Hello World!";
        int n = 0;
        int epo = 0;
        while(1){
            n = recv(clnt_sock, buf, BUFLEN, 0);
            epo++;
            if (epo == 1) {
                for (int n=0; n < 100 ; n++)
                    std::cout << buf[n] << ' ';
                std::cout << std::endl;
            }
            if (n < BUFLEN) 
                break;
        }
        shutdown(clnt_sock, SHUT_RD);
        std::cout << std::endl;
        std::cout << "send " << str << " size: " << sizeof(str) << std::endl;;
        send(clnt_sock, str, sizeof(str), 0);
        //关闭套接字
        shutdown(clnt_sock, SHUT_WR);
    }
    shutdown(serv_sock, SHUT_RDWR);
    return 0;
}