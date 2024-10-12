#
# Copyright (C) 2024  FreeIPA Contributors see COPYING for license
#
"""ALT Linux container services
"""
from ipaplatform.altlinux import services as altlinux_services
altlinux_container_system_units = altlinux_services.altlinux_system_units.copy()


class ALTLinuxContainerService(altlinux_services.ALTLinuxService):
    system_units = altlinux_container_system_units


def altlinux_container_service_class_factory(name, api=None):
    return altlinux_services.altlinux_service_class_factory(name, api)


class ALTLinuxContainerServices(altlinux_services.ALTLinuxServices):
    def service_class_factory(self, name, api=None):
        return altlinux_container_service_class_factory(name, api)


# System may support more time&date services. FreeIPA supports ntpd only, other
# services will be disabled during IPA installation
# In ALT distribution openntpd service name equal ntp service name
timedate_services = altlinux_services.timedate_services

service = altlinux_container_service_class_factory
knownservices = ALTLinuxContainerServices()
