# -*- coding: utf-8
"""Test cases"""

from collective.monkeypatcher.interfaces import IMonkeyPatchEvent

import common
import dummypatch


class TestMonkeyPatcher(common.MonkeypatcherTestCase):
    """We test all in this class"""

    def test_patchedClass(self):
        """We have our Dummy class's someMethod patched"""

        # Testing applyed patch
        ob = dummypatch.Dummy()
        self.failUnlessEqual(ob.someMethod(), "patched")

        # Testing docstring preservation
        docstring = dummypatch.Dummy.someMethod.__doc__
        self.failUnlessEqual(docstring, "someMethod docstring")
        return

    def test_patchedFunction(self):
        """We have our someFunction patched"""

        # Testing applyed patch
        self.failUnlessEqual(dummypatch.someFunction(1), 2)

        # Testing docstring monkeypatch note
        docstring = dummypatch.someFunction.__doc__
        self.failUnless(docstring.startswith("someFunction docstring"))
        self.failUnless(docstring.endswith(
            "'collective.monkeypatcher.tests.dummypatch.patchedFunction'"))
        return

    def test_patchWithHandler(self):
        """Patch applied with personal handler"""

        ob = dummypatch.Foo()
        self.failUnlessEqual(ob.someFooMethod(), "patchedFooMethod result")
        return

    def test_patchWithBuiltin(self):
        """see https://github.com/plone/collective.monkeypatcher/pull/2
        """
        ob = dummypatch.Foo()
        self.failUnlessEqual(ob.config, (1, 2))
        return

    def test_monkeyPatchEvent(self):
        """Do we notify ?"""

        events = dummypatch.all_patches
        expected_keys = set(
            ('description', 'original', 'replacement', 'zcml_info'))
        self.failUnlessEqual(len(events), 4)
        for event in events:

            # Interface conformance
            self.failUnless(IMonkeyPatchEvent.providedBy(event))

            # Checking available infos
            info_keys = set(event.patch_info.keys())
            self.failUnlessEqual(info_keys, expected_keys)
        return


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestMonkeyPatcher))
    return suite
