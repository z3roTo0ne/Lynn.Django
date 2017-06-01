import urllib2


r = urllib2.urlopen("https://cdb.api.qcloud.com/v2/index.php?Nonce=1949026579106452322&RequestClient=SDK_PYTHON_1.1&Region=gz&Signature=GZjmVJ2aEbrK7gojvNkyUjJvjLk%3D&SecretId=AKIDWxMDr345iqht1PJhXYi1k9zJ9khdvj1X&Timestamp=1467969147&Action=DescribeCdbInstances")
print r


