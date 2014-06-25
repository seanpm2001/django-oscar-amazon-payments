STATUS_RESPONSE_XML = (
    '<?xml version="1.0"?>' +
    '<GetServiceStatusResponse xmlns="http://mws.amazonservices.com/schema/OffAmazonPayments/2013-01-01">' +
    '<GetServiceStatusResult>' +
    '<Status>GREEN</Status>' +
    '<Timestamp>2014-06-11T13:40:53.969Z</Timestamp>' +
    '</GetServiceStatusResult>' +
    '<ResponseMetadata>' +
    '<RequestId>bf4c5241-fdce-4f56-92b1-b2680c3068ae</RequestId>' +
    '</ResponseMetadata>' +
    '</GetServiceStatusResponse>'
)

ORDER_REFERENCE_DETAILS_XML = (
    '<GetOrderReferenceDetailsResponse xmlns="http://mws.amazonservices.com/schema/OffAmazonPayments/2013-01-01">' +
    '<GetOrderReferenceDetailsResult>' +
    '<OrderReferenceDetails>' +
    '<AmazonOrderReferenceId>S02-4932843-1071433</AmazonOrderReferenceId>' +
    '<ExpirationTimestamp>2014-12-21T08:52:38.770Z</ExpirationTimestamp>' +
    '<Constraints>' +
    '<Constraint>' +
    '<ConstraintID>AmountNotSet</ConstraintID>' +
    '<Description>The seller has not set the amount for the Order Reference.</Description>' +
    '</Constraint>' +
    '</Constraints>' +
    '<IdList/>' +
    '<Destination>' +
    '<DestinationType>Physical</DestinationType>' +
    '<PhysicalDestination>' +
    '<PostalCode>SE1 5RB</PostalCode>' +
    '<CountryCode>GB</CountryCode>' +
    '<City>LONDON</City>' +
    '</PhysicalDestination>' +
    '</Destination>' +
    '<OrderReferenceStatus>' +
    '<State>Draft</State>' +
    '</OrderReferenceStatus>' +
    '<ReleaseEnvironment>Sandbox</ReleaseEnvironment>' +
    '<SellerOrderAttributes/>' +
    '<CreationTimestamp>2014-06-24T08:52:38.770Z</CreationTimestamp>' +
    '</OrderReferenceDetails>' +
    '</GetOrderReferenceDetailsResult>' +
    '<ResponseMetadata>' +
    '<RequestId>e13beadb-c4b1-4c0e-a5b8-b5f8dc2f33ac</RequestId>' +
    '</ResponseMetadata>' +
    '</GetOrderReferenceDetailsResponse>'
)

SET_ORDER_REFERENCE_DETAILS_RESPONSE_XML = (
    '<SetOrderReferenceDetailsResponse xmlns="http://mws.amazonservices.com/schema/OffAmazonPayments/2013-01-01">' +
    '<SetOrderReferenceDetailsResult>' +
    '<OrderReferenceDetails>' +
    '<AmazonOrderReferenceId>S02-1556010-3677478</AmazonOrderReferenceId>' +
    '<ExpirationTimestamp>2014-12-22T10:25:51.805Z</ExpirationTimestamp>' +
    '<OrderTotal>' +
    '<Amount>2.99</Amount>' +
    '<CurrencyCode>GBP</CurrencyCode>' +
    '</OrderTotal>' +
    '<Constraints>' +
    '<Constraint>' +
    '<ConstraintID>PaymentPlanNotSet</ConstraintID>' +
    '<Description>The buyer has not been able to select a Payment method for the given Order Reference.</Description>' +
    '</Constraint>' +
    '</Constraints>' +
    '<Destination>' +
    '<DestinationType>Physical</DestinationType>' +
    '<PhysicalDestination>' +
    '<PostalCode>SE1 5RB</PostalCode>' +
    '<CountryCode>GB</CountryCode>' +
    '<City>LONDON</City>' +
    '</PhysicalDestination>' +
    '</Destination>' +
    '<OrderReferenceStatus>' +
    '<State>Draft</State>' +
    '</OrderReferenceStatus>' +
    '<ReleaseEnvironment>Sandbox</ReleaseEnvironment>' +
    '<SellerOrderAttributes>' +
    '<StoreName>Oscar Sandbox</StoreName>' +
    '<SellerOrderId>1234</SellerOrderId>' +
    '</SellerOrderAttributes>' +
    '<CreationTimestamp>2014-06-25T10:25:51.805Z</CreationTimestamp>' +
    '</OrderReferenceDetails>' +
    '</SetOrderReferenceDetailsResult>' +
    '<ResponseMetadata>' +
    '<RequestId>11c37534-de6a-4ee9-a07f-a44c7f6aece6</RequestId>' +
    '</ResponseMetadata>' +
    '</SetOrderReferenceDetailsResponse>'
)

CONFIRM_ORDER_RESPONSE_XML = (
    '<ConfirmOrderReferenceResponse xmlns="http://mws.amazonservices.com/schema/OffAmazonPayments/2013-01-01">' +
    '<ResponseMetadata>' +
    '<RequestId>41474366-b298-494c-830c-9c14a1240a81</RequestId>' +
    '</ResponseMetadata>' +
    '</ConfirmOrderReferenceResponse>'
)

INVALID_SIGNATURE_RESPONSE = (
    '<?xml version="1.0"?>' +
    '<ErrorResponse xmlns="http://mws.amazonservices.com/schema/OffAmazonPayments/2013-01-01">' +
    '<Error>' +
    '<Type>Sender</Type>' +
    '<Code>SignatureDoesNotMatch</Code>' +
    '<Message>The request signature we calculated does not match the signature you provided. Check your AWS Secret Access Key and signing method. Consult the service documentation for details.</Message>' +
    '</Error>' +
    '<RequestID>fe91b76f-5ae1-4965-b16a-6d15d0495e00</RequestID>' +
    '</ErrorResponse>'
)
