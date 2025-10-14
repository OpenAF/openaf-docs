---
layout: default
title: ow.ai
parent: Reference
grand_parent: OpenAF docs
---


## ow.ai

### $gpt

__$gpt(aModel) : $gpt__

````
Creates a GPT AI model of aType (e.g. "openai" or "ollama") with aOptions.

aModel can be a map with the following properties:
- type: the type of the model (e.g. "openai", "ollama", "anthropic")
- options: a map with the options for the model (e.g. { key: "your-api-key", model: "gpt-3.5-turbo", temperature: 0.7, url: "https://api.openai.com/" })
- conversation: an array of messages to start the conversation (e.g. [{ role: "system", content: "You are a helpful assistant." }, { role: "user", content: "Hello!" }])
- tools: a map with the tools to use in the conversation (e.g. { "tool1": { type: "function", function: { name: "tool1", description: "A tool that does something", parameters: { type: "object", properties: { param1: { type: "string" } } } }, fn: function(args) { return args.param1; } } })
- timeout: the timeout for the requests in milliseconds (defaults to 15 minutes)
- noSystem: if true, it will not output the system messages (defaults to true)
- instructions: a string or an array of strings with the instructions for the model (e.g. "json", "boolean", "sql", "js", "path")
- headers: a map with the headers to use in the requests (e.g. { "Content-Type": "application/json" })
- params: a map with the parameters to use in the requests (e.g. { "max_tokens": 1000, "top_p": 1, "frequency_penalty": 0, "presence_penalty": 0 })

If aModel is not provided, it will try to get the model from the environment variable "OAF_MODEL" with the map in JSON or SLON format.
````
### $gpt.close

__$gpt.close()__

````
Closes the current GPT model.
````
### $gpt.iniPrompt

__$gpt.iniPrompt(aPrompt, aRole, aModel, aTemperature) : String__

````
Tries to prompt aPrompt (a string or an array of strings) and aModel (defaults to the one provided on the constructor) after cleaning the current conversation.
````
### $gpt.prompt

__$gpt.prompt(aPrompt, aRole, aModel, aTemperature, tools) : String__

````
Tries to prompt aPrompt (a string or an array of strings) and aModel (defaults to the one provided on the constructor).
````
### $gpt.promptBool

__$gpt.promptBool(aPrompt, aRole, aModel, aTemperature, tools) : boolean__

````
Tries to prompt aPrompt (a string or an array of strings) and aModel (defaults to the one provided on the constructor) returning a boolean.
````
### $gpt.promptImage

__$gpt.promptImage(aPrompt, aImage, aDetailLevel, aRole, aModel, aTemperature, jsonFlag) : String__

````
Tries to prompt aPrompt (a string or an array of strings) with aImage (a file path or a base64 string representation), aRole (defaults to "user") and aModel (defaults to the one provided on the constructor).
````
### $gpt.promptImgGen

__$gpt.promptImgGen(aPrompt, aModel, aPath) : Array__

````
Tries to prompt aPrompt and aModel (defaults to the one provided on the constructor) to generate one or more images and aPath to which the number of the image and ".png" will be saved to. Returns an array of the image files generated.
````
### $gpt.promptJSON

__$gpt.promptJSON(aPrompt, aModel, aTemperature)__

````
Tries to prompt aPrompt (a string or an array of strings) and aModel (defaults to the one provided on the constructor) returning a Javascript function.
````
### $gpt.promptMD

__$gpt.promptMD(aPrompt, aRole, aModel, aTemperature, tools) : String__

````
Tries to prompt aPrompt (a string or an array of strings) and aModel (defaults to the one provided on the constructor) returning a markdown string.
````
### $gpt.promptPath

__$gpt.promptPath(aPrompt, aJSONSchemaDef, aModel, aTemperature)__

````
Tries to prompt aPrompt (a string or an array of strings) and aModel (defaults to the one provided on the constructor) returning a JMESPath query.
````
### $gpt.promptSQL

