%define nft_rpmversion 1.0.4
%define nft_specrelease 3
%define libnftnl_ver 1.2.2-1

Name:           nftables
Version:        %{nft_rpmversion}
Release:        %{nft_specrelease}%{?dist}%{?buildid}
# Upstream released a 0.100 version, then 0.4. Need Epoch to get back on track.
Epoch:          1
Summary:        Netfilter Tables userspace utillites

License:        GPLv2
URL:            https://netfilter.org/projects/nftables/
Source0:        %{url}/files/%{name}-%{version}.tar.bz2
Source1:        nftables.service
Source2:        nftables.conf
Source3:        main.nft
Source4:        router.nft
Source5:        nat.nft
Source6:        nft-test.stderr.expect
Source7:        run-tests.stderr.expect
Source8:        monitor-run-tests.stderr.expect

Patch1:             0001-tests-shell-runtime-set-element-automerge.patch
Patch2:             0002-rule-collapse-set-element-commands.patch
Patch3:             0003-intervals-do-not-report-exact-overlaps-for-new-eleme.patch
Patch4:             0004-intervals-do-not-empty-cache-for-maps.patch
Patch5:             0005-intervals-Do-not-sort-cached-set-elements-over-and-o.patch
Patch6:             0006-doc-Document-limitations-of-ipsec-expression-with-xf.patch
Patch7:             0007-tests-py-Add-a-test-for-failing-ipsec-after-counter.patch
Patch8:             0008-parser-add-missing-synproxy-scope-closure.patch
Patch9:             0009-scanner-don-t-pop-active-flex-scanner-scope.patch
Patch10:            0010-intervals-fix-crash-when-trying-to-remove-element-in.patch
Patch11:            0011-intervals-check-for-EXPR_F_REMOVE-in-case-of-element.patch
Patch12:            0012-netlink_delinearize-allow-postprocessing-on-concaten.patch
Patch13:            0013-netlink_delinearize-postprocess-binary-ands-in-conca.patch
Patch14:            0014-proto-track-full-stack-of-seen-l2-protocols-not-just.patch
Patch15:            0015-debug-dump-the-l2-protocol-stack.patch
Patch16:            0016-tests-add-a-test-case-for-ether-and-vlan-listing.patch
Patch17:            0017-netlink_delinearize-also-postprocess-OP_AND-in-set-e.patch
Patch18:            0018-evaluate-search-stacked-header-list-for-matching-pay.patch
Patch19:            0019-src-allow-anon-set-concatenation-with-ether-and-vlan.patch
Patch20:            0020-evaluate-set-eval-ctx-for-add-update-statements-with.patch
Patch21:            0021-monitor-Sanitize-startup-race-condition.patch
Patch22:            0022-netlink_delinearize-fix-decoding-of-concat-data-elem.patch
Patch23:            0023-netlink_linearize-fix-timeout-with-map-updates.patch
Patch24:            0024-tests-add-a-test-case-for-map-update-from-packet-pat.patch
Patch25:            0025-owner-Fix-potential-array-out-of-bounds-access.patch
Patch26:            0026-mnl-dump_nf_hooks-leaks-memory-in-error-path.patch
Patch27:            0027-meta-parse_iso_date-returns-boolean.patch
Patch28:            0028-netlink-Fix-for-potential-NULL-pointer-deref.patch
Patch29:            0029-optimize-Do-not-return-garbage-from-stack.patch
Patch30:            0030-optimize-Clarify-chain_optimize-array-allocations.patch
Patch31:            0031-netlink_delinearize-Sanitize-concat-data-element-dec.patch
Patch32:            0032-tests-monitor-Summarize-failures-per-test-case.patch
Patch33:            0033-rule-check-address-family-in-set-collapse.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: make
BuildRequires: gcc
BuildRequires: flex
BuildRequires: bison
BuildRequires: pkgconfig(libmnl) >= 1.0.4
BuildRequires: gmp-devel
BuildRequires: readline-devel
BuildRequires: pkgconfig(libnftnl) >= %{libnftnl_ver}
BuildRequires: systemd
BuildRequires: asciidoc
BuildRequires: pkgconfig(xtables) >= 1.6.1
BuildRequires: jansson-devel
BuildRequires: python3-devel

Requires: libnftnl >= %{libnftnl_ver}

%description
Netfilter Tables userspace utilities.

%package        devel
Summary:        Development library for nftables / libnftables
Group:          Development/Libraries
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig

%description devel
Development tools and static libraries and header files for the libnftables library.

%package -n     python3-nftables
Summary:        Python module providing an interface to libnftables
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n python3-nftables
The nftables python module provides an interface to libnftables via ctypes.

%prep
%autosetup -p1
cp -a %{SOURCE6} ./tests/py/
cp -a %{SOURCE7} ./tests/shell/
cp -a %{SOURCE8} ./tests/monitor/run-tests.stderr.expect

%build
autoreconf -fi
rm -Rf autom4te*.cache config.h.in~
%configure --disable-silent-rules --with-json --with-xtables \
	--enable-python --with-python-bin=%{__python3} --with-cli=readline
make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Don't ship static lib (for now at least)
rm -f $RPM_BUILD_ROOT/%{_libdir}/libnftables.a

chmod 644 $RPM_BUILD_ROOT/%{_mandir}/man8/nft*

mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
cp -a %{SOURCE1} $RPM_BUILD_ROOT/%{_unitdir}/

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig
cp -a %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/

rm $RPM_BUILD_ROOT/%{_datadir}/nftables/*.nft
cp %{SOURCE3} %{SOURCE4} %{SOURCE5} \
	$RPM_BUILD_ROOT/%{_sysconfdir}/nftables/

find $RPM_BUILD_ROOT/%{_sysconfdir} \
	\( -type d -exec chmod 0700 {} \; \) , \
	\( -type f -exec chmod 0600 {} \; \)

# make nftables.py use the real library file name
# to avoid nftables-devel package dependency
sofile=$(readlink $RPM_BUILD_ROOT/%{_libdir}/libnftables.so)
sed -i -e 's/\(sofile=\)".*"/\1"'$sofile'"/' \
	$RPM_BUILD_ROOT/%{python3_sitelib}/nftables/nftables.py
touch -r %{SOURCE2} $RPM_BUILD_ROOT/%{python3_sitelib}/nftables/nftables.py

%post
%systemd_post nftables.service

%preun
%systemd_preun nftables.service

%postun
%systemd_postun_with_restart nftables.service

%post devel
%ldconfig_post

%postun devel
%ldconfig_postun

%files
%license COPYING
%config(noreplace) %{_sysconfdir}/nftables/
%config(noreplace) %{_sysconfdir}/sysconfig/nftables.conf
%{_sbindir}/nft
%{_libdir}/libnftables.so.*
%{_mandir}/man5/libnftables-json.5*
%{_mandir}/man8/nft*
%{_unitdir}/nftables.service
%{_docdir}/nftables/examples/*.nft

%files devel
%{_libdir}/libnftables.so
%{_libdir}/pkgconfig/libnftables.pc
%{_includedir}/nftables/libnftables.h
%{_mandir}/man3/libnftables.3*

%files -n python3-nftables
%{python3_sitelib}/nftables-*.egg-info
%{python3_sitelib}/nftables/

%changelog
* Thu Sep 21 2023 Phil Sutter <psutter@redhat.com> [1.0.4-3.el8]
- spec: Rename variables to avoid a clash (Phil Sutter) [INTERNAL]
- rule: check address family in set collapse (Phil Sutter) [RHEL-5160]

* Thu Jul 20 2023 Phil Sutter <psutter@redhat.com> [1.0.4-2.el8]
- Add expected error records for testsuite runs (Phil Sutter) [2211076]
- tests: monitor: Summarize failures per test case (Phil Sutter) [2211076]

* Tue May 30 2023 Phil Sutter <psutter@redhat.com> [1.0.4-1.el8]
- Synchronize patch level with nftables-1.0.4-10.el9 (Phil Sutter) [2211076]
- Rebase onto version 1.0.4 (Phil Sutter) [2211076]

* Thu Apr 28 2022 Phil Sutter <psutter@redhat.com> [0.9.3-26.el8]
- libnftables: call nft_cmd_expand() only with CMD_ADD (Phil Sutter) [2073287]
- src: add CMD_OBJ_SETELEMS (Phil Sutter) [2073287]
- src: rename CMD_OBJ_SETELEM to CMD_OBJ_ELEMENTS (Phil Sutter) [2073287]
- rule: fix element cache update in __do_add_setelems() (Phil Sutter) [2073287]
- rule: memleak in __do_add_setelems() (Phil Sutter) [2073287]
- tests: shell: auto-removal of chain hook on netns removal (Phil Sutter) [2070924]
- mnl: do not use expr->identifier to fetch device name (Phil Sutter) [2070924]

* Fri Feb 04 2022 Phil Sutter <psutter@redhat.com> [0.9.3-25.el8]
- mnl: do not build nftnl_set element list (Phil Sutter) [2047821]
- tests: py: add dnat to port without defining destination address (Phil Sutter) [2030773]
- evaluate: fix inet nat with no layer 3 info (Phil Sutter) [2030773]
- evaluate: attempt to set_eval flag if dynamic updates requested (Phil Sutter) [2039594]
- src: support for restoring element counters (Phil Sutter) [2039594]
- netlink: remove unused parameter from netlink_gen_stmt_stateful() (Phil Sutter) [2039594]

* Wed Dec 08 2021 Phil Sutter <psutter@redhat.com> [0.9.3-24.el8]
- tests: shell: better parameters for the interval stack overflow test (Phil Sutter) [1908127]
- tests: shell: $NFT needs to be invoked unquoted (Phil Sutter) [1908127]

* Fri Nov 05 2021 Phil Sutter <psutter@redhat.com> [0.9.3-23.el8]
- tests: cover baecd1cf2685 ("segtree: Fix segfault when restoring a huge interval set") (Phil Sutter) [1908127]
- segtree: Fix segfault when restoring a huge interval set (Phil Sutter) [1908127]

* Wed Oct 06 2021 Phil Sutter <psutter@redhat.com> [0.9.3-22.el8]
- json: Drop pointless assignment in exthdr_expr_json() (Phil Sutter) [1999059]
- parser_json: Fix for memleak in tcp option error path (Phil Sutter) [1999059]
- parser_bison: Fix for implicit declaration of isalnum (Phil Sutter) [1999059]
- parser_json: Fix error reporting for invalid syntax (Phil Sutter) [1994141]

* Mon Aug 02 2021 Phil Sutter <psutter@redhat.com> [0.9.3-21.el8]
- tests: shell: Fix bogus testsuite failure with 100Hz (Phil Sutter) [1919203]
- doc: nft.8: Extend monitor description by trace (Phil Sutter) [1820365]
- include: missing sctp_chunk.h in Makefile.am (Phil Sutter) [1979334]
- exthdr: Implement SCTP Chunk matching (Phil Sutter) [1979334]
- scanner: sctp: Move to own scope (Phil Sutter) [1979334]
- scanner: introduce start condition stack (Phil Sutter) [1979334]
- json: Simplify non-tcpopt exthdr printing a bit (Phil Sutter) [1979334]
- json: tcp: add raw tcp option match support (Phil Sutter) [1979334]
- tcp: add raw tcp option match support (Phil Sutter) [1979334]
- tcpopt: allow to check for presence of any tcp option (Phil Sutter) [1979334]
- tcpopt: split tcpopt_hdr_fields into per-option enum (Phil Sutter) [1979334]
- tcpopt: rename noop to nop (Phil Sutter) [1979334]
- tcpopts: clean up parser -> tcpopt.c plumbing (Phil Sutter) [1979334]
- parser: merge sack-perm/sack-permitted and maxseg/mss (Phil Sutter) [1979334]
- tests/py: Move tcpopt.t to any/ directory (Phil Sutter) [1979334]

* Thu May 20 2021 Phil Sutter <psutter@redhat.com> [0.9.3-20.el8]
- src: Optimize prefix matches on byte-boundaries (Phil Sutter) [1934926]
- src: Support odd-sized payload matches (Phil Sutter) [1934926]
- spec: Add an rpminspect.yaml file to steer rpminspect (Phil Sutter) [1962184]
- spec: Explicitly state dist string in Release tag (Phil Sutter) [1962184]

* Wed May 19 2021 Phil Sutter <psutter@redhat.com> [0.9.3-19.el8]
- evaluate: Reject quoted strings containing only wildcard (Phil Sutter) [1818117]
- tests: monitor: use correct $nft value in EXIT trap (Phil Sutter) [1919203]
- monitor: Fix for use after free when printing map elements (Phil Sutter) [1919203]
- tests: Disable tests known to fail on RHEL8 (Phil Sutter) [1919203]

* Sat Feb 20 2021 Phil Sutter <psutter@redhat.com> [0.9.3-18.el8]
- json: init parser state for every new buffer/file (Phil Sutter) [1930873]

* Tue Jan 12 2021 Phil Sutter <psutter@redhat.com> [0.9.3-17.el8]
- json: don't leave dangling pointers on hlist (Phil Sutter) [1900565]
- json: Fix seqnum_to_json() functionality (Phil Sutter) [1900565]
- json: echo: Speedup seqnum_to_json() (Phil Sutter) [1900565]
- proto: Fix ARP header field ordering (Phil Sutter) [1896334]
- proto: add sctp crc32 checksum fixup (Phil Sutter) [1895804]
- mergesort: unbreak listing with binops (Phil Sutter) [1891790]
- evaluate: missing datatype definition in implicit_set_declaration() (Phil Sutter) [1877022]
- evaluate: Perform set evaluation on implicitly declared (anonymous) sets (Phil Sutter) [1877022]
- src: store expr, not dtype to track data in sets (Phil Sutter) [1877022]

* Sat Aug 08 2020 Phil Sutter <psutter@redhat.com> [0.9.3-16.el8]
- src: Set NFT_SET_CONCAT flag for sets with concatenated ranges (Phil Sutter) [1820684]
- include: Resync nf_tables.h cache copy (Phil Sutter) [1820684]

* Tue Jun 30 2020 Phil Sutter <psutter@redhat.com> [0.9.3-15.el8]
- segtree: Fix get element command with prefixes (Phil Sutter) [1832235]
- tests: 0034get_element_0: do not discard stderr (Phil Sutter) [1832235]
- segtree: Merge get_set_interval_find() and get_set_interval_end() (Phil Sutter) [1832235]
- segtree: Use expr_clone in get_set_interval_*() (Phil Sutter) [1832235]
- segtree: Fix missing expires value in prefixes (Phil Sutter) [1832235]

* Wed Jun 24 2020 Phil Sutter <psutter@redhat.com> [0.9.3-14.el8]
- JSON: Improve performance of json_events_cb() (Phil Sutter) [1835300]
- doc: Document notrack statement (Phil Sutter) [1841292]

* Wed May 27 2020 Phil Sutter <psutter@redhat.com> [0.9.3-13.el8]
- parser_json: Support ranges in concat expressions (Phil Sutter) [1805798]

* Thu Mar 26 2020 Phil Sutter <psutter@redhat.com> [0.9.3-12.el8]
- Restore default config to be empty (Phil Sutter) [1694723]

* Mon Feb 17 2020 Phil Sutter <psutter@redhat.com> [0.9.3-11.el8]
- Package requires libnftnl-1.1.5-3 (Phil Sutter) [1795224]
- src: Add support for concatenated set ranges (Phil Sutter) [1795224]
- src: Add support for NFTNL_SET_DESC_CONCAT (Phil Sutter) [1795224]
- include: resync nf_tables.h cache copy (Phil Sutter) [1795224]
- parser: add a helper for concat expression handling (Phil Sutter) [1795224]

* Wed Feb 12 2020 Phil Sutter <psutter@redhat.com> [0.9.3-10.el8]
- scanner: Extend asteriskstring definition (Phil Sutter) [1763652]
- doc: nft.8: Mention wildcard interface matching (Phil Sutter) [1763652]
- tests: py: Support testing host binaries (Phil Sutter) [1754047]
- tests: monitor: Support testing host's nft binary (Phil Sutter) [1754047]
- tests: monitor: Support running individual test cases (Phil Sutter) [1754047]
- tests: json_echo: Support testing host binaries (Phil Sutter) [1754047]
- tests: json_echo: Fix for Python3 (Phil Sutter) [1754047]

* Mon Jan 27 2020 Phil Sutter <psutter@redhat.com> [0.9.3-9.el8]
- netlink: Avoid potential NULL-pointer deref in netlink_gen_payload_stmt() (Phil Sutter) [1793030]
- netlink: Fix leaks in netlink_parse_cmp() (Phil Sutter) [1793030]
- netlink: Fix leak in unterminated string deserializer (Phil Sutter) [1793030]

* Fri Jan 17 2020 Phil Sutter <psutter@redhat.com> [0.9.3-8.el8]
- cache: Fix for doubled output after reset command (Phil Sutter) [1790793]
- tests: shell: Search diff tool once and for all (Phil Sutter) [1790793]
- xfrm: spi is big-endian (Phil Sutter) [1790963]

* Mon Jan 13 2020 Phil Sutter <psutter@redhat.com> [0.9.3-7.el8]
- monitor: Fix output for ranges in anonymous sets (Phil Sutter) [1774742]

* Fri Jan 10 2020 Phil Sutter <psutter@redhat.com> [0.9.3-6.el8]
- monitor: Do not decompose non-anonymous sets (Phil Sutter) [1774742]
- main: restore --debug (Phil Sutter) [1778883]
- main: enforce options before commands (Phil Sutter) [1778883]

* Fri Jan 10 2020 Phil Sutter <psutter@redhat.com> [0.9.3-5.el8]
- Install an improved sample config (Phil Sutter) [1694723]

* Wed Dec 04 2019 Phil Sutter <psutter@redhat.com> [0.9.3-4.el8]
- Explicitly depend on newer libnftl version (Phil Sutter) [1643192]

* Tue Dec 03 2019 Phil Sutter <psutter@redhat.com> [0.9.3-3.el8]
- Fix permissions of osf-related configs (Phil Sutter) [1776462]

* Tue Dec 03 2019 Phil Sutter <psutter@redhat.com> [0.9.3-2.el8]
- Add example scripts to nftables package (Phil Sutter) [1643192]

* Mon Dec 02 2019 Phil Sutter <psutter@redhat.com> [0.9.3-1.el8]
- Rebase onto upstream release 0.9.3 (Phil Sutter) [1643192]

* Mon Oct 21 2019 Phil Sutter <psutter@redhat.com> [0.9.2-4.el8]
- tproxy: Add missing error checking when parsing from netlink (Phil Sutter) [1643192]
- parser_json: Fix checking of parse_policy() return code (Phil Sutter) [1643192]

* Fri Oct 18 2019 Phil Sutter <psutter@redhat.com> [0.9.2-3.el8]
- spec: Avoid multilib problems due to updated nftables.py (Phil Sutter) [1643192]

* Fri Oct 18 2019 Phil Sutter <psutter@redhat.com> [0.9.2-2.el8]
- rule: Fix for single line ct timeout printing (Phil Sutter) [1643192]
- tests/monitor: Fix for changed ct timeout format (Phil Sutter) [1643192]
- monitor: Add missing newline to error message (Phil Sutter) [1643192]
- src: restore --echo with anonymous sets (Phil Sutter) [1643192]

* Tue Oct 15 2019 Phil Sutter <psutter@redhat.com> [0.9.2-1.el8]
- src: obj: fix memleak in handle_free() (Phil Sutter) [1643192]
- libnftables: memleak when list of commands is empty (Phil Sutter) [1643192]
- mnl: do not cache sender buffer size (Phil Sutter) [1643192]
- src: meter: avoid double-space in list ruleset output (Phil Sutter) [1643192]
- src: parser_json: fix crash while restoring secmark object (Phil Sutter) [1643192]
- nftables: don't crash in 'list ruleset' if policy is not set (Phil Sutter) [1643192]
- json: tests: fix typo in ct expectation json test (Phil Sutter) [1643192]
- parser_bison: Fix 'exists' keyword on Big Endian (Phil Sutter) [1643192]
- json: fix type mismatch on "ct expect" json exporting (Phil Sutter) [1643192]
- libnftables: use-after-free in exit path (Phil Sutter) [1643192]
- netlink_delinearize: fix wrong conversion to "list" in ct mark (Phil Sutter) [1643192]
- mnl: fix --echo buffer size again (Phil Sutter) [1643192]
- parser_json: fix crash on insert rule to bad references (Phil Sutter) [1643192]
- evaluate: flag fwd and queue statements as terminal (Phil Sutter) [1643192]
- tests: shell: check that rule add with index works with echo (Phil Sutter) [1643192]
- cache: fix --echo with index/position (Phil Sutter) [1643192]
- src: secmark: fix brace indentation and missing quotes in selctx output (Phil Sutter) [1643192]
- Add python3-nftables sub-package (Phil Sutter) [1643192]
- Rebase onto upstream version 0.9.2 (Phil Sutter) [1643192]

* Mon Aug 12 2019 Phil Sutter <psutter@redhat.com> - 1:0.9.0-14
- src: fix jumps on bigendian arches
- src: json: fix constant parsing on bigendian

* Thu Aug 08 2019 Phil Sutter <psutter@redhat.com> - 1:0.9.0-13
- Fix for adding a rule with index and set reference

* Wed Jul 31 2019 Phil Sutter <psutter@redhat.com> - 1:0.9.0-12
- Fix permissions of /etc/nftables directory

* Wed Jun 26 2019 Phil Sutter <psutter@redhat.com> - 1:0.9.0-11
- Fix segfault with xtables support

* Wed Jun 26 2019 Phil Sutter <psutter@redhat.com> - 1:0.9.0-10
- Fix typo in spec file

* Wed Jun 26 2019 Phil Sutter <psutter@redhat.com> - 1:0.9.0-9
- Allow variables in jump statement
- Make example configs readable only by root
- Document nft list parameters
- Document vmap statement
- Install netdev-ingress.nft sample config in the right spot
- Backport upstream fixes since last release

* Fri Mar 01 2019 Phil Sutter - 1:0.9.0-8
- Add missing patch to spec file

* Fri Dec 21 2018 Phil Sutter - 1:0.9.0-7
- src: Reject 'export vm json' command

* Tue Dec 18 2018 Phil Sutter - 1:0.9.0-6
- Rebuild for updated libnftnl

* Thu Dec 13 2018 Phil Sutter - 1:0.9.0-5
- nft.8: Document log level audit
- nft.8: Clarify 'index' option of add rule command

* Thu Oct 25 2018 Phil Sutter - 1:0.9.0-4
- Add fixes for covscan report
- Fix for ECN keyword in LHS of relational
- Update meta pkt_type value description
- Fix for segfault with JSON output if xt expression is present
- Add missing nft suffix to files included from /etc/sysconfig/nftables.conf
- Use native JSON API in nft monitor

* Thu Oct 11 2018 Phil Sutter - 1:0.9.0-3
- Enable xtables support
- Enable JSON support

* Mon Sep 10 2018 Phil Sutter - 1:0.9.0-2
- Allow icmpx in inet/bridge families

* Tue Aug 14 2018 Phil Sutter - 1:0.9.0-1
- New version 0.9.0
- Install libnftables
- Add devel sub-package
- Add gcc BuildRequires

* Sat Mar 03 2018 Kevin Fenzi <kevin@scrye.com> - 0.8.3-1
- Update to 0.8.3. Fixes bug #1551207

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Kevin Fenzi <kevin@scrye.com> - 0.8.2-1
- Update to 0.8.2. Fixes bug #1541582

* Tue Jan 16 2018 Kevin Fenzi <kevin@scrye.com> - 0.8.1-1
- Update to 0.8.1. Fixes bug #1534982

* Sun Oct 22 2017 Kevin Fenzi <kevin@scrye.com> - 0.8-1
- Update to 0.8. 

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1:0.7-2
- Rebuild for readline 7.x

* Thu Dec 22 2016 Kevin Fenzi <kevin@scrye.com> - 0.7-1
- Update to 0.7

* Fri Jul 15 2016 Kevin Fenzi <kevin@scrye.com> - 0.6-2
- Rebuild for new glibc symbols

* Thu Jun 02 2016 Kevin Fenzi <kevin@scrye.com> - 0.6-1
- Update to 0.6.

* Sun Apr 10 2016 Kevin Fenzi <kevin@scrye.com> - 0.5-4
- Add example config files and move config to /etc/sysconfig. Fixes bug #1313936

* Fri Mar 25 2016 Kevin Fenzi <kevin@scrye.com> - 0.5-3
- Add systemd unit file. Fixes bug #1313936

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 17 2015 Kevin Fenzi <kevin@scrye.com> 0.5-1
- Update to 0.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 10 2015 Kevin Fenzi <kevin@scrye.com> 0.4-2
- Add patch to fix nft -f dep gen.

* Fri Dec 26 2014 Kevin Fenzi <kevin@scrye.com> 0.4-1
- Update to 0.4
- Add Epoch to fix versioning. 

* Wed Sep 03 2014 Kevin Fenzi <kevin@scrye.com> 0.100-4.20140903git
- Update to 20140903 snapshot

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100-4.20140704git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 04 2014 Kevin Fenzi <kevin@scrye.com> 0.100-3.20140704git
- Update to new snapshot

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100-2.20140426git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 26 2014 Kevin Fenzi <kevin@scrye.com> 0.100-1.20140426git
- Update t0 20140426

* Sun Mar 30 2014 Kevin Fenzi <kevin@scrye.com> 0.100-1.20140330git
- Update to 20140330 snapshot
- Sync versions to be post 0.100 release.

* Wed Mar 26 2014 Kevin Fenzi <kevin@scrye.com> 0-0.7.20140326git
- Update to 20140326 snapshot
- Fix permissions on man pages. 

* Mon Mar 24 2014 Kevin Fenzi <kevin@scrye.com> 0-0.6.20140324git
- Update to 20140324 snapshot

* Fri Mar 07 2014 Kevin Fenzi <kevin@scrye.com> 0-0.5.20140307git
- Update to 20140307

* Sat Jan 25 2014 Kevin Fenzi <kevin@scrye.com> 0-0.4.20140125git
- Update to 20140125 snapshot

* Sat Jan 18 2014 Kevin Fenzi <kevin@scrye.com> 0-0.3.20140118git
- Update to 20140118 snapshot
- Fixed License tag to be correct
- Fixed changelog
- nft scripts now use full path for nft
- Fixed man page building
- Dropped unneeded rm in install
- Patched build to not be silent. 

* Tue Dec 03 2013 Kevin Fenzi <kevin@scrye.com> 0-0.2.20131202git
- Use upstream snapshots for source.
- Use 0 for version. 

* Sat Nov 30 2013 Kevin Fenzi <kevin@scrye.com> 0-0.1
- initial version for Fedora review
