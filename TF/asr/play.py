#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: play.py
@time: 2021/10/4 4:18 下午
@desc:
"""
import tempfile
import wave
import soundfile

import pyaudio
import os
import tensorflow as tf
import numpy as np
import keyboard

CHUNK = 16000
FORMAT = pyaudio.paInt16
SAMPWIDTH = pyaudio.get_sample_size(FORMAT)


# format = pyaudio.get_format_from_width(SAMPWIDTH)


def transfer(frames):
    with tempfile.TemporaryFile() as f:
        wf = wave.open(f, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(pyaudio.get_sample_size(FORMAT))
        wf.setframerate(16000)
        wf.writeframes(frames)
        wf.close()
        f.seek(0)
        wav_frames, sr = soundfile.read(f, dtype='float32')
        return wav_frames


class Model:
    _stream_flag = 0
    _one_line_flag = 0
    _one_line_cache = b''

    def __init__(self):
        self._interpreter = self._init_model()
        self._input_details = self._interpreter.get_input_details()
        self._output_details = self._interpreter.get_output_details()

    def load_stream(self, stream):
        self.stream = stream

    def _init_model(self):
        TFLite_model = "/Users/coffee/Documents/code/ASR_TFLite/pre_trained_models/English"
        m1 = "subword-conformer.latest_for_english.tflite"
        m2 = "subsampling-conformer.latest-for-english.tflite"
        interpreter = tf.lite.Interpreter(model_path=os.path.join(TFLite_model, m1))
        print("allocate_tensors")
        return interpreter

    def handle(self, in_data, frame_count, time_info, status):
        if self._stream_flag:
            data = transfer(in_data)
            print(data)
            assert frame_count == len(data)
            self.transcribe(data)
        else:
            self._one_line_cache += in_data
        return (None, pyaudio.paContinue)

    def transcribe(self, frames):
        self._interpreter.set_tensor(self._input_details[0]['index'], frames)
        self._interpreter.set_tensor(self._input_details[1]['index'], self.state1)
        self._interpreter.set_tensor(self._input_details[2]['index'], self.state2)
        self._interpreter.invoke()
        hyp = self._interpreter.get_tensor(self._output_details[0]['index'])
        print("".join([chr(u) for u in hyp]))
        self.state1 = self._interpreter.get_tensor(self._output_details[1]['index'])
        self.state2 = self._interpreter.get_tensor(self._output_details[2]['index'])

    def stream_transcribe(self):
        self._stream_flag ^= 1
        if self._stream_flag:
            self._start_stream_transcribe()
        else:
            self._stop_stream_transcirbe()

    def _start_stream_transcribe(self):
        print("start stream_transcribe...")
        self._interpreter.resize_tensor_input(self._input_details[0]["index"], (CHUNK,))
        self._interpreter.allocate_tensors()
        self.state1 = np.array(0).astype('int32')
        self.state2 = np.zeros([1, 2, 1, 320]).astype('float32')
        self.stream.start_stream()

    def _stop_stream_transcirbe(self):
        print("stop stream_transcribe...")
        self.stream.stop_stream()

    def one_line_transcribe(self):
        self._one_line_flag ^= 1
        if self._one_line_flag:
            self._start_one_line_transcirbe()
        else:
            self._stop_one_line_transcirbe()

    def _start_one_line_transcirbe(self):
        print("start one_line_transcribe...")
        self.state1 = np.array(0).astype('int32')
        self.state2 = np.zeros([1, 2, 1, 320]).astype('float32')
        self._one_line_cache = b''
        self.stream.start_stream()

    def _stop_one_line_transcirbe(self):
        print("stop one_line_transcribe...")
        self.stream.stop_stream()
        frames = transfer(self._one_line_cache)
        self._interpreter.resize_tensor_input(self._input_details[0]["index"], frames.shape)
        self._interpreter.allocate_tensors()
        self.transcribe(frames)


def main():
    # prepare audio recorder
    print("model start")
    m = Model()

    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT,
        channels=1,
        rate=16000,
        input=True,
        start=False,
        frames_per_buffer=CHUNK,
        stream_callback=m.handle)
    m.load_stream(stream)

    print("Press:")
    keyboard.add_hotkey('left', m.stream_transcribe)
    keyboard.add_hotkey('right', m.one_line_transcribe)
    keyboard.wait('esc')
    stream.close()
    p.terminate()


if __name__ == "__main__":
    main()
