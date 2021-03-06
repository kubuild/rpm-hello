# https://rpm-packaging-guide.github.io/#hello-world
Name:       hello-world
Version:    1
Release:    1
Summary:    Most simple RPM package, for example purposes
License:    MIT

%description
This is my first RPM package, which does nothing.

%prep
# we have no source, so nothing here

%build
cat > hello-world.sh <<EOF
#!/usr/bin/bash
echo Hello world
EOF

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 hello-world.sh %{buildroot}/usr/bin/hello-world.sh

%files
/usr/bin/hello-world.sh

%changelog
* Mon May 31 2021 Leonardo Rossetti <me@lrossetti.com>