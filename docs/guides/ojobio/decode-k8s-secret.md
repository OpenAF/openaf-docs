---
layout: default
title: Decode a Kubernetes secret
parent: oJobIO
grand_parent: Guides
---

# Decode a Kubernetes secret

If you need to decode an existing Kubernetes file-based secret you can execute the following commands easily to obtain the original copies of the files used in the secret:

```bash
kubectl get secret my-secret -n my-namespace -o yaml | ojob ojob.io/kube/expandSecret toFolder=output
```

This will actually retrieve _my-secret_ from the _my-namespace_ Kubernetes namespace, pipe the YAML contents to the _ojob.io/kube/expandSecret_ and create the corresponding files in the _output_ folder (using the "toFolder" argument).

It's possible to use also other arguments if needed. Example:

```bash
ojob ojob.io/kube/expandSecret input=my-secret.yml file=justASingleFileOfMany.crt toFolder=output
```

This will use the previously saved _my-secret.yml_ and, if it has many secret files, it will only retrieve the _justASingleFileOfMany.crt_ and place the original copy on the folder _output_.

> Note: You can always download and use your own copy of the ojob.io/kube/expandSecret ojob. For that just follow the instructions on [Get oJob](get-ojob)