__$gpt.promptSQL(aPrompt, aTableDefs, aDBName, aModel, aTemperature, tools)__

````
Tries to prompt aPrompt (a string or an array of strings) and aModel (defaults to the one provided on the constructor) returning a SQL query.
````
### $gpt.setTool

__$gpt.setTool(aName, aDesc, aParams, aFn) : ow.ai.gpt__

````
Sets a tool with aName, aDesc (description), aParams (a json schema) and aFn (a javascript function tha receives a map according with the provided json schema and returns a map)
````
### $gpt.sysPrompt

__$gpt.sysPrompt(aPrompt, aModel, aTemperature) : String__

````
Tries to prompt system aPrompt (a string or an array of strings) and aModel (defaults to the one provided on the constructor).
````
### $gpt.withContext

__$gpt.withContext(anObject, aContext) : ow.ai.gpt__

````
Adds a context to the current conversation.
````
### $gpt.withJSONAssert

__$gpt.withJSONAssert(aPath, anAssert) : ow.ai.gpt__

````
Adds a JSON path aPath to be asserted with anAssert (e.g. isArray or isMap).
````
### $gpt.withSQLTables

__$gpt.withSQLTables(aDBName, aTablesDefs) : ow.ai.gpt__

````
Adds aDBName with aTableDefs to be used with promptSQL.
````
### ow.ai.cluster

__ow.ai.cluster(args) : Object__

````
Wraps access to clustering of data. The result will be an object with a classify method that will  return the clustering result given the provided data. Args expects different arguments depending on type of  clustering:

   args.type                (String) "kmeans" (default)
   args.numberOfClusters    (Number) number of clusters to use (default to 5)
   classify(normalizedData) (Map)    returns a map of centroids and cluster assignments


````
### ow.ai.decisionTree

__ow.ai.decisionTree(aMap) : Object__

````
Provides a wrapper to access the existing decision tree algorithms included:

ID3:
  type              'id3'
  trainingSet       (array of maps)   The training data
  categoryAttr      (key name)        The map key to build the decision tree on
  ignoredAttributes (array of keys)   The list of keys to be ignored in each map

RandomForest:
  type              'randomforest'
  trainingSet       (array of maps)   The training data
  categoryAttr      (key name)        The map key to build the decision tree on
  ignoredAttributes (array of keys)   The list of keys to be ignored in each map
  treesNumber       (number)          The number of decision trees to use

C45:
  type              'c45'
  data              (array of arrays) The training data
  features          (arrays of keys)  The keys name by order of each array data value
  featureTypes      (arrays of types) Categorization of each attribute between 'category' and 'number'
  target            (key)             The target key name (the last of each array data value)
````
### ow.ai.gpt

__ow.ai.gpt(aType, aOptions) : ow.ai.gpt__

````
Creates a GPT AI model of aType (e.g. "openai" or "ollama") with aOptions.

````
### ow.ai.gpt.addDeveloperPrompt

__ow.ai.gpt.addDeveloperPrompt(aPrompt) : ow.ai.gpt__

````
Adds aPrompt (a string or an array of strings) with aRole (defaults to "developer") to the current conversation.
````
### ow.ai.gpt.addPrompt

__ow.ai.gpt.addPrompt(aPrompt, aRole) : ow.ai.gpt__

````
Adds aPrompt (a string or an array of strings) with aRole (defaults to "user") to the current conversation.
````
### ow.ai.gpt.addSystemPrompt

__ow.ai.gpt.addSystemPrompt(aPrompt) : ow.ai.gpt__

````
Adds aPrompt (a string or an array of strings) with aRole (defaults to "user") to the current conversation.
````
### ow.ai.gpt.addUserPrompt

__ow.ai.gpt.addUserPrompt(aPrompt) : ow.ai.gpt__

````
Adds aPrompt (a string or an array of strings) with aRole (defaults to "user") to the current conversation.
````
### ow.ai.gpt.booleanPrompt

