%define nft_rpmversion 1.0.9
%define nft_specrelease 9

Name:           nftables
Version:        %{nft_rpmversion}
Release:        %{nft_specrelease}%{?dist}%{?buildid}
# Upstream released a 0.100 version, then 0.4. Need Epoch to get back on track.
Epoch:          1
Summary:        Netfilter Tables userspace utillites

License:        GPLv2
URL:            https://netfilter.org/projects/nftables/
Source0:        %{url}/files/%{name}-%{version}.tar.xz
Source1:        nftables.service
Source2:        nftables.conf
Source3:        main.nft
Source4:        router.nft
Source5:        nat.nft
Source6:        nft-test.stderr.expect
Source7:        run-tests.stderr.expect
Source8:        monitor_run-tests.stderr.expect

Patch1:             0001-Add-support-for-table-s-persist-flag.patch
Patch2:             0002-cache-Always-set-NFT_CACHE_TERSE-for-list-cmd-with-t.patch
Patch3:             0003-json-deal-appropriately-with-multidevice-in-chain.patch
Patch4:             0004-parser_json-fix-handle-memleak-from-error-path.patch
Patch5:             0005-tests-shell-Fix-sets-reset_command_0-for-current-ker.patch
Patch6:             0006-tests-shell-connect-chains-to-hook-point.patch
Patch7:             0007-datatype-rt_symbol_table_init-to-search-for-iproute2.patch
Patch8:             0008-tests-py-remove-huge-limit-test-cases.patch
Patch9:             0009-tests-py-add-missing-json.output-data.patch
Patch10:            0010-tests-py-missing-json-output-in-never-merge-across-n.patch
Patch11:            0011-Revert-doc-part-of-src-add-tcp-option-reset-support.patch
Patch12:            0012-Revert-doc-part-of-meta-introduce-meta-broute-suppor.patch
Patch13:            0013-Revert-doc-part-of-exthdr-add-boolean-DCCP-option-ma.patch
Patch14:            0014-src-netlink-fix-crash-when-ops-doesn-t-support-udata.patch
Patch15:            0015-src-fix-reset-element-support-for-interval-set-type.patch
Patch16:            0016-parser_bison-Fix-for-broken-compatibility-with-older.patch
Patch17:            0017-tests-shell-add-missing-elem_opts_compat_0.nodump-fi.patch
Patch18:            0018-tests-shell-cover-long-interface-name-in-0042chain_v.patch
Patch19:            0019-parser_bison-fix-length-check-for-ifname-in-ifname_e.patch
Patch20:            0020-tests-shell-fix-mount-command-in-test-wrapper.sh.patch
Patch21:            0021-tproxy-Drop-artificial-port-printing-restriction.patch
Patch22:            0022-meta-fix-hour-decoding-when-timezone-offset-is-negat.patch
Patch23:            0023-evaluate-reset-statement-length-context-only-for-set.patch
Patch24:            0024-evaluate-place-byteorder-conversion-before-rshift-in.patch
Patch25:            0025-src-add-free_const-and-use-it-instead-of-xfree.patch
Patch26:            0026-src-remove-xfree-and-use-plain-free.patch
Patch27:            0027-netlink-fix-buffer-size-for-user-data-in-netlink_del.patch
Patch28:            0028-tests-shell-split-merge-nat-optimization-in-two-test.patch
Patch29:            0029-tests-shell-split-set-NAT-interval-test.patch
Patch30:            0030-src-expand-create-commands.patch
Patch31:            0031-json-fix-use-after-free-in-table_flags_json.patch
Patch32:            0032-tests-shell-restore-pipapo-and-chain-binding-coverag.patch
Patch33:            0033-tests-shell-skip-if-kernel-does-not-support-flowtabl.patch
Patch34:            0034-evaluate-fix-rule-replacement-with-anon-sets.patch
Patch35:            0035-tests-shell-adjust-add-after-delete-flowtable-for-ol.patch
Patch36:            0036-tests-shell-flush-connlimit-sets.patch
Patch37:            0037-evaluate-bogus-error-when-adding-devices-to-flowtabl.patch
Patch38:            0038-tests-shell-split-nat-inet-tests.patch
Patch39:            0039-evaluate-clone-unary-expression-datatype-to-deal-wit.patch
Patch40:            0040-evaluate-reject-sets-with-no-key.patch
Patch41:            0041-evaluate-prevent-assert-when-evaluating-very-large-s.patch
Patch42:            0042-evaluate-disable-meta-set-with-ranges.patch
Patch43:            0043-monitor-add-support-for-concatenated-set-ranges.patch
Patch44:            0044-evaluate-reject-set-definition-with-no-key.patch
Patch45:            0045-parser-tcpopt-fix-tcp-option-parsing-with-NUM-length.patch
Patch46:            0046-evaluate-reset-statement-length-context-before-evalu.patch
Patch47:            0047-tests-py-missing-json-output-in-meta.t-with-vlan-map.patch
Patch48:            0048-parser_bison-fix-objref-statement-corruption.patch
Patch49:            0049-evaluate-fix-bogus-assertion-failure-with-boolean-da.patch
Patch50:            0050-parser_bison-close-chain-scope-before-chain-release.patch
Patch51:            0051-meta-fix-tc-classid-parsing-out-of-bounds-access.patch
Patch52:            0052-evaluate-exthdr-statement-arg-must-be-not-be-a-range.patch
Patch53:            0053-src-reject-large-raw-payload-and-concat-expressions.patch
Patch54:            0054-evaluate-fix-stack-overflow-with-huge-priority-strin.patch
Patch55:            0055-tests-shell-add-test-to-cover-payload-transport-matc.patch
Patch56:            0056-parser_bison-error-out-on-duplicated-type-typeof-ele.patch
Patch57:            0057-netlink-fix-stack-overflow-due-to-erroneous-rounding.patch
Patch58:            0058-parser_bison-ensure-all-timeout-policy-names-are-rel.patch
Patch59:            0059-tests-shell-prefer-project-nft-to-system-wide-nft.patch
Patch60:            0060-doc-incorrect-datatype-description-for-icmpv6_type-a.patch
Patch61:            0061-evaluate-add-missing-range-checks-for-dup-fwd-and-pa.patch
Patch62:            0062-evaluate-skip-anonymous-set-optimization-for-concate.patch
Patch63:            0063-evaluate-do-not-fetch-next-expression-on-runaway-num.patch
Patch64:            0064-evaluate-error-out-when-store-needs-more-than-one-12.patch
Patch65:            0065-rule-fix-sym-refcount-assertion.patch
Patch66:            0066-json-Support-sets-auto-merge-option.patch
Patch67:            0067-evaluate-don-t-assert-on-net-transport-header-confli.patch
Patch68:            0068-evaluate-fix-check-for-unknown-in-cmd_op_to_name.patch
Patch69:            0069-cache-Optimize-caching-for-list-tables-command.patch
Patch70:            0070-evaluate-skip-byteorder-conversion-for-selector-smal.patch
Patch71:            0071-netlink_delinearize-move-concat-and-value-postproces.patch
Patch72:            0072-expression-missing-line-in-describe-command-with-inv.patch
Patch73:            0073-evaluate-permit-use-of-host-endian-constant-values-i.patch
Patch74:            0074-tests-shell-permit-use-of-host-endian-constant-value.patch
Patch75:            0075-src-improve-error-reporting-for-destroy-command.patch
Patch76:            0076-parser-compact-interval-typeof-rules.patch
Patch77:            0077-parser-compact-type-typeof-set-rules.patch
Patch78:            0078-rule-fix-ASAN-errors-in-chain-priority-to-textual-na.patch
Patch79:            0079-nftables-do-mot-merge-payloads-on-negation.patch
Patch80:            0080-tests-py-add-payload-merging-test-cases.patch
Patch81:            0081-parser-json-Support-for-synproxy-objects.patch
Patch82:            0082-doc-libnftables-json-Drop-invalid-ops-from-match-exp.patch
Patch83:            0083-netlink_delinearize-restore-binop-syntax-when-listin.patch
Patch84:            0084-evaluate-display-Range-negative-size-error.patch
Patch85:            0085-src-disentangle-ICMP-code-types.patch
Patch86:            0086-tests-py-complete-icmp-and-icmpv6-update.patch
Patch87:            0087-tests-shell-payload-matching-requires-egress-support.patch
Patch88:            0088-tests-shell-check-for-reset-tcp-options-support.patch
Patch89:            0089-doc-nft.8-Two-minor-synopsis-fixups.patch
Patch90:            0090-mergesort-Avoid-accidental-set-element-reordering.patch
Patch91:            0091-doc-nft.8-Fix-markup-in-ct-expectation-synopsis.patch
Patch92:            0092-cache-check-for-NFT_CACHE_REFRESH-in-current-request.patch
Patch93:            0093-evaluate-bogus-protocol-conflicts-in-vlan-with-impli.patch
Patch94:            0094-evaluate-Fix-incorrect-checking-the-base-variable-in.patch
Patch95:            0095-scanner-inet_pton-allows-for-broader-IPv4-Mapped-IPv.patch
Patch96:            0096-monitor-too-large-shift-exponent-displaying-payload-.patch
Patch97:            0097-cmd-provide-better-hint-if-chain-is-already-declared.patch
Patch98:            0098-cmd-skip-variable-set-elements-when-collapsing-comma.patch
Patch99:            0099-tests-shell-skip-ip-option-tests-if-kernel-does-not-.patch
Patch100:           0100-src-add-string-preprocessor-and-use-it-for-log-prefi.patch
Patch101:           0101-intervals-fix-element-deletions-with-maps.patch
Patch102:           0102-parser_bison-recursive-table-declaration-in-deprecat.patch
Patch103:           0103-evaluate-set-on-expr-len-for-catchall-set-elements.patch
Patch104:           0104-segtree-set-on-EXPR_F_KERNEL-flag-for-catchall-eleme.patch
Patch105:           0105-optimize-clone-counter-before-insertion-into-set-ele.patch
Patch106:           0106-libnftables-skip-useable-checks-for-dev-stdin.patch
Patch107:           0107-parser_json-use-stdin-buffer-if-available.patch
Patch108:           0108-optimize-skip-variables-in-nat-statements.patch
Patch109:           0109-datatype-reject-rate-in-quota-statement.patch
Patch110:           0110-cache-rule-by-index-requires-full-cache.patch
Patch111:           0111-datatype-improve-error-reporting-when-time-unit-is-n.patch
Patch112:           0112-parser_bison-allow-0-burst-in-limit-rate-byte-mode.patch
Patch113:           0113-parser_json-fix-crash-in-json_parse_set_stmt_list.patch
Patch114:           0114-json-Support-maps-with-concatenated-data.patch
Patch115:           0115-parser_json-release-buffer-returned-by-json_dumps.patch
Patch116:           0116-parser_json-fix-several-expression-memleaks-from-err.patch
Patch117:           0117-cache-reset-filter-for-each-command.patch
Patch118:           0118-cache-accumulate-flags-in-batch.patch
Patch119:           0119-cache-only-dump-rules-for-the-given-table.patch
Patch120:           0120-cache-add-filtering-support-for-objects.patch
Patch121:           0121-cache-consolidate-reset-command.patch
Patch122:           0122-cache-assert-filter-when-calling-nft_cache_evaluate.patch
Patch123:           0123-cache-remove-full-cache-requirement-when-echo-flag-i.patch
Patch124:           0124-cache-relax-requirement-for-replace-rule-command.patch
Patch125:           0125-cache-position-does-not-require-full-cache.patch
Patch126:           0126-libnftables-Zero-ctx-vars-after-freeing-it.patch
Patch127:           0127-tests-shell-stabilize-packetpath-payload.patch
Patch128:           0128-proto-use-NFT_PAYLOAD_L4CSUM_PSEUDOHDR-flag-to-mangl.patch
Patch129:           0129-tests-py-fix-up-udp-csum-fixup-output.patch
Patch130:           0130-cache-initialize-filter-when-fetching-implicit-chain.patch
Patch131:           0131-libnftables-json-fix-raw-payload-expression-document.patch
Patch132:           0132-src-collapse-set-element-commands-from-parser.patch
Patch133:           0133-rule-netlink-attribute-offset-is-uint32_t-for-struct.patch
Patch134:           0134-mnl-update-cmd_add_loc-to-take-struct-nlmsghdr.patch
Patch135:           0135-mnl-rename-to-mnl_seqnum_alloc-to-mnl_seqnum_inc.patch
Patch136:           0136-src-fix-extended-netlink-error-reporting-with-large-.patch
Patch137:           0137-tests-monitor-fix-up-test-case-breakage.patch
Patch138:           0138-doc-extend-description-of-fib-expression.patch
Patch139:           0139-json-collapse-set-element-commands-from-parser.patch
Patch140:           0140-json-Support-typeof-in-set-and-map-types.patch
Patch141:           0141-tests-py-Fix-for-storing-payload-into-missing-file.patch
Patch142:           0142-optimize-compare-expression-length.patch
Patch143:           0143-intervals-set-internal-element-location-with-the-del.patch
Patch144:           0144-parser_bison-fix-UaF-when-reporting-table-parse-erro.patch
Patch145:           0145-intervals-add-helper-function-to-set-previous-elemen.patch
Patch146:           0146-src-add-EXPR_RANGE_VALUE-expression-and-use-it.patch
Patch147:           0147-intervals-do-not-merge-intervals-with-different-time.patch
Patch148:           0148-evaluate-remove-variable-shadowing.patch
Patch149:           0149-netlink_delinarize-fix-bogus-munging-of-mask-value.patch
Patch150:           0150-ipopt-use-ipv4-address-datatype-for-address-field-in.patch
Patch151:           0151-tests-shell-delete-netdev-chain-after-test.patch
Patch152:           0152-datatype-clamp-boolean-value-to-0-and-1.patch
Patch153:           0153-parser_bison-turn-redundant-ip-option-type-field-mat.patch
Patch154:           0154-parser_bison-compact-and-simplify-list-and-reset-syn.patch
Patch155:           0155-evaluate-auto-merge-is-only-available-for-singleton-.patch
Patch156:           0156-fib-Change-data-type-of-fib-oifname-to-ifname.patch
Patch157:           0157-evaluate-optimize-zero-length-range.patch
Patch158:           0158-payload-return-early-if-dependency-is-not-a-payload-.patch
Patch159:           0159-payload-honor-inner-payload-description-in-payload_e.patch
Patch160:           0160-segtree-fix-string-data-initialisation.patch
Patch161:           0161-evaluate-release-existing-datatype-when-evaluating-u.patch
Patch162:           0162-segtree-incomplete-output-in-get-element-command-wit.patch
Patch163:           0163-src-do-not-merge-a-set-with-a-erroneous-one.patch
Patch164:           0164-tests-shell-detach-synproxy-test.patch
Patch165:           0165-src-print-set-element-with-multi-word-description-in.patch
Patch166:           0166-netlink-fix-stack-buffer-overrun-when-emitting-range.patch
Patch167:           0167-parser_bison-reject-non-serializeable-typeof-express.patch
Patch168:           0168-evaluate-don-t-allow-nat-map-with-specified-protocol.patch
Patch169:           0169-evaluate-fix-assertion-failure-with-malformed-map-de.patch
Patch170:           0170-tests-shell-extend-coverage-for-set-element-statemen.patch
Patch171:           0171-parser_bison-consolidate-counter-grammar-rule-for-se.patch
Patch172:           0172-parser_bison-consolidate-limit-grammar-rule-for-set-.patch
Patch173:           0173-parser_bison-consolidate-quota-grammar-rule-for-set-.patch
Patch174:           0174-parser_bison-consolidate-last-grammar-rule-for-set-e.patch
Patch175:           0175-parser_bison-consolidate-connlimit-grammar-rule-for-.patch
Patch176:           0176-json-make-sure-timeout-list-is-initialised.patch
Patch177:           0177-evaluate-don-t-update-cache-for-anonymous-chains.patch
Patch178:           0178-tests-shell-missing-ct-count-elements-in-new-set_stm.patch
Patch179:           0179-optimize-compact-bitmask-matching-in-set-map.patch
Patch180:           0180-optimize-incorrect-comparison-for-reject-statement.patch
Patch181:           0181-json-don-t-BUG-when-asked-to-list-synproxies.patch
Patch182:           0182-evaluate-compact-STMT_F_STATEFUL-checks.patch
Patch183:           0183-evaluate-only-allow-stateful-statements-in-set-and-m.patch
Patch184:           0184-cache-don-t-crash-when-filter-is-NULL.patch
Patch185:           0185-optimize-expand-expression-list-when-merging-into-co.patch
Patch186:           0186-cache-prevent-possible-crash-rule-filter-is-NULL.patch
Patch187:           0187-parser_json-allow-statement-stateful-statement-only-.patch
Patch188:           0188-parser_json-reject-empty-jump-goto-chain.patch
Patch189:           0189-parser_json-bail-out-on-malformed-statement-in-set.patch
Patch190:           0190-evaluate-bail-out-if-ct-saddr-daddr-dependency-canno.patch
Patch191:           0191-optimize-invalidate-merge-in-case-of-duplicated-key-.patch
Patch192:           0192-parser_bison-add-selector_expr-rule-to-restrict-type.patch
Patch193:           0193-netlink-bogus-concatenated-set-ranges-with-netlink-m.patch
Patch194:           0194-doc-Fix-typo-in-nat-statement-prefix-description.patch
Patch195:           0195-parser_json-Introduce-parse_flags_array.patch
Patch196:           0196-json-Print-single-synproxy-flags-as-non-array.patch
Patch197:           0197-json-Print-single-set-flag-as-non-array.patch
Patch198:           0198-tests-shell-Add-test-case-for-JSON-flags-arrays.patch
Patch199:           0199-json-Print-single-fib-flag-as-non-array.patch
Patch200:           0200-json-Accept-more-than-two-operands-in-binary-express.patch
Patch201:           0201-json-Fix-for-memleak-in-__binop_expr_json.patch
Patch202:           0202-json-Introduce-json_add_array_new.patch
Patch203:           0203-netlink-Catch-unknown-types-when-deserializing-objec.patch
Patch204:           0204-netlink-Avoid-potential-NULL-ptr-deref-parsing-set-e.patch
Patch205:           0205-tests-shell-check-for-features-not-available-in-5.4.patch
Patch206:           0206-tests-py-fix-json-single-flag-output-for-fib-synprox.patch
Patch207:           0207-json-prevent-null-deref-if-chain-policy-is-not-set.patch
Patch208:           0208-json-work-around-fuzzer-induced-assert-crashes.patch
Patch209:           0209-netlink-Fix-for-potential-crash-parsing-a-flowtable.patch
Patch210:           0210-netlink-Do-not-allocate-a-bogus-flowtable-priority-e.patch
Patch211:           0211-tests-monitor-Fix-for-single-flag-array-avoidance.patch
Patch212:           0212-tests-shell-combine-dormant-flag-with-netdevice-remo.patch
Patch213:           0213-tests-shell-Adjust-to-ifname-based-hooks.patch
Patch214:           0214-tests-py-Properly-fix-JSON-equivalents-for-netdev-re.patch
Patch215:           0215-netlink-Avoid-crash-upon-missing-NFTNL_OBJ_CT_TIMEOU.patch
Patch216:           0216-src-BASECHAIN-flag-no-longer-implies-presence-of-pri.patch
Patch217:           0217-tests-py-prepare-for-set-debug-change.patch
Patch218:           0218-debug-include-kernel-set-information-on-cache-fill.patch
Patch219:           0219-parser_bison-allow-delete-command-with-map-via-handl.patch
Patch220:           0220-rule-skip-fuzzy-lookup-if-object-name-is-not-availab.patch
Patch221:           0221-parser_bison-only-reset-by-name-is-supported-by-now.patch
Patch222:           0222-cache-assert-name-is-non-nul-when-looking-up.patch
Patch223:           0223-tests-py-clean-up-set-backend-support-fallout.patch
Patch224:           0224-json-reject-too-long-interface-names.patch
Patch225:           0225-tests-shell-Fix-ifname_based_hooks-feature-check.patch
Patch226:           0226-fib-allow-to-check-if-route-exists-in-maps.patch
Patch227:           0227-fib-allow-to-use-it-in-set-statements.patch
Patch228:           0228-tests-py-re-enables-nft-test.py-to-load-the-local-nf.patch
Patch229:           0229-rule-print-chain-and-flowtable-devices-in-quotes.patch
Patch230:           0230-evaluate-validate-set-expression-type-before-accessi.patch
Patch231:           0231-mnl-Call-mnl_attr_nest_end-just-once.patch
Patch232:           0232-doc-nft.8-Minor-NAT-STATEMENTS-section-review.patch
Patch233:           0233-src-netlink-netlink_delinearize_table-may-return-NUL.patch
Patch234:           0234-tests-py-Drop-stale-entries-since-redundant-test-cas.patch
Patch235:           0235-tests-py-Drop-duplicate-test-from-inet-geneve.t.patch
Patch236:           0236-tests-py-Drop-duplicate-test-from-inet-gre.t.patch
Patch237:           0237-tests-py-Drop-duplicate-test-from-inet-gretap.t.patch
Patch238:           0238-tests-py-Drop-stale-entry-from-inet-tcp.t.json.patch
Patch239:           0239-tests-py-Drop-duplicate-test-from-inet-vxlan.t.patch
Patch240:           0240-tests-py-Drop-stale-entry-from-ip-snat.t.json.patch
Patch241:           0241-tests-py-Drop-stale-entries-from-ip6-ct-meta-.t.json.patch
Patch242:           0242-tests-py-Drop-stale-entry-from-ip-snat.t.payload.patch
Patch243:           0243-tests-py-Fix-tests-added-for-icmpv6-taddr-support.patch
Patch244:           0244-json-Do-not-reduce-single-item-arrays-on-output.patch
Patch245:           0245-segtree-incorrect-type-when-aggregating-concatenated.patch
Patch246:           0246-src-ensure-chain-policy-evaluation-when-specified.patch
Patch247:           0247-fib-restore-JSON-output-for-relational-expressions.patch
Patch248:           0248-mnl-silence-compiler-warning.patch
Patch249:           0249-tests-monitor-Fix-for-flag-arrays-in-JSON-output.patch
Patch250:           0250-mnl-continue-on-ENOBUFS-errors-when-processing-batch.patch
Patch251:           0251-monitor-Quote-device-names-in-chain-declarations-too.patch
Patch252:           0252-tests-monitor-Fix-regex-collecting-expected-echo-out.patch
Patch253:           0253-monitor-Recognize-flowtable-add-del-events.patch
Patch254:           0254-monitor-Inform-JSON-printer-when-reporting-an-object.patch
Patch255:           0255-tests-Prepare-exit-codes-for-automake.patch
Patch256:           0256-fib-Fix-for-existence-check-on-Big-Endian.patch
Patch257:           0257-tests-py-objects.t-must-use-input-not-output.patch
Patch258:           0258-doc-fix-tcpdump-example.patch
Patch259:           0259-src-parser_json-fix-format-string-bugs.patch
Patch260:           0260-optimize-Fix-verdict-expression-comparison.patch
Patch261:           0261-datatype-Fix-boolean-type-on-Big-Endian.patch
Patch262:           0262-tests-py-any-ct.t.json.output-Drop-leftover-entry.patch
Patch263:           0263-tests-py-Fix-for-using-wrong-payload-path.patch
Patch264:           0264-tests-py-Do-not-rely-upon-end-marker.patch
Patch265:           0265-tests-py-inet-osf.t-Fix-element-ordering-in-JSON-equ.patch
Patch266:           0266-tests-py-Implement-payload_record.patch
Patch267:           0267-doc-don-t-suggest-to-disable-GSO.patch
Patch268:           0268-doc-libnftables-json-Describe-RULESET-object.patch
Patch269:           0269-rule-skip-CMD_OBJ_SETELEMS-with-no-elements-after-se.patch
Patch270:           0270-tests-json_echo-Drop-rule-handle-before-multi-add.patch
Patch271:           0271-monitor-fix-memleak-in-setelem-cb.patch
Patch272:           0272-tcpopt-add-symbol-table-for-mptcp-suboptions.patch
Patch273:           0273-netlink_delinearize-also-consider-exthdr-type-when-t.patch
Patch274:           0274-expression-propagate-key-datatype-for-anonymous-sets.patch
Patch275:           0275-expression-expr_build_udata_recurse-should-recurse.patch
Patch276:           0276-tests-py-any-tcpopt.t.json-Fix-JSON-equivalent.patch
Patch277:           0277-mergesort-Fix-sorting-of-string-values.patch
Patch278:           0278-mergesort-Align-concatenation-sort-order-with-Big-En.patch
Patch279:           0279-segtree-Fix-range-aggregation-on-Big-Endian.patch
Patch280:           0280-json-complete-multi-statement-set-element-support.patch
Patch281:           0281-parser_bison-add-range-check-for-synproxy-wscale.patch
Patch282:           0282-cache-Relax-chain_cache_dump-filter-application.patch
Patch283:           0283-cache-Include-chains-flowtables-and-objects-in-netli.patch
Patch284:           0284-cache-Respect-family-in-all-list-commands.patch
Patch285:           0285-cache-Filter-for-table-when-listing-sets-or-maps.patch
Patch286:           0286-cache-Filter-for-table-when-listing-flowtables.patch
Patch287:           0287-segtree-Fix-for-variable-sized-object-may-not-be-ini.patch
Patch288:           0288-mnl-Fix-ordering-of-hooks-in-list-hooks-output.patch
Patch289:           0289-tests-py-don-t-use-a-fixed-filename.patch
Patch290:           0290-tests-py-print-the-file-name-as-intended.patch
Patch291:           0291-tests-py-osf-is-ip-only.patch
Patch292:           0292-cache-honor-c-check-for-reset-commands.patch
Patch293:           0293-parser_json-fix-map-set-type-confusion-crash-in-map-.patch
Patch294:           0294-segtree-rename-set_elem_add-to-set_elem_expr_add.patch
Patch295:           0295-src-remove-EXPR_SET_ELEM-in-range_expr_value_-low-hi.patch
Patch296:           0296-segtree-replace-default-case-by-specific-types-in-ge.patch
Patch297:           0297-segtree-fix-get-element-command-with-open-intervals.patch
Patch298:           0298-tests-py-Fix-keep-test-runner-option.patch
Patch299:           0299-datatype-don-t-return-a-const-string-from-cgroupv2_g.patch
Patch300:           0300-rule-constify-set_is_non_concat_range.patch
Patch301:           0301-tests-py-Fix-some-JSON-equivalents.patch
Patch302:           0302-json-Dump-flowtable-hook-spec-only-if-present.patch
Patch303:           0303-tests-monitor-enclose-device-names-in-quotes.patch
Patch304:           0304-tests-monitor-Extend-testcases-a-bit.patch
Patch305:           0305-tests-monitor-Label-diffs-to-help-users.patch
Patch306:           0306-tests-monitor-Run-in-own-netns.patch
Patch307:           0307-tests-monitor-Become-PWD-agnostic.patch
Patch308:           0308-tests-monitor-Test-JSON-echo-mode-as-well.patch
Patch309:           0309-tests-monitor-Excercise-all-syntaxes-and-variants-by.patch
Patch310:           0310-tests-monitor-Fix-for-out-of-path-call.patch
Patch311:           0311-netlink-add-and-use-nft_data_memcpy-helper.patch

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
BuildRequires: pkgconfig(libnftnl) >= 1.2.6
BuildRequires: systemd
BuildRequires: asciidoc
BuildRequires: pkgconfig(xtables) >= 1.6.1
BuildRequires: jansson-devel
BuildRequires: python3-devel

