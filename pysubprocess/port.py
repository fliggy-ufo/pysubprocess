'''Port of subprocess module.'''
import socket
from typing import List
from contextlib import closing
from pysubprocess.base import PysubprocessError, Base, PopenExtra, shell

class LSOFProcInfo(object):

    def __init__(self, command, pid, user, fd, type, device, sizeoff, node, name):
        self.command = command
        self.pid = pid
        self.user = user
        self.fd = fd
        self.type = type
        self.device = device
        self.sizeoff = sizeoff
        self.node = node
        self.name = name


def format_lsof_proc_info_list(stdout_data: str, format_json: bool = False) -> List:
    lines: List[str] = stdout_data.strip().split('\n')[1:]
    formatted_proc_info_list: List[LSOFProcInfo] = []
    for line in lines:
        formatted_proc_info_list.append(LSOFProcInfo(*line.split()[:-2], ' '.join(line.split()[-2:])).__dict__ if \
                                        format_json else LSOFProcInfo(*line.split()[:-2], ' '.join(line.split()[-2:])))
    return formatted_proc_info_list


class Port(Base):

    def find_free_port(self) -> int:
        '''Find not used port in tcp port range.'''
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as server:
            server.bind(('', 0))
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            return server.getsockname()[1]

    def find_porc_info_list_by_port(self, port: str, format_json: bool = False) -> list:
        '''Find process info list by port.
        Args:
            format_json: bool, return dict or custom object.
        Exception:
            raise PysubprocessError
        '''
        proc: PopenExtra = shell(f'lsof -i:{port}')
        if not proc.success and proc.stderr_data:
            raise PysubprocessError(proc.stderr_data)
        if not proc.success and not proc.stderr_data:
            return []
        return format_lsof_proc_info_list(stdout_data=proc.stdout_data, format_json=format_json)
