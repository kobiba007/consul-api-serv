bind_addr   = "{{ GetInterfaceIP `eth1` }}"
bootstrap_expect = 1
client_addr = "0.0.0.0"
data_dir    = "/var/lib/consul"
server      = true
telemetry {
  disable_compat_1.9 = true
}
ui_config {
  enabled = true
}
