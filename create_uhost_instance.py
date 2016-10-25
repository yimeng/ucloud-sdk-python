#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sdk import UcloudApiClient
from config import *
import sys
import json

#实例化 API 句柄


if __name__=='__main__':
    arg_length = len(sys.argv)
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters={
            "Action":"CreateUHostInstance",
            "Zone":zone,
            "Region":region,
            "Name":name,
            "ImageId":"uimage-qegj3w",
            "LoginMode":"Password",
            "Password":password,
            "Tag":tag,
            "ChargeType":"Dynamic",
            "CPU":"1",
            "Memory":"2048",
            "StorageType":"LocalDisk",
            "DiskSpace":"0",
            "UHostType":"Normal",
            "SecurityGroupId":SecurityGroupId
            }
    response = ApiClient.get("/", Parameters);
    print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
