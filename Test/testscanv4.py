#!/usr/bin/env python
# -*-coding:Utf-8 -*

def scan_for_devices(timeout):
    """Scan for bluetooth low energy devices.

    Note this must be run as root!"""
    from bluepy.btle import Scanner

    scanner = Scanner()
    result = []
    device = "d7:ef:13:27:15:29"
    for device in scanner.scan(timeout):
        result.append((device.addr, device.getValueText(9)))
    return result