%generate_buildrequires
cd py/
%pyproject_buildrequires

%description
Netfilter Tables userspace utilities.

%package        devel
Summary:        Development library for nftables / libnftables
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig

%description devel
Development tools and static libraries and header files for the libnftables library.

%package -n     python3-nftables
Summary:        Python module providing an interface to libnftables
Requires:       %{name} = %{epoch}:%{version}-%{release}
%{?python_provide:%python_provide python3-nftables}

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
%configure --disable-silent-rules --with-xtables --with-json --with-cli=readline
%make_build
cd py/
%pyproject_wheel

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

cd py/
%pyproject_install
%pyproject_save_files nftables

%post
%systemd_post nftables.service
%ldconfig_post

%preun
%systemd_preun nftables.service

%postun
%systemd_postun_with_restart nftables.service
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

%files -n python3-nftables -f %{pyproject_files}

%changelog
* Wed Jul 29 2026 Phil Sutter <psutter@redhat.com> [1.0.9-9.el9]
- netlink: add and use nft_data_memcpy helper (Phil Sutter) [RHEL-190549]

* Wed Jul 22 2026 Phil Sutter <psutter@redhat.com> [1.0.9-8.el9]
- spec: Update expected test suite results (Phil Sutter) [RHEL-190549]
- tests: monitor: Fix for out-of-path call (Phil Sutter) [RHEL-190549]
- tests: monitor: Excercise all syntaxes and variants by default (Phil Sutter) [RHEL-190549]
- tests: monitor: Test JSON echo mode as well (Phil Sutter) [RHEL-190549]
- tests: monitor: Become $PWD agnostic (Phil Sutter) [RHEL-190549]
- tests: monitor: Run in own netns (Phil Sutter) [RHEL-190549]
- tests: monitor: Label diffs to help users (Phil Sutter) [RHEL-190549]
- tests: monitor: Extend testcases a bit (Phil Sutter) [RHEL-190549]
- tests: monitor: enclose device names in quotes (Phil Sutter) [RHEL-190549]
- json: Dump flowtable hook spec only if present (Phil Sutter) [RHEL-190549]
- tests: py: Fix some JSON equivalents (Phil Sutter) [RHEL-190549]
- rule: constify set_is_non_concat_range() (Phil Sutter) [RHEL-190549]
- datatype: don't return a const string from cgroupv2_get_path() (Phil Sutter) [RHEL-190549]
- tests: py: Fix --keep test runner option (Phil Sutter) [RHEL-190549]
- segtree: fix get element command with open intervals (Phil Sutter) [RHEL-190549]
- segtree: replace default case by specific types in get_set_intervals() (Phil Sutter) [RHEL-190549]
- src: remove EXPR_SET_ELEM in range_expr_value_{low,high}() (Phil Sutter) [RHEL-190549]
- segtree: rename set_elem_add() to set_elem_expr_add() (Phil Sutter) [RHEL-190549]
- parser_json: fix map/set type confusion crash in map statement parser (Phil Sutter) [RHEL-190549]
- cache: honor -c/--check for reset commands (Phil Sutter) [RHEL-190549]
- tests: py: osf is ip-only (Phil Sutter) [RHEL-190549]
- tests: py: print the file name as intended (Phil Sutter) [RHEL-190549]
- tests: py: don't use a fixed filename (Phil Sutter) [RHEL-190549]
- mnl: Fix ordering of hooks in 'list hooks' output (Phil Sutter) [RHEL-190549]
- segtree: Fix for variable-sized object may not be initialized (Phil Sutter) [RHEL-190549]
- cache: Filter for table when listing flowtables (Phil Sutter) [RHEL-190549]
- cache: Filter for table when listing sets or maps (Phil Sutter) [RHEL-190549]
- cache: Respect family in all list commands (Phil Sutter) [RHEL-190549]
- cache: Include chains, flowtables and objects in netlink debug output (Phil Sutter) [RHEL-190549]
- cache: Relax chain_cache_dump filter application (Phil Sutter) [RHEL-190549]
- parser_bison: add range check for synproxy wscale (Phil Sutter) [RHEL-190549]
- json: complete multi-statement set element support (Phil Sutter) [RHEL-190549]
- segtree: Fix range aggregation on Big Endian (Phil Sutter) [RHEL-190549]
- mergesort: Align concatenation sort order with Big Endian (Phil Sutter) [RHEL-190549]
- mergesort: Fix sorting of string values (Phil Sutter) [RHEL-190549]
- tests: py: any/tcpopt.t.json: Fix JSON equivalent (Phil Sutter) [RHEL-190549]
- expression: expr_build_udata_recurse should recurse (Phil Sutter) [RHEL-190549]
- expression: propagate key datatype for anonymous sets (Phil Sutter) [RHEL-190549]
- netlink_delinearize: also consider exthdr type when trimming binops (Phil Sutter) [RHEL-190549]
- tcpopt: add symbol table for mptcp suboptions (Phil Sutter) [RHEL-190549]
- monitor: fix memleak in setelem cb (Phil Sutter) [RHEL-190549]
- tests: json_echo: Drop rule handle before multi-add (Phil Sutter) [RHEL-190549]
- rule: skip CMD_OBJ_SETELEMS with no elements after set flush (Phil Sutter) [RHEL-190549]
- doc: libnftables-json: Describe RULESET object (Phil Sutter) [RHEL-190549]
- doc: don't suggest to disable GSO (Phil Sutter) [RHEL-190549]
- tests: py: Implement payload_record() (Phil Sutter) [RHEL-190549]
- tests: py: inet/osf.t: Fix element ordering in JSON equivalents (Phil Sutter) [RHEL-190549]
- tests: py: Do not rely upon '[end]' marker (Phil Sutter) [RHEL-190549]
- tests: py: Fix for using wrong payload path (Phil Sutter) [RHEL-190549]
- tests: py: any/ct.t.json.output: Drop leftover entry (Phil Sutter) [RHEL-190549]
- datatype: Fix boolean type on Big Endian (Phil Sutter) [RHEL-190549]
- optimize: Fix verdict expression comparison (Phil Sutter) [RHEL-190549]
- src: parser_json: fix format string bugs (Phil Sutter) [RHEL-190549]
- doc: fix tcpdump example (Phil Sutter) [RHEL-190549]
- tests: py: objects.t: must use input, not output (Phil Sutter) [RHEL-190549]
- fib: Fix for existence check on Big Endian (Phil Sutter) [RHEL-190549]
- tests: Prepare exit codes for automake (Phil Sutter) [RHEL-190549]
- monitor: Inform JSON printer when reporting an object delete event (Phil Sutter) [RHEL-190549]
- monitor: Recognize flowtable add/del events (Phil Sutter) [RHEL-190549]
- tests: monitor: Fix regex collecting expected echo output (Phil Sutter) [RHEL-190549]
- monitor: Quote device names in chain declarations, too (Phil Sutter) [RHEL-190549]
- mnl: continue on ENOBUFS errors when processing batch (Phil Sutter) [RHEL-190549]
- tests: monitor: Fix for flag arrays in JSON output (Phil Sutter) [RHEL-190549]
- mnl: silence compiler warning (Phil Sutter) [RHEL-190549]
- fib: restore JSON output for relational expressions (Phil Sutter) [RHEL-190549]
- src: ensure chain policy evaluation when specified (Phil Sutter) [RHEL-190549]
- segtree: incorrect type when aggregating concatenated set ranges (Phil Sutter) [RHEL-190549]
- json: Do not reduce single-item arrays on output (Phil Sutter) [RHEL-190549]
- tests: py: Fix tests added for 'icmpv6 taddr' support (Phil Sutter) [RHEL-190549]
- tests: py: Drop stale entry from ip/snat.t.payload (Phil Sutter) [RHEL-190549]
- tests: py: Drop stale entries from ip6/{ct,meta}.t.json (Phil Sutter) [RHEL-190549]
- tests: py: Drop stale entry from ip/snat.t.json (Phil Sutter) [RHEL-190549]
- tests: py: Drop duplicate test from inet/vxlan.t (Phil Sutter) [RHEL-190549]
- tests: py: Drop stale entry from inet/tcp.t.json (Phil Sutter) [RHEL-190549]
- tests: py: Drop duplicate test from inet/gretap.t (Phil Sutter) [RHEL-190549]
- tests: py: Drop duplicate test from inet/gre.t (Phil Sutter) [RHEL-190549]
- tests: py: Drop duplicate test from inet/geneve.t (Phil Sutter) [RHEL-190549]
- tests: py: Drop stale entries since redundant test case removal (Phil Sutter) [RHEL-190549]
- src: netlink: netlink_delinearize_table() may return NULL (Phil Sutter) [RHEL-190549]
- doc: nft.8: Minor NAT STATEMENTS section review (Phil Sutter) [RHEL-190549]
- mnl: Call mnl_attr_nest_end() just once (Phil Sutter) [RHEL-190549]
- evaluate: validate set expression type before accessing flags (Phil Sutter) [RHEL-190549]
- rule: print chain and flowtable devices in quotes (Phil Sutter) [RHEL-190549]
- tests: py: re-enables nft-test.py to load the local nftables.py (Phil Sutter) [RHEL-190549]
- fib: allow to use it in set statements (Phil Sutter) [RHEL-190549]
- fib: allow to check if route exists in maps (Phil Sutter) [RHEL-190549]
- tests: shell: Fix ifname_based_hooks feature check (Phil Sutter) [RHEL-190549]
- json: reject too long interface names (Phil Sutter) [RHEL-190549]
- tests/py: clean up set backend support fallout (Phil Sutter) [RHEL-190549]
- cache: assert name is non-nul when looking up (Phil Sutter) [RHEL-190549]
- parser_bison: only reset by name is supported by now (Phil Sutter) [RHEL-190549]
- rule: skip fuzzy lookup if object name is not available (Phil Sutter) [RHEL-190549]
- parser_bison: allow delete command with map via handle (Phil Sutter) [RHEL-190549]
- debug: include kernel set information on cache fill (Phil Sutter) [RHEL-190549]
- tests/py: prepare for set debug change (Phil Sutter) [RHEL-190549]
- src: BASECHAIN flag no longer implies presence of priority expression (Phil Sutter) [RHEL-190549]
- netlink: Avoid crash upon missing NFTNL_OBJ_CT_TIMEOUT_ARRAY attribute (Phil Sutter) [RHEL-190549]
- tests: py: Properly fix JSON equivalents for netdev/reject.t (Phil Sutter) [RHEL-190549]
- tests: shell: Adjust to ifname-based hooks (Phil Sutter) [RHEL-190549]
- tests: shell: combine dormant flag with netdevice removal (Phil Sutter) [RHEL-190549]
- tests: monitor: Fix for single flag array avoidance (Phil Sutter) [RHEL-190549]
- netlink: Do not allocate a bogus flowtable priority expr (Phil Sutter) [RHEL-190549]
- netlink: Fix for potential crash parsing a flowtable (Phil Sutter) [RHEL-190549]
- json: work around fuzzer-induced assert crashes (Phil Sutter) [RHEL-190549]
- json: prevent null deref if chain->policy is not set (Phil Sutter) [RHEL-190549]
- tests: py: fix json single-flag output for fib & synproxy (Phil Sutter) [RHEL-190549]
- tests: shell: check for features not available in 5.4 (Phil Sutter) [RHEL-190549]
- netlink: Avoid potential NULL-ptr deref parsing set elem expressions (Phil Sutter) [RHEL-190549]
- netlink: Catch unknown types when deserializing objects (Phil Sutter) [RHEL-190549]
- json: Introduce json_add_array_new() (Phil Sutter) [RHEL-190549]
- json: Fix for memleak in __binop_expr_json (Phil Sutter) [RHEL-190549]
- json: Accept more than two operands in binary expressions (Phil Sutter) [RHEL-190549]
- json: Print single fib flag as non-array (Phil Sutter) [RHEL-190549]
- tests: shell: Add test case for JSON 'flags' arrays (Phil Sutter) [RHEL-190549]
- json: Print single set flag as non-array (Phil Sutter) [RHEL-190549]
- json: Print single synproxy flags as non-array (Phil Sutter) [RHEL-190549]
- parser_json: Introduce parse_flags_array() (Phil Sutter) [RHEL-190549]
- doc: Fix typo in nat statement 'prefix' description (Phil Sutter) [RHEL-190549]
- netlink: bogus concatenated set ranges with netlink message overrun (Phil Sutter) [RHEL-190549]
- parser_bison: add selector_expr rule to restrict typeof_expr (Phil Sutter) [RHEL-190549]
- optimize: invalidate merge in case of duplicated key in set/map (Phil Sutter) [RHEL-190549]
- evaluate: bail out if ct saddr/daddr dependency cannot be inserted (Phil Sutter) [RHEL-190549]
- parser_json: bail out on malformed statement in set (Phil Sutter) [RHEL-190549]
- parser_json: reject empty jump/goto chain (Phil Sutter) [RHEL-190549]
- parser_json: allow statement stateful statement only in set elements (Phil Sutter) [RHEL-190549]
- cache: prevent possible crash rule filter is NULL (Phil Sutter) [RHEL-190549]
- optimize: expand expression list when merging into concatenation (Phil Sutter) [RHEL-190549]
- cache: don't crash when filter is NULL (Phil Sutter) [RHEL-190549]
- evaluate: only allow stateful statements in set and map definitions (Phil Sutter) [RHEL-190549]
- evaluate: compact STMT_F_STATEFUL checks (Phil Sutter) [RHEL-190549]
- json: don't BUG when asked to list synproxies (Phil Sutter) [RHEL-190549]
- optimize: incorrect comparison for reject statement (Phil Sutter) [RHEL-190549]
- optimize: compact bitmask matching in set/map (Phil Sutter) [RHEL-190549]
- tests: shell: missing ct count elements in new set_stmt test (Phil Sutter) [RHEL-190549]
- evaluate: don't update cache for anonymous chains (Phil Sutter) [RHEL-190549]
- json: make sure timeout list is initialised (Phil Sutter) [RHEL-190549]
- parser_bison: consolidate connlimit grammar rule for set elements (Phil Sutter) [RHEL-190549]
- parser_bison: consolidate last grammar rule for set elements (Phil Sutter) [RHEL-190549]
- parser_bison: consolidate quota grammar rule for set elements (Phil Sutter) [RHEL-190549]
- parser_bison: consolidate limit grammar rule for set elements (Phil Sutter) [RHEL-190549]
- parser_bison: consolidate counter grammar rule for set elements (Phil Sutter) [RHEL-190549]
- tests: shell: extend coverage for set element statements (Phil Sutter) [RHEL-190549]
- evaluate: fix assertion failure with malformed map definitions (Phil Sutter) [RHEL-190549]
- evaluate: don't allow nat map with specified protocol (Phil Sutter) [RHEL-190549]
- parser_bison: reject non-serializeable typeof expressions (Phil Sutter) [RHEL-190549]
- netlink: fix stack buffer overrun when emitting ranged expressions (Phil Sutter) [RHEL-190549]
- src: print set element with multi-word description in single one line (Phil Sutter) [RHEL-190549]
- tests: shell: detach synproxy test (Phil Sutter) [RHEL-190549]
- src: do not merge a set with a erroneous one (Phil Sutter) [RHEL-190549]
- segtree: incomplete output in get element command with maps (Phil Sutter) [RHEL-190549]
- evaluate: release existing datatype when evaluating unary expression (Phil Sutter) [RHEL-190549]
- segtree: fix string data initialisation (Phil Sutter) [RHEL-190549]
- payload: honor inner payload description in payload_expr_cmp() (Phil Sutter) [RHEL-190549]
- payload: return early if dependency is not a payload expression (Phil Sutter) [RHEL-190549]
- evaluate: optimize zero length range (Phil Sutter) [RHEL-190549]
- fib: Change data type of fib oifname to "ifname" (Phil Sutter) [RHEL-190549]
- evaluate: auto-merge is only available for singleton interval sets (Phil Sutter) [RHEL-190549]
- parser_bison: compact and simplify list and reset syntax (Phil Sutter) [RHEL-190549]
- parser_bison: turn redundant ip option type field match into boolean (Phil Sutter) [RHEL-190549]
- datatype: clamp boolean value to 0 and 1 (Phil Sutter) [RHEL-190549]
- tests: shell: delete netdev chain after test (Phil Sutter) [RHEL-190549]
- ipopt: use ipv4 address datatype for address field in ip options (Phil Sutter) [RHEL-190549]
- netlink_delinarize: fix bogus munging of mask value (Phil Sutter) [RHEL-190549]
- evaluate: remove variable shadowing (Phil Sutter) [RHEL-190549]
- intervals: do not merge intervals with different timeout (Phil Sutter) [RHEL-190549]
- src: add EXPR_RANGE_VALUE expression and use it (Phil Sutter) [RHEL-190549]
- intervals: add helper function to set previous element (Phil Sutter) [RHEL-190549]
- parser_bison: fix UaF when reporting table parse error (Phil Sutter) [RHEL-190549]
- intervals: set internal element location with the deletion trigger (Phil Sutter) [RHEL-190549]
- optimize: compare expression length (Phil Sutter) [RHEL-190549]
- tests: py: Fix for storing payload into missing file (Phil Sutter) [RHEL-190549]
- json: Support typeof in set and map types (Phil Sutter) [RHEL-190549]
- json: collapse set element commands from parser (Phil Sutter) [RHEL-190549]
- doc: extend description of fib expression (Phil Sutter) [RHEL-190549]
- tests: monitor: fix up test case breakage (Phil Sutter) [RHEL-190549]
- src: fix extended netlink error reporting with large set elements (Phil Sutter) [RHEL-190549]
- mnl: rename to mnl_seqnum_alloc() to mnl_seqnum_inc() (Phil Sutter) [RHEL-190549]
- mnl: update cmd_add_loc() to take struct nlmsghdr (Phil Sutter) [RHEL-190549]
- rule: netlink attribute offset is uint32_t for struct nlerr_loc (Phil Sutter) [RHEL-190549]
- src: collapse set element commands from parser (Phil Sutter) [RHEL-190549]
- libnftables-json: fix raw payload expression documentation (Phil Sutter) [RHEL-190549]
- cache: initialize filter when fetching implicit chains (Phil Sutter) [RHEL-190549]
- tests: py: fix up udp csum fixup output (Phil Sutter) [RHEL-190549]
- proto: use NFT_PAYLOAD_L4CSUM_PSEUDOHDR flag to mangle UDP checksum (Phil Sutter) [RHEL-190549]
- tests: shell: stabilize packetpath/payload (Phil Sutter) [RHEL-190549]
- libnftables: Zero ctx->vars after freeing it (Phil Sutter) [RHEL-190549]
- cache: position does not require full cache (Phil Sutter) [RHEL-190549]
- cache: relax requirement for replace rule command (Phil Sutter) [RHEL-190549]
- cache: remove full cache requirement when echo flag is set on (Phil Sutter) [RHEL-190549]
- cache: assert filter when calling nft_cache_evaluate() (Phil Sutter) [RHEL-190549]
- cache: consolidate reset command (Phil Sutter) [RHEL-190549]
- cache: add filtering support for objects (Phil Sutter) [RHEL-190549]
- cache: only dump rules for the given table (Phil Sutter) [RHEL-190549]
- cache: accumulate flags in batch (Phil Sutter) [RHEL-190549]
- cache: reset filter for each command (Phil Sutter) [RHEL-190549]
- parser_json: fix several expression memleaks from error path (Phil Sutter) [RHEL-190549]
- parser_json: release buffer returned by json_dumps (Phil Sutter) [RHEL-190549]
- json: Support maps with concatenated data (Phil Sutter) [RHEL-190549]
- parser_json: fix crash in json_parse_set_stmt_list (Phil Sutter) [RHEL-190549]
- parser_bison: allow 0 burst in limit rate byte mode (Phil Sutter) [RHEL-190549]
- datatype: improve error reporting when time unit is not correct (Phil Sutter) [RHEL-190549]
- cache: rule by index requires full cache (Phil Sutter) [RHEL-190549]
- datatype: reject rate in quota statement (Phil Sutter) [RHEL-190549]
- optimize: skip variables in nat statements (Phil Sutter) [RHEL-190549]
- parser_json: use stdin buffer if available (Phil Sutter) [RHEL-190549]
- libnftables: skip useable checks for /dev/stdin (Phil Sutter) [RHEL-190549]
- optimize: clone counter before insertion into set element (Phil Sutter) [RHEL-190549]
- segtree: set on EXPR_F_KERNEL flag for catchall elements in the cache (Phil Sutter) [RHEL-190549]
- evaluate: set on expr->len for catchall set elements (Phil Sutter) [RHEL-190549]
- parser_bison: recursive table declaration in deprecated meter statement (Phil Sutter) [RHEL-190549]
- intervals: fix element deletions with maps (Phil Sutter) [RHEL-190549]
- src: add string preprocessor and use it for log prefix string (Phil Sutter) [RHEL-190549]
- tests: shell: skip ip option tests if kernel does not support it (Phil Sutter) [RHEL-190549]
- cmd: skip variable set elements when collapsing commands (Phil Sutter) [RHEL-190549]
- cmd: provide better hint if chain is already declared with different type/hook/priority (Phil Sutter) [RHEL-190549]
- monitor: too large shift exponent displaying payload expression (Phil Sutter) [RHEL-190549]
- scanner: inet_pton() allows for broader IPv4-Mapped IPv6 addresses (Phil Sutter) [RHEL-190549]
- evaluate: Fix incorrect checking the `base` variable in case of IPV6 (Phil Sutter) [RHEL-190549]
- evaluate: bogus protocol conflicts in vlan with implicit dependencies (Phil Sutter) [RHEL-190549]
- cache: check for NFT_CACHE_REFRESH in current requested cache too (Phil Sutter) [RHEL-190549]
- doc: nft.8: Fix markup in ct expectation synopsis (Phil Sutter) [RHEL-190549]
- mergesort: Avoid accidental set element reordering (Phil Sutter) [RHEL-190549]
- doc: nft.8: Two minor synopsis fixups (Phil Sutter) [RHEL-190549]
- tests: shell: check for reset tcp options support (Phil Sutter) [RHEL-190549]
- tests: shell: payload matching requires egress support (Phil Sutter) [RHEL-190549]
- tests: py: complete icmp and icmpv6 update (Phil Sutter) [RHEL-190549]
- src: disentangle ICMP code types (Phil Sutter) [RHEL-190549]
- evaluate: display "Range negative size" error (Phil Sutter) [RHEL-190549]
- netlink_delinearize: restore binop syntax when listing ruleset for flags (Phil Sutter) [RHEL-190549]
- doc: libnftables-json: Drop invalid ops from match expression (Phil Sutter) [RHEL-190549]
- parser: json: Support for synproxy objects (Phil Sutter) [RHEL-190549]
- tests: py: add payload merging test cases (Phil Sutter) [RHEL-190549]
- nftables: do mot merge payloads on negation (Phil Sutter) [RHEL-190549]
- rule: fix ASAN errors in chain priority to textual names (Phil Sutter) [RHEL-190549]
- parser: compact type/typeof set rules (Phil Sutter) [RHEL-190549]
- parser: compact interval typeof rules (Phil Sutter) [RHEL-190549]
- src: improve error reporting for destroy command (Phil Sutter) [RHEL-190549]
- tests: shell: permit use of host-endian constant values in set lookup keys (Phil Sutter) [RHEL-190549]
- evaluate: permit use of host-endian constant values in set lookup keys (Phil Sutter) [RHEL-190549]
- expression: missing line in describe command with invalid expression (Phil Sutter) [RHEL-190549]
- netlink_delinearize: move concat and value postprocessing to helpers (Phil Sutter) [RHEL-190549]
- evaluate: skip byteorder conversion for selector smaller than 2 bytes (Phil Sutter) [RHEL-190549]
- cache: Optimize caching for 'list tables' command (Phil Sutter) [RHEL-190549]
- evaluate: fix check for unknown in cmd_op_to_name (Phil Sutter) [RHEL-190549]
- evaluate: don't assert on net/transport header conflict (Phil Sutter) [RHEL-190549]
- json: Support sets' auto-merge option (Phil Sutter) [RHEL-190549]
- rule: fix sym refcount assertion (Phil Sutter) [RHEL-190549]
- evaluate: error out when store needs more than one 128bit register of align fixup (Phil Sutter) [RHEL-190549]
- evaluate: do not fetch next expression on runaway number of concatenation components (Phil Sutter) [RHEL-190549]
- evaluate: skip anonymous set optimization for concatenations (Phil Sutter) [RHEL-190549]
- evaluate: add missing range checks for dup,fwd and payload statements (Phil Sutter) [RHEL-190549]
- doc: incorrect datatype description for icmpv6_type and icmpvx_code (Phil Sutter) [RHEL-190549]
- tests: shell: prefer project nft to system-wide nft (Phil Sutter) [RHEL-190549]
- parser_bison: ensure all timeout policy names are released (Phil Sutter) [RHEL-190549]
- netlink: fix stack overflow due to erroneous rounding (Phil Sutter) [RHEL-190549]
- parser_bison: error out on duplicated type/typeof/element keywords (Phil Sutter) [RHEL-190549]
- tests: shell: add test to cover payload transport match and mangle (Phil Sutter) [RHEL-190549]
- evaluate: fix stack overflow with huge priority string (Phil Sutter) [RHEL-190549]
- src: reject large raw payload and concat expressions (Phil Sutter) [RHEL-190549]
- evaluate: exthdr: statement arg must be not be a range (Phil Sutter) [RHEL-190549]
- meta: fix tc classid parsing out-of-bounds access (Phil Sutter) [RHEL-190549]
- parser_bison: close chain scope before chain release (Phil Sutter) [RHEL-190549]
- evaluate: fix bogus assertion failure with boolean datatype (Phil Sutter) [RHEL-190549]
- parser_bison: fix objref statement corruption (Phil Sutter) [RHEL-190549]
- tests: py: missing json output in meta.t with vlan mapping (Phil Sutter) [RHEL-190549]
- evaluate: reset statement length context before evaluating statement (Phil Sutter) [RHEL-190549]
- parser: tcpopt: fix tcp option parsing with NUM + length field (Phil Sutter) [RHEL-190549]
- evaluate: reject set definition with no key (Phil Sutter) [RHEL-190549]
- monitor: add support for concatenated set ranges (Phil Sutter) [RHEL-190549]
- evaluate: disable meta set with ranges (Phil Sutter) [RHEL-190549]
- evaluate: prevent assert when evaluating very large shift values (Phil Sutter) [RHEL-190549]
- evaluate: reject sets with no key (Phil Sutter) [RHEL-190549]
- evaluate: clone unary expression datatype to deal with dynamic datatype (Phil Sutter) [RHEL-190549]
- tests: shell: split nat inet tests (Phil Sutter) [RHEL-190549]
- evaluate: bogus error when adding devices to flowtable (Phil Sutter) [RHEL-190549]
- tests: shell: flush connlimit sets (Phil Sutter) [RHEL-190549]
- tests: shell: adjust add-after-delete flowtable for older kernels (Phil Sutter) [RHEL-190549]
- evaluate: fix rule replacement with anon sets (Phil Sutter) [RHEL-190549]
- tests: shell: skip if kernel does not support flowtable counter (Phil Sutter) [RHEL-190549]
- tests: shell: restore pipapo and chain binding coverage in standalone 30s-stress (Phil Sutter) [RHEL-190549]
- json: fix use after free in table_flags_json() (Phil Sutter) [RHEL-190549]
- src: expand create commands (Phil Sutter) [RHEL-190549]
- tests: shell: split set NAT interval test (Phil Sutter) [RHEL-190549]
- tests: shell: split merge nat optimization in two tests (Phil Sutter) [RHEL-190549]
- netlink: fix buffer size for user data in netlink_delinearize_chain() (Phil Sutter) [RHEL-190549]
- src: remove xfree() and use plain free() (Phil Sutter) [RHEL-190549]
- src: add free_const() and use it instead of xfree() (Phil Sutter) [RHEL-190549]
- evaluate: place byteorder conversion before rshift in payload expressions (Phil Sutter) [RHEL-190549]
- evaluate: reset statement length context only for set mappings (Phil Sutter) [RHEL-190549]
- meta: fix hour decoding when timezone offset is negative (Phil Sutter) [RHEL-190549]
- tproxy: Drop artificial port printing restriction (Phil Sutter) [RHEL-190549]
- tests/shell: fix mount command in "test-wrapper.sh" (Phil Sutter) [RHEL-190549]
- parser_bison: fix length check for ifname in ifname_expr_alloc() (Phil Sutter) [RHEL-190549]
- tests/shell: cover long interface name in "0042chain_variable_0" test (Phil Sutter) [RHEL-190549]
- tests/shell: add missing "elem_opts_compat_0.nodump" file (Phil Sutter) [RHEL-190549]
- parser_bison: Fix for broken compatibility with older dumps (Phil Sutter) [RHEL-190549]

