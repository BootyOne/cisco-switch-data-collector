import os

from netmiko import ConnectHandler


def collect_switch_data_netmiko() -> dict:
    switch = {
        'device_type': 'cisco_ios_telnet',
        'ip': os.environ.get('IP'),
        'port': os.environ.get('PORT')
    }

    try:
        with ConnectHandler(**switch) as net_connect:
            version = net_connect.send_command('show version')
            startup_config = net_connect.send_command('show startup-config')
            running_config = net_connect.send_command('show running-config')
            acl_info = net_connect.send_command('show access-lists')
            interface_info = net_connect.send_command('show interfaces')
    except Exception as e:
        print(f"Произошла ошибка при подключении или выполнении команды: {e}")
        exit(99)

    return {
        'version': version,
        'startup_config': startup_config,
        'running_config': running_config,
        'acl_info': acl_info,
        'interface_info': interface_info,
    }


if __name__ == "__main__":
    data = collect_switch_data_netmiko()
    for key in data:
        print(f"{key}:\n{'=' * len(key)}{data[key]}\n{'=' * len(key)}\n")
