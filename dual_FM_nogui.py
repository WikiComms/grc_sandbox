#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Dual Fm Nogui
# Generated: Sun May 17 20:06:33 2015
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import time

class dual_FM_nogui(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Dual Fm Nogui")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 10e6
        self.freq_2 = freq_2 = 102.5e6
        self.freq_1 = freq_1 = 95.7e6
        self.channel_width = channel_width = 200e3
        self.channel_offset2 = channel_offset2 = 96.5e6
        self.channel_offset1 = channel_offset1 = 96.5e6
        self.audio_gain2 = audio_gain2 = 1
        self.audio_gain1 = audio_gain1 = 1

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=12,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=12,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(freq_1, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(0, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((audio_gain2, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((audio_gain1, ))
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_wfm_rcv_1_0 = analog.wfm_rcv(
        	quad_rate=480e3,
        	audio_decimation=10,
        )
        self.analog_wfm_rcv_1 = analog.wfm_rcv(
        	quad_rate=480e3,
        	audio_decimation=10,
        )
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, channel_offset2 - freq_2, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, channel_offset1 - freq_1, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_1_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.analog_wfm_rcv_1_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_wfm_rcv_1, 0))
        self.connect((self.analog_wfm_rcv_1, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))



    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)

    def get_freq_2(self):
        return self.freq_2

    def set_freq_2(self, freq_2):
        self.freq_2 = freq_2
        self.analog_sig_source_x_0_0.set_frequency(self.channel_offset2 - self.freq_2)

    def get_freq_1(self):
        return self.freq_1

    def set_freq_1(self, freq_1):
        self.freq_1 = freq_1
        self.osmosdr_source_0.set_center_freq(self.freq_1, 0)
        self.analog_sig_source_x_0.set_frequency(self.channel_offset1 - self.freq_1)

    def get_channel_width(self):
        return self.channel_width

    def set_channel_width(self, channel_width):
        self.channel_width = channel_width

    def get_channel_offset2(self):
        return self.channel_offset2

    def set_channel_offset2(self, channel_offset2):
        self.channel_offset2 = channel_offset2
        self.analog_sig_source_x_0_0.set_frequency(self.channel_offset2 - self.freq_2)

    def get_channel_offset1(self):
        return self.channel_offset1

    def set_channel_offset1(self, channel_offset1):
        self.channel_offset1 = channel_offset1
        self.analog_sig_source_x_0.set_frequency(self.channel_offset1 - self.freq_1)

    def get_audio_gain2(self):
        return self.audio_gain2

    def set_audio_gain2(self, audio_gain2):
        self.audio_gain2 = audio_gain2
        self.blocks_multiply_const_vxx_0_0.set_k((self.audio_gain2, ))

    def get_audio_gain1(self):
        return self.audio_gain1

    def set_audio_gain1(self, audio_gain1):
        self.audio_gain1 = audio_gain1
        self.blocks_multiply_const_vxx_0.set_k((self.audio_gain1, ))

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = dual_FM_nogui()
    tb.start()
    raw_input('Press Enter to quit: ')
    tb.stop()
    tb.wait()
