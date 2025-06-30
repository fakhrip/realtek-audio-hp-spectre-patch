Name:           snd-hda-realtek-patch
Version:        8.0
Release:        8%{?dist}
Summary:        Patched snd-hda-codec-realtek module
License:        GPLv2
BuildArch:      noarch

%description
Patched Realtek driver with GPIO fixup for HP Spectre.

%install
mkdir -p %{buildroot}/usr/lib/modules/6.14.9-200.fc41.x86_64/kernel/sound/pci/hda
install -m 644 %{_sourcedir}/snd-hda-codec-realtek.ko %{buildroot}/usr/lib/modules/6.14.9-200.fc41.x86_64/kernel/sound/pci/hda/
install -m 644 %{_sourcedir}/snd-hda-codec-realtek.ko.xz %{buildroot}/usr/lib/modules/6.14.9-200.fc41.x86_64/kernel/sound/pci/hda/
install -m 644 %{_sourcedir}/snd-hda-codec.ko %{buildroot}/usr/lib/modules/6.14.9-200.fc41.x86_64/kernel/sound/pci/hda/
install -m 644 %{_sourcedir}/snd-hda-codec.ko.xz %{buildroot}/usr/lib/modules/6.14.9-200.fc41.x86_64/kernel/sound/pci/hda/


%files
/usr/lib/modules/*/kernel/sound/pci/hda/snd-hda-codec-realtek.ko
/usr/lib/modules/*/kernel/sound/pci/hda/snd-hda-codec-realtek.ko.xz
/usr/lib/modules/*/kernel/sound/pci/hda/snd-hda-codec.ko
/usr/lib/modules/*/kernel/sound/pci/hda/snd-hda-codec.ko.xz

