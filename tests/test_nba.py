#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_nba
----------------------------------

Tests for `nba` module.
"""

import unittest

import json
from sportsstats import nba


class TestNba(unittest.TestCase):

    def setUp(self):
        today = '04/09/2016'
        self.nba_stats = nba.Stats(today, today, '2015-16')
        self.expected_query_url = (
                "/stats/leaguedashptstats?"
                "College=&Conference=&Country=&DateFrom=04%2F09%2F2016&"
                "DateTo=04%2F09%2F2016&Division=&DraftPick=&DraftYear=&"
                "GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&"
                "Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=Totals&"
                "PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&"
                "PtMeasureType=SpeedDistance&Season=2015-16&SeasonSegment=&"
                "SeasonType=Regular+Season&StarterBench=&TeamID=0&"
                "VsConference=&VsDivision=&Weight="
                )
        pass

    def tearDown(self):
        del self.nba_stats
        pass

    def test_build_query_url(self):
        actual = self.nba_stats._Stats__build_query_url()
        self.assertEqual(actual, self.expected_query_url)

    def test_send_get_request(self):
        connection = self.nba_stats._Stats__send_get_request(
                self.expected_query_url)
        actual = connection.getresponse().status
        self.assertEqual(actual, 200)
        connection.close()

    def test_download(self):
        data = json.loads(self.nba_stats.download())
        actual = data['resultSets'][0]['rowSet'][72]
        #  expected = "[201939, 'Stephen Curry', 1610612744, 'GSW', 1, 1, 0,
        #               34.0, 12302, 2.3, 1.2, 1.2, 4.05, 4.98, 3.65]"
        self.assertEqual(actual[0], 201939)
        self.assertEqual(actual[1], 'Stephen Curry')

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
