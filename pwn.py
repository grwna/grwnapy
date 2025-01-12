from pwn import *

def find_offset(exe: elf, sendafter: str, cycle: int) -> int:
    """
    Find the offset in EIP using cyclic by launching proccess

    Args:
        exe (elf): Binary to be exploited
        sendafter (str): Bytes for which to send line after
        cycle (int): Cyclic amoun

    Returns: The offset
    """
    sendafter = sendafter.encode()
    payload = cyclic(cycle)
    # Launch process and send payload
    p = process(exe)
    p.sendlineafter(sendafter, payload)
    # Wait for the process to crash
    p.wait()

    # Print out the address of EIP/RIP at the time of crashing
    arch = context.arch
    if (arch == "i386"):
        ip_offset = cyclic_find(p.corefile.pc)  # x86
    elif (arch == "amd64"):
        ip_offset = cyclic_find(p.corefile.read(p.corefile.sp, 4))  # x64
    else:
        raise ValueError("Architecture invalid")
        return 0
    info('located EIP/RIP offset at {a}'.format(a=ip_offset))
    return ip_offset
