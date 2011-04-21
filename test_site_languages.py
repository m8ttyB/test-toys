#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Selenium Tests.
#
# The Initial Developer of the Original Code is
# Mozilla.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Matt Brandt <mbrandt@mozilla.com>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

import unittest
import pytest

import urllib2


class TestSiteLanguages(unittest.TestCase):

    prod_base_page = "http://input.mozilla.com/"
    stage_base_page = "http://input.stage.mozilla.com/"
    
    pages = ["","themes", "sites", "search"]
    
    release_locator = "/release/"
    beta_locator = "/beta/"
    
    languages  = ["ar","bg","ca","cs","da","de","el","en-us","es","fr","fy-nl","ga-ie","gl","he",
    "hr","hu","id","it","ja","ko","nb-no","nl","pl","pt-pt","ro","ru","sk","sl","sq","uk","vi",
    "zh-cn","zh-tw"]
    
    @pytest.mark.production
    def test_languages_on_production_site(self):
        """
        Test l10n on the production server.
        """
        for page in self.pages:
            url = self.prod_base_page + "%s" + self.release_locator + page
            self._run_test(url)

    @pytest.mark.stage
    def test_languages_on_stage_site(self):
        """
            Test l10n on the stage server.
        """
        for page in self.pages:
            url = self.stage_base_page + "%s" + self.beta_locator + page
            self._run_test(url)

    def _run_test(self, url):
        """
            Assert that the url returns a 200.
        """
        for language in self.languages:
            page = url % language
            response_code = self._get_response_code(page)
            message = "Visted: %s, response_code: %s" % (page, response_code)
            self.assertEqual(response_code, 200, msg=message)

    def _get_response_code(self, url):
        try:
            response = urllib2.urlopen(url)
            print "visiting:%s" % (response.geturl())
            return response.getcode()
        except urllib2.HTTPError, e:
            return e.code


if __name__ == '__main__':
    unittest.main()
