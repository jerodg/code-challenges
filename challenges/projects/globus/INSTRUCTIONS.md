# Full-Stack Engineer Coding Challenge

## CONFIDENTIALITY NOTICE

This challenge and your answers are confidential to globus.org. Do not share
this challenge or your answers with recruiters, coworkers, friends, etc.

This is a coding challenge which will test both your backend and frontend skills.

## Overview

The basic premise is to write a simple app that authenticates to Twitter and presents some
information from tweets.  Most of the app skeleton has been provided for you,
but you will need to fill in several methods related to authentication.

## Instructions

You will implement two OAuth endpoints in python as well as a method to fetch
and return a users home tweet timeline.

### Notes About the Code Provided

We have provided a partial outline for the backend and a functioning frontend
for this coding assignment.  You may replace any part of the code with which
you have been provided.  However, **please limit your third party packages to
the ones included in requirements.txt**.  In particular, do not rely on third
party oauth implementations.

The app.py file contains a Flask app and some sample helpers for
interacting with Twitter.

The settings.py file in the project contains an Application Token and Secret for
making authenticated requests against Twitter's API.

The application is already configured to read from the settings.py file and to
serve files from the `assets/` directory.

All methods that have comments "# FILL ME IN" need to be completed.

## Challenge Deliverables

Using the provided resources, complete the following components.

### Backend / API

You will need to complete the app's Oauth1.0 flow so that a user may login to
Twiter and grant the application the ability to see their profile and tweets.
To do that you need to:

1. Fill in the `get_oauth_headers` method that should construct the OAuth
   authorization header that will be used to authorize requests to Twitter's
   API.
2. Create a view at `/authorize` that fetches a request token and redirects
   the user to the Twitter API's `authorize` endpoint.  Error conditions
   should be handled with appropriate messages and status codes.
3. Create a view at `/callback` that handles a callback from Twitter after the
   user has completed an authentication flow.  It should be able to accept
   `oauth_token` and `oauth_verifier` query parameters and exchange them for
   access tokens and secrets.
4. Fill in the `get_timeline` method so it fetches the user's home timeline
   data from the twitter api using the newly acquired access tokens.
5. Fill in the `parse_tweet` method to return a dictionary with fields that
   are needed by the frontend.

The Twitter API documentation which you will need can be found here:

* https://developer.twitter.com/en/docs/twitter-api/v1
* https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens

The OAuth header format is documented here:

* https://tools.ietf.org/html/rfc5849#section-3.1
* https://developer.twitter.com/en/docs/authentication/oauth-1-0a/authorizing-a-request


### README Requirements

You have been provided with a basic readme which provides instructions for
setting up and running the app locally. If you add to this process, you must
enhance the readme with relevant instructions.

You may assume that readers are already familiar with basic tools such as
`make`, `virtualenv`, `npm`, and `pip`.

### Expectations & Notes

 * The URLs and views should be laid out in a RESTful fashion
 * Error handling matters
 * Clean markup and styles are important
 * Use best practices/conventions (e.g. PEP8 python code)
 * Please limit your use of third party libraries to those included in
     requirements.txt.
