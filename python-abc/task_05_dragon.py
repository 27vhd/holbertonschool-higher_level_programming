#!/usr/bin/env python3
"""Module for SwimMixin, FlyMixin, and Dragon classes."""


class SwimMixin:
    """Mixin that provides swimming ability."""

    def swim(self):
        """Prints swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying ability."""

    def fly(self):
        """Prints flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A Dragon class that can swim and fly."""

    def roar(self):
        """Prints roaring message."""
        print("The dragon roars!")
