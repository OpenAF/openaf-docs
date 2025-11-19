---
layout: default
title: oJob AWS ECR browse functionality
parent: oJob
grand_parent: Guides
---

# AWS ECR browse functionality

Starting on oJob-common oPack version 20250415 it's possible to use the common browse functionality to list the contents of a directory or a file. This functionality is generic enough to be applied to different scenarios like: browsing a local filesystem; browsing an object storage bucket; browsing an AWS ECR; browsing a Maven repository; etc.

> To install oJob-common either refer to it on an oJob (ojob > opacks > oJob-common) or install it directly by executing ``opack install ojob-common````

This ECR implementation also requires to install the 'AWS' oPack:

```bash
opack install AWS
```

## Example:

```yaml
ojob:
  daemon: true   # we want to run it as a daemon 
  opacks: 
  - oJob-common  # we want to install/include oJob-common
  - AWS          # we want to install/include AWS

include:
- oJobECR.yaml  # we want to add the oJob ECR browse functionality

todo:
- (ECRBrowse): 8888
  ((uri    )): /browse
  ((region )): us-east-1
  ((options)):
    usePull : false
    sortTab : true
    registry: "my.registry.com"
    refLink : {% raw %}"/pull-instructions.md?image={{image}}&type={{type}}"{% endraw %}
    footer  : |
        <div class="footer">
            <p>Powered by <a href="https://openaf.io">OpenAF</a></p>
        </div>
```

The `accessKey`, `secretKey` and `region` are not provided, the AWS oPack will use the default credentials from the environment. This is useful when running on AWS or other cloud providers that support IAM roles.

> You can also use `assumeRole` to assume a role in another account. This is useful when running on AWS or other cloud providers that support IAM roles.

**Arguments available:**

| Argument | Type | Description |
| -------- | ---- | ----------- |
| `accessKey` | String | The access key to use to connect to the AWS endpoint. |
| `secretKey` | String | The secret key to use to connect to the AWS endpoint. |
| `region` | String | The region to use to connect to the AWS endpoint. |
| `cache` | Number | The cache time in ms for the ECR lists |
| `restrict` | Array | A regular expression (or list) that if matched won't be listed or accessible. |
| `sortTab` | Boolean | If true, the ECR list will be sorted by tab. |
| `incURI` | Boolean | If true, the URI will be included in the ECR list. |
| `logo` | String | The logo to use when browsing the ECR. |
| `browse` | Boolean | If true, the ECR will be browsed. |
| `refLink` | String | The link to use when browsing the ECR with the handlebars arguments `image` and `type`. |

For performance reasons some fields might not be available until the cache, in background, is filled. This happens when browsing after the `cache` time. To avoid any consistency issues once the cache becomes invalid no value is showed on the UI until it's refreshed properly.

The `refLink` is a link to a page that will be opened when clicking on the image/chart tag name. The `image` and `type` are replaced with the corresponding image name & tag and artifact type (to be able to distinguish between a chart and an image). 
This is useful when you want to provide a link to a page with more information about the image/chart. 