* Wed Mar 18 2026 Phil Sutter <psutter@redhat.com> [1.0.9-7.el9]
- src: fix reset element support for interval set type (Phil Sutter) [RHEL-153461]
- src: netlink: fix crash when ops doesn't support udata (Phil Sutter) [RHEL-153461]

* Wed Nov 26 2025 Phil Sutter <psutter@redhat.com> [1.0.9-6.el9]
- Revert doc/ part of "exthdr: add boolean DCCP option matching" (Phil Sutter) [RHEL-126817]
- Revert doc/ part of "meta: introduce meta broute support" (Phil Sutter) [RHEL-126817]
- Revert doc/ part of "src: add tcp option reset support" (Phil Sutter) [RHEL-126817]
- spec: Update expected test suite results (Phil Sutter) [RHEL-126817]

* Thu Oct 16 2025 Phil Sutter <psutter@redhat.com> [1.0.9-5.el9]
- tests: py: missing json output in never merge across non-expression statements (Phil Sutter) [RHEL-114095]
- tests: py: add missing json.output data (Phil Sutter) [RHEL-114095]
- tests: py: remove huge-limit test cases (Phil Sutter) [RHEL-114095]
- datatype: rt_symbol_table_init() to search for iproute2 configs (Phil Sutter) [RHEL-114095]
- tests: shell: connect chains to hook point (Phil Sutter) [RHEL-114095]
- tests: shell: Fix sets/reset_command_0 for current kernels (Phil Sutter) [RHEL-114095]

