#include <iostream>
#include <string>

namespace TELEVISION
{

class Television;


class Remote
{
    public:
        friend class Television;
        Remote(){}
        void volUp(Television & tv);
        void volDown(Television & tv); 
        void onoff( Television & tv);
        void set_channel(Television & tv, int & c);
    private:
        void play_audio(const std::string & s);
};

class Television
{
    
    public:
        friend void Remote::set_channel(Television &, int &);
        enum {Off, On};
        Television(): vol(20), channel(0), state(Off){}
        void volUp() { vol++ ;}
        void volDown() {vol--;}
        void onoff() {state ^= 1;}
        void show();
        void play_audio_by_remote(Remote &, const std::string &);

    private:
        int channel;
        int vol;
        int state;
};

void play();
} // end namespace
