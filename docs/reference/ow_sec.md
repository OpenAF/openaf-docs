---
layout: default
title: ow.sec
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## ow.sec

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/js/owrap.sec.js) · [Baseline](../source-snapshot.md)

### $sec.$sec

`$sec.$sec(aRepo, dBucket, dLockSecret, aMainSecret, aFile) : $sec`

````text
Shortcut for acessing ow.sec.SBuckets given aMainSecret and, optionally, aRepo. A default dBucket and the corresponding dLockSecret can be provided.
````

### $sec.close

`$sec.close() : Object`

````text
Close the current repository.
````

### $sec.encSKey

`$sec.encSKey(aKey) : String`

Given `aKey` will return the encrypted version of it with the current main secret for the repo.

Example:

```javascript
$sec("test", "b1", $sec("test", __, __, "Password123").encSKey("Password1"), "Password123", "test.yml").set("mysecret", { l:"l", p:"p" })
// ...
$sec("test", "b1", $sec("test", __, __, "Password123").encSKey("Password1"), "Password123", "test.yml").get("mysecret")
```

### $sec.get

`$sec.get(aKey, aBucket, aLockSecret) : Object`

````text
Retrieves the secret object/string for aKey. Optionally you can provide a specific aBucket and the corresponding aLockSecret.
````

### $sec.getBucket

`$sec.getBucket(aBucket, aLockSecret) : String`

````text
Retrieves a encrypted SBucket string to be transported to another SBucket repo.  Optionally you can provide a specific aBucket and the corresponding aLockSecret.
````

### $sec.getFn

`$sec.getFn(aKey, aExtraArgs, aBucket, aLockSecret) : Object`

````text
Invokes a function using the secret arguments for aKey with non-secret aExtraArgs map (arguments should have the same name as the function help parameters). Optionally you can provide a specific aBucket and the corresponding aLockSecret.
````

### $sec.getObj

`$sec.getObj(aKey, aExtraArgs, aBucket, aLockSecret) : Object`

````text
Creates a new instance of an object using the secret arguments for aKey with non-secret aExtraArgs map (arguments should have the same name as the constructor help parameters). Optionally you can provide a specific aBucket and the corresponding aLockSecret.
````

### $sec.list

`$sec.list(aBucket, aLockSecret) : Array`

````text
Returns a map with a list of all the sBuckets on the current repo. If a specifc sBucket and aLockSecret isn't provide the current sBucket will have an associated array with the list of corresponding keys.
````

### $sec.procMap

`$sec.procMap(aMap, aPath) : Map`

Given `aMap` will process it and replace any secKey with the corresponding secret. Optionally you can provide `aPath` to
process only a specific path of the map.

`secKey`, `secRepo`, `secBucket`, `secPass`, `secMainPass`, `secFile`

### $sec.set

`$sec.set(aKey, aObj, aBucket, aLockSecret) : Object`

````text
Sets the secret aObj map/string associating it with aKey. Optionally you can provide a specific aBucket and the corresponding aLockSecret.
````

### $sec.setBucket

`$sec.setBucket(aBucketString, aBucket, aLockSecret) : String`

````text
Sets an encrypted SBucket string transported from another SBucket repo (the aLockSecret should be equal) Optionally you can provide a specific aBucket and the corresponding aLockSecret.
````

### $sec.setFn

`$sec.setFn(aKey, aFn, aArgs, aBucket, aLockSecret) : Object`

````text
Sets secret aArgs (map with the arguments names on the aFn help)) for calling aFn (string). Optionally you can provide a specific aBucket and the corresponding aLockSecret.
````

### $sec.setObj

`$sec.setObj(aKey, aObj, aArgs, aBucket, aLockSecret) : Object`

````text
Sets secret aArgs (map with the arguments names on the aObj constructor help)) for constructing aObj (string). Optionally you can provide a specific aBucket and the corresponding aLockSecret.
````

### $sec.unset

`$sec.unset(aKey, aBucket, aLockSecret) : Object`

````text
Unsets aKey for a SBucket. Optionally you can provide a specific aBucket and the corresponding aLockSecret.
````

### $sec.unsetBucket

`$sec.unsetBucket(aBucket)`

````text
Unsets aBucket from the current repo.
````

### $sec.unsetRepo

`$sec.unsetRepo()`

````text
Unsets the current repo.
````

### ow.sec.SBucket.SBucket

`ow.sec.SBucket.SBucket(aCh, aMainSecret, sBucket, aLockSecret) : sbucket`

````text
Creates a set of sbuckets on aCh using aMainSecret.  Defaults, if provided, to sBucket and aLockSecret.
````

### ow.sec.SBucket.createBucket

`ow.sec.SBucket.createBucket(sBucket, aLockSecret)`

````text
Creates a sbucket with a specific aLockSecret.
````

### ow.sec.SBucket.destroyBucket

`ow.sec.SBucket.destroyBucket(sBucket)`

````text
Destroys a sBucket.
````

### ow.sec.SBucket.getBucket

`ow.sec.SBucket.getBucket(sBucket, aLockSecret) : String`

````text
Given a sbucket and aLockSecret retrieves a string representation of the sbucket.
````