__ow.ai.gpt.booleanPrompt(aPrompt, aModel, aTemperature, tools) : boolean__

````
Tries to prompt aPrompt (a string or an array of strings) with aRole (defaults to "user") and aModel (defaults to the one provided on the constructor).
````
### ow.ai.gpt.cleanPrompt

__ow.ai.gpt.cleanPrompt() : ow.ai.gpt__

````
Cleans the current conversation.
````
### ow.ai.gpt.codePrompt

__ow.ai.gpt.codePrompt(aPrompt, aModel, aTemperature, aCommentChars) : String__

````
Tries to prompt aPrompt (a string or an array of strings) with aRole (defaults to "user") and aModel (defaults to the one provided on the constructor).
````
### ow.ai.gpt.getConversation

__ow.ai.gpt.getConversation() : Array__

````
Returns the current conversation.
````
### ow.ai.gpt.jsonPrompt

__ow.ai.gpt.jsonPrompt(aPrompt, aModel, aTemperature, tools) : Object__

````
Tries to prompt aPrompt (a string or an array of strings) with aRole (defaults to "user") and aModel (defaults to the one provided on the constructor).
````
### ow.ai.gpt.parseCode

__ow.ai.gpt.parseCode(anAnswer) : String__

````
Tries to parse anAnswer and return the code between \``` and \```.
````
### ow.ai.gpt.pathPrompt

__ow.ai.gpt.pathPrompt(aPrompt, aJSONSchemaDef, aModel, aTemperature, tools) : String__

````
Tries to prompt aPrompt (a string or an array of strings) with aRole (defaults to "user") and aModel (defaults to the one provided on the constructor).
````
### ow.ai.gpt.prompt

__ow.ai.gpt.prompt(aPrompt, aRole, aModel, aTemperature, aJsonFlag, tools) : String__

````
Tries to prompt aPrompt (a string or an array of strings) with aRole (defaults to "user") and aModel (defaults to the one provided on the constructor).
````
### ow.ai.gpt.promptImage

__ow.ai.gpt.promptImage(aPrompt, aImage, aDetailLevel, aRole, aModel, aTemperature, jsonFlag) : String__

````
Tries to prompt aPrompt (a string or an array of strings) with aImage (a file path or a base64 string representation), aRole (defaults to "user") and aModel (defaults to the one provided on the constructor).
````
### ow.ai.gpt.promptImgGen

__ow.ai.gpt.promptImgGen(aPrompt, aModel, anOutputPathPrefix) : Array__

````
Tries to prompt aPrompt (a string or an array of strings), aModel (defaults to the one provided on the constructor) to generate one or more images and anOutputPathPrefix to which the number of the image and ".png" will be appended. Returns an array of the files generated.
````
### ow.ai.gpt.prototype.getModels

__ow.ai.gpt.prototype.getModels() : Array__

````
Returns the available models from the GPT AI service.
````
### ow.ai.gpt.rawImgGen

__ow.ai.gpt.rawImgGen(aPrompt, aModel) : Map__

````
Tries to generate an image based on aPrompt (a string or an array of strings) with aModel (defaults to the one provided on the constructor). Returns the raw result.
````
### ow.ai.gpt.rawPrompt

__ow.ai.gpt.rawPrompt(aPrompt, aRole, aModel, aTemperature, aJsonFlag, tools) : String__

````
Tries to prompt aPrompt (a string or an array of strings) with aRole (defaults to "user") and aModel (defaults to the one provided on the constructor).
````
### ow.ai.gpt.setConversation

__ow.ai.gpt.setConversation(aConversation) : ow.ai.gpt__

````
Sets the current conversation to aConversation.
````
### ow.ai.gpt.setInstructions

__ow.ai.gpt.setInstructions(aType) : ow.ai.gpt__

````
Sets the instructions for the current conversation. aType can be a string (e.g. json, boolean, sql, js and path) or an array of strings.
````
### ow.ai.gpt.setTool

__ow.ai.gpt.setTool(aName, aDesc, aParams, aFn) : ow.ai.gpt__

````
Sets a tool with aName, aDesc (description), aParams (a json schema) and aFn (a javascript function tha receives a map according with the provided json schema and returns a map)
````
### ow.ai.gpt.sqlPrompt

__ow.ai.gpt.sqlPrompt(aPrompt, aTableDefs, aDBName, aModel, aTemperature, tools) : String__

````
Tries to prompt aPrompt (a string or an array of strings) with aRole (defaults to "user") and aModel (defaults to the one provided on the constructor).
````
### ow.ai.network

__ow.ai.network(aMap) : ow.ai.network__

````
Creates a neural network given the parameters in aMap. aMap should contain a "type" parameter to indicate the type of network (synaptic: perceptron, lstm, liquid or hopfield; brainjs: neuralnetwork, rnntimestep, lstmtimestep, grutimestep, rnn, lstm or gru).  Then aMap should contain a "args" parameter to provide each network inialization parameters. Please see "help ow.ai.network.[type of network]" for more details about each one.
````
### ow.ai.network.feedfoward

__ow.ai.network.feedfoward(args) : ow.ai.network__

````
Examples: https://github.com/BrainJS/brain.js?tab=readme-ov-file#examples Data format: https://github.com/BrainJS/brain.js?tab=readme-ov-file#neural-network-types Train: https://github.com/BrainJS/brain.js?tab=readme-ov-file#training-options
````
### ow.ai.network.forecast

__ow.ai.network.forecast(aInput, aCount) : Array__

````

````
### ow.ai.network.fromJson

__ow.ai.network.fromJson(aMap)__

````
Tries to rebuild the network from aMap returned previously by a toJson function.
````
### ow.ai.network.get

__ow.ai.network.get(inputArray) : Array__

````
Given an inputArray of decimal values, normalize between 0 and 1, will activate the current network and  return an output array of decimal values between 0 and 1.
````
### ow.ai.network.getBrainJSObject

__ow.ai.network.getBrainJSObject() : Object__

````
Returns the current BrainJS object.
````
### ow.ai.network.getSynapticObject

__ow.ai.network.getSynapticObject() : Object__

````
Returns the current Synaptic object.
````
### ow.ai.network.gru

__ow.ai.network.gru(args) : ow.ai.network__

````
Examples: https://github.com/BrainJS/brain.js?tab=readme-ov-file#examples Data format: https://github.com/BrainJS/brain.js?tab=readme-ov-file#for-training-with-rnn-lstm-and-gru Train: https://github.com/BrainJS/brain.js?tab=readme-ov-file#training-options
````
### ow.ai.network.grutimestep

__ow.ai.network.grutimestep(args) : ow.ai.network__

````
Examples: https://github.com/BrainJS/brain.js?tab=readme-ov-file#examples Data format: https://github.com/BrainJS/brain.js?tab=readme-ov-file#for-training-with-rnntimestep-lstmtimestep-and-grutimestep Train: https://github.com/BrainJS/brain.js?tab=readme-ov-file#training-options
````
### ow.ai.network.hopfield

__ow.ai.network.hopfield(args) : ow.ai.network__

````
Hopfield serves as a content-addressable memory remembering patterns and when feed with new patterns the network returns the most similar one from the patterns it was trained to remember. You need to provide then number of input patterns args = [ 10 ].
````
### ow.ai.network.liquid

__ow.ai.network.liquid(args) : ow.ai.network__

````
Liquid state machines are neural networks where neurons are randomly connected to each other. The recurrent nature of the connections turns the time varying input into a spatio-temporal pattern of activations in the network nodes. You need to provide args = [number of inputs, size of pool of neurons, number of outputs, number of random connections, number of random gates] (e.g. 2, 20, 1, 30, 10).
````
### ow.ai.network.lstm

__ow.ai.network.lstm(args) : ow.ai.network__

````
LSTM (Long short-term memory) are well-suited to learn from experience to classify, process and predict time series when there are very long time lags of unknown size between important events. There is a minimum of 3 layers (input, memory block (input, memory cell, forget gate, output gate), output). args = [2, 6, 1] means 2 input, 6 memory blocks, 1 output; args = [2, 4, 4, 4, 1] means 2 input neurons, 3 memory blocks and 1 output.
````
### ow.ai.network.lstmtimestep

__ow.ai.network.lstmtimestep(args) : ow.ai.network__

````
Examples: https://github.com/BrainJS/brain.js?tab=readme-ov-file#examples Data format: https://github.com/BrainJS/brain.js?tab=readme-ov-file#for-training-with-rnntimestep-lstmtimestep-and-grutimestep Train: https://github.com/BrainJS/brain.js?tab=readme-ov-file#training-options
````
### ow.ai.network.neuralnetwork

__ow.ai.network.neuralnetwork(args) : ow.ai.network__

````
Examples: https://github.com/BrainJS/brain.js?tab=readme-ov-file#examples Data format: https://github.com/BrainJS/brain.js?tab=readme-ov-file#for-training-with-neuralnetwork Train: https://github.com/BrainJS/brain.js?tab=readme-ov-file#training-options
````
### ow.ai.network.perceptron

__ow.ai.network.perceptron(args) : ow.ai.network__

````
Perceptron or feed-forward neural networks. There is a minimum of 3 layers (input, hidden and output) and a any nmumber of hidden layers. args = [2, 3, 1] means 2 input neurons, 3 hidden neurons and 1 output neuron; args = [2, 10, 10, 10, 10, 1] means 2 input neurons, 4 layers of 10 neurons and 1 output neuron.
````
### ow.ai.network.put

__ow.ai.network.put(inputArray, outputArray, learningRate)__

````
Given an inputArray of decimal values, normalize between 0 and 1, will activate the current network and then the outputArray of decimal values, normalize between 0 and 1, with an optionial learningRate (defaults to 0.3).
````
### ow.ai.network.readFile

__ow.ai.network.readFile(aFile)__

````
Rebuilds a network from a map stored in aFile previously with ow.ai.network.writeFile.
````
### ow.ai.network.recurrent

__ow.ai.network.recurrent(args) : ow.ai.network__

````
Examples: https://github.com/BrainJS/brain.js?tab=readme-ov-file#examples Data format: https://github.com/BrainJS/brain.js?tab=readme-ov-file#neural-network-types Train: https://github.com/BrainJS/brain.js?tab=readme-ov-file#training-options
````
### ow.ai.network.rnn

__ow.ai.network.rnn(args) : ow.ai.network__

````
Examples: https://github.com/BrainJS/brain.js?tab=readme-ov-file#examples Data format: https://github.com/BrainJS/brain.js?tab=readme-ov-file#for-training-with-rnn-lstm-and-gru Train: https://github.com/BrainJS/brain.js?tab=readme-ov-file#training-options
````
### ow.ai.network.rnntimestep

__ow.ai.network.rnntimestep(args) : ow.ai.network__

````
Examples: https://github.com/BrainJS/brain.js?tab=readme-ov-file#examples Data format: https://github.com/BrainJS/brain.js?tab=readme-ov-file#for-training-with-rnntimestep-lstmtimestep-and-grutimestep Train: https://github.com/BrainJS/brain.js?tab=readme-ov-file#training-options
````
### ow.ai.network.toJson

__ow.ai.network.toJson() : Map__

````
Returns a map representation of the current network to be later rebuilt with the fromJson function.
````
### ow.ai.network.train

__ow.ai.network.train(trainingData, trainArgs)__

````
Trains the current network with the trainingData provided. trainingData should be an array of maps. Each  map entry should have a input and output keys. Each input and output entries should be an array for the  entry values and output values normalized to a decimal number between 0 and 1. Example:
[{input: [0,0], output: [0]}, {input: [0,1], output: [1]}, {input: [1,0], output: [1]}, {input: [1,1], output :[0]}]\. 

````
### ow.ai.network.writeFile

__ow.ai.network.writeFile(aFile)__

````
Writes a compressed file with the map representation of the current network.
````
### ow.ai.normalize.denormalizeWithSchema

__ow.ai.normalize.denormalizeWithSchema(aMapOfNormalizedData, aMapSchema, convertBools) : Map__

````
Tries to denormalize aMapOfNormalizedData (result from ow.ai.normalize.withSchema) according with aMapSchema provided.
````
### ow.ai.normalize.intArray

__ow.ai.normalize.intArray(anArray) : Array__

````
Returns anArray where all numbers have been rounded to an integer value.
````
### ow.ai.normalize.quantitize

__ow.ai.normalize.quantitize(anArray, aLevels) : Array__

````
Given anArray of numbers tries to quantitize returning an array of values between 0 and aLevels. If aLevels is not provided it will default to 10.
````
### ow.ai.normalize.scaleArray

__ow.ai.normalize.scaleArray(anArray, aMax, aMin) : Array__

````
Given anArray of numbers tries to normalize returning an array of values between 0 and 1. If aMax or aMin are not provided they will be infered from the provided anArray.
````
### ow.ai.normalize.softMax

__ow.ai.normalize.softMax(anArray, aTemperature) : Array__

````
Given anArray of numbers tries to apply a Softmax function returning an array of values between 0 and 1. If aTemperature is provided it will be used to control the smoothness of the output.
````
### ow.ai.normalize.toFeaturesArray

__ow.ai.normalize.toFeaturesArray(anArrayOfObjects, ignoredAttrs) : Map__

````
Tries to convert anArrayOfObjects into an array of array of values where each value is positioned in the resulting array by the corresponding key sorted. The result will be a map with the resulting array in 'data' (with the features values ignoring any key on ignoredAttrs), the 'ignoredAttrs' and keys with all the 'keys' identified.
````
### ow.ai.normalize.withSchema

__ow.ai.normalize.withSchema(aSimpleMapOfData, aMapSchema, convertBools) : Array__

````
Tries to normalize and return aSimpleMapOfData normalized according with aMapSchema provided. Each element of aMapSchema should be a map describing how to normalize aSimpleMapOfData. Example:

var ar = [
   {name:'workout', duration:'120', enjoy: true, time:1455063275, tags:['gym', 'weights'], crucial: false },
   {name:'lunch', duration:'45', enjoy: false, time:1455063275, tags:['salad', 'wine'], crucial: true },
   {name:'sleep', duration:'420', enjoy: true, time:1455063275, tags:['bed', 'romance'], crucial: true}
];

var sar = {
   name    : { col: 0, oneOf: [ 'workout', 'lunch', 'sleep' ] },
   duration: { col: 1, min: 0, max: 1000 },
   enjoy   : { col: 2 },
   tags    : { col: 3, anyOf: [ 'gym', 'weights', 'salad', 'wine', 'bed', 'romance' ] },
   crucial : { col: 4, scaleOf: [
     { val: true,  weight: 0.85 },
     { val: false, weight: 0.15 }
   ]},
};

$from(ar).sort("time").select((r) => { return normalize(r, sar); });


````
### ow.ai.regression

__ow.ai.regression() : Regression__

````
Returns a Regression with the following functions:

   linear(data, options) : Map
   power(data, options) : Map
   exponential(data, options) : Map
   logarithmic(data, options) : Map
   polynomial(data, options) : Map

   data - an array of arrays of x, y values ([[0,1],[1,3],[2,5]])
   options - map to determine the order and precision ({ order: 2, precision: 5})


````
### ow.ai.valuesArray

__ow.ai.valuesArray(entriesspan) : Map__

````
Creates a valuesArray object with the following functions:

  getValues()     : Array
  push(value)     : void
  deviation()     : Number
  variance()      : Number
  movingAverage() : Number

entriesspan - number of entries to keep
````
