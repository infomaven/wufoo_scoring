"""
wufoo_reporter.weekly_location_reports.py
Purpose: POSTS aggregate data to forms hosted on wufoo.com 
Author: nwhitfield
Date: 6 Mar 2014

approved format: https://{subdomain}.wufoo.com/api/v3/forms/{formIdentifier}/entries.{xml|json}
{subdomain} = neighborhoodsonic
{formIdentifier} = s1m6or2u1rkli5v 

sample post made in PHP using CurlService class:
$service = new CurlService(CurlService::CONTENT_MULTI_PART, '224B-Rpbp-N7QC-Y75P', 'x');
$service ->init('https://fishbowl.wufoo.com/api/v/forms/nyform/entries.xml');
$r = $service->postAuthenticated(array('Field1' => 'Frank'));

# on Django, build a template with the following fields:
Field1: Location, Field2: Audit Name, Field8: Date, Field6: Score
"""
# todo: create a view 

# todo: create url entry in settings.py

# todo: create model (probably a modelform)

# todo: create template



