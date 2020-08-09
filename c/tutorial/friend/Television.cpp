#include "Television.hpp"
#include <iostream>
#include <string>

namespace TELEVISION
{
    void Television::show()
    {
        std::cout << "Tv is " << state << " channel is :" << channel 
            << " volume: " << vol << std::endl;
    }
    void Television::play_audio_by_remote(Remote & re, const std::string & s)
    {
        re.play_audio(s);
    }
    void Remote::volUp(Television & tv) 
    {
        tv.volUp();
    }
    void Remote::volDown(Television & tv) 
    {
        tv.volDown();
    }
    void Remote::onoff( Television & tv) 
    {
        tv.onoff();
    }

    void Remote::set_channel(Television & tv, int & i)
    {
        tv.channel = i;
    }

    void Remote::play_audio(const std::string & s)
    {
        std::cout << "[data from tv] " << s << std::endl;
    }

    void play()
    {
        Television tv1;
        Remote re;
        tv1.show();
        int c = 20;
        re.set_channel(tv1, c);
        tv1.show();
        std::string s = "nidfe";
        tv1.play_audio_by_remote(re, s);
        re.volUp(tv1);
        re.volUp(tv1);
        re.onoff(tv1);
        tv1.show();
    }
}