* Wed Apr 23 2025 Phil Sutter <psutter@redhat.com> [1.0.9-4.el9]
- parser_json: fix handle memleak from error path (Phil Sutter) [RHEL-88181]
- json: deal appropriately with multidevice in chain (Phil Sutter) [RHEL-88181]

* Tue Jul 02 2024 Phil Sutter <psutter@redhat.com> [1.0.9-3.el9]
- cache: Always set NFT_CACHE_TERSE for list cmd with --terse (Phil Sutter) [RHEL-45633]

* Fri Jun 14 2024 Phil Sutter <psutter@redhat.com> [1.0.9-2.el9]
- Add support for table's persist flag (Phil Sutter) [RHEL-32122]

* Fri Oct 27 2023 Phil Sutter <psutter@redhat.com> [1.0.9-1.el9]
- spec: Utilize pyproject-rpm-macros for the python sub-package (Phil Sutter) [RHEL-14191]
- Rebase onto version 1.0.9 (Phil Sutter) [RHEL-14191]

* Thu Sep 21 2023 Phil Sutter <psutter@redhat.com> [1.0.4-11.el9]
- rule: check address family in set collapse (Phil Sutter) [RHEL-5908]
- spec: Rename variables to avoid a clash (Phil Sutter) [INTERNAL]

