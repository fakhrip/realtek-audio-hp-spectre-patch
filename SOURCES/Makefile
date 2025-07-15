# List your object files here
obj-m += snd-hda-codec-realtek.o

# If snd-hda-codec-realtek.o depends on patch_realtek.c
snd-hda-codec-realtek-objs := patch_realtek.o

all:
	make -C /lib/modules/$(KERNELRELEASE)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(KERNELRELEASE)/build M=$(PWD) clean

