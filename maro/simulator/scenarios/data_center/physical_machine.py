# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

from typing import List, Set


class PhysicalMachine:
    """Physical machine object.

    Args:
        id (int): PM id, from 0 to N. N means the amount of PM, which can be set in config.
        cap_cpu (int): The capacity of cores of the PM, which can be set in config.
        cap_mem (int): The capacity of memory of the PM, which can be set in config.
    """
    def __init__(self, id: int, cap_cpu: int, cap_mem: int):
        # Required parameters.
        self.id = id
        self.cap_cpu: int = cap_cpu
        self.cap_mem: int = cap_mem
        # PM resource.
        self._vm_set: Set(int) = set()
        self.req_cpu: int = 0
        self.req_mem: int = 0
        self._util_cpu: float = 0.0
        self._util_series: List[float] = []

    @property
    def vm_set(self) -> Set(int):
        return self._vm_set

    def add_vm(self, vm_id: int):
        self._vm_set.add(vm_id)

    def remove_vm(self, vm_id: int):
        self._vm_set.remove(vm_id)

    @property
    def util_cpu(self):
        # PM CPU utilization (%).
        return self._util_cpu

    def update_util(self, tick: int, util_cpu: float):
        if tick > len(self._util_series):
            raise Exception(f"The insert tick is invalid.")

        # Update CPU utilization.
        self._util_cpu = util_cpu

        # Update the util series.
        if tick == len(self._util_series):
            self._util_series.append(util_cpu)
        elif tick < len(self._util_series):
            self._util_series[tick] = util_cpu