* Tue Feb 21 2023 Phil Sutter <psutter@redhat.com> [1.0.4-10.el9]
- netlink_delinearize: Sanitize concat data element decoding (Phil Sutter) [2160049]
- optimize: Clarify chain_optimize() array allocations (Phil Sutter) [2160049]
- optimize: Do not return garbage from stack (Phil Sutter) [2160049]
- netlink: Fix for potential NULL-pointer deref (Phil Sutter) [2160049]
- meta: parse_iso_date() returns boolean (Phil Sutter) [2160049]
- mnl: dump_nf_hooks() leaks memory in error path (Phil Sutter) [2160049]
- owner: Fix potential array out of bounds access (Phil Sutter) [2160049]

* Fri Feb 17 2023 Phil Sutter <psutter@redhat.com> [1.0.4-9.el9]
- tests: add a test case for map update from packet path with concat (Phil Sutter) [2094894]
- netlink_linearize: fix timeout with map updates (Phil Sutter) [2094894]
- netlink_delinearize: fix decoding of concat data element (Phil Sutter) [2094894]

* Thu Feb 09 2023 Phil Sutter <psutter@redhat.com> [1.0.4-8.el9]
- monitor: Sanitize startup race condition (Phil Sutter) [2130721]
- evaluate: set eval ctx for add/update statements with integer constants (Phil Sutter) [2094894]
- src: allow anon set concatenation with ether and vlan (Phil Sutter) [2094887]
- evaluate: search stacked header list for matching payload dep (Phil Sutter) [2094887]
- netlink_delinearize: also postprocess OP_AND in set element context (Phil Sutter) [2094887]
- tests: add a test case for ether and vlan listing (Phil Sutter) [2094887]
- debug: dump the l2 protocol stack (Phil Sutter) [2094887]
- proto: track full stack of seen l2 protocols, not just cumulative offset (Phil Sutter) [2094887]
- netlink_delinearize: postprocess binary ands in concatenations (Phil Sutter) [2094887]
- netlink_delinearize: allow postprocessing on concatenated elements (Phil Sutter) [2094887]
- intervals: check for EXPR_F_REMOVE in case of element mismatch (Phil Sutter) [2115627]
- intervals: fix crash when trying to remove element in empty set (Phil Sutter) [2115627]
- scanner: don't pop active flex scanner scope (Phil Sutter) [2113874]
- parser: add missing synproxy scope closure (Phil Sutter) [2113874]
- tests/py: Add a test for failing ipsec after counter (Phil Sutter) [2113874]
- doc: Document limitations of ipsec expression with xfrm_interface (Phil Sutter) [1806431]

