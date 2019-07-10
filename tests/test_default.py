def test_tlog_installed(host):
    tlog = host.package("tlog")
    assert tlog.is_installed


def test_sssd_snippet_config_file(host):
    f = host.file('/etc/sssd/conf.d/sssd-session-recording.conf')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o600


def test_tlog_config_file(host):
    f = host.file('/etc/tlog/tlog-rec-session.conf')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644
