Steps to compile:

1. sudo make -C /usr/src/kernels/$(uname -r) -j$(nproc) M=$PWD modules
2. sudo /usr/src/kernels/$(uname -r)/scripts/sign-file sha256 mok.key mok.der ./snd-hda-codec-realtek.ko
3. xz -e -z -f -9 --check=crc32 ./snd-hda-codec-realtek.ko
4. follow the instructions in the README.md file within [RPMS](./RPMS)