* Tue Jan 31 2023 Phil Sutter <psutter@redhat.com> [1.0.4-7.el9]
- One more attempt at fixing expected error records (Phil Sutter) [1973687]

* Tue Jan 31 2023 Phil Sutter <psutter@redhat.com> [1.0.4-6.el9]
- Realy fix expected error records (Phil Sutter) [1973687]

* Fri Jan 27 2023 Phil Sutter <psutter@redhat.com> [1.0.4-5.el9]
- Fix expected error records (Phil Sutter) [1973687]

* Fri Jan 20 2023 Phil Sutter <psutter@redhat.com> [1.0.4-4.el9]
- Add expected error records for testsuite runs (Phil Sutter) [1973687]

* Fri Nov 25 2022 Phil Sutter <psutter@redhat.com> [1.0.4-3.el9]
- Prevent port-shadow attacks in sample nat config (Phil Sutter) [2061940]

* Fri Jun 24 2022 Phil Sutter <psutter@redhat.com> [1.0.4-2.el9]
- intervals: Do not sort cached set elements over and over again (Phil Sutter) [1917398]
- intervals: do not empty cache for maps (Phil Sutter) [1917398]
- intervals: do not report exact overlaps for new elements (Phil Sutter) [1917398]
- rule: collapse set element commands (Phil Sutter) [1917398]
- tests: shell: runtime set element automerge (Phil Sutter) [1917398]

