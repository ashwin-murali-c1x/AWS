keys = []
def get_matching_s3_keys(bucket, prefix='', suffix=''):
    """
    Generate the keys in an S3 bucket.

    :param bucket: Name of the S3 bucket.
    :param prefix: Only fetch keys that start with this prefix (optional).
    :param suffix: Only fetch keys that end with this suffix (optional).
    :bucket name: soka-sample
    :prefix : pixel-json-shopclues
    """
    kwargs = {'Bucket': bucket, 'Prefix': prefix}
    while True:
        resp = s3_client.list_objects_v2(**kwargs)
        for obj in resp['Contents']:
            key = obj['Key']
            if key.endswith(suffix):
                yield key

        try:
            kwargs['ContinuationToken'] = resp['NextContinuationToken']
        except KeyError:
            break
for i in get_matching_s3_keys('soka-sample','pixel-json-shopclues'):
    keys.append(i)
print(keys)
