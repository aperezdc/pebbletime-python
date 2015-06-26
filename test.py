#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Adrian Perez <aperez@igalia.com>
#
# Distributed under terms of the MIT license.

import unittest


class TestLayoutInstantiation(unittest.TestCase):
    def test_valid_generic(self):
        from pebbletime import Layout
        ll = Layout("Test", tinyIcon = Layout.Icon.GENERIC)
        self.assertEqual("Test", ll.title)
        self.assertEqual(Layout.Type.GENERIC, ll.type)
        self.assertEqual(Layout.Icon.GENERIC, ll.tinyIcon)

    def test_valid_calendar_with_extra_fields(self):
        from pebbletime import Layout
        ll = Layout("Calendar", Layout.Type.CALENDAR,
                tinyIcon = Layout.Icon.REMINDER)
        self.assertEqual("Calendar", ll.title)
        self.assertEqual(Layout.Type.CALENDAR, ll.type)
        self.assertEqual(Layout.Icon.REMINDER, ll.tinyIcon)

    def test_valid_calendar(self):
        from pebbletime import Layout
        ll = Layout("Calendar", Layout.Type.CALENDAR)
        self.assertEqual("Calendar", ll.title)
        self.assertEqual(Layout.Type.CALENDAR, ll.type)

    def test_valid_reminder(self):
        from pebbletime import Layout
        ll = Layout("Remind", Layout.Type.REMINDER,
                tinyIcon = Layout.Icon.FLAG)
        self.assertEqual("Remind", ll.title)
        self.assertEqual(Layout.Type.REMINDER, ll.type)
        self.assertEqual(Layout.Icon.FLAG, ll.tinyIcon)

    def test_valid_notification(self):
        from pebbletime import Layout
        ll = Layout("Notif", Layout.Type.NOTIFICATION,
                tinyIcon = Layout.Icon.FLAG)
        self.assertEqual("Notif", ll.title)
        self.assertEqual(Layout.Type.NOTIFICATION, ll.type)
        self.assertEqual(Layout.Icon.FLAG, ll.tinyIcon)

    def test_valid_comm_notification(self):
        from pebbletime import Layout
        ll = Layout("Got mail!", Layout.Type.COMM,
                tinyIcon = Layout.Icon.GMAIL, sender = "Peter Parker")
        self.assertEqual("Got mail!", ll.title)
        self.assertEqual(Layout.Type.COMM, ll.type)
        self.assertEqual(Layout.Icon.GMAIL, ll.tinyIcon)
        self.assertEqual("Peter Parker", ll.sender)

    def test_valid_weather(self):
        from pebbletime import Layout
        ll = Layout("It's Sunny", Layout.Type.WEATHER,
                tinyIcon = Layout.Icon.TIMELINE_WEATHER,
                largeIcon = Layout.Icon.TIMELINE_SUN,
                locationName = "London")
        self.assertEqual("It's Sunny", ll.title)
        self.assertEqual(Layout.Type.WEATHER, ll.type)
        self.assertEqual(Layout.Icon.TIMELINE_WEATHER, ll.tinyIcon)
        self.assertEqual(Layout.Icon.TIMELINE_SUN, ll.largeIcon)
        self.assertEqual("London", ll.locationName)

    def test_valid_sports(self):
        from pebbletime import Layout
        ll = Layout("Cricket", Layout.Type.SPORTS,
                tinyIcon = Layout.Icon.CRICKET_GAME,
                largeIcon = Layout.Icon.CRICKET_GAME)
        self.assertEqual("Cricket", ll.title)
        self.assertEqual(Layout.Type.SPORTS, ll.type)
        self.assertEqual(Layout.Icon.CRICKET_GAME, ll.tinyIcon)
        self.assertEqual(Layout.Icon.CRICKET_GAME, ll.largeIcon)

    def test_invalid_missing_fields(self):
        from pebbletime import Layout
        # These layouts need extra parameters.
        for layout_type in (
                Layout.Type.GENERIC,
                Layout.Type.REMINDER,
                Layout.Type.NOTIFICATION,
                Layout.Type.COMM,
                Layout.Type.WEATHER,
                Layout.Type.SPORTS):
            with self.assertRaises(ValueError):
                ll = Layout("Test", layout_type)

