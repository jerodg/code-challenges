import binascii
import hmac
import logging
import time
from flask import Flask, redirect, send_file, session
from hashlib import sha1
from secrets import token_hex
from urllib.parse import quote, urlencode

log = logging.getLogger(__name__)

app = Flask(__name__, static_url_path="/assets", static_folder="assets")

# app.config.from_object("settings")
app.secret_key = token_hex()


@app.route("/authorize")
def authorize():
    """
    A method to redirect the user to twitter's authorize endpoint.

    reference:
      https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens
    """

    # TODO: FIll Me In


@app.route("/callback")
def callback():
    """
    A method to handle the callback from twitter's authorize url.
    reference:
      https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens
    """

    # TODO: FIll Me In


def get_timeline():
    """
    A method to fetch home timeline data using stored access tokens.
    This should simply return the raw json from an authenticated call against
    "https://api.twitter.com/1.1/statuses/home_timeline.json".

    reference:
      https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens
    """
    # TODO: FIll Me In


def parse_tweet(tweet):
    """
    Parse each tweet returned from get_timeline and return a dictionary with
    the following fields:

    * username: The tweet author's screen_name
    * text: The text of the tweet
    * tweet_id: The id of the tweet
    * profile_image_url: The url to fetch the tweet author's profile image
    * timestamp: The created_at time for the tweet formated as a integer unix timestamp
    """

    # TODO: Fill Me In


@app.route("/api/timeline")
def api_get_timeline():
    """api route, fetch data from Twitter API"""
    return {"tweets": [parse_tweet(tweet) for tweet in get_timeline()]}


@app.route("/timeline")
def view_timeline():
    """web route (serve html/css/js)"""
    return send_file("assets/index.html")


@app.route("/")
def root():
    if not get_token() or not get_secret():
        return redirect("/authorize")
    return redirect("/timeline")


def get_oauth_headers(method, url, params):
    """
    Constructs the http authorization header required for Oauth1 requests.
    This should use the parameters provided by `build_oauth_params`.

    reference:
        https://tools.ietf.org/html/rfc5849#section-3.1

    `method` is either "GET" or "POST" depending on the request.
    `url` is the base url being requested excluding the query and fragment.
    `params` is a dictionary of query or form parameters to be sent in the request.
    """

    # TODO: FIll Me In


def build_oauth_params(method, url, params):
    """
    Constructs the oauth parameters including signature that are required in
    the OAuth authentication header. You should not need to modify this.

    `method` is either "GET" or "POST" depending on the request.
    `url` is the base url being requested excluding the query and fragment.
    `params` is a dictionary of query or form parameters to be sent in the request.
    """
    # construct oauth header parameters
    oauth_params = {
        "oauth_consumer_key": app.config["TWITTER_API_KEY"],
        "oauth_nonce": token_hex(16),
        "oauth_signature_method": "HMAC-SHA1",
        "oauth_timestamp": str(int(time.time())),
        "oauth_version": "1.0",
        "oauth_token": get_token(),
    }

    # compute the signature from all parameters
    collected_params = {**oauth_params, **params}
    encoded_params = urlencode(sorted(collected_params.items()))
    base_string = "&".join([quote(method), quote(url, safe=""), quote(encoded_params)])
    key = "&".join(
        [quote(app.config["TWITTER_API_SECRET"], safe=""), quote(get_secret(), safe="")]
    )
    sig = hmac.new(key.encode("utf8"), base_string.encode("utf8"), sha1)
    sig_str = binascii.b2a_base64(sig.digest(), newline=False).decode("utf-8")
    oauth_params["oauth_signature"] = sig_str

    return oauth_params


def store_token(token):
    """
    Utility function to store a request or access token in the session.
    """
    session["access_token"] = token


def store_secret(secret):
    """
    Utility function to store a request or access secret in the session.
    """
    session["access_token_secret"] = secret


def get_token():
    """
    Utility function to retrieve a request or access token from the session.
    """
    return session.get("access_token", "")


def get_secret():
    """
    Utility function to retrieve a request or access token from the session.
    """
    return session.get("access_token_secret", "")
