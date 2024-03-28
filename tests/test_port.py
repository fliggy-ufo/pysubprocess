import unittest
from typing import List, Dict
from pysubprocess.port import Port, LSOFProcInfo, format_lsof_proc_info_list

class TestPort(unittest.TestCase):

    def setUp(self):
        self.port = Port()

    def tearDown(self):
        ...

    # def test_find_free_port(self):
    #     assert isinstance(self.port.find_free_port(), int)

    # def test_get_ps_list_by_port(self):
    #     self.port.find_porc_info_list_by_port('5037')

    def test_format_proc_info_list(self):
        test_stdouts = '''
        COMMAND     PID         USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
        ControlCe   728 youngfreefjs    8u  IPv4 0xa83ef9a3be19442f      0t0  TCP *:commplex-main (LISTEN)
        ControlCe   728 youngfreefjs    9u  IPv6 0xa83ef99ef0ee5597      0t0  TCP *:commplex-main (LISTEN)
        python3.1 50079 youngfreefjs    3u  IPv4 0xa83ef9a3bf9c042f      0t0  TCP localhost:commplex-main (LISTEN)
        python3.1 50079 youngfreefjs    5u  IPv4 0xa83ef9a3bf9c042f      0t0  TCP localhost:commplex-main (LISTEN)
        python3.1 50101 youngfreefjs    3u  IPv4 0xa83ef9a3bf9c042f      0t0  TCP localhost:commplex-main (LISTEN)
        python3.1 50101 youngfreefjs    5u  IPv4 0xa83ef9a3bf9c042f      0t0  TCP localhost:commplex-main (LISTEN)
        '''
        formatted: List[LSOFProcInfo] = format_lsof_proc_info_list(test_stdouts)
        assert len(formatted) == 6
        assert isinstance(formatted[0], LSOFProcInfo)


    def test_format_proc_info_list_json(self):
        test_stdouts = '''
        COMMAND     PID         USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
        ControlCe   728 youngfreefjs    8u  IPv4 0xa83ef9a3be19442f      0t0  TCP *:commplex-main (LISTEN)
        ControlCe   728 youngfreefjs    9u  IPv6 0xa83ef99ef0ee5597      0t0  TCP *:commplex-main (LISTEN)
        python3.1 50079 youngfreefjs    3u  IPv4 0xa83ef9a3bf9c042f      0t0  TCP localhost:commplex-main (LISTEN)
        python3.1 50079 youngfreefjs    5u  IPv4 0xa83ef9a3bf9c042f      0t0  TCP localhost:commplex-main (LISTEN)
        python3.1 50101 youngfreefjs    3u  IPv4 0xa83ef9a3bf9c042f      0t0  TCP localhost:commplex-main (LISTEN)
        python3.1 50101 youngfreefjs    5u  IPv4 0xa83ef9a3bf9c042f      0t0  TCP localhost:commplex-main (LISTEN)
        '''
        formatted: List[Dict] = format_lsof_proc_info_list(test_stdouts, format_json=True)
        assert len(formatted) == 6
        assert isinstance(formatted[0], Dict)

