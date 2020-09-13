#include <iostream>
#include <stdio.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <sys/socket.h>

void print_family(struct addrinfo *aip)
{
    printf(" family ");
    switch(aip->ai_family) {
        case AF_INET:
            printf("inet");
            break;
        case AF_INET6:
            printf("inet6");
            break;
        case AF_UNIX:
            printf("unix");
            break;
        case AF_UNSPEC:
            printf("unspecified");
            break;
        default:
            printf("unkonw");
    }
}

void print_type(struct addrinfo *aip)
{
    printf(" type ");
    switch (aip->ai_socktype) {
        case SOCK_STREAM:
            printf("stream");
            break;
        case SOCK_DGRAM:
            printf("datagram");
            break;
        case SOCK_SEQPACKET:
            printf("seqpacket");
            break;
        case SOCK_RAW:
            printf("raw");
            break;
        default:
            printf("unkonw (%d)", aip->ai_socktype);
    }
}


void print_protocol(struct  addrinfo *aip) 
{
    printf(" protocol ");
    switch (aip->ai_protocol) {
        case 0:
            printf("default");
            break;
        case IPPROTO_TCP:
            printf("tcp");
            break;
        case IPPROTO_RAW:
            printf("raw");
            break;
        default:
            printf("unknow (%d)", aip->ai_protocol);
    }
};

int main(int argc, char *argv[])
{
    struct addrinfo *ailist, *aip;
    struct addrinfo hint;
    struct sockaddr_in *sinp;
    const char *addr;
    int err;
    char abuf[INET_ADDRSTRLEN];
    if (argc !=3) {
        std::cerr << "usage: " << argv[0] << " nodename service" << std::endl;
        exit(1);
    }
    hint.ai_flags = AI_CANONNAME;
    hint.ai_flags = 0;
    hint.ai_socktype = 0;
    hint.ai_protocol = 0;
    hint.ai_addrlen = 0;
    hint.ai_canonname = NULL;
    hint.ai_addr = NULL;
    hint.ai_next = NULL;
    if ((err = getaddrinfo(argv[1], argv[2], &hint, &ailist)) !=0 ) {
        std::cerr << "getaddrinfo error: " << gai_strerror(err) << std::endl;
        exit(1);
    }
    for (aip = ailist; aip != NULL; aip = aip->ai_next) {
        print_family(aip);
        print_type(aip);
        print_protocol(aip);
        printf("\n\thost %s\n", aip->ai_canonname? aip->ai_canonname: "-");
        if (aip->ai_family == AF_INET) {
            sinp = (struct  sockaddr_in *)aip->ai_addr;
            addr = inet_ntop(AF_INET, &sinp->sin_addr, abuf, INET_ADDRSTRLEN);
            printf(" address %s", addr?addr: "unkonw");
            printf(" port %d\n", ntohs(sinp->sin_port));
        }
    }
    return 0;
}