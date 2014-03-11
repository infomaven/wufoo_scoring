wufoo_scoring is a extension of wufoo_quizzes by Robert Graham. 
It uses Django/Python with Postgres backend, and is presently configured for deployment to heroku.com cloud service

Author: Robert Graham (rgraham@whitetailsoftware.com)



LICENSE
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Dependencies:
pyfoo (https://github.com/wufoo/pyfoo)
python-dateutil (pip install python-dateutil)
Django==1.6.2
South==0.8.4
dj-database-url==0.2.2
dj-static==0.0.5
django-toolbelt==0.0.1
gunicorn==18.0
psycopg2==2.5.2
pystache==0.5.3
static==1.0.2
wsgiref==0.1.2

Basic Features:
1. Surveys become graded quizzes.
2. User emails with survey results. 
3. Admin emails with complete results in CSV.
4. Report showing graded scores for each location that submitted an entry
5. Weekly email to admin to alert of "missing entries"

Suggested tutorials to set up dev environment:
