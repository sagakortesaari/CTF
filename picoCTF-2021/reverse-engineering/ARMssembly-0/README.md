# ARMssembly 0

What integer does this program print with arguments 266134863 and 1592237099? File: `chall.S` Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

## Solution

Haven't seen ARM assembly before (only x86) so this one required me to look into how it works in order to break down the functions in `chall.S`. [This site was pretty good in order to do so](https://developer.arm.com/documentation/den0024/a/The-A64-instruction-set/Instruction-mnemonics). Looking into the different functions reveals the below:

**Main:**
```
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	x19, [sp, 16]
	str	w0, [x29, 44]
	str	x1, [x29, 32]
	ldr	x0, [x29, 32] # arg 0 end
	add	x0, x0, 8 # adds 8 bytes to the value of x0, we're now at arg 1
	ldr	x0, [x0] # x0 = "266134863"
	bl	atoi # converts the above string to an int
	mov	w19, w0 # w19 = 266134863
	ldr	x0, [x29, 32] # arg 1 end
	add	x0, x0, 16 # adds 16 bytes to the value of x0, we're now at arg 2
	ldr	x0, [x0] # x0 = "1592237099"
	bl	atoi # converts the above string to an int
	mov	w1, w0 # w1 = 1592237099
	mov	w0, w19 # w0 = 266134863
	bl	func1
	mov	w1, w0
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	printf
	mov	w0, 0
	ldr	x19, [sp, 16]
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
```

I've tried commenting my thought process in the main function above. This was quite tricky initially to figure out what's actually going on, but I believe the trick is to look at the `atoi` calls and from there figure out that we are converting ascii characters to ints in memory. After that it's straightforward to realize that we are working with the args to the program.

 
**func1:**
```
	sub	sp, sp, #16
	str	w0, [sp, 12] # Store the value of register w0 on addr sp + 12
	str	w1, [sp, 8] # Store the value of register w1 on addr sp + 8 (a w register is 4 bytes, hence why we have decreased with 4)
	ldr	w1, [sp, 12] # Load the value of addr sp + 12 into w1
	ldr	w0, [sp, 8] # Load the value of addr sp + 8 into w0 (w0 and w1 will essentially have switched places now)
	cmp	w1, w0 # Compare w1 and w0 (performs w1 - w0)
	bls	.L2 # Jumps to .L2 if the cmp instruction resulted in a value of 0 or below 0
	ldr	w0, [sp, 12]
	b	.L3
```

From the looks of main above, going into func1, we will have `w0 = 266134863` and `w1 = 1592237099`. We see that the registers will essentially switch values, so `w0 = 1592237099` and `w1 = 266134863`. The compare instruction will result in a negative value, hence we will jump to `.L2`.

**.L2:**
```
ldr	w0, [sp, 8]
```

Loads the value from sp+8 into w0. Looking above from `func1`, we see that the original `w1` was stored in [sp+8]. This means that w0 will now contain `1592237099`. We will then continue down to `.L3`.

**.L3:**
```
	add	sp, sp, 16
	ret
	.size	func1, .-func1
	.section	.rodata
	.align	3
```

We first add 16 to our stack pointer, which *I think* means that we are basically deleting the stack frame containing the return address etc to func 1? So basically with the `ret` instruction here, we will jump back to `.main`, and not `.L1`. We will then move the value from w0 to w1, and w1 is then printed via the `printf` function. (Hopefully this is the right explanation, otherwise I haven't figured it out).. 

Converting `1592237099` to hex gives us 5EE79C2B, and thus the flag is `picoCTF{5EE79C2B}` 💕

## Remarks

This turned out to be quite challenging for me, I am not used to reading ARM assembly (never done it before), but it taught me a lot by doing so. I got frustrated when I didn't understand what was happening in the `.L3` function above (the `add sp, sp, 16`) and therefore it took me a bit long to figure this out. Oh well - I want to learn more about reverse engineering so I guess this is a good start!