#
# Copyright (C) 2020  FreeIPA Contributors see COPYING for license
#
"""Fedora container paths
"""
import os

from ipaplatform.altlinux.paths import ALTLinuxPathNamespace


def data(path):
    return os.path.join("/data", path[1:])


class ALTLinuxContainerPathNamespace(ALTLinuxPathNamespace):
    VAR_LOG_HTTPD_DIR = data(ALTLinuxPathNamespace.VAR_LOG_HTTPD_DIR)
    VAR_LOG_HTTPD_ERROR = data(ALTLinuxPathNamespace.VAR_LOG_HTTPD_ERROR)
    NAMED_MANAGED_KEYS_DIR = data(ALTLinuxPathNamespace.NAMED_MANAGED_KEYS_DIR)
    NAMED_PID = data(ALTLinuxPathNamespace.NAMED_PID)
    BIND_LDAP_DNS_IPA_WORKDIR = data(ALTLinuxPathNamespace.BIND_LDAP_DNS_IPA_WORKDIR)
    BIND_LDAP_DNS_ZONE_WORKDIR = data(ALTLinuxPathNamespace.BIND_LDAP_DNS_ZONE_WORKDIR)
    VAR_OPENDNSSEC_DIR = data(ALTLinuxPathNamespace.VAR_OPENDNSSEC_DIR)
    OPENDNSSEC_KASP_DB = data(ALTLinuxPathNamespace.OPENDNSSEC_KASP_DB)
    IPA_ODS_EXPORTER_CCACHE = data(ALTLinuxPathNamespace.IPA_ODS_EXPORTER_CCACHE)
    OPENSSL_DIR = data(ALTLinuxPathNamespace.OPENSSL_DIR)
    OPENSSL_CERTS_DIR = data(ALTLinuxPathNamespace.OPENSSL_CERTS_DIR)
    OPENSSL_PRIVATE_DIR = data(ALTLinuxPathNamespace.OPENSSL_PRIVATE_DIR)
    VAR_KERBEROS_KRB5KDC_DIR = data(ALTLinuxPathNamespace.VAR_KERBEROS_KRB5KDC_DIR)
    VAR_KRB5KDC_K5_REALM = data(ALTLinuxPathNamespace.VAR_KRB5KDC_K5_REALM)
    CACERT_PEM = data(ALTLinuxPathNamespace.CACERT_PEM)
    KRB5KDC_KADM5_ACL = data(ALTLinuxPathNamespace.KRB5KDC_KADM5_ACL)
    KRB5KDC_KADM5_KEYTAB = data(ALTLinuxPathNamespace.KRB5KDC_KADM5_KEYTAB)
    KDC_CERT = data(ALTLinuxPathNamespace.KDC_CERT)
    KDC_KEY = data(ALTLinuxPathNamespace.KDC_KEY)

    KRB5_CONF = data(ALTLinuxPathNamespace.KRB5_CONF)
    KRB5_KEYTAB = data(ALTLinuxPathNamespace.KRB5_KEYTAB)
    KRB5KDC_KDC_CONF = data(ALTLinuxPathNamespace.KRB5KDC_KDC_CONF)
    NAMED_KEYTAB = data(ALTLinuxPathNamespace.NAMED_KEYTAB)
    NAMED_CUSTOM_CONF = data(ALTLinuxPathNamespace.NAMED_CUSTOM_CONF)
    NAMED_CUSTOM_OPTIONS_CONF = data(
        ALTLinuxPathNamespace.NAMED_CUSTOM_OPTIONS_CONF
    )
    NAMED_LOGGING_OPTIONS_CONF = data(
        ALTLinuxPathNamespace.NAMED_LOGGING_OPTIONS_CONF
    )
    NSSWITCH_CONF = data(ALTLinuxPathNamespace.NSSWITCH_CONF)
    PKI_CONFIGURATION = data(ALTLinuxPathNamespace.PKI_CONFIGURATION)
    SAMBA_DIR = data(ALTLinuxPathNamespace.SAMBA_DIR)
    HTTPD_IPA_WSGI_MODULES_CONF = None
    HTTPD_PASSWD_FILE_FMT = data(ALTLinuxPathNamespace.HTTPD_PASSWD_FILE_FMT)

    # In some contexts, filesystem mounts may be owned by unmapped users
    # (e.g. "emptyDir" mounts in Kubernetes / OpenShift when using user
    # namespaces).  This causes systemd-tmpfiles(8) to fail, as a
    # consequence of systemd's path processing routines which reject
    # this scenario.  Therefore we provide a way to substitute
    # systemd-tmpfiles with a "clone" program.
    #
    SYSTEMD_TMPFILES = os.environ.get(
        'IPA_TMPFILES_PROG', ALTLinuxPathNamespace.SYSTEMD_TMPFILES)


paths = ALTLinuxContainerPathNamespace()
