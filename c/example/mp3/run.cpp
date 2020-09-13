#define DR_MP3_IMPLEMENTATION
#include "dr_mp3.h"
#include <iostream>
#include <fstream>
#include <vector>

// int readStreamIntoBuffer(
//     std::istream& inputStream,
//     std::shared_ptr<IOBuffer> buffer,
//     int bytesToRead) {
//   assert(bytesToRead > 0);
//   assert(buffer);
//   int bytesRead = 0;
//   buffer->ensure<char>(bytesToRead);
//   char* inputPtrChar = buffer->data<char>();
//   while (bytesRead < bytesToRead && inputStream.good()) {
//     inputStream.read(inputPtrChar + bytesRead, bytesToRead - bytesRead);
//     bytesRead += inputStream.gcount();
//   }
//   buffer->move<char>(bytesRead);
//   return bytesRead;
// }

void show(drmp3 & pMp3) 
{
    std::cout << " mp3.currentPCMFrame : " << pMp3.currentPCMFrame << std::endl;
    std::cout << " mp3.dataSize: " << pMp3.dataSize << " mp3.dataCapacity: " << pMp3.dataCapacity << std::endl;
    std::cout << " mp3.pData: " << pMp3.pData  << std::endl;
    std::cout << " mp3.memory.currentReadPos: " << pMp3.memory.currentReadPos  <<  " mp3.memory.dataSize: " << pMp3.memory.dataSize << std::endl;
}

int main(int argc, char const *argv[])
{
    drmp3 mp3;
    drmp3_config cfg {1, 16000};
    if (!drmp3_init_file(&mp3, "test.mp3", &cfg, nullptr)) {
        std::cout << "file wrror\n";
        return 1;
    }
    std::cout << "channels: " << mp3.channels << " sampleRate: " << mp3.sampleRate << std::endl;
    std::cout << " drmp3_get_pcm_frame_count: " << drmp3_get_pcm_frame_count(&mp3) << std::endl;
    show(mp3);
    
    
    
    uint64_t framesToRead = 5000;
    int16_t buffer[framesToRead];
    drmp3_uint64 s = drmp3_read_pcm_frames_s16(&mp3, framesToRead, buffer);
    std::cout << " == after read == " <<std::endl;
    show(mp3);
    std::cout << s << std::endl;
    for (int i = 0; i < framesToRead; i++) {
        std::cout << buffer[i] << " ";
    }
    drmp3_uninit(&mp3);

    std::ifstream inputFileStream("test.wav", std::ios::binary);
    inputFileStream.ignore(44);
    int16_t fbuff[framesToRead];
    std::cout << " ===== ==========" << std::endl;
    if (inputFileStream.good()){
        std::cout << "read" << std::endl;
        inputFileStream.read((char*)fbuff, framesToRead*2);
    }
    std::cout << sizeof(fbuff) << std::endl;
    for (int i = 0; i < framesToRead; i++) {
        std::cout << fbuff[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}


