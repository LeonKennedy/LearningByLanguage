#ifndef MOVE_SEMANTICS_H_
#define MOVE_SEMANTICS_H_

class Useless
{
    private:
        int n;
        char * pc;
        static int ct;
        void ShowObject() const;
    public:
        Useless();
        explicit Useless(int k);
        Useless(int , char);
        Useless(const Useless &);
        Useless(Useless &&); // move constructor
        ~Useless();
        Useless operator+(const Useless &) const;
        void ShowData() const;
};


void play_useless();

#endif