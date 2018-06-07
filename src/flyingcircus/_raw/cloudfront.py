"""Raw representations of every data type in the AWS CloudFront service.

See Also:
    `AWS developer guide for CloudFront
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html>`_

This file is automatically generated, and should not be directly edited.
"""

from ..core import Resource

__all__ = [
    "CloudFrontOriginAccessIdentity",
    "Distribution",
    "StreamingDistribution",
]


class CloudFrontOriginAccessIdentity(Resource):
    """A Cloud Front Origin Access Identity for CloudFront.

    See Also:
        `AWS Cloud Formation documentation for CloudFrontOriginAccessIdentity
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html>`_
    """

    RESOURCE_TYPE = "AWS::CloudFront::CloudFrontOriginAccessIdentity"

    RESOURCE_PROPERTIES = {
        "CloudFrontOriginAccessIdentityConfig",
    }


class Distribution(Resource):
    """A Distribution for CloudFront.

    See Also:
        `AWS Cloud Formation documentation for Distribution
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html>`_
    """

    RESOURCE_TYPE = "AWS::CloudFront::Distribution"

    RESOURCE_PROPERTIES = {
        "DistributionConfig",
        "Tags",
    }


class StreamingDistribution(Resource):
    """A Streaming Distribution for CloudFront.

    See Also:
        `AWS Cloud Formation documentation for StreamingDistribution
        <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html>`_
    """

    RESOURCE_TYPE = "AWS::CloudFront::StreamingDistribution"

    RESOURCE_PROPERTIES = {
        "StreamingDistributionConfig",
        "Tags",
    }