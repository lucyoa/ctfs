segment .text
    global asm1
asm1:
	push   ebp
	mov    ebp,esp
	cmp    DWORD [ebp+0x8],0x421
	jg     asm1+37
	cmp    DWORD [ebp+0x8],0x1b4
	jne    asm1+29
	mov    eax,DWORD [ebp+0x8]
	add    eax,0x13
	jmp    asm1+60
	mov    eax,DWORD [ebp+0x8]
	sub    eax,0x13
	jmp    asm1+60
	cmp    DWORD [ebp+0x8],0x7f7
	jne    asm1+54
	mov    eax,DWORD [ebp+0x8]
	sub    eax,0x13
	jmp    asm1+60
	mov    eax,DWORD [ebp+0x8]
	add    eax,0x13
	pop    ebp
	ret    

