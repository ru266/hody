class TwitterFetcherError(Exception):
    """Base exception class for Twitter fetcher errors"""
    pass

class InvalidCredentials(TwitterFetcherError):
    """Raised when API credentials are invalid"""
    pass

class UserNotFound(TwitterFetcherError):
    """Raised when requested user is not found"""
    pass

class RateLimitExceeded(TwitterFetcherError):
    """Raised when Twitter API rate limit is exceeded"""
    pass