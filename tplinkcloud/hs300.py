from .device_type import TPLinkDeviceType
from .emeter_device import TPLinkEMeterDevice
from .hs300_child import HS300Child
from .device_child_info import TPLinkDeviceChildInfo

class HS300SysInfo:

    def __init__(self, sys_info):
        self.sw_ver = sys_info.get('sw_ver')
        self.hw_ver = sys_info.get('hw_ver')
        self.model = sys_info.get('model')
        self.device_id = sys_info.get('deviceId')
        self.oem_id = sys_info.get('oemId')
        self.hw_id = sys_info.get('hwId')
        self.rssi = sys_info.get('rssi')
        self.longitude_i = sys_info.get('longitude_i')
        self.latitude_i = sys_info.get('latitude_i')
        self.alias = sys_info.get('alias')
        self.status = sys_info.get('status')
        self.mic_type = sys_info.get('mic_type')
        self.feature = sys_info.get('feature')
        self.mac = sys_info.get('mac')
        self.updating = sys_info.get('updating')
        self.led_off = sys_info.get('led_off')
        self.children = sys_info.get('children')
        self.child_num = sys_info.get('child_num')
        self.err_code = sys_info.get('err_code')

class HS300(TPLinkEMeterDevice):

    def __init__(self, client, device_id, device_info):
        super().__init__(client, device_id, device_info)
        self.model_type = TPLinkDeviceType.HS300
    
    def get_children(self):
        sys_info = HS300SysInfo(self.get_sys_info())
        children = []
        for child_info in sys_info.children:
            device_child_info = TPLinkDeviceChildInfo(child_info)
            device_child = HS300Child(self.client, self.device_id, device_child_info.id, device_child_info)
            children.append(device_child)
        return children

    # An override of an identified TPLinkDevice
    def has_children(self):
        return True
