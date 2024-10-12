#
# Copyright (C) 2024  FreeIPA Contributors see COPYING for license
#
"""ALT Linux container constants
"""
from ipaplatform.altlinux.constants import ALTLinuxConstantsNamespace, User, Group


__all__ = ("constants", "User", "Group")


class ALTLinuxContainerConstantsNamespace(ALTLinuxConstantsNamespace):
    pass


constants = ALTLinuxContainerConstantsNamespace()
