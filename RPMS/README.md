Build using this command:

```
rpmbuild --define "_topdir $PWD" -bb SPECS/snd-hda-realtek-patch.spec
```

Install the .rpm in bluefin fedora based on using this:

```
sudo rpm-ostree install --force-replacefiles ./{name_of_the_rpm_file}.rpm
```
