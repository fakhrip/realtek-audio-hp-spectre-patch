Name:           snd-hda-realtek-patch
Version:        9.0
Release:        9%{?dist}
Summary:        Patched snd-hda-codec-realtek module
License:        GPLv2
BuildArch:      noarch

%description
Patched Realtek driver with GPIO fixup for HP Spectre.

%install
KVER=$(uname -r)
mkdir -p %{buildroot}/usr/lib/modules/$KVER/kernel/sound/pci/hda
install -m 644 %{_sourcedir}/snd-hda-codec-realtek.ko %{buildroot}/usr/lib/modules/$KVER/kernel/sound/pci/hda/
install -m 644 %{_sourcedir}/snd-hda-codec-realtek.ko.xz %{buildroot}/usr/lib/modules/$KVER/kernel/sound/pci/hda/

%files
/usr/lib/modules/*/kernel/sound/pci/hda/snd-hda-codec-realtek.ko
/usr/lib/modules/*/kernel/sound/pci/hda/snd-hda-codec-realtek.ko.xz
