Steps to compile:

1. wget https://kojipkgs.fedoraproject.org/packages/kernel/6.14.9/200.fc41/src/kernel-6.14.9-200.fc41.src.rpm
2. rpm2cpio kernel-6.14.9-200.fc41.src.rpm | cpio -idmv
3. tar -xf linux-6.14.9.tar.xz
4. cd linux-6.14.9
5. make defconfig
6. make modules_prepare
7. cd sound/pci/hda
8. copy over the patched code here and replace the existing one
9. make -C /usr/src/linux-6.14.9/ -j$(nproc) modules
10. copy the resulting .ko files to this directory
11. follow the instructions in the README.md file within [RPMS](./RPMS)
