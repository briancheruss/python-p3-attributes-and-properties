#!/usr/bin/env python3

class Person:
    pass
    APPROVED_JOBS = [
        "Admin",
        "Customer Service",
        "Human Resources",
        "ITC",
        "Production",
        "Legal",
        "Finance",
        "Sales",
        "General Management",
        "Research & Development",
        "Marketing",
        "Purchasing"
    ]

    def __init__(self, name, job):
        self._name = None
        self._job = None
        self._set_name(name)
        self._set_job(job)

    def _get_name(self):
        return self._name

    def _set_name(self, value):
        if isinstance(value, str) and len(value) < 25:
            self._name = value.title()
        else:
            print("Name must be a string under 25 characters.")

    def _get_job(self):
        return self._job

    def _set_job(self, value):
        if value in self.APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in the list of approved jobs.")

    name = property(_get_name, _set_name)
    job = property(_get_job, _set_job)

