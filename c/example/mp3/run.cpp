#define DR_MP3_IMPLEMENTATION
#include "dr_mp3.h"
#include <iostream>

int main(int argc, char const *argv[])
{
    drmp3 mp3;
    drmp3_config cfg {1, 16000};
    if (!drmp3_init_file(&mp3, "test.mp3", &cfg, nullptr)) {
        std::cout << "file wrror\n";
        return 1;
    }
    drmp3_uint32 channels = mp3.channels;
    drmp3_uint32 sampleRate = mp3.sampleRate;
    std::cout << "channels: " << channels << " sampleRate: " << sampleRate << std::endl;
    return 0;
}
