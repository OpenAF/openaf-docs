---
layout: default
title: oafp reference list of examples
parent: oafp
grand_parent: Guides
---

# oafp reference list of examples

Examples of use of _oafp_ avaiable also in [https://ojob.io/oafp-examples.yaml](https://ojob.io/oafp-examples.yaml).

## 📚 Contents

| Category | Sub-category | #   | Description |
|:---------|:-------------|:----|:------------|
| AI | Conversation | [1](#1) | Send multiple requests to an OpenAI model keeping the conversation between interactions and setting the temperature parameter |
| AI | Ollama | [2](#2) | Setting up access to Ollama and ask for data to an AI LLM model |
| AI | OpenAI | [3](#3) | Setting up the OpenAI LLM model and gather the data into a data.json file |
| AI | Prompt | [4](#4) | Example of generating data from an AI LLM prompt |
| AI | Summarize | [5](#5) | Use an AI LLM model to summarize the weather information provided in a JSON format |
| APIs | Network | [6](#6) | Converting the Cloudflare DNS trace info |
| APIs | Network | [7](#7) | Converting the Google DNS DoH query result |
| APIs | Network | [8](#8) | Generating a simple map of the current public IP address |
| AWS | EC2 | [9](#9) | Given all AWS EC2 instances in an account produces a table with name, type, vpc and private ip sorted by vpc |
| AWS | EKS | [10](#10) | Builds an excel spreadsheet with all persistent volumes associated with an AWS EKS &#x27;XYZ&#x27; with the corresponding Kubernetes namespace, pvc and pv names |
| AWS | Lambda | [11](#11) | Prepares a table of AWS Lambda functions with their corresponding main details |
| AWS | Lambda | [12](#12) | Prepares a table, for a specific AWS Lambda function during a specific time periods, with number of invocations and minimum, average and maximum duration per periods from AWS CloudWatch |
| DB | H2 | [13](#13) | Perform a SQL query over a H2 database. |
| DB | H2 | [14](#14) | Store the json result of a command into a H2 database table. |
| DB | SQLite | [15](#15) | Perform a query over a database using JDBC. |
| DB | SQLite | [16](#16) | Store the json result on a SQLite database table. |
| Docker | Containers | [17](#17) | Output a table with the list of running containers. |
| Docker | Network | [18](#18) | Output a table with the docker networks info. |
| Docker | Stats | [19](#19) | Output a table with the docker stats broken down for each value. |
| Docker | Storage | [20](#20) | Output a table with the docker volumes info. |
| ElasticSearch | Cluster | [21](#21) | Get an ElasticSearch/OpenSearch cluster nodes overview |
| ElasticSearch | Cluster | [22](#22) | Get an ElasticSearch/OpenSearch cluster per host data allocation |
| ElasticSearch | Cluster | [23](#23) | Get an ElasticSearch/OpenSearch cluster settings flat |
| ElasticSearch | Cluster | [24](#24) | Get an ElasticSearch/OpenSearch cluster settings non-flatted |
| ElasticSearch | Cluster | [25](#25) | Get an ElasticSearch/OpenSearch cluster stats per node |
| ElasticSearch | Cluster | [26](#26) | Get an overview of an ElasticSearch/OpenSearch cluster health |
| ElasticSearch | Indices | [27](#27) | Get an ElasticSearch/OpenSearch count per index |
| ElasticSearch | Indices | [28](#28) | Get an ElasticSearch/OpenSearch indices overview |
| ElasticSearch | Indices | [29](#29) | Get an ElasticSearch/OpenSearch settings for a specific index |
| Generic | Excel | [30](#30) | Building an Excel file with the AWS IPv4 and IPv6 ranges (1). |
| Generic | Excel | [31](#31) | Building an Excel file with the AWS IPv4 and IPv6 ranges (2). |
| Generic | Excel | [32](#32) | Building an Excel file with the AWS IPv4 and IPv6 ranges (3). |
| Generic | Excel | [33](#33) | Processes each json file in /some/data creating and updating the data.xlsx file with a sheet for each file. |
| Generic | Excel | [34](#34) | Store and retrieve data from an Excel spreadsheet |
| Generic | RSS | [35](#35) | Example of generating a HTML list of titles, links and publication dates from a RSS feed |
| Generic | Text | [36](#36) | Get a json with lyrics of a song. |
| GitHub | Releases | [37](#37) | Builds a table of GitHub project releases |
| GitHub | Releases | [38](#38) | Parses the latest GitHub project release markdown notes |
| Grid | Java | [39](#39) | Parse a Java stacktrace into a looping grid. |
| Grid | Kubernetes | [40](#40) | Displays a continuous updating grid with a line chart with the number of CPU throtlles and bursts recorded in the Linux cgroup cpu stats of a container running in Kubernetes and the source cpu.stats data |
| Grid | Unix | [41](#41) | Output a chart with the current Unix load using uptime |
| JSON Schemas | Lists | [42](#42) | Get a list of JSON schemas from Schema Store catalog |
| Kubernetes | Containers | [43](#43) | Parse the Linux cgroup cpu stats on a container running in Kubernetes |
| Kubernetes | Kubectl | [44](#44) | Build an output table with Kubernetes pods with namespace, pod name, container name and corresponding resources using kubectl |
| Kubernetes | Kubectl | [45](#45) | Build an output table with Kubernetes pods with node, namespace, pod name, container name and corresponding resources using kubectl |
| Kubernetes | Kubectl | [46](#46) | List of Kubernetes CPU, memory and storage stats per node using kubectl |
| Kubernetes | Kubectl | [47](#47) | List of Kubernetes pods per namespace and kind using kubectl |
| Mac | Brew | [48](#48) | List all the packages and corresponding versions installed in a Mac by brew. |
| Mac | Info | [49](#49) | Parses the current Mac OS overview information |
| OpenAF | Channels | [50](#50) | Copy the json result of a command into an etcd database using OpenAF&#x27;s channels |
| OpenAF | Channels | [51](#51) | Getting all data stored in an etcd database using OpenAF&#x27;s channels |
| OpenAF | Channels | [52](#52) | Perform a query to a metric &amp; label, with a start and end time, to a Prometheus server using OpenAF&#x27;s channels |
| OpenAF | Channels | [53](#53) | Retrieve all keys stores in a H2 MVStore file using OpenAF&#x27;s channels |
| OpenAF | Channels | [54](#54) | Store and retrieve data from a Redis database |
| OpenAF | Channels | [55](#55) | Store and retrieve data from a RocksDB database |
| OpenAF | Channels | [56](#56) | Store the json results of a command into a H2 MVStore file using OpenAF&#x27;s channels |
| OpenAF | Network | [57](#57) | List all network addresses returned from the current DNS server for a hostname using OpenAF |
| OpenAF | OS | [58](#58) | Current OS information visible to OpenAF |
| OpenAF | TLS | [59](#59) | List the TLS certificates of a target host with a sorted alternative names using OpenAF |
| OpenAF | oPacks | [60](#60) | Listing all currently accessible OpenAF&#x27;s oPacks |
| OpenAF | oafp | [61](#61) | Filter the OpenAF&#x27;s oafp examples list by a specific word in the description |
| OpenAF | oafp | [62](#62) | List the OpenAF&#x27;s oafp examples by category, sub-category and description |
| Unix | Alpine | [63](#63) | List all installed packages in an Alpine system |
| Unix | Compute | [64](#64) | Parses the Linux /proc/cpuinfo into an array |
| Unix | Debian/Ubuntu | [65](#65) | List all installed packages in a Debian/Ubuntu system |
| Unix | Files | [66](#66) | Converting the Linux&#x27;s /etc/os-release to SQL insert statements. |
| Unix | Files | [67](#67) | Converting the Unix&#x27;s syslog into a json output. |
| Unix | Files | [68](#68) | Parses the Linux /etc/passwd to a table order by uid and gid. |
| Unix | Generic | [69](#69) | Creates, in unix, a data.ndjson file where each record is formatted from json files in /some/data |
| Unix | Network | [70](#70) | Loop over the current Linux active network connections |
| Unix | Network | [71](#71) | Parse the Linux &#x27;arp&#x27; command output |
| Unix | Network | [72](#72) | Parse the Linux &#x27;ip tcp_metrics&#x27; command |
| Unix | Network | [73](#73) | Parse the result of the Linux route command |
| Unix | OpenSuse | [74](#74) | List all installed packages in an OpenSuse system or zypper based system |
| Unix | RedHat | [75](#75) | List all installed packages in a RedHat system or rpm based system (use rpm --querytags to list all fields available) |
| Unix | Storage | [76](#76) | Converting the Unix&#x27;s df output |
| Unix | Storage | [77](#77) | Parses the result of the Unix ls command |
| Unix | SystemCtl | [78](#78) | Converting the Unix&#x27;s systemctl list-timers |
| Unix | SystemCtl | [79](#79) | Converting the Unix&#x27;s systemctl list-units |
| Unix | SystemCtl | [80](#80) | Converting the Unix&#x27;s systemctl list-units into an overview table |
| Unix | UBI | [81](#81) | List all installed packages in an UBI system |
| Windows | Network | [82](#82) | Output a table with the current route table using Windows&#x27; PowerShell |
| Windows | Network | [83](#83) | Output a table with the list of network interfaces using Windows&#x27; PowerShell |
| Windows | PnP | [84](#84) | Output a table with USB/PnP devices using Windows&#x27; PowerShell |
| Windows | Storage | [85](#85) | Output a table with the attached disk information using Windows&#x27; PowerShell |

## 📗 Examples

---

##### 1
### 📖 AI | Conversation
Send multiple requests to an OpenAI model keeping the conversation between interactions and setting the temperature parameter
```bash
export OAFP_MODEL="(type: openai, model: 'gpt-3.5-turbo-0125', key: ..., timeout: 900000, temperature: 0)"
echo "List all countries in the european union" | oafp in=llm out=ctree llmconversation=cvst.json
echo "Add the corresponding country capital" | oafp in=llm out=ctree llmconversation=cvst.json
rm cvst.json
```
---

##### 2
### 📖 AI | Ollama
Setting up access to Ollama and ask for data to an AI LLM model
```bash
export OAFP_MODEL="(type: ollama, model: 'mistral', url: 'https://models.local', timeout: 900000)"
echo "Output a JSON array with 15 cities where each entry has the 'city' name, the estimated population and the corresponding 'country'" | oafp input=llm output=json > data.json
oafp data.json output=ctable sql="select * order by population desc"
```
---

##### 3
### 📖 AI | OpenAI
Setting up the OpenAI LLM model and gather the data into a data.json file
```bash
export OAFP_MODEL="(type: openai, model: gpt-3.5-turbo, key: ..., timeout: 900000)"
echo "list all United Nations secretaries with their corresponding 'name', their mandate 'begin date', their mandate 'end date' and their corresponding secretary 'numeral'" | oafp input=llm output=json > data.json
```
---

##### 4
### 📖 AI | Prompt
Example of generating data from an AI LLM prompt
```bash
export OAFP_MODEL="(type: openai, model: 'gpt-3.5-turbo-0125', key: '...', timeout: 900000)"
oafp in=llm data="produce a list of 25 species of 'flowers' with their english and latin name and the continent where it can be found" out=json > data.json
```
---

##### 5
### 📖 AI | Summarize
Use an AI LLM model to summarize the weather information provided in a JSON format
```bash
export OAFP_MODEL="(type: openai, model: 'gpt-3.5-turbo-0125', key: '...', timeout: 900000)"
oafp url="https://wttr.in?format=j2" llmcontext="current and forecast weather" llmprompt="produce a summary of the current and forecasted weather" out=md
```
---

##### 6
### 📖 APIs | Network
Converting the Cloudflare DNS trace info
```bash
curl -s https://1.1.1.1/cdn-cgi/trace | oafp in=ini out=ctree
```
---

##### 7
### 📖 APIs | Network
Converting the Google DNS DoH query result
```bash
oafp path=Answer from="sort(data)" out=ctable url="https://8.8.8.8/resolve?name=yahoo.com&type=a"
```
---

##### 8
### 📖 APIs | Network
Generating a simple map of the current public IP address
```bash
curl -s https://ifconfig.co/json | oafp flatmap=true out=map
```
---

##### 9
### 📖 AWS | EC2
Given all AWS EC2 instances in an account produces a table with name, type, vpc and private ip sorted by vpc
```bash
aws ec2 describe-instances | ./oafp path="Reservations[].Instances[].{name:join('',Tags[?Key=='Name'].Value),type:InstanceType,vpc:VpcId,ip:PrivateIpAddress} | sort_by(@, &vpc)" output=ctable
```
---

##### 10
### 📖 AWS | EKS
Builds an excel spreadsheet with all persistent volumes associated with an AWS EKS &#x27;XYZ&#x27; with the corresponding Kubernetes namespace, pvc and pv names
```bash
# sudo yum install -y fontconfig
aws ec2 describe-volumes | oafp path="Volumes[?Tags[?Key=='kubernetes.io/cluster/XYZ']|[0].Value=='owned'].{VolumeId:VolumeId,Name:Tags[?Key=='Name']|[0].Value,KubeNS:Tags[?Key=='kubernetes.io/created-for/pvc/namespace']|[0].Value,KubePVC:Tags[?Key=='kubernetes.io/created-for/pvc/name']|[0].Value,KubePV:Tags[?Key=='kubernetes.io/created-for/pv/name']|[0].Value,AZ:AvailabilityZone,Size:Size,Type:VolumeType,CreateTime:CreateTime,State:State,AttachTime:join(',',nvl(Attachments[].AttachTime,from_slon('[]'))[]),InstanceId:join(',',nvl(Attachments[].InstanceId,from_slon('[]'))[])}" from="sort(KubeNS,KubePVC)" out=xls xlsfile=xyz_pvs.xlsx
```
---

##### 11
### 📖 AWS | Lambda
Prepares a table of AWS Lambda functions with their corresponding main details
```bash
aws lambda list-functions | oafp path="Functions[].{Name:FunctionName,Runtime:Runtime,Arch:join(',',Architectures),Role:Role,MemorySize:MemorySize,EphStore:EphemeralStorage.Size,CodeSize:CodeSize,LastModified:LastModified}" from="sort(Name)" out=ctable
```
---

##### 12
### 📖 AWS | Lambda
Prepares a table, for a specific AWS Lambda function during a specific time periods, with number of invocations and minimum, average and maximum duration per periods from AWS CloudWatch
```bash
export _SH="aws cloudwatch get-metric-statistics --namespace AWS/Lambda --start-time 2024-03-01T00:00:00Z --end-time 2024-04-01T00:00:00Z --period 3600 --dimensions Name=FunctionName,Value=my-function"
$_SH --statistics Sum --metric-name Invocations  | oafp path="Datapoints[].{ts:Timestamp,cnt:Sum}" out=ndjson > data.ndjson
$_SH --statistics Average --metric-name Duration | oafp path="Datapoints[].{ts:Timestamp,avg:Average}" out=ndjson >> data.ndjson
$_SH --statistics Minimum --metric-name Duration | oafp path="Datapoints[].{ts:Timestamp,min:Minimum}" out=ndjson >> data.ndjson
$_SH --statistics Maximum --metric-name Duration | oafp path="Datapoints[].{ts:Timestamp,max:Maximum}" out=ndjson >> data.ndjson
oafp data.ndjson ndjsonjoin=true opath="[].{ts:ts,cnt:nvl(cnt,\`0\`),min:nvl(min,\`0\`),avg:nvl(avg,\`0\`),max:nvl(max,\`0\`)}" out=json | oafp isql="select \"ts\",max(\"cnt\") \"cnt\",max(\"min\") \"min\",max(\"avg\") \"avg\",max(\"max\") \"max\" group by \"ts\" order by \"ts\"" opath="[].{ts:ts,cnt:cnt,min:from_ms(min,'(abrev:true,pad:true)'),avg:from_ms(avg,'(abrev:true,pad:true)'),max:from_ms(max,'(abrev:true,pad:true)')}" out=ctable
```
---

##### 13
### 📖 DB | H2
Perform a SQL query over a H2 database.
```bash
echo "select * from \"data\"" | oafp in=db indbjdbc="jdbc:h2:./data" indbuser=sa indbpass=sa out=ctable
```
---

##### 14
### 📖 DB | H2
Store the json result of a command into a H2 database table.
```bash
oaf -c "\$o(listFilesRecursive('.'),{__format:'json'})" | oafp out=db dbjdbc="jdbc:h2:./data" dbuser=sa dbpass=sa dbtable=data
```
---

##### 15
### 📖 DB | SQLite
Perform a query over a database using JDBC.
```bash
ojob ojob.io/db/getDriver op=install db=sqlite
echo "select * from data" | oafp in=db indbjdbc="jdbc:sqlite:data.db" indbtable=data indblib=sqlite out=ctable
```
---

##### 16
### 📖 DB | SQLite
Store the json result on a SQLite database table.
```bash
ojob ojob.io/db/getDriver op=install db=sqlite
oaf -c "\$o(listFilesRecursive('.'),{__format:'json'})" | oafp out=db dbjdbc="jdbc:sqlite:data.db" dbtable=data dblib=sqlite
```
---

##### 17
### 📖 Docker | Containers
Output a table with the list of running containers.
```bash
oafp cmd="docker ps --format json" input=ndjson ndjsonjoin=true path="[].{id:ID,name:Names,state:State,image:Image,networks:Networks,ports:Ports,Status:Status}" sql="select * order by networks,state,name" output=ctable
```
---

##### 18
### 📖 Docker | Network
Output a table with the docker networks info.
```bash
docker network ls --format json | oafp in=ndjson ndjsonjoin=true out=ctable
```
---

##### 19
### 📖 Docker | Stats
Output a table with the docker stats broken down for each value.
```bash
oafp cmd="docker stats --no-stream" in=lines linesvisual=true linesjoin=true out=ctree path="[].{containerId:\"CONTAINER ID\",pids:PIDS,name:\"NAME\",cpuPerc:\"CPU %\",memory:\"MEM USAGE / LIMIT\",memPerc:\"MEM %\",netIO:\"NET I/O\",blockIO:\"BLOCK I/O\"}|[].{containerId:containerId,pids:pids,name:name,cpuPerc:replace(cpuPerc,'%','',''),memUsage:from_bytesAbbr(split(memory,' / ')[0]),memLimit:from_bytesAbbr(split(memory,' / ')[1]),memPerc:replace(memPerc,'%','',''),netIn:from_bytesAbbr(split(netIO,' / ')[0]),netOut:from_bytesAbbr(split(netIO,' / ')[1]),blockIn:from_bytesAbbr(split(blockIO,' / ')[0]),blockOut:from_bytesAbbr(split(blockIO,' / ')[1])}" out=ctable
```
---

##### 20
### 📖 Docker | Storage
Output a table with the docker volumes info.
```bash
docker volume ls --format json | oafp in=ndjson ndjsonjoin=true out=ctable
```
---

##### 21
### 📖 ElasticSearch | Cluster
Get an ElasticSearch/OpenSearch cluster nodes overview
```bash
export ES_URL=http://elastic.search:9200
export ES_EXTRA="--insecure"
curl -s "$ES_URL/_cat/nodes?format=json" $ES_EXTRA | oafp sql="select * order by ip" out=ctable
```
---

##### 22
### 📖 ElasticSearch | Cluster
Get an ElasticSearch/OpenSearch cluster per host data allocation
```bash
export ES_URL=http://elastic.search:9200
export ES_EXTRA="--insecure"
curl -s "$ES_URL/_cat/allocation?format=json&bytes=b" $ES_EXTRA | oafp sql="select * order by host" out=ctable
```
---

##### 23
### 📖 ElasticSearch | Cluster
Get an ElasticSearch/OpenSearch cluster settings flat
```bash
export ES_URL=http://elastic.search:9200
export ES_EXTRA="--insecure"
curl -s "$ES_URL/_cluster/settings?include_defaults=true&flat_settings=true" $ES_EXTRA | oafp out=ctree
```
---

##### 24
### 📖 ElasticSearch | Cluster
Get an ElasticSearch/OpenSearch cluster settings non-flatted
```bash
export ES_URL=http://elastic.search:9200
export ES_EXTRA="--insecure"
curl -s "$ES_URL/_cluster/settings?include_defaults=true" $ES_EXTRA | oafp out=ctree
```
---

##### 25
### 📖 ElasticSearch | Cluster
Get an ElasticSearch/OpenSearch cluster stats per node
```bash
export ES_URL=http://elastic.search:9200
export ES_EXTRA="--insecure"
curl -s "$ES_URL/_nodes/stats/indices/search" $ES_EXTRA | oafp out=ctree
```
---

##### 26
### 📖 ElasticSearch | Cluster
Get an overview of an ElasticSearch/OpenSearch cluster health
```bash
export ES_URL=http://elastic.search:9200
export ES_EXTRA="--insecure"
curl -s "$ES_URL/_cat/health?format=json" $ES_EXTRA | oafp out=ctable
```
---

##### 27
### 📖 ElasticSearch | Indices
Get an ElasticSearch/OpenSearch count per index
```bash
export ES_URL=http://elastic.search:9200
export ES_EXTRA="--insecure"
curl -s "$ES_URL/kibana_sample_data_flights/_count" $ES_EXTRA | oafp
```
---

##### 28
### 📖 ElasticSearch | Indices
Get an ElasticSearch/OpenSearch indices overview
```bash
export ES_URL=http://elastic.search:9200
export ES_EXTRA="--insecure"
curl -s "$ES_URL/_cat/indices?format=json&bytes=b" $ES_EXTRA | oafp sql="select * order by index" out=ctable
```
---

##### 29
### 📖 ElasticSearch | Indices
Get an ElasticSearch/OpenSearch settings for a specific index
```bash
export ES_URL=http://elastic.search:9200
export ES_EXTRA="--insecure"
curl -s "$ES_URL/kibana_sample_data_flights/_settings" $ES_EXTRA | oafp out=ctree
```
---

##### 30
### 📖 Generic | Excel
Building an Excel file with the AWS IPv4 and IPv6 ranges (1).
```bash
curl https://ip-ranges.amazonaws.com/ip-ranges.json > ip-ranges.json
```
---

##### 31
### 📖 Generic | Excel
Building an Excel file with the AWS IPv4 and IPv6 ranges (2).
```bash
oafp ip-ranges.json path=prefixes out=xls xlsfile=aws-ip-ranges.xlsx xlssheet=ipv4
```
---

##### 32
### 📖 Generic | Excel
Building an Excel file with the AWS IPv4 and IPv6 ranges (3).
```bash
oafp ip-ranges.json path=ipv6_prefixes out=xls xlsfile=aws-ip-ranges.xlsx xlssheet=ipv6
```
---

##### 33
### 📖 Generic | Excel
Processes each json file in /some/data creating and updating the data.xlsx file with a sheet for each file.
```bash
find /some/data -name "*.json" | xargs -I '{}' /bin/sh -c 'oafp file={} output=xls xlsfile=data.xlsx xlsopen=false xlssheet=$(echo {} | sed "s/.*\/\(.*\)\.json/\1/g" )'
```
---

##### 34
### 📖 Generic | Excel
Store and retrieve data from an Excel spreadsheet
```bash
# Storing data
oafp cmd="oaf -c \"sprint(listFilesRecursive('/usr/bin'))\"" out=xls xlsfile=data.xlsx
# Retrieve data
oafp in=xls file=data.xlsx xlscol=A xlsrow=1 out=pjson
```
---

##### 35
### 📖 Generic | RSS
Example of generating a HTML list of titles, links and publication dates from a RSS feed
```bash
oafp url="https://blog.google/rss" path="rss.channel.item" sql="select title, link, pubDate" output=html
```
---

##### 36
### 📖 Generic | Text
Get a json with lyrics of a song.
```bash
curl -s https://api.lyrics.ovh/v1/Coldplay/Viva%20La%20Vida | oafp path="substring(lyrics,index_of(lyrics, '\n'),length(lyrics))"
```
---

##### 37
### 📖 GitHub | Releases
Builds a table of GitHub project releases
```bash
curl -s https://api.github.com/repos/openaf/openaf/releases | oafp sql="select name, tag_name, published_at order by published_at" output=ctable
```
---

##### 38
### 📖 GitHub | Releases
Parses the latest GitHub project release markdown notes
```bash
curl -s https://api.github.com/repos/openaf/openaf/releases | oafp path="[0].body" output=md
```
---

##### 39
### 📖 Grid | Java
Parse a Java stacktrace into a looping grid.
```bash
oafp /tmp/hsperfdata_user/12345 in=hsperf path=java out=grid grid="[[(title:Threads,type:chart,obj:'int threads.live:green:live threads.livePeak:red:peak threads.daemon:blue:daemon -min:0')|(title:Class Loaders,type:chart,obj:'int cls.loadedClasses:blue:loaded cls.unloadedClasses:red:unloaded')]|[(title:Heap,type:chart,obj:'bytes __mem.total:red:total __mem.used:blue:used -min:0')|(title:Metaspace,type:chart,obj:'bytes __mem.metaTotal:blue:total __mem.metaUsed:green:used -min:0')]]" loop=1
```
---

##### 40
### 📖 Grid | Kubernetes
Displays a continuous updating grid with a line chart with the number of CPU throtlles and bursts recorded in the Linux cgroup cpu stats of a container running in Kubernetes and the source cpu.stats data
```bash
oafp cmd="cat /sys/fs/cgroup/cpu.stat | sed 's/ /: /g'" in=yaml out=grid grid="[[(title:cpu.stat,type:tree)|(title:chart,type:chart,obj:'int nr_throttled:red:throttled nr_bursts:blue:bursts -min:0 -vsize:10')]]" loop=1
```
---

##### 41
### 📖 Grid | Unix
Output a chart with the current Unix load using uptime
```bash
oafp cmd="uptime" in=raw path="replace(trim(@), '.+ ([\d\.]+), ([\d\.]+), ([\d\.]+)\$', '', '\$1|\$2|\$3').split(@,'|')" out=chart chart="dec2 [0]:green:load -min:0" loop=1 loopcls=true
```
---

##### 42
### 📖 JSON Schemas | Lists
Get a list of JSON schemas from Schema Store catalog
```bash
oafp cmd="curl https://raw.githubusercontent.com/SchemaStore/schemastore/master/src/api/json/catalog.json" path="schemas[].{name:name,description:description,files:to_string(fileMatch)}" out=ctable
```
---

##### 43
### 📖 Kubernetes | Containers
Parse the Linux cgroup cpu stats on a container running in Kubernetes
```bash
cat /sys/fs/cgroup/cpu.stat | sed 's/ /: /g' | oafp in=yaml out=ctree
```
---

##### 44
### 📖 Kubernetes | Kubectl
Build an output table with Kubernetes pods with namespace, pod name, container name and corresponding resources using kubectl
```bash
kubectl get pods -A -o json | oafp path="items[].amerge({ ns: metadata.namespace, pod: metadata.name }, spec.containers[].{ container: name, resources: to_slon(resources) })[]" sql="select ns, pod, container, resources order by ns, pod, container" out=ctable
```
---

##### 45
### 📖 Kubernetes | Kubectl
Build an output table with Kubernetes pods with node, namespace, pod name, container name and corresponding resources using kubectl
```bash
kubectl get pods -A -o json | oafp path="items[].amerge({ node: spec.nodeName, ns: metadata.namespace, pod: metadata.name }, spec.containers[].{ container: name, resources: to_slon(resources) })[]" sql="select node, ns, pod, container, resources order by node, ns, pod, container" out=ctable
```
---

##### 46
### 📖 Kubernetes | Kubectl
List of Kubernetes CPU, memory and storage stats per node using kubectl
```bash
oafp cmd="kubectl get nodes -o json" path="items[].{node:metadata.name,totalCPU:status.capacity.cpu,allocCPU:status.allocatable.cpu,totalMem:to_bytesAbbr(from_bytesAbbr(status.capacity.memory)),allocMem:to_bytesAbbr(from_bytesAbbr(status.allocatable.memory)),totalStorage:to_bytesAbbr(from_bytesAbbr(status.capacity.\"ephemeral-storage\")),allocStorage:to_bytesAbbr(to_number(status.allocatable.\"ephemeral-storage\")),conditions:join(\`, \`,status.conditions[].reason)}" output=ctable
```
---

##### 47
### 📖 Kubernetes | Kubectl
List of Kubernetes pods per namespace and kind using kubectl
```bash
oafp cmd="kubectl get pods -A -o json" path="items[].{ns:metadata.namespace,kind:metadata.ownerReferences[].kind,name:metadata.name,status:status.phase,restarts:sum(status.containerStatuses[].restartCount),node:spec.nodeName,age:timeago(status.startTime)}" sql="select * order by status,name" output=ctable
```
---

##### 48
### 📖 Mac | Brew
List all the packages and corresponding versions installed in a Mac by brew.
```bash
brew list --versions | oafp in=lines linesjoin=true path="[].split(@,' ').{package:[0],version:[1]}|sort_by(@,&package)" out=ctable
```
---

##### 49
### 📖 Mac | Info
Parses the current Mac OS overview information
```bash
system_profiler SPSoftwareDataType -json | oafp path="SPSoftwareDataType[0]" out=ctree
```
---

##### 50
### 📖 OpenAF | Channels
Copy the json result of a command into an etcd database using OpenAF&#x27;s channels
```bash
oaf -c "\$o(io.listFiles('.').files,{__format:'json'})" | oafp out=ch ch="(type: etcd3, options: (host: localhost, port: 2379), lib: 'etcd3.js')" chkey=canonicalPath
```
---

##### 51
### 📖 OpenAF | Channels
Getting all data stored in an etcd database using OpenAF&#x27;s channels
```bash
echo "" | oafp in=ch inch="(type: etcd3, options: (host: localhost, port: 2379), lib: 'etcd3.js')" out=ctable
```
---

##### 52
### 📖 OpenAF | Channels
Perform a query to a metric &amp; label, with a start and end time, to a Prometheus server using OpenAF&#x27;s channels
```bash
oafp in=ch inch="(type:prometheus,options:(urlQuery:'http://prometheus.local'))" inchall=true data="(start:'2024-03-22T19:00:00.000Z',end:'2024-03-22T19:05:00.000Z',step:60,query:go_memstats_alloc_bytes_total{job=\"prometheus\"})" path="[].values[].{date:to_date(mul([0],to_number('1000'))),value:[1]}" out=ctable
```
---

##### 53
### 📖 OpenAF | Channels
Retrieve all keys stores in a H2 MVStore file using OpenAF&#x27;s channels
```bash
echo "" | oafp in=ch inch="(type: mvs, options: (file: data.db))" out=ctable
```
---

##### 54
### 📖 OpenAF | Channels
Store and retrieve data from a Redis database
```bash
# Install rocksdb opack: 'opack install redis'
#
# Storing data
oafp cmd="oaf -c \"sprint(listFilesRecursive('/usr/bin'))\"" out=ch ch="(type: redis, lib: redis.js, options: (host: '127.0.0.1', port: 6379))" chkey=canonicalPath
# Retrieve data
echo "" | oafp in=ch inch="(type: redis, lib: redis.js, options: (host: '127.0.0.1', port: 6379))" out=pjson
```
---

##### 55
### 📖 OpenAF | Channels
Store and retrieve data from a RocksDB database
```bash
# Install rocksdb opack: 'opack install rocksdb'
#
# Storing data
oafp cmd="oaf -c \"sprint(listFilesRecursive('/usr/bin'))\"" out=ch ch="(type: rocksdb, lib: rocksdb.js, options: (path: db))" chkey=canonicalPath
# Retrieve data
echo "" | oafp in=ch inch="(type: rocksdb, lib: rocksdb.js, options: (path: db))" out=pjson
```
---

##### 56
### 📖 OpenAF | Channels
Store the json results of a command into a H2 MVStore file using OpenAF&#x27;s channels
```bash
oaf -c "\$o(listFilesRecursive('.'),{__format:'json'})" | oafp out=ch ch="(type: mvs, options: (file: data.db))" chkey=canonicalPath
```
---

##### 57
### 📖 OpenAF | Network
List all network addresses returned from the current DNS server for a hostname using OpenAF
```bash
oaf -c "sprint(ow.loadNet().getDNS('yahoo.com'))" | oafp from="sort(Address)" out=ctable
```
---

##### 58
### 📖 OpenAF | OS
Current OS information visible to OpenAF
```bash
oafp -v path=os
```
---

##### 59
### 📖 OpenAF | TLS
List the TLS certificates of a target host with a sorted alternative names using OpenAF
```bash
oaf -c "sprint(ow.loadNet().getTLSCertificates('yahoo.com',443))" | oafp path="[].{issuer:issuerDN,subject:subjectDN,notBefore:notBefore,notAfter:notAfter,alternatives:join(' | ',sort(map(&[1],nvl(alternatives,\`[]\`))))}" out=ctree
```
---

##### 60
### 📖 OpenAF | oPacks
Listing all currently accessible OpenAF&#x27;s oPacks
```bash
oaf -c "sprint(getOPackRemoteDB())" | oafp maptoarray=true opath="[].{name:name,description:description,version:version}" from="sort(name)" out=ctable
```
---

##### 61
### 📖 OpenAF | oafp
Filter the OpenAF&#x27;s oafp examples list by a specific word in the description
```bash
oafp url="https://gist.githubusercontent.com/nmaguiar/557e12e4a840d513635b3a57cb57b722/raw/oafp-examples.yaml" in=yaml out=template path=data templatepath=tmpl sql="select * where d like '%something%'"
```
---

##### 62
### 📖 OpenAF | oafp
List the OpenAF&#x27;s oafp examples by category, sub-category and description
```bash
oafp url="https://gist.githubusercontent.com/nmaguiar/557e12e4a840d513635b3a57cb57b722/raw/oafp-examples.yaml" in=yaml path="data[].{category:c,subCategory:s,description:d}" from="sort(category,subCategory,description)" out=ctable
```
---

##### 63
### 📖 Unix | Alpine
List all installed packages in an Alpine system
```bash
apk list -I | oafp in=lines linesjoin=true path="[].replace(@,'(.+) (.+) {(.+)} \((.+)\) \[(.+)\]','','\$1|\$2|\$3|\$4').split(@,'|').{package:[0],arch:[1],source:[2],license:[3]}" out=ctable
```
---

##### 64
### 📖 Unix | Compute
Parses the Linux /proc/cpuinfo into an array
```bash
cat /proc/cpuinfo | sed "s/^$/---/mg" | ./oafp in=yaml path="[?not_null(@)]" out=ctree
```
---

##### 65
### 📖 Unix | Debian/Ubuntu
List all installed packages in a Debian/Ubuntu system
```bash
apt list --installed | sed "1d" | oafp in=lines linesjoin=true path="[].split(@,' ').{pack:split([0],'/')[0],version:[1],arch:[2]}" out=ctable
```
---

##### 66
### 📖 Unix | Files
Converting the Linux&#x27;s /etc/os-release to SQL insert statements.
```bash
oafp cmd="cat /etc/os-release" in=ini outkey=release path="[@]" sql="select '$HOSTNAME' \"HOST\", *" out=sql sqlnocreate=true
```
---

##### 67
### 📖 Unix | Files
Converting the Unix&#x27;s syslog into a json output.
```bash
cat syslog | oafp in=raw path="split(trim(@),'\n').map(&split(@, ' ').{ date: concat([0],concat(' ',[1])), time: [2], host: [3], process: [4], message: join(' ',[5:]) }, [])"
```
---

##### 68
### 📖 Unix | Files
Parses the Linux /etc/passwd to a table order by uid and gid.
```bash
oafp cmd="cat /etc/passwd" in=csv inputcsv="(withHeader: false, withDelimiter: ':')" path="[].{user:f0,pass:f1,uid:to_number(f2),gid:to_number(f3),description:f4,home:f5,shell:f6}" out=json | oafp from="notStarts(user, '#').sort(uid, gid)" out=ctable
```
---

##### 69
### 📖 Unix | Generic
Creates, in unix, a data.ndjson file where each record is formatted from json files in /some/data
```bash
find /some/data -name "*.json" -exec oafp {} output=json \; > data.ndjson
```
---

##### 70
### 📖 Unix | Network
Loop over the current Linux active network connections
```bash
oafp cmd="netstat -tun | sed \"1d\"" in=lines linesvisual=true linesjoin=true linesvisualsepre="\\s+(\\?\!Address)" out=ctable loop=1
```
---

##### 71
### 📖 Unix | Network
Parse the Linux &#x27;arp&#x27; command output
```bash
arp | oafp in=lines linesvisual=true linesjoin=true out=ctable
```
---

##### 72
### 📖 Unix | Network
Parse the Linux &#x27;ip tcp_metrics&#x27; command
```bash
ip tcp_metrics | sed 's/^/target: /g' | sed 's/$/\n\n---\n/g' | sed 's/ \([a-z]*\) /\n\1: /g' | head -n -2 | oafp in=yaml path="[].{target:target,age:from_timeAbbr(replace(age,'[sec|\.]','','')),cwnd:cwnd,rtt:from_timeAbbr(rtt),rttvar:from_timeAbbr(rttvar),source:source}" sql="select * order by target" out=ctable
```
---

##### 73
### 📖 Unix | Network
Parse the result of the Linux route command
```bash
route | sed "1d" | oafp in=lines linesjoin=true linesvisual=true linesvisualsepre="\s+" out=ctable
```
---

##### 74
### 📖 Unix | OpenSuse
List all installed packages in an OpenSuse system or zypper based system
```bash
zypper se -is | egrep "^i" | oafp in=lines linesjoin=true path="[].split(@,'|').{name:[1],version:[2],arch:[3],repo:[4]}" out=ctable
```
---

##### 75
### 📖 Unix | RedHat
List all installed packages in a RedHat system or rpm based system (use rpm --querytags to list all fields available)
```bash
rpm -qa --qf "%{NAME}|%{VERSION}|%{PACKAGER}|%{VENDOR}|%{ARCH}\n" | oafp in=lines linesjoin=true path="[].split(@,'|').{package:[0],version:[1],packager:[2],vendor:[3],arch:[4]}" from="sort(package)" out=ctable
```
---

##### 76
### 📖 Unix | Storage
Converting the Unix&#x27;s df output
```bash
df --output=target,fstype,size,used,avail,pcent | tail -n +2 | oafp in=lines linesjoin=true path="[].split_re(@, ' +').{filesystem:[0],type:[1],size:[2],used:[3],available:[4],use:[5]}" out=ctable
```
---

##### 77
### 📖 Unix | Storage
Parses the result of the Unix ls command
```bash
ls -lad --time-style="+%Y-%m-%d %H:%M" * | oafp in=lines path="map(&split_re(@,'\\s+').{permissions:[0],id:[1],user:[2],group:[3],size:[4],date:[5],time:[6],file:[7]},[])" linesjoin=true out=ctable
```
---

##### 78
### 📖 Unix | SystemCtl
Converting the Unix&#x27;s systemctl list-timers
```bash
systemctl list-timers | head -n -3 | oafp in=lines linesvisual=true linesjoin=true out=ctable
```
---

##### 79
### 📖 Unix | SystemCtl
Converting the Unix&#x27;s systemctl list-units
```bash
systemctl list-units | head -n -6 | oafp in=lines linesvisual=true linesjoin=true path="[].delete(@,'')" out=ctable
```
---

##### 80
### 📖 Unix | SystemCtl
Converting the Unix&#x27;s systemctl list-units into an overview table
```bash
systemctl list-units | head -n -6 | oafp in=lines linesvisual=true linesjoin=true path="[].delete(@,'')" sql="select \"LOAD\", \"ACTIVE SUB\", count(1) as \"COUNT\" group by \"LOAD\", \"ACTIVE SUB\"" sqlfilter=advanced out=ctable
```
---

##### 81
### 📖 Unix | UBI
List all installed packages in an UBI system
```bash
microdnf repoquery --setopt=cachedir=/tmp --installed | oafp in=lines linesjoin=true path="[].replace(@,'(.+)\.(\w+)\.(\w+)\$','','\$1|\$2|\$3').split(@,'|').{package:[0],dist:[1],arch:[2]}" out=ctable
```
---

##### 82
### 📖 Windows | Network
Output a table with the current route table using Windows&#x27; PowerShell
```bash
Get-NetRoute | ConvertTo-Json | .\oafp.bat path="[].{destination:DestinationPrefix,gateway:NextHop,interface:InterfaceAlias,metric:InterfaceMetric}" sql=select\ *\ order\ by\ interface,destination out=ctable
```
---

##### 83
### 📖 Windows | Network
Output a table with the list of network interfaces using Windows&#x27; PowerShell
```bash
Get-NetIPAddress | ConvertTo-Json | .\oafp.bat path="[].{ipAddress:IPAddress,prefixLen:PrefixLength,interface:InterfaceAlias}" sql=select\ *\ order\ by\ interface out=ctable
```
---

##### 84
### 📖 Windows | PnP
Output a table with USB/PnP devices using Windows&#x27; PowerShell
```bash
Get-PnpDevice -PresentOnly | ConvertTo-Csv -NoTypeInformation | .\oafp.bat in=csv path="[].{class:PNPClass,service:Service,name:FriendlyName,id:InstanceId,description:Description,deviceId:DeviceID,status:Status,present:Present}" sql=select\ *\ order\ by\ class,service out=ctable
```
---

##### 85
### 📖 Windows | Storage
Output a table with the attached disk information using Windows&#x27; PowerShell
```bash
Get-Disk | ConvertTo-Csv -NoTypeInformation | .\oafp.bat in=csv path="[].{id:trim(UniqueId),name:FriendlyName,isBoot:IsBoot,location:Location,size:to_bytesAbbr(to_number(Size)),allocSize:to_bytesAbbr(to_number(AllocatedSize)),sectorSize:LogicalSectorSize,phySectorSize:PhysicalSectorSize,numPartitions:NumberOfPartitions,partitioning:PartitionStyle,health:HealthStatus,bus:BusType,manufacturer:Manufacturer,model:Model,firmwareVersion:FirmwareVersion,serialNumber:SerialNumber}" out=ctable
```

