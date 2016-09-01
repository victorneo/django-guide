# Optimizing Database Calls

## Introduction

For web applications, one of the [top ten performance problems](http://apmblog.dynatrace.com/2010/06/15/top-10-performance-problems-taken-from-zappos-monster-and-co/) encountered by developers is due to the database. Carelessly making too many calls to the database will cause the database to be flooded with a large amount SQL queries that it will not be able to handle. The problem is made worse when the SQL queries themselves are not optimized and take forever to complete.

There are two database performance questions that you should ask when seeking out problematic areas with database performance:

- How many SQL queries does my webpage require?
- How long does it take for each of the SQL query to complete?

In this guide, we will do a detailed walkthrough on the tools that can help answer the two questions above followed how you can tackle them.

### Django ORM

Django's [Object Relational Mapper](https://docs.djangoproject.com/en/1.9/topics/db/) (ORM) provides a nice level of abstraction between their Models and low-level database implementation.

For most parts, you can use the ORM to retrieve the data you require without having to worry too much about performance. In the event that you do running your own custom SQL scripts or subqueries, Django has [built-in support](https://docs.djangoproject.com/en/1.9/topics/db/sql/) for that as well.

## Tools To Help Identify Problematic Areas

If you are new to Django or web development, it might be hard to imagine where you might find problem areas with database performance. Fortunately, there are third-party or community supported tools that lets you examine the number of database queries that your Django view requires.

The first tool that we will cover is the [Django Debug Toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar) (DDT) and the second tool is [Silk](https://github.com/django-silk/silk). While DDT is the de facto tool for investigating performance issues with Django, Silk has a couple of nifty features up its sleeves that makes it easier to use when building APIs.

### Django Debug Toolbar

[Django Debug Toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar) (DDT) provides a comprehensive set of data panels that allows you to identify performance bottlenecks in your code. One of the data panels they provide shows you the number of SQL queries that your Django view requires in order to fully render a page.

![Django Debug Toolbar](https://github.com/victorneo/django-guide/raw/master/assets/database/debug_toolbar.png "Django Debug Toolbar")

You can install DDT by following the instructions on their [installation page](http://django-debug-toolbar.readthedocs.io/en/stable/installation.html). Once installed, you should see a sidebar similar to the one in the screenshot above appearing on the side of your webpage when you run the development server. Clicking on the SQL panel will give you the answers you seek for the two database performance questions.

![Debugging SQL](https://github.com/victorneo/django-guide/raw/master/assets/database/debug_sql.png "Debugging SQL")

To be continued..