* Thu Jun 09 2022 Phil Sutter <psutter@redhat.com> - 1:1.0.4-1
- Review package dependencies
- new version 1.0.4

* Tue Mar 01 2022 Phil Sutter <psutter@redhat.com> - 1:0.9.8-13
- tests: extend dtype test case to cover expression with integer type
- evaluate: set evaluation context for set elements

* Fri Jan 14 2022 Phil Sutter <psutter@redhat.com> - 1:0.9.8-12
- evaluate: pick data element byte order, not dtype one

* Wed Dec 08 2021 Phil Sutter <psutter@redhat.com> - 1:0.9.8-11
- tests: py: add dnat to port without defining destination address
- evaluate: fix inet nat with no layer 3 info
- include: missing sctp_chunk.h in Makefile.am
- exthdr: Implement SCTP Chunk matching
- scanner: sctp: Move to own scope
- scanner: introduce start condition stack
- json: Simplify non-tcpopt exthdr printing a bit

* Wed Dec 08 2021 Phil Sutter <psutter@redhat.com> - 1:0.9.8-10
- tests: shell: better parameters for the interval stack overflow test
- tests: shell: $NFT needs to be invoked unquoted

* Thu Nov 11 2021 Phil Sutter <psutter@redhat.com> - 1:0.9.8-9
- doc: nft.8: Extend monitor description by trace

