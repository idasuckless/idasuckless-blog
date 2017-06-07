Title: The BRK is a lie
Date: 2017-06-08 12:00
Category: Blog

### The bug

IDA thinks that BRK on ARM64 doesn't stop the execution flow.

### The consequences

Programs often use BRK to crash when something wrong happen (assert fail, security condition unmet etc.), to crash the program or let the analyst attach it's debugger. 
As IDA thinks that the execution continue after the BRK, this break all its analysis. This can be especially painful to fix especially if the BRK is just before an address table or in the middle of a function.

### The support answers (and why they are wrong)

> I'm not sure stopping the flow on BRK is a good idea. Debuggers may use it to add breakpoints which means functions would get truncated while debugging.

IDA knows where it put breakpoints and knows the original byte, it won't truncate anything.

> Using BRK as a way to stop execution is the same as using any other invalid opcode or instruction that generates an exception. There are tons of ways of doing that. One can easily imagine a progrem where BRK #7 breaks executino while BRK #5 doesn't, for example.

No it is not, BRK is a documented instruction, it is a software breakpoint and it is designed to generate a trap exception. There is no trick involved.

* http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.den0024a/BCGGEIFD.html
* https://patchwork.kernel.org/patch/6861231/

A *progrem* that would use BRK as a "normal" instruction would need to catch the generated exceptions, it is not a normal behaviour, this is obfuscation (nanomites...).

> Your best best is to write a processor extension plugin that would recognize BRK#0 and tell IDA not to create cross-references from it.

Translation: *fix our bugs yourself*.

### The *fix*

Well actually, we do what they told us to do and we coded a processor extension plugin... It's surprinsigly not too slow for a python code and works great. You can get the code here: [Make BRK break again](https://github.com/idasuckless/idasuckless-code/blob/master/plugins/make_brk_break_again.py "URL to the 'Make BRK break again' plugin code")

