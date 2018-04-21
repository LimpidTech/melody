import collections
import functools
import hashlib
import hmac
import operator

from django import http

from django.conf import settings

MAILGUN_API_KEY = str.encode(settings.MAILGUN_API_KEY)

SignatureVerificationInfo = collections.namedtuple(
    'SignatureVerificationInfo', [
        'signature',
        'timestamp',
        'token',
    ]
)


def get_signature_verification_info(
        request,
        get_signature,
        get_timestamp,
        get_token,
):
    """ Get SignatureVerificationInfo for the given request.  """

    signature = get_signature(request.data)

    if signature is None:
        raise ValueError('A signature must be provided')

    token = get_token(request.data)

    if signature is None:
        raise ValueError('A token must be provided')

    timestamp = get_timestamp(request.data)

    if signature is None:
        raise ValueError('A timestamp must be provided')

    # TODO: Ensure timestamp isn't unreasonably backdated or in the future

    return SignatureVerificationInfo(
        signature=signature,
        token=token,
        timestamp=timestamp,
    )


def signature_is_valid(request, *verification_getters):
    """ Our signature verification algorithm. """

    verification_info = get_signature_verification_info(
        request,
        *verification_getters,
    )

    signed_value = f'{verification_info.timestamp}{verification_info.token}'

    signature = hmac.new(
        key=MAILGUN_API_KEY,
        msg=str.encode(signed_value),
        digestmod=hashlib.sha256,
    ).hexdigest()

    return hmac.compare_digest(
        signature,
        verification_info.signature,
    )


def signature_required(
        get_signature=operator.itemgetter('signature'),
        get_timestamp=operator.itemgetter('timestamp'),
        get_token=operator.itemgetter('token'),
):
    """ Validates the provided signature before executing the view function.

    Extracts a signature, token, and timestamp from request.data using the
    provided getter functions. Ensures that signature is valid for the given
    timestamp/token combination, or raises ValueError.

    """

    def signature_required_decorator(wrapped_fn):
        @functools.wraps(wrapped_fn)
        def raise_unsigned(self, request, *args, **kwargs):
            try:
                is_valid = signature_is_valid(
                    request,
                    get_signature,
                    get_timestamp,
                    get_token,
                )
            except ValueError:
                is_valid = False

            if not is_valid:
                return http.HttpResponseForbidden(
                    (
                        'The provided signature was not signed with '
                        'the expected key. Ignoring this request.'
                    ),
                )

            return wrapped_fn(self, request, *args, **kwargs)

        return raise_unsigned

    return signature_required_decorator