* Fri Nov 05 2021 Phil Sutter <psutter@redhat.com> - 1:0.9.8-8
- tests: cover baecd1cf2685 ("segtree: Fix segfault when restoring a huge interval set")
- segtree: Fix segfault when restoring a huge interval set

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1:0.9.8-7
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Jun 18 2021 Phil Sutter <psutter@redhat.com> - 1:0.9.8-6
- json: init parser state for every new buffer/file

* Tue Jun 15 2021 Phil Sutter <psutter@redhat.com> - 1:0.9.8-5
- src: add xzalloc_array() and use it to allocate the expression hashtable

* Mon Jun 14 2021 Phil Sutter <psutter@redhat.com> - 1:0.9.8-4
- Install an improved sample config
- Fix permissions of osf-related configs
- rule: Fix for potential off-by-one in cmd_add_loc()
- netlink_delinearize: Fix suspicious calloc() call
- netlink: Avoid memleak in error path of netlink_delinearize_obj()
- netlink: Avoid memleak in error path of netlink_delinearize_table()
- netlink: Avoid memleak in error path of netlink_delinearize_chain()
- netlink: Avoid memleak in error path of netlink_delinearize_set()
- json: Drop pointless assignment in exthdr_expr_json()
- evaluate: Mark fall through case in str2hooknum()
- parser_json: Fix for memleak in tcp option error path
- parser_bison: Fix for implicit declaration of isalnum
- main: fix nft --help output fallout from 719e4427
- tests: add icmp/6 test where dependency should be left alone
- payload: check icmp dependency before removing previous icmp expression

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1:0.9.8-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Kevin Fenzi <kevin@scrye.com> - 0.9.8-1
- Update to 0.9.8. Fixes rhbz#1916940

* Sat Oct 31 2020 Kevin Fenzi <kevin@scrye.com> - 0.9.7-1
- Update to 0.9.7. Fixes bug #1891769

* Thu Oct 29 2020 Stephen Gallagher <sgallagh@redhat.com> - 1:0.9.6-2
- Drop upstreamed patch

* Sat Sep 05 2020 Neal Gompa <ngompa13@gmail.com> - 1:0.9.6-1
- Update to 0.9.6 (RH#1846663)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 1:0.9.3-5
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:0.9.3-4
- Rebuilt for Python 3.9

* Fri May 15 2020 Richard Shaw <hobbes1069@gmail.com> - 1:0.9.3-3
- Add patch for json performance with ipsets, fixes RHBZ#1834853.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Phil Sutter <psutter@redhat.com> - 1:0.9.3-1
- Update to 0.9.3. Fixes bug #1778959

* Tue Oct 01 2019 Phil Sutter <psutter@redhat.com> - 1:0.9.2-3
- Drop unneeded docbook2X build dependency
- Add python3-nftables sub-package

* Fri Aug 23 2019 Kevin Fenzi <kevin@scrye.com> - 0.9.2-2
- Move libnftables section 3 man page to devel package.

* Fri Aug 23 2019 Kevin Fenzi <kevin@scrye.com> - 0.9.2-1
- Update to 0.9.2. Fixes bug #1743223

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Kevin Fenzi <kevin@scrye.com> - 0.9.1-2
- Add some filters to nftables.conf

* Tue Jun 25 2019 Kevin Fenzi <kevin@scrye.com> - 0.9.1-1
- Update to 0.9.1. Fixes bug #1723515

* Mon Jun 17 2019 Kevin Fenzi <kevin@scrye.com> - 0.9.0-7
- Rebuild for new libnftnl.

* Sat Mar 16 2019 Kevin Fenzi <kevin@scrye.com> - 1:0.9.0-6
- Fix permissions. Bug #1685242

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:0.9.0-5
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 04 2018 Kevin Fenzi <kevin@scrye.com> - 0.9.0-3
- Fix config file to have correct include names. Fixes bug #1642103

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Kevin Fenzi <kevin@scrye.com> - 0.9.0-1
- Update to 0.9.0. Fixes bug #1589404

* Fri May 11 2018 Kevin Fenzi <kevin@scrye.com> - 0.8.5-1
- Update to 0.8.5. Fixes bug #1576802

* Sun May 06 2018 Kevin Fenzi <kevin@scrye.com> - 0.8.4-2
- Fix devel package to require the Epoch too.
- Fix libraries split

* Fri May 04 2018 Kevin Fenzi <kevin@scrye.com> - 0.8.4-1
- Update to 0.8.4. Fixes bug #1574096

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