### ow.sec.SBucket.getKeys

`ow.sec.SBucket.getKeys(sBucket, aLockSecret, aKey) : Map`

````text
Returns a map with a list of all the sBuckets on the current repo. If a specifc sBucket and aLockSecret isn't provide the current sBucket will have an associated array with the list of corresponding keys.
````

### ow.sec.SBucket.getNewFn

`ow.sec.SBucket.getNewFn(sBucket, aLockSecret, aKey, defaultArgs)`

````text
For the sBucket with aLockSecret will invoke a function and set arguments using aKey.
````

### ow.sec.SBucket.getNewObj

`ow.sec.SBucket.getNewObj(sBucket, aLockSecret, aKey, defaultArgs)`

````text
For the sBucket with aLockSecret create an object with the arguments in aKey.
````

### ow.sec.SBucket.getSBucket

`ow.sec.SBucket.getSBucket() : String`

````text
Returns a string representation of the sbucket.
````

### ow.sec.SBucket.getSNewFn

`ow.sec.SBucket.getSNewFn(Key)`

````text
Will invoke a function and set arguments using aKey.
````

### ow.sec.SBucket.getSNewObj

`ow.sec.SBucket.getSNewObj(aKey)`

````text
Create an object with the arguments in aKey.
````

### ow.sec.SBucket.getSSecret

`ow.sec.SBucket.getSSecret(aKey) : Map`

````text
Returns the associated aKey value.
````

### ow.sec.SBucket.getSSecretAs

`ow.sec.SBucket.getSSecretAs(aEncryptKey, aKey) : Map`

````text
Returns the associated aKey encrypted with aEncryptKey.
````

### ow.sec.SBucket.getSecret

`ow.sec.SBucket.getSecret(sBucket, aLockSecret, aKey) : Map`

````text
Given a sbucket and a specific aLockSecret will return the associated aKey.
````

### ow.sec.SBucket.getSecretAs

`ow.sec.SBucket.getSecretAs(sBucket, aLockSecret, aEncryptKey, aKey) : Map`

````text
Given a sbucket and a specific aLockSecret will return the associated aKey encrypted with aEncryptKey.
````

### ow.sec.SBucket.setBucket

`ow.sec.SBucket.setBucket(sBucket, aLockSecret, aBucketString)`

````text
Given a sbucket, aLockSecret will set the sbucket to the provided aBucketString.
````

### ow.sec.SBucket.setNewFn

`ow.sec.SBucket.setNewFn(sBucket, aLockSecret, aKey, aFn, args)`

````text
For the sBucket with aLockSecret will set aKey to use aFn with the arguments map ($fnDev4Help).
````

### ow.sec.SBucket.setNewObj

`ow.sec.SBucket.setNewObj(sBucket, aLockSecret, aKey, aObject, args)`

````text
For the sBucket with aLockSecret will set aKey to create aObject with the arguments map ($fnDev4Help).
````

### ow.sec.SBucket.setSBucket

`ow.sec.SBucket.setSBucket(aBucketString)`

````text
Set the current sbucket to the provided aBucketString.
````

### ow.sec.SBucket.setSNewFn

`ow.sec.SBucket.setSNewFn(aKey, aFn, args)`

````text
For the sBucket with aLockSecret will set aKey to use aFn with the arguments map ($fnDev4Help).
````

### ow.sec.SBucket.setSNewObj

`ow.sec.SBucket.setSNewObj(aKey, aObject, args)`

````text
Will set aKey to create aObject with the arguments map ($fnDev4Help).
````

### ow.sec.SBucket.setSSecret

`ow.sec.SBucket.setSSecret(aKey, aObj)`

````text
Sets aKey to aObj (string or map)
````

### ow.sec.SBucket.setSecret

`ow.sec.SBucket.setSecret(sBucket, aLockSecret, aKey, aObj)`

````text
Given a sbucket and aLockSecret will set aKey to aObj (string or map)
````

### ow.sec.SBucket.unsetSSecret

`ow.sec.SBucket.unsetSSecret(aKey)`

````text
Unsets aKey.
````

### ow.sec.SBucket.unsetSecret

`ow.sec.SBucket.unsetSecret(sBucket, aLockSecret, aKey)`

````text
Given a sbucket and aLockSecret will unset aKey.
````

### ow.sec.closeMainSBuckets

`ow.sec.closeMainSBuckets()`

````text
Close the default SBucket.
````

### ow.sec.closeSBuckets

`ow.sec.closeSBuckets(aRepo, aFile)`

````text
Close a previously open aRepo SBucket.
````

### ow.sec.openMainSBuckets

`ow.sec.openMainSBuckets(aMainSecret)`

````text
Open the default SBucket using aMainSecret.
````

### ow.sec.openSBuckets

`ow.sec.openSBuckets(aRepo, aMainSecret, aFile)`

````text
Opens aRepo SBucket using aMainSecret.
````

### ow.sec.purgeMainSBuckets

`ow.sec.purgeMainSBuckets()`

````text
Purge the default SBucket.
````

### ow.sec.purgeSBuckets

`ow.sec.purgeSBuckets(aRepo, aFile)`

````text
Purge aRepo SBucket.
````
{% endraw %}
