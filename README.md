This is created because audio is not working when the device goes to suspend mode which is exactly like the issue mentioned in this post https://forums.fedoraforum.org/showthread.php?334031-Speaker-no-audio-on-HP-Laptop-Spectre&p=1890200

The fix is basically to put the `HP Spectre x360 Convertible 14-ea1xxx` sound driver subsystem_id which happen to be 0x103c89db within the `patch_realtek.c`

Note: changes within the `hda_auto_parser.c` are only for debugging purposes
